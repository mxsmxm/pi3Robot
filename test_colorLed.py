from robot import Robot
from time import sleep


bot=Robot()
red=(255,0,0)
pink=(255,0,100)
yellow=(255,100,0)
purple=(255,0,255)

while 1:
    bot.leds.fill(red)
    bot.leds.show()
    sleep(0.5)
    bot.leds.fill(pink)
    bot.leds.show()
    sleep(0.5)
    bot.leds.fill(yellow)
    bot.leds.show()
    sleep(0.5)
    bot.leds.fill(purple)
    bot.leds.show()
    sleep(0.5)
