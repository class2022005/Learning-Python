#!/usr/bin/env python3

def xor_padded(data,key):

    ct = bytearray()
    for index in range(len(data)):
        ct.append(data[index] ^ key[index])
    return ct

if __name__ == "__main__":
    print('\nXOR one time pad example\nMessage and Key must be same length')
    msg = input('Enter a message: ').encode('ascii')    # i.e. 'My message'
    key = input('Enter a key: ').encode('ascii')        # i.e. 'qwertyasdf'

    ct = xor_padded(msg,key)
    print(f'\nEncoded message:\n{ct}')
    pt = xor_padded(ct,key)
    print(f'\nDecoded message:\n{pt}')
    print(f'\nBack to a string:\n{bytes(pt).decode("ascii")}')