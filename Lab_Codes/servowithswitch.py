import RPi.GPIO as GPIO
import time

# Use BOARD pin numbering
GPIO.setmode(GPIO.BOARD)

# GPIO pin definitions
SERVO_PIN = 12   # Pin connected to the servo signal wire
BUTTON_PIN = 40  # Pin connected to the button
LED_PIN = 7      # Optional: Pin connected to an LED to indicate button press

# Set up GPIO pins
GPIO.setup(SERVO_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Button with pull-up resistor
GPIO.setup(LED_PIN, GPIO.OUT)

# Servo setup
pwm = GPIO.PWM(SERVO_PIN, 50)  # 50Hz frequency for servo
pwm.start(0)  # Start PWM with 0% duty cycle (servo off)

# Initialize variables
servo_angle = 0  # Start at 0 degrees
step = 10  # Step to increase/decrease angle with each button press

def set_servo_angle(angle):
    """Move servo to the specified angle."""
    duty = 2 + (angle / 18)  # Convert angle to duty cycle
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)  # Allow servo to reach the position
    pwm.ChangeDutyCycle(0)  # Stop sending signal

try:
    print("Press the button to control the servo.")
    while True:
        # Check button state
        button_state = GPIO.input(BUTTON_PIN)
        if button_state == GPIO.LOW:  # Button pressed
            GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on LED
            # Increment servo angle
            servo_angle += step
            if servo_angle > 180:  # Wrap around if angle exceeds max
                servo_angle = 0
            print(f"Moving servo to {servo_angle} degrees.")
            set_servo_angle(servo_angle)
            time.sleep(0.3)  # Debounce delay for button
        else:
            GPIO.output(LED_PIN, GPIO.LOW)  # Turn off LED
        time.sleep(0.05)  # Polling delay

except KeyboardInterrupt:
    print("Exiting...")
finally:
    pwm.stop()
    GPIO.cleanup()
