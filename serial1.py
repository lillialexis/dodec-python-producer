#!/usr/bin/env python

import time
import os, pty, serial

# master, slave = pty.openpty()
# s_name = os.ttyname(slave)
#
# ser = serial.Serial(s_name,)
#
# # To Write to the device
# ser.write(bytes([0, 1, 2, 3, 4, 5]))
#
# # To read from the device
# os.read(master, 1000)

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='/dev/slave',
    baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS,
    rtscts=True,
    dsrdtr=True
)

# ser.open()
# ser.isOpen()

print('Enter your commands below.\r\nInsert "exit" to leave the application.')

input=1
while 1 :
    # # get keyboard input
    # input = input(">> ")
    #     # Python 3 users
    #     # input = input(">> ")
    # if input == 'exit':
    #     ser.close()
    #     exit()
    # else:
        # send the character to the device
        # (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
        ser.write(bytes([0, 1]))
        out = ''
        # let's wait one second before reading output (let's give device time to answer)
        time.sleep(1)
        while ser.inWaiting() > 0:
            out += ser.read(1).decode("utf-8")

        if out != '':
            print(">>" + out)



