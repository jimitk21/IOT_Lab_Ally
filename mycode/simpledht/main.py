import time
import board
import adafruit_dht

# Initialize the DHT11 sensor
sensor = adafruit_dht.DHT11(board.D4)

while True:
    try:
        # Read temperature and humidity values
        temperature_c = sensor.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = sensor.humidity

        # Print the values to the console
        print(
            "Temp={0:0.1f}°C, Temp={1:0.1f}°F, Humidity={2:0.1f}%".format(
                temperature_c, temperature_f, humidity
            )
        )
    except RuntimeError as error:
        # Errors happen fairly often with DHT sensors, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        # Clean up and raise the error if an unexpected exception occurs
        sensor.exit()
        raise error

    # Wait for 3 seconds before the next reading
    time.sleep(3.0)
