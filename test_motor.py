from robot import Robot
from Adafruit_MotorHAT import Adafruit_MotorHAT as MotorHAT
from time import sleep

r=Robot()

r.set_left(50)
r.set_right(50)

sleep(1)

r.set_left(-50)
r.set_right(-50)

sleep(1)