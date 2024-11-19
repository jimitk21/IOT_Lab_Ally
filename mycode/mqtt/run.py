import paho.mqtt.client as mqtt

# MQTT Broker Configuration
broker_url = "test.mosquitto.org"
broker_port = 1883
topic = "jjkk/mqtt/on/off"

# Initialize MQTT client
client = mqtt.Client()

# Connect to the broker
client.connect(broker_url, broker_port)

# Publish message to turn the LED ON
# client.publish(topic, "ON")

# Or to turn the LED OFF
client.publish(topic, "OFF")

print(f"Message published to topic '{topic}'")
