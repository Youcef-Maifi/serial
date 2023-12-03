#!/usr/bin/env python

import serial, sys

if len(sys.argv) != 2:
    print "python: Usage_serial_test <port name like: /dev/serial/by-id/usb-1a86_USB_Serial-if00-port0>"
    sys.exit(1)

sio = serial.Serial(sys.argv[1], 115200)
sio.timeout = 250

while True:
    sio.write("Testing.")
    print sio.read(8)

