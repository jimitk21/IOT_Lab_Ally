

import requests

# ThingSpeak API details
write_api_key = '8FRPEODGUBW32SKA'  # Corrected key
field1_value = 0  # Example value for LED Control
field2_value = 90  # Example value for Servo Position

# Constructing the URL
url = f"https://api.thingspeak.com/update?api_key={write_api_key}&field1={field1_value}&field2={field2_value}"

# Sending the request
response = requests.get(url)

# Printing the response
print(response.text)
