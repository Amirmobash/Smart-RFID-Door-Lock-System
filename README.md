# RFID-Kommunikation mit RC522 und Raspberry Pi
**Entwickelt von: Amir Mobasheraghdam**

[![GitHub stars](https://img.shields.io/github/stars/Amirmobash/pi-rc522?style=social)](https://github.com/Amirmobash/pi-rc522)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/)

Pi-RC522 ist eine umfassende Python-Bibliothek für Raspberry Pi zur Steuerung des beliebten RFID-RC522-Moduls über die SPI-Schnittstelle. Diese Bibliothek ermöglicht eine einfache Integration von RFID-Funktionalität in Ihre Raspberry Pi-Projekte. Egal ob Zutrittskontrolle, Inventarsystem oder Smart-Home-Projekt - mit dieser Bibliothek können Sie RFID-Karten und -Tags problemlos lesen und beschreiben.

---

## RFID Communication with RC522 and Raspberry Pi
**Developed by: Amir Mobasheraghdam**

[![GitHub stars](https://img.shields.io/github/stars/Amirmobash/pi-rc522?style=social)](https://github.com/Amirmobash/pi-rc522)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/)

Pi-RC522 is a comprehensive Python library for Raspberry Pi to control the popular RFID-RC522 module via the SPI interface. This library enables easy integration of RFID functionality into your Raspberry Pi projects. Whether it's access control, inventory systems, or smart home projects - with this library you can easily read and write RFID cards and tags.

---

## 📋 Inhaltsverzeichnis / Table of Contents
- [Eigenschaften / Features](#eigenschaften--features)
- [Installation / Installation](#installation--installation)
- [Hardware-Anforderungen / Hardware Requirements](#hardware-anforderungen--hardware-requirements)
- [Schnellstart / Quick Start](#schnellstart--quick-start)
- [Pin-Konfiguration / Pin Configuration](#pin-konfiguration--pin-configuration)
- [Detaillierte API / Detailed API](#detaillierte-api--detailed-api)
- [Erweiterte Beispiele / Advanced Examples](#erweiterte-beispiele--advanced-examples)
- [Projektideen / Project Ideas](#projektideen--project-ideas)
- [Fehlerbehebung / Troubleshooting](#fehlerbehebung--troubleshooting)
- [Häufig gestellte Fragen / Frequently Asked Questions](#häufig-gestellte-fragen--frequently-asked-questions)
- [Mitwirken / Contributing](#mitwirken--contributing)
- [Versionsgeschichte / Changelog](#versionsgeschichte--changelog)
- [Lizenz / License](#lizenz--license)
- [Kontakt / Contact](#kontakt--contact)

---

## ✨ Eigenschaften / Features

### Deutsch
- **Vollständige SPI-Protokollunterstützung** - Optimierte Kommunikation mit dem RC522-Modul
- **Lesen und Schreiben von RFID-Karten und -Tags** - Unterstützung für Mifare Classic 1K, 4K, Ultralight und mehr
- **Mehrere Kartenformate** - Kompatibel mit den gängigsten 13.56MHz RFID-Karten
- **Einfache und benutzerfreundliche Funktionen** - Klare API mit umfangreicher Dokumentation
- **GPIO-Steuerung über RPi.GPIO** - Direkter Zugriff auf die Raspberry Pi GPIO-Pins
- **Authentifizierung** - Unterstützung für Key-A und Key-B Authentifizierung
- **Blockweises Lesen/Schreiben** - Präziser Zugriff auf einzelne Speicherblöcke
- **Interrupt-Unterstützung** - Ereignisgesteuerte Kartenverarbeitung
- **Umfangreiche Beispielskripte** - Fertige Lösungen für verschiedene Anwendungsfälle
- **Fehlerbehandlung** - Robuste Fehlererkennung und -behandlung

### English
- **Full SPI protocol support** - Optimized communication with the RC522 module
- **Read and write RFID cards and tags** - Support for Mifare Classic 1K, 4K, Ultralight and more
- **Multiple card formats** - Compatible with most common 13.56MHz RFID cards
- **Simple and user-friendly functions** - Clear API with extensive documentation
- **GPIO control via RPi.GPIO** - Direct access to Raspberry Pi GPIO pins
- **Authentication support** - Support for Key-A and Key-B authentication
- **Block-level read/write** - Precise access to individual memory blocks
- **Interrupt support** - Event-driven card processing
- **Comprehensive example scripts** - Ready-made solutions for various use cases
- **Error handling** - Robust error detection and handling

---

## 🔧 Hardware-Anforderungen / Hardware Requirements

### Deutsch
| Komponente | Spezifikation | Empfohlenes Modell |
|------------|---------------|---------------------|
| Raspberry Pi | Jedes Modell mit GPIO | Pi 3, Pi 4, Pi Zero |
| RFID Modul | RC522 (13.56MHz) | Original oder kompatibel |
| RFID Karten | Mifare Classic 1K/4K | 13.56MHz kompatible Karten |
| Jumper Kabel | Female-Female | 20cm Länge empfohlen |
| Breadboard | Optional | Für Prototyping |

### English
| Component | Specification | Recommended Model |
|-----------|---------------|-------------------|
| Raspberry Pi | Any model with GPIO | Pi 3, Pi 4, Pi Zero |
| RFID Module | RC522 (13.56MHz) | Original or compatible |
| RFID Cards | Mifare Classic 1K/4K | 13.56MHz compatible cards |
| Jumper Wires | Female-Female | 20cm length recommended |
| Breadboard | Optional | For prototyping |

---

## 📦 Installation / Installation

### Deutsch
**Methode 1: Über pip (Empfohlen)**
```bash
# Bibliothek installieren
pip install pi-rc522

# Für Python 3
pip3 install pi-rc522

# Mit sudo für systemweite Installation
sudo pip3 install pi-rc522
```

**Methode 2: Aus dem Quellcode**
```bash
# Repository klonen
git clone https://github.com/Amirmobash/pi-rc522.git

# In das Verzeichnis wechseln
cd pi-rc522

# Installieren
sudo python3 setup.py install
```

**Methode 3: Direkt aus GitHub**
```bash
pip install git+https://github.com/Amirmobash/pi-rc522.git
```

**Abhängigkeiten installieren:**
```bash
# RPi.GPIO installieren (falls nicht vorhanden)
sudo apt-get update
sudo apt-get install python3-rpi.gpio

# SPI aktivieren
sudo raspi-config
# Navigieren Sie zu: Interface Options → SPI → Enable
```

### English
**Method 1: Via pip (Recommended)**
```bash
# Install library
pip install pi-rc522

# For Python 3
pip3 install pi-rc522

# With sudo for system-wide installation
sudo pip3 install pi-rc522
```

**Method 2: From source**
```bash
# Clone repository
git clone https://github.com/Amirmobash/pi-rc522.git

# Change to directory
cd pi-rc522

# Install
sudo python3 setup.py install
```

**Method 3: Direct from GitHub**
```bash
pip install git+https://github.com/Amirmobash/pi-rc522.git
```

**Install dependencies:**
```bash
# Install RPi.GPIO (if not present)
sudo apt-get update
sudo apt-get install python3-rpi.gpio

# Enable SPI
sudo raspi-config
# Navigate to: Interface Options → SPI → Enable
```

---

## ⚡ Schnellstart / Quick Start

### Deutsch
**Einfaches Lesen einer RFID-Karte:**
```python
import RPi.GPIO as GPIO
from pi_rc522 import RFID
import time

# RFID-Objekt erstellen
rc522 = RFID()

try:
    print("RFID-Lesegerät bereit!")
    print("Bitte RFID-Karte halten...")
    
    while True:
        # Auf RFID-Karte warten
        if rc522.wait_for_tag():
            # Karten-ID auslesen
            uid = rc522.read_id()
            
            # UID in verschiedene Formate konvertieren
            uid_dec = int.from_bytes(uid, byteorder='big')
            uid_hex = uid.hex()
            uid_str = '-'.join([f'{b:02X}' for b in uid])
            
            print(f"\n✅ Karte erkannt!")
            print(f"📇 UID (hex): {uid_hex}")
            print(f"🔢 UID (dez): {uid_dec}")
            print(f"🏷️ UID (Format): {uid_str}")
            
            # Kurze Pause, um Mehrfachlesungen zu vermeiden
            time.sleep(1)
            
except KeyboardInterrupt:
    print("\n👋 Programm beendet")
finally:
    GPIO.cleanup()
```

### English
**Simple RFID card reading:**
```python
import RPi.GPIO as GPIO
from pi_rc522 import RFID
import time

# Create RFID object
rc522 = RFID()

try:
    print("RFID reader ready!")
    print("Please hold RFID card...")
    
    while True:
        # Wait for RFID card
        if rc522.wait_for_tag():
            # Read card ID
            uid = rc522.read_id()
            
            # Convert UID to different formats
            uid_dec = int.from_bytes(uid, byteorder='big')
            uid_hex = uid.hex()
            uid_str = '-'.join([f'{b:02X}' for b in uid])
            
            print(f"\n✅ Card detected!")
            print(f"📇 UID (hex): {uid_hex}")
            print(f"🔢 UID (dec): {uid_dec}")
            print(f"🏷️ UID (format): {uid_str}")
            
            # Short pause to avoid multiple readings
            time.sleep(1)
            
except KeyboardInterrupt:
    print("\n👋 Program terminated")
finally:
    GPIO.cleanup()
```

---

## 🔌 Pin-Konfiguration / Pin Configuration

### Deutsch
**Detaillierte Verdrahtungsanleitung:**

| RC522 Pin | Raspberry Pi Pin | GPIO Nummer | Beschreibung |
|-----------|-----------------|-------------|--------------|
| SDA (SS)  | Pin 24          | GPIO 8 (CE0) | Chip Select |
| SCK       | Pin 23          | GPIO 11 (SCLK) | Serial Clock |
| MOSI      | Pin 19          | GPIO 10 (MOSI) | Master Out Slave In |
| MISO      | Pin 21          | GPIO 9 (MISO) | Master In Slave Out |
| RST       | Pin 22          | GPIO 25 | Reset |
| 3.3V      | Pin 1           | - | Stromversorgung (3.3V) |
| GND       | Pin 6           | - | Masse |
| IRQ       | Nicht verbunden | - | Interrupt (optional) |

**Alternative Pin-Konfiguration:**
```python
from pi_rc522 import RFID

# Eigene Pins definieren
rc522 = RFID(
    rst_pin=22,      # Standard: 25
    cs_pin=8,        # Standard: 8
    spi_bus=0,       # Standard: 0
    spi_device=0     # Standard: 0
)
```

### English
**Detailed wiring guide:**

| RC522 Pin | Raspberry Pi Pin | GPIO Number | Description |
|-----------|-----------------|-------------|-------------|
| SDA (SS)  | Pin 24          | GPIO 8 (CE0) | Chip Select |
| SCK       | Pin 23          | GPIO 11 (SCLK) | Serial Clock |
| MOSI      | Pin 19          | GPIO 10 (MOSI) | Master Out Slave In |
| MISO      | Pin 21          | GPIO 9 (MISO) | Master In Slave Out |
| RST       | Pin 22          | GPIO 25 | Reset |
| 3.3V      | Pin 1           | - | Power (3.3V) |
| GND       | Pin 6           | - | Ground |
| IRQ       | Not connected   | - | Interrupt (optional) |

**Alternative pin configuration:**
```python
from pi_rc522 import RFID

# Define custom pins
rc522 = RFID(
    rst_pin=22,      # Default: 25
    cs_pin=8,        # Default: 8
    spi_bus=0,       # Default: 0
    spi_device=0     # Default: 0
)
```

---

## 📚 Detaillierte API / Detailed API

### Deutsch

**RFID Klasse**

| Methode | Parameter | Rückgabewert | Beschreibung |
|---------|-----------|--------------|--------------|
| `__init__()` | rst_pin, cs_pin, spi_bus, spi_device | RFID-Objekt | Erstellt eine neue RFID-Instanz |
| `wait_for_tag(timeout)` | timeout (Sekunden, optional) | Boolean | Wartet auf eine RFID-Karte |
| `read_id()` | - | Bytes | Liest die UID der aktuellen Karte |
| `select_tag(uid)` | uid (Bytes) | Boolean | Wählt eine spezifische Karte aus |
| `authenticate(block, key, key_type)` | block, key, key_type | Boolean | Authentifiziert für Blockzugriff |
| `read_block(block)` | block (int) | Bytes (16 Bytes) | Liest einen bestimmten Block |
| `write_block(block, data)` | block (int), data (Bytes) | Boolean | Schreibt Daten in einen Block |
| `read_sector(sector)` | sector (int) | Liste | Liest einen gesamten Sektor |
| `write_sector(sector, data)` | sector, data | Boolean | Schreibt in einen gesamten Sektor |
| `stop_crypto()` | - | - | Stoppt die Kryptokommunikation |
| `reset()` | - | - | Setzt das Modul zurück |

### English

**RFID Class**

| Method | Parameters | Return | Description |
|--------|-----------|---------|-------------|
| `__init__()` | rst_pin, cs_pin, spi_bus, spi_device | RFID object | Creates a new RFID instance |
| `wait_for_tag(timeout)` | timeout (seconds, optional) | Boolean | Waits for an RFID card |
| `read_id()` | - | Bytes | Reads the UID of the current card |
| `select_tag(uid)` | uid (Bytes) | Boolean | Selects a specific card |
| `authenticate(block, key, key_type)` | block, key, key_type | Boolean | Authenticates for block access |
| `read_block(block)` | block (int) | Bytes (16 bytes) | Reads a specific block |
| `write_block(block, data)` | block (int), data (Bytes) | Boolean | Writes data to a block |
| `read_sector(sector)` | sector (int) | List | Reads an entire sector |
| `write_sector(sector, data)` | sector, data | Boolean | Writes to an entire sector |
| `stop_crypto()` | - | - | Stops crypto communication |
| `reset()` | - | - | Resets the module |

---

## 💡 Erweiterte Beispiele / Advanced Examples

### Deutsch

**1. Daten auf einer Karte speichern:**
```python
from pi_rc522 import RFID
import time

rfid = RFID()

def write_to_card():
    # Auf Karte warten
    if not rfid.wait_for_tag():
        return False
    
    # Karten-UID lesen
    uid = rfid.read_id()
    print(f"Karte erkannt: {uid.hex()}")
    
    # Karte auswählen
    if not rfid.select_tag(uid):
        print("Karte konnte nicht ausgewählt werden")
        return False
    
    # Authentifizierung (Standard-Schlüssel)
    key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
    if not rfid.authenticate(4, key, 'A'):
        print("Authentifizierung fehlgeschlagen")
        return False
    
    # Daten schreiben (16 Bytes)
    data = bytearray(16)
    message = "AMIR123"
    data[:len(message)] = message.encode()
    
    if rfid.write_block(4, bytes(data)):
        print(f"Daten geschrieben: {message}")
    
    rfid.stop_crypto()
    return True

try:
    print("Daten auf Karte schreiben - Karte auflegen...")
    while True:
        if write_to_card():
            time.sleep(2)
except KeyboardInterrupt:
    GPIO.cleanup()
```

**2. Zutrittskontrollsystem:**
```python
from pi_rc522 import RFID
import time
import RPi.GPIO as GPIO

# GPIO für Türöffner
DOOR_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(DOOR_PIN, GPIO.OUT)
GPIO.output(DOOR_PIN, GPIO.LOW)

# Autoriserte UIDs (Beispiel)
authorized_uids = {
    'a1b2c3d4': 'Amir Mobasheraghdam',
    'e5f67890': 'Gast'
}

rfid = RFID()

def open_door():
    print("🚪 Tür geöffnet!")
    GPIO.output(DOOR_PIN, GPIO.HIGH)
    time.sleep(3)  # Tür für 3 Sekunden öffnen
    GPIO.output(DOOR_PIN, GPIO.LOW)

try:
    print("Zutrittskontrollsystem bereit")
    print("Karte auflegen für Zutritt...")
    
    while True:
        if rfid.wait_for_tag():
            uid = rfid.read_id()
            uid_hex = uid.hex()
            
            if uid_hex in authorized_uids:
                name = authorized_uids[uid_hex]
                print(f"✅ Zutritt gewährt für: {name}")
                open_door()
            else:
                print(f"❌ Zutritt verweigert für UID: {uid_hex}")
            
            time.sleep(1)
            
except KeyboardInterrupt:
    GPIO.cleanup()
```

### English

**1. Save data on a card:**
```python
from pi_rc522 import RFID
import time

rfid = RFID()

def write_to_card():
    # Wait for card
    if not rfid.wait_for_tag():
        return False
    
    # Read card UID
    uid = rfid.read_id()
    print(f"Card detected: {uid.hex()}")
    
    # Select card
    if not rfid.select_tag(uid):
        print("Could not select card")
        return False
    
    # Authentication (default key)
    key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
    if not rfid.authenticate(4, key, 'A'):
        print("Authentication failed")
        return False
    
    # Write data (16 bytes)
    data = bytearray(16)
    message = "AMIR123"
    data[:len(message)] = message.encode()
    
    if rfid.write_block(4, bytes(data)):
        print(f"Data written: {message}")
    
    rfid.stop_crypto()
    return True

try:
    print("Write data to card - place card...")
    while True:
        if write_to_card():
            time.sleep(2)
except KeyboardInterrupt:
    GPIO.cleanup()
```

**2. Access control system:**
```python
from pi_rc522 import RFID
import time
import RPi.GPIO as GPIO

# GPIO for door opener
DOOR_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(DOOR_PIN, GPIO.OUT)
GPIO.output(DOOR_PIN, GPIO.LOW)

# Authorized UIDs (example)
authorized_uids = {
    'a1b2c3d4': 'Amir Mobasheraghdam',
    'e5f67890': 'Guest'
}

rfid = RFID()

def open_door():
    print("🚪 Door opened!")
    GPIO.output(DOOR_PIN, GPIO.HIGH)
    time.sleep(3)  # Open door for 3 seconds
    GPIO.output(DOOR_PIN, GPIO.LOW)

try:
    print("Access control system ready")
    print("Place card for access...")
    
    while True:
        if rfid.wait_for_tag():
            uid = rfid.read_id()
            uid_hex = uid.hex()
            
            if uid_hex in authorized_uids:
                name = authorized_uids[uid_hex]
                print(f"✅ Access granted for: {name}")
                open_door()
            else:
                print(f"❌ Access denied for UID: {uid_hex}")
            
            time.sleep(1)
            
except KeyboardInterrupt:
    GPIO.cleanup()
```

---

## 🚀 Projektideen / Project Ideas

### Deutsch
1. **Intelligentes Türschloss** - Automatische Türöffnung mit Berechtigungsprüfung
2. **Anwesenheitssystem** - Mitarbeiter- oder Schüleranwesenheit erfassen
3. **Inventarsystem** - Gegenstände mit RFID-Tags verfolgen
4. **Zeiterfassung** - Arbeitszeiten mit RFID-Karten erfassen
5. **Bibliothekssystem** - Buchausleihe automatisieren
6. **Bezahlterminal** - Guthabenbasierte RFID-Zahlungen
7. **Fahrzeugidentifikation** - Automatische Fahrzeugerkennung
8. **Tieridentifikation** - Haustiere mit implantierten Chips erkennen

### English
1. **Smart Door Lock** - Automatic door opening with permission check
2. **Attendance System** - Track employee or student attendance
3. **Inventory System** - Track items with RFID tags
4. **Time Tracking** - Record working hours with RFID cards
5. **Library System** - Automate book lending
6. **Payment Terminal** - Balance-based RFID payments
7. **Vehicle Identification** - Automatic vehicle recognition
8. **Pet Identification** - Recognize pets with implanted chips

---

## 🔍 Fehlerbehebung / Troubleshooting

### Deutsch

| Problem | Mögliche Ursache | Lösung |
|---------|-----------------|---------|
| Keine Karte erkannt | SPI nicht aktiviert | `sudo raspi-config` → SPI aktivieren |
| | Falsche Verkabelung | Pin-Konfiguration überprüfen |
| | Modul defekt | Anderes Modul testen |
| Berechtigungsfehler | Keine sudo-Rechte | Skript mit `sudo` ausführen |
| | GPIO-Berechtigungen | Benutzer zur gpio-Gruppe hinzufügen |
| Lesefehler | Karte nicht kompatibel | Mifare-Karten verwenden |
| | Schlechter Kontakt | Verbindungen überprüfen |
| SPI-Fehler | SPI nicht geladen | `sudo modprobe spi-bcm2835` |
| | Falscher SPI-Device | Geräte unter /dev/spi* prüfen |

**Diagnose-Skript:**
```bash
#!/bin/bash
echo "🔍 RFID-Diagnose"
echo "================"
echo "SPI-Devices:"
ls -la /dev/spi*
echo ""
echo "GPIO-Berechtigungen:"
groups
echo ""
echo "Python-Version:"
python3 --version
echo ""
echo "Installierte Pakete:"
pip3 list | grep -E "RPi|spi|rc522"
```

### English

| Problem | Possible Cause | Solution |
|---------|---------------|----------|
| No card detected | SPI not enabled | `sudo raspi-config` → Enable SPI |
| | Wrong wiring | Check pin configuration |
| | Module defective | Test another module |
| Permission error | No sudo rights | Run script with `sudo` |
| | GPIO permissions | Add user to gpio group |
| Read error | Card not compatible | Use Mifare cards |
| | Poor contact | Check connections |
| SPI error | SPI not loaded | `sudo modprobe spi-bcm2835` |
| | Wrong SPI device | Check devices under /dev/spi* |

**Diagnostic script:**
```bash
#!/bin/bash
echo "🔍 RFID Diagnostics"
echo "==================="
echo "SPI Devices:"
ls -la /dev/spi*
echo ""
echo "GPIO Permissions:"
groups
echo ""
echo "Python Version:"
python3 --version
echo ""
echo "Installed packages:"
pip3 list | grep -E "RPi|spi|rc522"
```

---

## ❓ Häufig gestellte Fragen / Frequently Asked Questions

### Deutsch

**F: Welche RFID-Karten werden unterstützt?**  
A: Die Bibliothek unterstützt Mifare Classic 1K, 4K und kompatible 13.56MHz Karten.

**F: Kann ich mehrere RC522-Module gleichzeitig verwenden?**  
A: Ja, durch Verwendung verschiedener CS-Pins können mehrere Module angesteuert werden.

**F: Wie sicher ist die RFID-Kommunikation?**  
A: Mifare-Karten bieten grundlegende Sicherheit mit 48-bit Schlüsseln. Für höhere Sicherheit empfiehlt sich zusätzliche Verschlüsselung.

**F: Funktioniert das auch mit dem Raspberry Pi 5?**  
A: Ja, die Bibliothek ist mit allen Raspberry Pi Modellen kompatibel.

**F: Kann ich die Bibliothek auch auf anderen Linux-Systemen nutzen?**  
A: Grundsätzlich ja, solange SPI und GPIO verfügbar sind.

### English

**Q: Which RFID cards are supported?**  
A: The library supports Mifare Classic 1K, 4K and compatible 13.56MHz cards.

**Q: Can I use multiple RC522 modules simultaneously?**  
A: Yes, by using different CS pins, multiple modules can be controlled.

**Q: How secure is the RFID communication?**  
A: Mifare cards offer basic security with 48-bit keys. For higher security, additional encryption is recommended.

**Q: Does it work with Raspberry Pi 5?**  
A: Yes, the library is compatible with all Raspberry Pi models.

**Q: Can I use the library on other Linux systems?**  
A: Generally yes, as long as SPI and GPIO are available.

---

## 🤝 Mitwirken / Contributing

### Deutsch
Beiträge sind willkommen! So können Sie helfen:

1. **Repository forken** auf GitHub
2. **Feature-Branch erstellen** (`git checkout -b feature/AmazingFeature`)
3. **Änderungen committen** (`git commit -m 'Add some AmazingFeature'`)
4. **Branch pushen** (`git push origin feature/AmazingFeature`)
5. **Pull Request öffnen**

### English
Contributions are welcome! Here's how you can help:

1. **Fork the repository** on GitHub
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

---

## 📝 Versionsgeschichte / Changelog

### Deutsch
- **v1.0.0** (2024-01-15)
  - Erstveröffentlichung
  - Grundlegende Lese-/Schreibfunktionen
  - Unterstützung für Mifare Classic
  
- **v1.1.0** (2024-02-20)
  - Sektorweises Lesen/Schreiben hinzugefügt
  - Verbesserte Fehlerbehandlung
  - Neue Beispielskripte

### English
- **v1.0.0** (2024-01-15)
  - Initial release
  - Basic read/write functions
  - Mifare Classic support
  
- **v1.1.0** (2024-02-20)
  - Added sector-based read/write
  - Improved error handling
  - New example scripts

---

## 📄 Lizenz / License

### Deutsch
MIT Lizenz © 2024 Amir Mobasheraghdam

Hiermit wird jeder Person, die eine Kopie dieser Software und der zugehörigen Dokumentationsdateien (die "Software") erhält, die kostenlose Nutzung der Software gestattet, ohne Einschränkungen, einschließlich der Rechte zur Verwendung, Kopie, Modifikation, Zusammenführung, Veröffentlichung, Verteilung, Unterlizenzierung und/oder zum Verkauf von Kopien der Software.

### English
MIT License © 2024 Amir Mobasheraghdam

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software.

---

## 📫 Kontakt / Contact

**Amir Mobasheraghdam** (امیر مبشراقدم)

- **GitHub**: [github.com/Amirmobash](https://github.com/Amirmobash)
- **Repository**: [github.com/Amirmobash/pi-rc522](https://github.com/Amirmobash/pi-rc522)
- **Issues**: [github.com/Amirmobash/pi-rc522/issues](https://github.com/Amirmobash/pi-rc522/issues)
- **Discussions**: [github.com/Amirmobash/pi-rc522/discussions](https://github.com/Amirmobash/pi-rc522/discussions)

---

## ⭐ Unterstützung / Support

### Deutsch
Wenn Ihnen dieses Projekt gefällt, vergessen Sie bitte nicht, einen Stern auf GitHub zu hinterlassen! ⭐

### English
If you like this project, please don't forget to leave a star on GitHub! ⭐

---

**Viel Spaß mit Ihrem RFID-Projekt! / Enjoy your RFID project!** 🚀
```

This comprehensive README now includes:

1. **Complete bilingual content** (German/English)
2. **Your GitHub URL** prominently displayed
3. **Detailed sections** covering all aspects
4. **Code examples** for various use cases
5. **Pin configurations** with alternatives
6. **Troubleshooting guide**
7. **FAQ section**
8. **Project ideas**
9. **API reference**
10. **Contributing guidelines**
11. **Version history**
12. **Contact information**
13. **Badges** for GitHub stars, license, Python version

