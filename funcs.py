from state import registers, flags

rM = 0
rN = 0
rD = 0
iM = 0

#Takes a uint and returns a int64. If the original value would
#require more than 64 bits, MSBs will be dropped until result
#is within range
def s64(value):
    return -(value & 0x8000000000000000) | (value & 0x7fffffffffffffff)

def add(args):
    rD = int(args[0][1::])
    rN = int(args[1][1::])
    rM = int(args[2][1::])
    registers[rD].int = registers[rN].int + registers[rM].int

def addi(args):
    rD = int(args[0][1::])
    rN = int(args[1][1::])
    iM = int(args[2])
    registers[rD].int = registers[rN].int + iM

def adds(args):
    rD = int(args[0][1::])
    rN = int(args[1][1::])
    rM = int(args[2][1::])
    registers[rD].int = s64(registers[rN].int + registers[rM].int)
    #show stored result as int and hex
    print(registers[rD].int, ' ', registers[rD])
    if not registers[rD].int:
        flags[0] = 1
    if registers[rD].int < 0:
        flags[1] = 1
    if (registers[rD].int < registers[rN].int + registers[rM].int):
        flags[2] = 1
        flags[3] = 1
    #show flags: [0] = Z, [1] = N, [2] = C, [3] = V
    print(flags)


def addis(args):
    rD = int(args[0][1::])
    rN = int(args[1][1::])
    iM = int(args[2])
    
    registers[rD].int = s64(registers[rN].int + iM)
    #show stored result as int and hex
    print(registers[rD].int, ' ', registers[rD])
    if not registers[rD].int:
        flags[0] = 1
    if registers[rD].int < 0:
        flags[1] = 1
    if (registers[rD].int < registers[rN].int + iM):
        flags[2] = 1
        flags[3] = 1
    #show flags: [0] = Z, [1] = N, [2] = C, [3] = V
    print(flags)

def aand(args):
    rD = int(args[0][1::])
    rN = int(args[1][1::])
    rM = int(args[2][1::])
    registers[rD].int = registers[rN].int & registers[rM].int

def andi(args):
    rD = int(args[0][1::])
    rN = int(args[1][1::])
    iM = int(args[2])
    registers[rD].int = registers[rN].int & iM

def ands(args):
    rD = int(args[0][1::])
    rN = int(args[1][1::])
    rM = int(args[2][1::])
    registers[rD].int = s64(registers[rN].int & registers[rM].int)
    #show stored result as int and hex
    print(registers[rD].int, ' ', registers[rD])
    if not registers[rD].int:
        flags[0] = 1
    if registers[rD].int < 0:
        flags[1] = 1
    if (registers[rD].int < registers[rN].int & registers[rM].int):
        flags[2] = 1
        flags[3] = 1
    #show flags: [0] = Z, [1] = N, [2] = C, [3] = V
    print(flags)

def andis(args):
    rD = int(args[0][1::])
    rN = int(args[1][1::])
    iM = int(args[2])
    
    registers[rD].int = s64(registers[rN].int & iM)
    #show stored result as int and hex
    print(registers[rD].int, ' ', registers[rD])
    if not registers[rD].int:
        flags[0] = 1
    if registers[rD].int < 0:
        flags[1] = 1
    if (registers[rD].int < registers[rN].int & iM):
        flags[2] = 1
        flags[3] = 1
    #show flags: [0] = Z, [1] = N, [2] = C, [3] = V
    print(flags)

def b(args):
    # Find the label location
    label = values[1] + ": "
    for j in range(len(LegCode)):
        if label in LegCode[j]:
            N = j
    return

def bcond(args):
    #rT = int(args[0][1::])
   
    #if flags set to any of the conditonal notices
    # then do N = the line# where the label: is located
    return

def bl(args):
    registers[30].int = N + 1
    label = values[1] + ": "
    for j in range(len(LegCode)):
        if label in LegCode[j]:
            N = j
    return

def br(args):
    # rD = int(args[0][1::])
    # NEED A PC var in global
    # N = the line# where the label: is located
    return

def cbz(args):
    if flags[0] == 0:
        # Find the label location
        label = values[2] + ": "
        for j in range(len(LegCode)):
            if label in LegCode[j]:
                N = j
    return
        
def cbnz(args):
    if flags[0] != 0:
        # Find the label location
        label = values[2] + ": "
        for j in range(len(LegCode)):
            if label in LegCode[j]:
                N = j
    return

def eor(args):
    rD = int(args[0][1::])
    rN = int(args[1][1::])
    rM = int(args[2][1::])
    registers[rD].int = registers[rN].int ^ registers[rM].int

def eori(args):
    rD = int(args[0][1::])
    rN = int(args[1][1::])
    iM = int(args[2])
    registers[rD].int = registers[rN].int ^ iM

def ldur(args):
    rT = int(args[0][1::])
    rN = int(args[1][1::])
    iM = int(args[2])
    
    #registers[rT].int = mem[s64(registers[rN].int + iM)]
    
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
    rD = int(args[0][1::])
    rN = int(args[1][1::])
    iM = int(args[2])
    registers[rD].int = registers[rN].int << iM

def lsr(args):
    rD = int(args[0][1::])
    rN = int(args[1][1::])
    iM = int(args[2])
    registers[rD].int = registers[rN].int >> iM

def orr(args):
    rD = int(args[0][1::])
    rN = int(args[1][1::])
    rM = int(args[2][1::])
    registers[rD].int = registers[rN].int | registers[rM].int

def orri(args):
    rD = int(args[0][1::])
    rN = int(args[1][1::])
    iM = int(args[2])
    registers[rD].int = registers[rN].int | iM

def sub(args):
    rD = int(args[0][1::])
    rN = int(args[1][1::])
    rM = int(args[2][1::])
    registers[rD].int = registers[rN].int - registers[rM].int

def subi(args):
    rD = int(args[0][1::])
    rN = int(args[1][1::])
    iM = int(args[2])
    registers[rD].int = registers[rN].int - iM

def subs(args):
    rD = int(args[0][1::])
    rN = int(args[1][1::])
    rM = int(args[2][1::])
    registers[rD].int = s64(registers[rN].int - registers[rM].int)
    #show stored result as int and hex
    print(registers[rD].int, ' ', registers[rD])
    if not registers[rD].int:
        flags[0] = 1
    if registers[rD].int < 0:
        flags[1] = 1
    if (registers[rD].int < registers[rN].int - registers[rM].int):
        flags[2] = 1
        flags[3] = 1
    #show flags: [0] = Z, [1] = N, [2] = C, [3] = V
    print(flags)

def subis(args):
    rD = int(args[0][1::])
    rN = int(args[1][1::])
    iM = int(args[2])
    
    registers[rD].int = s64(registers[rN].int - iM)
    #show stored result as int and hex
    print(registers[rD].int, ' ', registers[rD])
    if not registers[rD].int:
        flags[0] = 1
    if registers[rD].int < 0:
        flags[1] = 1
    if (registers[rD].int < registers[rN].int - iM):
        flags[2] = 1
        flags[3] = 1
    #show flags: [0] = Z, [1] = N, [2] = C, [3] = V
    print(flags)

def stur(args):
    rT = int(args[0][1::])
    rN = int(args[1][1::])
    iM = int(args[2])
    
    #mem[s64(registers[rN].int + iM)]= registers[rT].int
    return

def sturb(args):
    return

def sturh(args):
    return

def sturw(args):
    return

def stxr(args):
    return
