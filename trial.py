import time
import RPi.GPIO as GPIO
import serial
import string
import pynmea2
import requests
import pywhatkit
from datetime import datetime,timedelta

# Setup GPIO for buzzer
#buzzer_pin = 24 
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(buzzer_pin, GPIO.OUT)
ser = serial.Serial('/dev/ttyACM0', 9600)
# Setup serial connection for GPS

# Function to read GPS data
def read_gps():
	current_time = datetime.now()
	scheduled_time = current_time + timedelta(seconds=30)
	gps_ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)
	dataout =pynmea2.NMEAStreamReader() 
	newdata=gps_ser.readline()
	if '$GPRMC' in str(newdata):
		newmsg=pynmea2.parse(newdata.decode('utf-8',errors='ignore'))  
		lat=str(newmsg.latitude) 
		lng=str(newmsg.longitude) 
		h = current_time.hour
		m = current_time.minute + 1
		return lat,lng, h ,m

# Main loop
detected = False
while True:
    line = ser.readline().decode('utf-8').strip()
    print("MQ3 Value:", line)
    
    # Check alcohol level
    if int(line) > 55 and not detected:
        #GPIO.output(buzzer_pin, GPIO.HIGH)
        print("Buzzer activated")
        
        # Read GPS coordinates and get location
        latitude, longitude, h, m = read_gps()

        emer = f'High Alcohol level : http://maps.google.com/?q={latitude},{longitude}'
        # Send location via WhatsApp
        pywhatkit.sendwhatmsg('+916363999471', emer ,h,m,32)
        
        detected = True
    elif int(line) <= 100 and detected:
        #GPIO.output(buzzer_pin, GPIO.LOW)
        detected = False

    time.sleep(3)
