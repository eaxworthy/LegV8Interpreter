
import bitstring as b

REG = []
MEM = []
STK = []
LBS = {}
#let 0 = Z, 1 = N, 2 = C, 3 = V
flags = [0, 0, 0, 0]

ip = 0

#initialize registers
for count in range(32):
    x = b.BitArray(int = 0, length = 64)
    REG.append(x)
REG[28].int = 999

#initialize memory
for count in range(1000):
    x = b.BitArray(int = 0, length = 64)
    MEM.append(x)

#initialize stack
for count in range(1000):
    x = b.BitArray(int = 0, length = 64)
    STK.append(x)

def printRegs():
    for i in range(32):
        print("X", i, ": ", REG[i])

def printStack():
    for i in range(999, 700, -1):
        if STK[i].int != 0:
            print("S", i, ": ", STK[i])

def printLabels():
    print(LBS.items())

def printFlags():
    for i in range(4):
        print(flags[i], i)    
