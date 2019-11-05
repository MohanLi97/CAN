#!/usr/bin/env python
# coding: utf-8

"""
This example shows how recieving a single message works.
"""

from __future__ import print_function
import time
import can

def send_one():


    bus = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=500000)


    msg = can.Message(arbitration_id=0x204,
                      data=[0xFF,0xFF,0x04,0x80,0x00,0xFF,0xFF,0xFF],
                      is_extended_id=False)


    bus.set_filters(filters=[{"can_id": 0x204,"can_mask":0x7FF,"extended":False}])
    

    while True:

	recvmsg=bus.recv()
	time.sleep(5)
	bus.send(msg)
	bus.flush_tx_buffer()
	time.sleep(5)	
	print(recvmsg)
send_one()
