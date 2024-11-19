# sudo apt install mosquitto mosquitto-clients
# python3 -m venv myenv
# source myenv/bin/activate
# sudo apt install mosquitto mosquitto-clients
# pip install paho-mqtt
# pip3 install RPi.GPIO

import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

# GPIO Setup
LED_PIN = 4  # Corrected assignment and added '='

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Callback when a message is received
def on_message(client, userdata, message):
    payload = message.payload.decode()  # Corrected variable assignment
    print(f"Received message: {payload}")  # Updated the print statement to use the variable

    if payload == "ON":
        GPIO.output(LED_PIN, GPIO.HIGH)
    elif payload == "OFF":
        GPIO.output(LED_PIN, GPIO.LOW)

# MQTT Setup
broker_url = "test.mosquitto.org"  # Eclipse Mosquitto public broker
broker_port = 1883  # Default unencrypted MQTT port
topic = "jaypatel/home/room/led"

client = mqtt.Client()
client.connect(broker_url, broker_port)

client.subscribe(topic)
client.on_message = on_message

# Start MQTT client loop
client.loop_start()

try:
    while True:
        pass  # Keep the script running
except KeyboardInterrupt:
    print("Script interrupted by user")
finally:
    client.loop_stop()  # Stop the MQTT client loop
    GPIO.cleanup()  # Clean up GPIO setup


have desktop terminal ma niche varo cmd run kaeje

mosquitto_pub -h test.mosquitto.org -t jaypatel/home/room/led -m "ON"
