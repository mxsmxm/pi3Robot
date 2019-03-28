from Adafruit_MotorHAT import Adafruit_MotorHAT as MotorHAT
#

import time
import atexit

# create a default object, no changes to I2C address or frequency
mh = MotorHAT(addr=0x60)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(MotorHAT.RELEASE)
    mh.getMotor(2).run(MotorHAT.RELEASE)

atexit.register(turnOffMotors)

################################# DC motor test!
lMotor=mh.getMotor(1)
rMotor=mh.getMotor(2)

# set the speed to start, from 0 (off) to 255 (max speed)
lMotor.setSpeed(150)
rMotor.setSpeed(150)

# lMotor.run(MotorHAT.FORWARD)
# rMotor.run(MotorHAT.FORWARD)

# time.sleep(1)

# lMotor.run(MotorHAT.BACKWARD)
# rMotor.run(MotorHAT.FORWARD)
# time.sleep(1)

# lMotor.run(MotorHAT.FORWARD)
# rMotor.run(MotorHAT.BACKWARD)
# time.sleep(1)

lMotor.run(MotorHAT.BACKWARD)
rMotor.run(MotorHAT.BACKWARD)
time.sleep(2)