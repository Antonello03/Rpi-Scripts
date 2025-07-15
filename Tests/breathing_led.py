#!/usr/bin/env python3
from gpiozero import PWMLED
from time import sleep
from math import sin, pi

led = PWMLED(17)
period = 2.0 

try:
    while True:
        steps = 100
        for i in range(steps):
            led.value = (sin(i / steps * pi) + 1) / 2  # 0→1→0
            sleep(period / steps)
except KeyboardInterrupt:
    led.off()
