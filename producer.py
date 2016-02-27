#!/usr/bin/env python3
import colorsys as cs
import time as time
import serial

N = 181
frames_per_second = 30

def update(frame_number):
    # Get an index which we can use to re-spawn the oldest raindrop.
    current_index = frame_number % N

    startingHue = frame_number % 255
    colors = []

    i = 0
    while (i < N):
        hue = startingHue if startingHue < 255 else startingHue - 255
        colors.append(cs.hsv_to_rgb(hue / 255, 1.0, 1.0))
        startingHue += 1
        i += 1

    ser = serial.Serial(0)  # open first serial port
    print(ser.portstr)      # check which port was really used
    ser.write("hello")      # write a string
    ser.close()

    return


while(1):
    i = 0
    update(i)
    i+=1

    time.sleep(1/frames_per_second)
