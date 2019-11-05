#!/usr/bin/env python
# coding: utf-8

"""
This example shows how sending a single message works.
"""

from __future__ import print_function
import time
import can

def send_one():


    bus = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=500000)


    msg = can.Message(arbitration_id=0x204,
                      data=[0xFF,0xFF,0x04,0x80,0x00,0xFF,0xFF,0xFF],
                      is_extended_id=False)

    while True:

	bus.send(msg)
	time.sleep(5)

send_one()
