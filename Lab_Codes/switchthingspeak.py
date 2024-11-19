import RPi.GPIO as GPIO
import requests
import time

# GPIO Setup
GPIO.setmode(GPIO.BOARD)

# Define GPIO pins
BUTTON_PIN = 40  # Pin connected to the button
LED_PIN = 7      # Optional: LED to indicate switch state

# Setup GPIO pins
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Button with pull-up resistor
GPIO.setup(LED_PIN, GPIO.OUT)

# ThingSpeak API details
WRITE_API_KEY = 'HT7036XQF47NLNWZ'
THING_URL = f"https://api.thingspeak.com/update?api_key={WRITE_API_KEY}"

# Initialize state
previous_state = None  # To track state changes

def send_to_thingspeak(state):
    """
    Sends the switch state to ThingSpeak.
    """
    payload = {'field1': state}  # Send state in field1
    try:
        response = requests.get(THING_URL, params=payload)
        if response.status_code == 200:
            print(f"State {state} sent to ThingSpeak successfully: {response.text}")
        else:
            print(f"Failed to send data to ThingSpeak. Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error sending data to ThingSpeak: {e}")

try:
    print("Monitoring the switch. Press CTRL+C to exit.")
    while True:
        # Read the button state
        button_state = GPIO.input(BUTTON_PIN)
        current_state = "High" if button_state == GPIO.LOW else "Low"  # Button pressed is "High"

        # Turn the LED on/off based on the state
        GPIO.output(LED_PIN, GPIO.HIGH if current_state == "High" else GPIO.LOW)

        # Send state to ThingSpeak if it changes
        if current_state != previous_state:
            print(f"Switch state changed: {current_state}")
            send_to_thingspeak(current_state)
            previous_state = current_state

        time.sleep(0.1)  # Small delay for responsiveness

except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()
