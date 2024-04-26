# Driver Drowsiness Detection with Alcohol Sensor

This project combines driver drowsiness detection using facial recognition with Haar cascades and alcohol sensing using an alcohol sensor module. The system is designed to run on a Raspberry Pi and sends alerts via WhatsApp when signs of drowsiness or alcohol consumption are detected. Additionally, an MQ-3 alcohol sensor connected to an Arduino sends its value to the Raspberry Pi, which then uses a GPS module and a buzzer to alert the driver in real-time.

## Features

- Detects driver drowsiness based on facial landmarks and eye movement.
- Monitors alcohol levels using an MQ-3 alcohol sensor module connected to an Arduino, with the value sent to the Raspberry Pi.
- Sends real-time alerts via WhatsApp when drowsiness or high alcohol levels are detected.
- Uses a GPS module connected to the Raspberry Pi to get the current location and a buzzer to alert the driver.

## Prerequisites

- Raspberry Pi with Raspbian OS
- Arduino (for MQ-3 sensor)
- Python 3 installed on Raspberry Pi
- Required Python libraries:
 - OpenCV
 - PyWhatKit
 - RPi.GPIO
 - picamera2
 - pynmea2
 - gpiozero
- Alcohol sensor module (e.g., MQ-3)
- Webcam module compatible with Raspberry Pi (e.g., PiCamera v2)
- GPS module compatible with Raspberry Pi
- Buzzer

## Installation

1. Clone the repository:
```bash git clone https://github.com/Hariram-6674/Driver-Drowsiness-Detection-with-Alcohol-Sensor.git```

2. Install required Python libraries:
```bash pip3 install opencv-python pywhatkit picamera2 pynmea2 gpiozero```

3. Connect the alcohol sensor module to the Arduino and the Arduino to the Raspberry Pi.
4. Connect the GPS module and the buzzer to the Raspberry Pi GPIO pins.

## Usage

1. Run the main script `drowsiness_alcohol_detection.py`
2. Run the alert script `trial.py`
3. The script will continuously monitor for signs of drowsiness and alcohol consumption.
4. If drowsiness or high alcohol levels are detected, an alert will be sent via WhatsApp, and the GPS module will provide the current location. A buzzer will also sound to alert the driver.

## Configuration

- **WhatsApp API Credentials**: Ensure that you have configured PyWhatKit with your WhatsApp API credentials. You can do this by following the instructions in the PyWhatKit documentation.
- **Alcohol Sensor Calibration**: Adjust the alcohol sensor threshold in the code according to your sensor's sensitivity and calibration.





