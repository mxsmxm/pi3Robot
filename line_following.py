from robot import Robot
from time import sleep
on_line_color=(0,255,0)#在线上的颜色
off_line_color=(255,0,0)#脱线的颜色


class LineFollower:
    def __init__(self,robot,forward_speed=30,turn_speed=-30):
        self.robot=robot
        self.forward_speed=forward_speed
        self.turn_speed=turn_speed
        self.left_indicator=range(0,2)
        self.right_indicator=range(6,8)

    def when_left_off_line(self):
        self.robot.set_left(self.forward_speed)
        for i in self.left_indicator:
            self.robot.leds[i]=off_line_color
        self.robot.leds.show()
    def when_right_off_line(self):
        self.robot.set_right(self.forward_speed)
        for i in self.right_indicator:
            self.robot.leds[i]=off_line_color
        self.robot.leds.show()

    def when_left_on_line(self):
        self.robot.set_left(self.turn_speed)
        for i in self.left_indicator:
            self.robot.leds[i]=on_line_color
        self.robot.leds.show()
    def when_right_on_line(self):
        self.robot.set_right(self.turn_speed)
        for i in self.right_indicator:
            self.robot.leds[i]=on_line_color
        self.robot.leds.show()

    def run(self):
        self.robot.left_line_sensor.when_line=self.when_left_on_line
        self.robot.left_line_sensor.when_no_line=self.when_left_off_line
        self.robot.right_line_sensor.when_line=self.when_right_on_line
        self.robot.right_line_sensor.when_no_line=self.when_right_off_line
        #开始驱动
        self.robot.set_left(self.forward_speed)
        self.robot.set_right(self.forward_speed)
        while True:
            sleep(0.02)

robot=Robot()
line_follower=LineFollower(robot,30,20)
line_follower.run()
    