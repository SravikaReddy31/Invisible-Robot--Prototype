import motor_control as motor
import time

def avoid_obstacle(distance):
    if distance < 20:
        motor.stop()
        time.sleep(1)
        motor.backward()
        time.sleep(1)
        motor.left()
        time.sleep(1)
        motor.stop()
    elif distance < 50:
        motor.stop()
    else:
        motor.forward()
