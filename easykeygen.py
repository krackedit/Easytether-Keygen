#!/usr/bin/env python3
# A simple keygen written in python for EasyTether.

loop = 0
while loop == 0:
    imei = input("Enter IMEI Number:")
    if len(imei) >= 10 and len(imei) < 16:
        try:
            int(imei)
        except ValueError:
            print ("Contains a non numeric character, Try Agian ")
        else:
            loop = 1
    else:
        print("Length of string invalid, Try Agian.")
x = -1
key = 0
for i in range(10):
    if x < 4:
        x = x + 1
    else:
        x = len(imei) + i - 10
    n = ord(imei[x]) & 0xFF
    key += (((49635 * n & 0xFFFF) >> 1) - n & 0xFFFF) & 0xFFFF
print("Your registration key: %05d" % (0xFFFF & key))
