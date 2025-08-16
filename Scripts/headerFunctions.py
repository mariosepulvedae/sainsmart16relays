#!/usr/bin/env python3


def lrc(b):
    b = bytearray.fromhex(b)
    l = 0
    for i in b:
        l = (l+i)&0xff
    
    return ((l ^ 0xff) + 1) & 0xff

def cmd(relay, command):
    on = "FE0500{:02X}{:02X}00".format(relay, command)
    packet = ":{}{:02X}\r\n".format(on, lrc(on))
    return packet.encode('ascii')

def on_cmd(relay):
    return cmd(relay, 0xFF)

def off_cmd(relay):
    return cmd(relay, 0x00)

def all_on():
    return ":FE0F0000001002FFFFE3\r\n".encode('ascii')

def all_off():
    return ":FE0F00000010020000E1\r\n".encode('ascii')

def status():
    return ":FE0100000010F1\r\n".encode('ascii')
