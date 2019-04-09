from gpiozero import LED,LineSensor
from time import sleep

red = LED(17)
lsensor=LineSensor(23,pull_up=True)
rsensor=LineSensor(16,pull_up=True)

lsensor.when_line= lambda: red.on()
lsensor.when_no_line= lambda:red.off()

while True:
    sleep(0.02)