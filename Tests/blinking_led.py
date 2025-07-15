#!/usr/bin/env python3
from gpiozero import LED
from time import sleep


pin = 17 
led = LED(pin)
t = 0.5
times = 5

for i in range(times):
        led.on()
        sleep(t)
        led.off()
        sleep(t)