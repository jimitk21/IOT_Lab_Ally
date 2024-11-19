#sudo raspi-config
#sudo apt-get install RPi.GPIO
# or
#sudo apt-get install python3-rpi.gpio 


import RPi.GPIO as GPIO
import time

# Use BOARD pin numbering
GPIO.setmode(GPIO.BOARD)

# Define the GPIO pins for the LED and the button
LED_PIN = 7
BUTTON_PIN = 40

# Set up the GPIO pins
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Internal pull-up

try:
    while True:
        # Read the state of the button
        button_state = GPIO.input(BUTTON_PIN)

        if button_state == GPIO.LOW:  # Button pressed
            GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on LED
        else:
            GPIO.output(LED_PIN, GPIO.LOW)  # Turn off LED

        time.sleep(0.05)  # Reduce delay for better responsiveness

except KeyboardInterrupt:
    print("Exiting...")
finally:
    # Clean up GPIO settings
    GPIO.cleanup()
