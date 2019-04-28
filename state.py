#TODO: Maybe switch over to using bitstrings instead of numbers
#      to make 2's complement easier so that we don't go over
#      the 8 byte size limit?
import bitstring as b

REG = []
MEM = []
STK = []

#initialize registers
for count in range(32):
    x = b.BitArray(int = 0, length = 64)
    REG.append(x)

#initialize memory
for count in range(1000):
    x = b.BitArray(int = 0, length = 64)
    MEM.append(x)

XZR = 31

#let 0 = Z, 1 = N, 2 = C, 3 = V
flags = [0, 0, 0, 0]

def printRegs():
    for i in range(32):
        print("X", i, ": ", REG[i])
