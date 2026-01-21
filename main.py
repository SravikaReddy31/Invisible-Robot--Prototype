import time
import RPi.GPIO as GPIO

import motor_control as motor
import ultrasonic
import obstacle_logic
import danger_alert

try:
    print("🚀 Invisible Military Robot Started")
    while True:
        distance = ultrasonic.get_distance()
        danger_alert.show_status(distance)
        obstacle_logic.avoid_obstacle(distance)
        time.sleep(0.5)

except KeyboardInterrupt:
    print("🛑 Program stopped")

finally:
    motor.stop()
    GPIO.cleanup()
