from state import registers, flags

rM = 0
rN = 0
rD = 0
iM = 0

def add(args):
    rD = int(args[0][1::])
    rN = int(args[1][1::])
    rM = int(args[2][1::])
    registers[rD] = registers[rN].int + registers[rM].int

def addi(args):
    rD = int(args[0][1::])
    rN = int(args[1][1::])
    iM = int(args[2])
    registers[rD] = registers[rN].int + iM

def adds(args):
    rD = int(args[0][1::])
    rN = int(args[1][1::])
    rM = int(args[2][1::])
    registers[rD] = registers[rN].int + registers[rM].int
    if not registers[rD]:
        flags[0] = 1
    if (registers[rD] < registers[rN].int + registers[rM].int):
        flags[3] = 1    
    print(registers[rD], flags[0])

def addis(args):
    return

def aand(args):
    return

def andi(args):
    return

def ands(args):
    return

def andis(args):
    return

def b(args):
    return

def bcond(args):
    return

def bl(args):
    return

def br(args):
    return

def cbz(args):
    return

def cbnz(args):
    return

def eor(args):
    return

def eori(args):
    return

def ldur(args):
    return

def ldurb(args):
    return

def ldurh(args):
    return

def ldursw(args):
    return

def ldxr(args):
    return

def lsl(args):
    return

def lsr(args):
    return

def orr(args):
    return

def orri(args):
    return

def sub(args):
    return

def subi(args):
    return

def subs(args):
    return

def subis(args):
    return

def stur(args):
    return

def sturb(args):
    return

def sturh(args):
    return

def sturw(args):
    return

def stxr(args):
    return
