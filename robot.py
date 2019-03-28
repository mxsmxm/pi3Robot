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

    #将速度转换成0-100之间
    def speedConvert(self,speed):
        #选择 运行模式,默认为MotorHAT.RELEASE
        mode=MotorHAT.RELEASE
        output_speed=speed
        if speed>100:
            output_speed=100
        elif speed<-100:
            output_speed=-100
        
        if speed>0:
            mode=MotorHAT.FORWARD
        elif speed<0:
            mode=MotorHAT.BACKWARD

        output_speed=int(abs(output_speed)/100*255)

        return (mode,output_speed)

    def set_left(self,speed):
        (mode,output_speed)=self.speedConvert(speed)
        self.left_motor.setSpeed(output_speed)
        self.left_motor.run(mode)
    def set_right(self,speed):
        (mode,output_speed)=self.speedConvert(speed)
        self.right_motor.setSpeed(output_speed)
        self.right_motor.run(mode)

    
    def turnOffMotors(self):
        self.left_motor.run(MotorHAT.RELEASE)
        self.right_motor.run(MotorHAT.RELEASE)

        


