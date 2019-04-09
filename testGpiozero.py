from gpiozero import LED,LineSensor
from time import sleep

red = LED(17)
lsensor=LineSensor(23)
rsensor=LineSensor(16)

lsensor.when_line= lambda: red.on()
rsensor.when_line= lambda:red.off()

while True:
    sleep(0.02)