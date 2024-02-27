# Automatic Shades

**Shawn Brutus. Nick Ek, Ethan Secakusuma**

### Description

The Automatic Shades project is designed to automate the control of window shades based on environmental conditions. It utilizes a Raspberry Pi 4B along with various sensors and a motor to adjust the shades automatically.

### Key Features

- **Temperature Regulation:** Automatically adjust the shades based on temperature readings from the temperature sensor to maintain optimal indoor conditions.
  
- **Light Sensing:** Utilize the light sensor to adjust the shades according to the ambient light levels, providing comfort and energy efficiency.

- **User Interface:** Incorporate a touch screen for GUI (Graphical User Interface) to allow users to interact with the system and manually control the shades if needed.

### Bill of Materials

- 1x - **Raspberry Pi 4B**
- 1x - **Digital Thermometer Temperature Sensor: DS18B20**
- 1x - **Photoresistor: Ky-018**
- 1x - **Analog to Digital Converter: ADS1115**

### Installation

Follow these steps to set up the Automatic Shades project:

1. Connect the Raspberry Pi 4B to the necessary peripherals and ensure it is properly configured.
   
3. Install the required libraries and dependencies for the sensors and motor control.
   
4. Clone the project repository:
   ```bash
   git clone https://github.com/nickek/Automatic_Shades.git
   
5. In the project directory create a python virtual environment:
   ```bash
   python3 -m venv venv
   
6. Then activate the virtual environment:
   ```bash
   source venv\bin\activate
   
7. Once you are in the virtual environment, pip install the requirements document:
   ```bash
   pip3 install -r requirements.txt
   
8. When you have the neccessary libraries and dependencies installed, you can run the program:
   ```bash
   python3 main.py
