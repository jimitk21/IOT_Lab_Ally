# python3 -m venv myenv
# source myenv/bin/activate
# python3 -m pip install adafruit-circuitpython-dht
# pip3 install requests

import time
import board
import adafruit_dht
import requests

# Initialize the DHT11 sensor on GPIO4
try:
    sensor = adafruit_dht.DHT11(board.D4)
    print("DHT11 sensor initialized.")
except Exception as e:
    print(f"Error initializing sensor: {e}")

# ThingSpeak Channel Information
THINGSPEAK_CHANNEL_ID = "2741246"
THINGSPEAK_API_KEY = "72EF2GAF9BA9UAEC"
THINGSPEAK_URL = "https://api.thingspeak.com/update"

while True:
    try:
        # Read the sensor data
        temperature_c = sensor.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = sensor.humidity

        if temperature_c is None or humidity is None:
            print("Failed to retrieve data from the sensor. Retrying...")
            time.sleep(2.0)
            continue  # Skip the rest of this iteration

        # Print the readings
        print("Temp = {0:0.1f}C, Temp = {1:0.1f}F, Humidity = {2:0.1f}%".format(temperature_c, temperature_f, humidity))

        # Send data to ThingSpeak
        response = requests.get(THINGSPEAK_URL, params={
            'api_key': THINGSPEAK_API_KEY,
            'field1': temperature_c,
            'field2': humidity
        })

        # Check if the data was sent successfully
        if response.status_code == 200:
            print("Data successfully sent to ThingSpeak.")
        else:
            print(f"Failed to send data to ThingSpeak. Status code: {response.status_code}")

    except RuntimeError as error:
        # Errors happen fairly often with DHT sensors, just keep going
        print(f"Runtime error: {error.args[0]}")
        time.sleep(2.0)
        continue
    except Exception as error:
        # Cleanup and raise the error
        sensor.exit()
        print(f"Unexpected error: {error}")
        break

    # Wait 15 seconds before sending the next set of data
    time.sleep(15.0)
