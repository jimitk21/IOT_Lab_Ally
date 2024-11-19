# python3 -m venv myenv
# source myenv/bin/activate
# pip3 install RPi.GPIO
# pip3 install requests

import RPi.GPIO as GPIO
import requests
import time

# Setup GPIO pins
LED_PIN = 4
SERVO_PIN = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Servo PWM setup
pwm = GPIO.PWM(SERVO_PIN, 50)  # 50Hz frequency
pwm.start(0)

# ThingSpeak API details
CHANNEL_ID = '2741373'
WRITE_API_KEY = 'HT7036XQF47NLNWZ'
READ_API_KEY = '0RED8G4EOYFH0C0A'
READ_API_URL = f'https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json?api_key={READ_API_KEY}&results=1'

def set_led(state):
    GPIO.output(LED_PIN, GPIO.HIGH if state == '1' else GPIO.LOW)

def set_servo(angle):
    duty = 2 + (angle / 18)
    GPIO.output(SERVO_PIN, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)
    GPIO.output(SERVO_PIN, False)
    pwm.ChangeDutyCycle(0)

try:
    while True:
        response = requests.get(READ_API_URL)
        data = response.json()

        # Check if 'feeds' has data
        if 'feeds' in data and data['feeds']:
            led_state = data['feeds'][0].get('field1')
            servo_angle = data['feeds'][0].get('field2')

            # Check if fields are not None
            if led_state is not None and servo_angle is not None:
                servo_angle = int(servo_angle)  # Convert servo angle to integer
                set_led(led_state)
                set_servo(servo_angle)
            else:
                print("Missing data for LED state or servo angle")
        else:
            print("No data received from ThingSpeak")

        time.sleep(15)  # Wait before the next update
except KeyboardInterrupt:
    print("Experiment stopped")
finally:
    pwm.stop()
    GPIO.cleanup()


#cmd code aane biji file ma banavje same folder

import requests

write_api_key = 'HT7036XQF47NLNWZ'
field1_value = 0  # Example value for LED Control
field2_value = 5 # Example value for Servo Position

url = f"https://api.thingspeak.com/update?api_key={write_api_key}&field1={field1_value}&field2={field2_value}"
response = requests.get(url)
print(response.text)