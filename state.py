
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
REG[28].int = 1000

#initialize memory
for count in range(1000):
    x = b.BitArray(int = 0, length = 8)
    MEM.append(x)

#initialize stack
for count in range(1000):
    x = b.BitArray(int = 0, length = 8)
    STK.append(x)

def printRegs():
    print ( "\n{:=>49}".format("") ,"\nPrinting Registers:", "\n{:=>49}".format(""))
    for i in range(32):
        print('{:<30}{:<40}'.format(str("X%d:" % i), str(REG[i])))
    print ("\n{:=>49}".format(""))

def printStack():
    print ("\n{:=>49}".format("") ,"\nPrinting Stack:", "\n{:=>49}".format(""))
    counter = 0
    for i in range(len(STK)-1, -1, -1):
        if STK[i].int != 0:
            print('{:<30}{:<40}'.format(str("STK[%d]:" % i), str(STK[i])))
            counter += 1
    if not counter:
        print ("Stack is empty")
    print("\n(Bytes not shown hold 0x00)")
    print ("{:=>49}".format(""))


def printMem():
    print ("\n{:=>49}".format(""), "\nPrinting Memory:", "\n{:=>49}".format(""))
    counter = 0
    for i in range(len(MEM)-1, -1, -1):
        if MEM[i].int != 0:
            print('{:<30}{:<40}'.format(str("MEM[%d]:" % i), str(MEM[i])))
            counter += 1
    if not counter:
        print ("Memory is empty")
    print("\n(Bytes not shown hold 0x00)")
    print ("{:=>49}".format(""))


def printLabels():
    print ("\n{:=>49}".format(""), "\nPrinting Labels:", "\n{:=>49}".format(""))
    print(LBS.items())

def printFlags():
    print ("\n{:=>49}".format(""), "\nPrinting Flags:", "\n{:=>49}".format(""))
    for i in range(4):
        if i == 0:
            _flag = "Zero"
        elif i == 1:
            _flag = "Negative"
        elif i == 2:
            _flag = "Carry"
        elif i == 3:
            _flag = "Overflow"
        print('{:<30}{:<40}'.format(_flag, str(flags[i])))
    print ("\n{:=>49}".format(""))
