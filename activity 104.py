#!/usr/bin/env python3

class MacAddress:
    OUI = {
        bytes([0xda,0xa1,0x19]): 'Google, Inc.',
        bytes([0xca,0x12,0x5c]): 'Microsoft Corporation',
        bytes([0x3b,0x35,0x41]): 'Raspberry Pi (Trading) Ltd',
    }

    def __init__(self,mac):
        self.mac = mac

    def is_multicast(self):
        if self.addres

    def organization(self):
        

    def __str__(self):
        return "{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x} unknown"
    
if __name__ == '__main__':
    