# Smart-RFID-Door-Lock-System
DoorLockD Client is a sophisticated, modular access control system designed for Raspberry Pi that uses RFID technology for secure door access management. The system features a plugin architecture allowing easy extension and customization.
✨ Features
🔒 Secure RFID Access - Support for multiple RFID card types

🧩 Modular Architecture - Dynamic module loading and management

📊 Comprehensive Logging - Console and file logging with configurable levels

⚡ Event-Driven - Efficient inter-module communication system

🔧 Configurable - Easy TOML-based configuration

🚀 Production Ready - Proper signal handling and graceful shutdown

🏗️ System Architecture
Core Components
Data Container - Centralized data management

Module Manager - Dynamic module lifecycle management

Event System - Inter-module communication

I/O Wrapper - Hardware abstraction layer

Configuration Manager - TOML-based settings

Module Types
RFID Readers - MFRC522, PN532 support

Network Clients - MQTT, HTTP API

Access Control - User management, time restrictions

Notification - Email, SMS alerts

Logging - Advanced logging modules

🛠️ Installation
Prerequisites
bash
# Raspberry Pi OS
sudo apt update
sudo apt install python3 python3-pip git

# Enable SPI for RFID readers
sudo raspi-config
# Interface Options -> SPI -> Enable
Installation Steps
bash
# Clone repository
git clone https://github.com/amirmoba/doorlockd-client.git
cd doorlockd-client

# Install dependencies
pip3 install -r requirements.txt

# Configure system
cp config.ini.example config.ini
nano config.ini
⚙️ Configuration
Basic Configuration (config.ini)
toml
[doorlockd]
stderr_level = "INFO"
logfile_name = "doorlockd.log"
logfile_level = "DEBUG"
enable_modules = true

[module.rfid_reader]
type = "rfid_mfrc522"
enabled = true
spi_bus = 0
spi_device = 0
reset_pin = 25

[module.mqtt_client]
type = "mqtt"
enabled = true
broker = "mqtt.local"
port = 1883
🚀 Usage
Starting the Service
bash
# Development mode
python3 doorlockd_client.py

# Production mode (with systemd)
sudo systemctl enable doorlockd-client
sudo systemctl start doorlockd-client
Module Development
Create custom modules by extending the base module class:

python
from libs.Module import Module

class CustomRFIDReader(Module):
    def setup(self):
        self.logger.info("Initializing custom RFID reader")
        
    def enable(self):
        self.logger.info("Starting RFID scanning")
        
    def disable(self):
        self.logger.info("Stopping RFID reader")
🔌 Hardware Setup
RFID Reader Connection (MFRC522)
MFRC522 Pin	Raspberry Pi Pin
SDA	GPIO 8 (CE0)
SCK	GPIO 11 (SCLK)
MOSI	GPIO 10 (MOSI)
MISO	GPIO 9 (MISO)
GND	GND
RST	GPIO 25
3.3V	3.3V
📊 Logging
The system provides comprehensive logging:

python
# Log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
dc.logger.debug("Detailed debugging information")
dc.logger.info("System operation information")
dc.logger.warning("Warning messages")
dc.logger.error("Error conditions")
dc.logger.critical("Critical system failures")
🐛 Troubleshooting
Common Issues
SPI Not Enabled

bash
lsmod | grep spi
# Enable via raspi-config if missing
Permission Denied

bash
sudo usermod -a -G spi,gpio $USER
sudo reboot
Module Loading Failed

Check module configuration in config.ini

Verify module files exist in libs/Module/implementations/

🤝 Contributing
We welcome contributions! Please see our Contributing Guide for details.

Development Setup
bash
git clone https://github.com/amirmoba/doorlockd-client.git
cd doorlockd-client
python3 -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt
📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

👨‍💻 Developer
Amir Mobasheraghdam - Lead Developer & Maintainer

GitHub: @amirmoba

📞 Support
📚 Documentation

🐛 Issue Tracker

💬 Discussions

🙏 Acknowledgments
Raspberry Pi Foundation

RFID-RC522 community

Python packaging community
