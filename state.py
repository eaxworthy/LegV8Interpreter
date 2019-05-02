
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
    print ("\n=================================================\nPrinting Registers:\n=================================================")
    for i in range(32):
        print('{:<30}{:<40}'.format(str("X%d:" % i), str(REG[i])))

def printStack():
    print ("\n=================================================\nPrinting Stack:\n=================================================")
    for i in range(999, -1, -1):
        if STK[i].int != 0:
            print('{:<30}{:<40}'.format(str("STK%d:" % i), str(STK[i])))

def printMem():
    print ("\n=================================================\nPrinting Memory:\n=================================================")
    for i in range(999, -1, -1):
        if MEM[i].int != 0:
            print('{:<30}{:<40}'.format(str("MEM%d:" % i), str(MEM[i])))

def printLabels():
    print ("\n=================================================\nPrinting Labels:\n=================================================")
    print(LBS.items())

def printFlags():
    print ("\n=================================================\nPrinting Flags:\n=================================================")
    for i in range(4):
        print(flags[i], i)    
