#sudo raspi-config
#sudo apt-get install RPi.GPIO
# or
#sudo apt-get install python3-rpi.gpio 


import RPi.GPIO as GPIO
 
import time

GPIO.setmode(GPIO.BOARD)
 
 
 
# Set up GPIO pin 4 as an output
 
LED_PIN = 7
 
GPIO.setup(LED_PIN, GPIO.OUT)
 
 
 
try:
 
    while True:
 
        # Turn the LED on
 
        GPIO.output(LED_PIN, GPIO.HIGH)
 
        time.sleep(1)  # Wait for 1 second
 
 
 
        # Turn the LED off
 
        GPIO.output(LED_PIN, GPIO.LOW)
 
        time.sleep(1)  # Wait for 1 second
 
 
 
except KeyboardInterrupt:
 
    # Cleanup GPIO settings before exiting
 
    GPIO.cleanup()
