import spidev
import ws2812
from random import  randint
import time

spi=spidev.SpiDev()
spi.open(0,0)

N=8
pixels=[]
for x in range(0,8):
    pixels.append([0,0,0])

while 1:
    for i in range(0,N):
        pixels[i]=[255,0,0]
        ws2812.write2812(spi,pixels)
    time.sleep(0.1)
