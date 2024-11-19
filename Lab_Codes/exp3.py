#Lab - 3 
#Configure GPIO of RPi
#sudo apt-get update  
#sudo apt-get install python3-rpi.gpio 
 
#Task - 1 
 
import RPi.GPIO as GPIO
 
import time
 
 
#Task 2
 
import RPi.GPIO as GPIO
 
import time
 
 
 
# Set up the GPIO mode
 
GPIO.setmode(GPIO.BCM)
 
# Define the GPIO pins for the LED and the button
 
LED_PIN =  4
 
BUTTON_PIN = 21
 
# Set up the GPIO pins
 
GPIO.setup(LED_PIN, GPIO.OUT)
 
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Use an internal pull-up resistor
 
try:
 
    while True:
 
        # Read the state of the button
 
        button_state = GPIO.input(BUTTON_PIN)
 
         
 
        if button_state == GPIO.LOW:  # Button is pressed
 
            GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on LED
 
        else:
 
            GPIO.output(LED_PIN, GPIO.LOW)  # Turn off LED
 
         
 
        time.sleep(0.1)  # Small delay to debounce the button
 
except KeyboardInterrupt:
 
    # Clean up GPIO settings before exiting
 
    GPIO.cleanup()
 
 
 
# Use the board pin numbering
 
GPIO.setmode(GPIO.BCM)
 
 
 
# Set up GPIO pin 4 as an output
 
LED_PIN = 4
 
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
 
 