from Adafruit_MotorHAT import Adafruit_MotorHAT as MotorHAT
import atexit

class Robot():
    def __init__(self,mh_addr=0x60):
        #使用给定的地址设置motorHAT
        self._mh=MotorHAT(addr=mh_addr)

        #设置两个马达
        self.left_motor=self._mh.getMotor(1)
        self.right_motor=self._mh.getMotor(2)
        # recommended for auto-disabling motors on shutdown!
        atexit.register(self.turnOffMotors)

    
    def turnOffMotors(self):
        self.left_motor.run(MotorHAT.RELEASE)
        self.right_motor.run(MotorHAT.RELEASE)

        


