#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

laser_port = 17

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(laser_port, GPIO.OUT)
    GPIO.output(laser_port, GPIO.HIGH)


def loop():
    while True:
        print('laser on')
        GPIO.output(laser_port, GPIO.LOW)
        time.sleep(10.0)
        print('laser off')
        GPIO.output(laser_port, GPIO.HIGH)
        time.sleep(1.0)
   
def destroy():
    GPIO.output(laser_port, GPIO.LOW)
    GPIO.cleanup()
    

if __name__ == '__main__': 
    setup()


try:
    loop()
except KeyboardInterrupt:
    destroy()
