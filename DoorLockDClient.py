#!/usr/bin/env python3
"""
DoorLockD Client - Smart Door Lock System
A modular RFID-based access control system for Raspberry Pi
"""

import sys
import os
import signal
import threading
import toml
import logging
from libs.data_container import data_container as dc
from libs.IOWrapper.ioHelpers import IoPortsShelf
from libs.Events import Events
from libs.Module import ModuleManager

# Developer: Amir Mobasheraghdam
# GitHub: https://github.com/amirmoba/doorlockd-client

class DoorLockDClient:
    """
    Main application class for DoorLockD Client
    A smart door lock system using RFID technology
    """
    
    def __init__(self):
        """Initialize the DoorLockD Client application"""
        self.setup_application_info()
        self.setup_data_container()
        
    def setup_application_info(self):
        """Set application name and version information"""
        dc.app_name = "doorlockd-client"
        dc.app_ver = self.get_git_version()
        dc.app_name_ver = f"{dc.app_name}({dc.app_ver})"
        
    def setup_data_container(self):
        """Initialize the global data container with required attributes"""
        dc.config = {}
        dc.module = None
        dc.e = None
        dc.logger = None
        dc.io_port = IoPortsShelf()
        
    def get_git_version(self):
        """
        Get git version information including branch, commit hash and dirty status
        
        Returns:
            str: Version string in format 'branchname-commithash-dirty'
        """
        try:
            import subprocess
            version = (
                subprocess.check_output(["git", "describe", "--all", "--long", "--dirty"])
                .decode("ascii")
                .strip()
            )
            return version
        except Exception as e:
            print(f"Warning: Could not read version from git: {e}")
            return "version-unknown"
    
    def load_configuration(self):
        """
        Load and parse configuration from TOML file
        
        Raises:
            SystemExit: If config file is missing or invalid
        """
        try:
            dc.config = toml.load("config.ini")
            dc.logger.info("Configuration loaded successfully")
        except FileNotFoundError:
            sys.exit("❌ Configuration file 'config.ini' not found.")
        except toml.TomlDecodeError as e:
            sys.exit(f"❌ Invalid configuration file: {e}")
    
    def setup_logging(self):
        """
        Configure logging system with console and file handlers
        """
        logger = logging.getLogger()
        
        # Create formatter for log messages
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        
        # Console handler (stderr)
        console_handler = logging.StreamHandler()
        console_level = dc.config.get("doorlockd", {}).get("stderr_level", "INFO")
        console_handler.setLevel(getattr(logging, console_level.upper()))
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        
        # File handler if configured
        logfile_name = dc.config.get("doorlockd", {}).get("logfile_name")
        if logfile_name:
            file_handler = logging.FileHandler(logfile_name)
            file_level = dc.config.get("doorlockd", {}).get("logfile_level", "INFO")
            file_handler.setLevel(getattr(logging, file_level.upper()))
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
            
            dc.logger.info(f"Logging to file: {logfile_name} (level: {file_level})")
        
        # Set overall logger level
        logger.setLevel(min([handler.level for handler in logger.handlers]))
        dc.logger = logger
        
        # Warn about deprecated configuration
        deprecated_log_level = dc.config.get("doorlockd", {}).get("log_level")
        if deprecated_log_level:
            logger.warning(
                f"Deprecated config 'doorlockd.log_level' will be ignored: {deprecated_log_level}"
            )
    
    def setup_event_system(self):
        """Initialize the event system for inter-module communication"""
        dc.e = Events()
        dc.logger.debug("Event system initialized")
    
    def setup_module_manager(self):
        """Initialize the module manager for dynamic module loading"""
        dc.module = ModuleManager()
        dc.logger.debug("Module manager initialized")
    
    def setup_exception_handling(self):
        """Configure global exception handling for threads"""
        def global_exception_handler(args):
            """Handle uncaught exceptions in threads"""
            error_msg = f"Uncaught exception in thread: {args.exc_value}"
            dc.module.abort(error_msg, args.exc_value)
        
        threading.excepthook = global_exception_handler
        dc.logger.debug("Global exception handler configured")
    
    def setup_signal_handlers(self):
        """Configure signal handlers for graceful shutdown"""
        def signal_handler(signum, frame):
            """Handle termination signals"""
            signal_name = "SIGINT" if signum == signal.SIGINT else "SIGTERM"
            dc.module.exit(f"Received {signal_name}")
        
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
        dc.logger.debug("Signal handlers configured")
    
    def initialize_modules(self):
        """
        Load, setup, and enable all configured modules
        
        Returns:
            bool: True if modules initialized successfully, False otherwise
        """
        try:
            # Load modules from configuration
            module_configs = dc.config.get("module", {})
            dc.module.load_all(module_configs)
            
            # Initialize modules in proper sequence
            dc.module.do_all("setup")
            dc.module.do_all("enable")
            
            dc.logger.info("All modules initialized successfully")
            return True
            
        except Exception as e:
            dc.logger.error(f"Failed to initialize modules: {e}")
            return False
    
    def main_loop(self):
        """
        Main application loop - runs until shutdown signal received
        """
        try:
            dc.logger.info(f"🚀 {dc.app_name_ver} entering main loop")
            dc.module.main_loop()
            
        except KeyboardInterrupt:
            dc.logger.info("Main loop interrupted by user")
        except Exception as e:
            dc.logger.error(f"Main loop error: {e}")
    
    def shutdown(self):
        """
        Graceful shutdown sequence for all modules and resources
        """
        dc.logger.info("Initiating shutdown sequence...")
        
        # Disable all modules
        dc.module.do_all("disable")
        
        # Teardown all modules
        dc.module.do_all("teardown")
        
        # Log shutdown reason
        if dc.module.abort_msg:
            dc.logger.warning(f"Shutdown due to abort: {dc.module.abort_msg}")
        elif dc.module.exit_msg:
            dc.logger.info(f"Shutdown requested: {dc.module.exit_msg}")
        else:
            dc.logger.info("Normal shutdown completed")
    
    def run(self):
        """
        Main application entry point
        """
        try:
            # Initialization sequence
            self.load_configuration()
            self.setup_logging()
            dc.logger.info(f"🔧 {dc.app_name_ver} starting up...")
            
            self.setup_event_system()
            self.setup_module_manager()
            self.setup_exception_handling()
            self.setup_signal_handlers()
            
            # Check if modules should be enabled
            if not dc.config.get("doorlockd", {}).get("enable_modules", True):
                dc.logger.warning("Modules are disabled in configuration")
                return
            
            # Initialize and run modules
            if self.initialize_modules():
                self.main_loop()
            
        except Exception as e:
            dc.logger.critical(f"Fatal error during startup: {e}")
            sys.exit(1)
        finally:
            self.shutdown()


def main():
    """
    Application entry point - creates and runs the DoorLockD Client
    """
    app = DoorLockDClient()
    app.run()


if __name__ == "__main__":
    main()
