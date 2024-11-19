# python3 -m venv myenv
# source myenv/bin/activate
# python3 -m pip install adafruit-circuitpython-dht

# Based on Adafruit_CircuitPython_DHT Library Example

import time
import board
import adafruit_dht


sensor = adafruit_dht.DHT11(board.D4)

while True:
    try:
        # Print the values to the serial port
        temperature_c = sensor.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = sensor.humidity
        print("Temp={0:0.1f} C, Temp={1:0.1f} F, Humidity={2:0.1f}%".format(temperature_c, temperature_f, humidity))

    except RuntimeError as error:
        # Errors happen fairly often, DHTs are hard to read, keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        sensor.exit()
        raise error

    time.sleep(3.0)