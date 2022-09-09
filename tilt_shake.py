#!/usr/bin/env python

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
tile_port = 17
shake_port = 22

GPIO.setup(tile_port, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(shake_port, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def switch_tilt(channel):
    if not GPIO.input(channel):
        print("tilt~~")    
    
def switch_shake(channel):
    if not GPIO.input(channel):
        print("shake~~")

GPIO.add_event_detect(shake_port, GPIO.FALLING, callback=switch_shake, bouncetime=100)
GPIO.add_event_detect(tile_port, GPIO.FALLING, callback=switch_tilt, bouncetime=100)

while True:
    pass
