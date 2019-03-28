from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

################################# DC motor test!
lMotor=mh.getMotor(1)
rMotor=mh.getMotor(2)

# set the speed to start, from 0 (off) to 255 (max speed)
lMotor.setSpeed(150)
rMotor.setSpeed(150)

lMotor.run(Adafruit_MotorHAT.FORWARD)
rMotor.run(Adafruit_MotorHAT.FORWARD)

time.sleep(1)