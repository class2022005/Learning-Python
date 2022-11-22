#!/usr/bin/env python3

message = b"my hidden message"

def simple_xor(data):
    ct = bytearray()
    for index in range(len(data)):
        ct.append(data[index] ^ 1)
    return ct

if __name__ == "__main__":
    print(f'Simple XOR message:\n{message}')
    xor_simple_CT = simple_xor(message)
    print(f'\nSimple XOR CT:\n{xor_simple_CT}')
    print(f'Simple XOR message returned to original state:\n{simple_xor(xor_simple_CT)}')