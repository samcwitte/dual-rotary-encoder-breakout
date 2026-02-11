# MIT License (MIT)
# Copyright (c) 2026 Samuel Witte
# https://opensource.org/licenses/MIT

# Example script for the Raspberry Pi Pico

# Documentation:
#   https://github.com/MikeTeachman/micropython-rotary

# This script holds two values - one for each rotary encoder

import time
from rotary_irq_rp2 import RotaryIRQ
from machine import Pin

pinA1 = 21
pinA2 = 20
pinB1 = 14
pinB2 = 15

sw = Pin(13, Pin.IN)

r1 = RotaryIRQ(pin_num_clk=pinA1, pin_num_dt=pinB1, min_val=0, max_val=99, reverse=False, half_step=True, pull_up=True, range_mode=RotaryIRQ.RANGE_BOUNDED)
r2 = RotaryIRQ(pin_num_clk=pinA2, pin_num_dt=pinB2, min_val=0, max_val=99, reverse=False, half_step=True, pull_up=True, range_mode=RotaryIRQ.RANGE_WRAP)

val_old1 = r1.value()
val_old2 = r2.value()

while True:
    try:
        val_new1 = r1.value()
        val_new2 = r2.value()
        
        if val_old1 != val_new1:
            val_old1 = val_new1
        
        if val_old2 != val_new2:
            val_old2 = val_new2
        
        if sw.value():
            print("click!")
            
        time.sleep_ms(50)
    except KeyboardInterrupt:
        break
