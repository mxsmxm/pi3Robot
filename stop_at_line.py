from robot import Robot
from time import sleep
from gpiozero import LineSensor

r=Robot()

lsensor=LineSensor(23)
rsensor=LineSensor(16)

lsensor.when_line=r.turnOffMotors
rsensor.when_line=r.turnOffMotors

r.set_left(-40)
r.set_right(-40)

while True:
    sleep(0.02)