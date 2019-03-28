from robot import Robot
from Adafruit_MotorHAT import Adafruit_MotorHAT as MotorHAT
from time import sleep

r=Robot()

r.left_motor.set_speed(100)
r.right_motor.set_speed(100)
r.left_motor.run(MotorHAT.FORWARD)
r.right_motor.run(MotorHAT.FORWARD)

sleep(2)