#!/usr/bin/env python
# coding: utf-8

"""
This example shows how sending a single message works.
"""

from __future__ import print_function

import can

def send_one():


    bus = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=250000);


    msg = can.Message(arbitration_id=0x204,
                      data=[0, 25, 0, 1, 3, 1, 4, 1],
                      is_extended_id=False);

    bus.set_filters(filters=[{"can_id": 0x204,"can_mask":0x21,"extended":False}]);
    while True:
        bus.send(msg(is_error_frame=True));
        print("Message sent on {}".format(bus.channel_info));
