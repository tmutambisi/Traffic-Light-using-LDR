# Traffic-Light-using-LDR
This project implements a light-dependent resistor (LDR) control system using a microcontroller to manage LED indicators based on ambient light levels. The software uses a simple state machine to toggle between green, amber, and red LEDs depending on whether it's day or night, as determined by the LDR readings.


## Overview
This is a light-dependent resistor (LDR) control system designed for managing LED indicators based on ambient light levels. This software automatically toggles between green, amber, and red LEDs, signaling whether it is day or night.

## Features
- **Day/Night Detection**: Automatically adjusts LED behavior based on light intensity.
- **LED Indicators**: Displays different colors (green, amber, red) to signal night and day states.
- **Customizable Threshold**: Easily adjustable light threshold for LDR sensitivity.

## Requirements
- Microcontroller with ADC capabilities (e.g., Raspberry Pi Pico)
- LDR sensor
- Three LEDs (red, green, amber)
- Appropriate resistors for LEDs and LDR

## Installation
1. Clone the repository to your local machine:
   ```
