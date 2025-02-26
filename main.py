#TUNGASONIC SOFTWARES
###################################
from machine import Pin, ADC
import time

# Define pins for LEDs
red_led = Pin(0, Pin.OUT)
green_led = Pin(1, Pin.OUT)
amber_led = Pin(2, Pin.OUT)
ldr = ADC(Pin(27))  # Define pin for LDR

# Threshold for LDR
LIGHT_THRESHOLD = 500  # Adjust this value based on your testing

while True:
    ldr_value = ldr.read_u16()  # Read LDR value

    if ldr_value < LIGHT_THRESHOLD: 
         # NIGHT TIME
        # Green light
        green_led.on  # Turn on green LED
        red_led.value(0)    # Turn off red LED
        amber_led.value(0)  # Turn off amber LED
        time.sleep(5)      # Green for 5 seconds

        # Amber light
        amber_led.value(1)  # Turn on amber LED
        green_led.value(0)  # Turn off green LED
        time.sleep(2)       # Amber for 2 seconds

        # Red light
        red_led.value(1)    # Turn on red LED
        amber_led.value(0)  # Turn off amber LED
        time.sleep(3)       # Red for 3 seconds

    else:  
        # DAY TIME
        # Green light
        green_led.value(1)  # Turn on green LED
        red_led.value(0)    # Turn off red LED
        amber_led.value(0)  # Turn off amber LED
        time.sleep(10)      # Green for 10 seconds

        # Amber light
        amber_led.value(1)  # Turn on amber LED
        green_led.value(0)  # Turn off green LED
        time.sleep(5)       # Amber for 5 seconds

        # Red light
        red_led.value(1)    # Turn on red LED
        amber_led.value(0)  # Turn off amber LED
        time.sleep(10)      # Red for 10 seconds