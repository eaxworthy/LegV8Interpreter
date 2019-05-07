from state import REG, STK, LBS, MEM, printLabels
import state as s
import bitstring as b

rM = 0
rN = 0
rD = 0
iM = 0

def sign_extend(value, bits):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

def get_byte(value, n):
    # convert number into binary first
    binary = format(value, '064b')

    end = len(binary) - 1
    start = end - n + 1

    # extract k bit sub-string
    byte = binary[start: end + 1]

    return s.b.BitArray(int = int(byte, 2), length=64)

#Takes a uint and returns a int64. If the original value would
#require more than 64 bits, MSBs will be dropped until result
#is within range
def s64(value):
    return -(value & 0x8000000000000000) | (value & 0x7fffffffffffffff)

#tested
def add(args):
    rD = int(args[0][1::])
    rN = int(args[1][1::])
    rM = int(args[2][1::])
    REG[rD].int = s64(REG[rN].int + REG[rM].int)
    return

#tested
def addi(args):
    rD = int(args[0][1::])
    rN = int(args[1][1::])
    iM = int(args[2])
    REG[rD].int = s64(REG[rN].int + s64(iM))
    return

#tested
def adds(args):
    rD = int(args[0][1::])
    rN = int(args[1][1::])
    rM = int(args[2][1::])
    s.flags = [0]*4
    REG[rD].int = s64(REG[rN].int + REG[rM].int)
    if not REG[rD].int:
        s.flags[0] = 1
    if REG[rD].int < 0:
        s.flags[1] = 1
    if(REG[rD].uint < REG[rN].uint or REG[rD].uint < REG[rM].uint):
        s.flags[2] = 1
    if (REG[rD].int != REG[rN].int + REG[rM].int):
        s.flags[3] = 1
    #show flags: [0] = Z, [1] = N, [2] = C, [3] = V
    return

#tested
def addis(args):
    rD = int(args[0][1::])
    rN = int(args[1][1::])
    iM = int(args[2])
    s.flags = [0]*4
    REG[rD].int = s64(REG[rN].int + s64(iM))
    if not REG[rD].int:
        s.flags[0] = 1
    if REG[rD].int < 0:
        s.flags[1] = 1
    if(REG[rD].uint < REG[rN].uint or REG[rD] < s64(iM).uint):
        s.flags[2] = 1
    if (REG[rD].int != REG[rN].int + iM):
        s.flags[3] = 1
    #show flags: [0] = Z, [1] = N, [2] = C, [3] = V
    return

#tested
def aand(args):
    rD = int(args[0][1::])
    rN = int(args[1][1::])
    rM = int(args[2][1::])
    REG[rD].int = REG[rN].int & REG[rM].int
    return

#tested
def andi(args):
    rD = int(args[0][1::])
    rN = int(args[1][1::])
    iM = int(args[2])
    REG[rD].int = s64(REG[rN].int & s64(iM))
    return

#tested
def ands(args):
    rD = int(args[0][1::])
    rN = int(args[1][1::])
    rM = int(args[2][1::])
    s.flags = [0]*4
    REG[rD].int = s64(REG[rN].int & REG[rM].int)
    if not REG[rD].int:
        s.flags[0] = 1
    if REG[rD].int < 0:
        s.flags[1] = 1
    return

#tested
def andis(args):
    rD = int(args[0][1::])
    rN = int(args[1][1::])
    iM = int(args[2])
    s.flags = [0]*4
    REG[rD].int = s64(REG[rN].int & s64(iM))
    #show stored result as int and hex
    if not REG[rD].int:
        s.flags[0] = 1
    if REG[rD].int < 0:
        s.flags[1] = 1
    #show flags: [0] = Z, [1] = N, [2] = C, [3] = V
    return

#tested
def b(args):
    # Find the label location
    if args[0] in LBS:
        s.ip = LBS[args[0]]
    return

#tested
def beq(args):
    if s.flags[0]:
        if args[0] in LBS:
            s.ip = LBS[args[0]]
    return

#tested
def bne(args):
    if not s.flags[0]:
        if args[0] in LBS:
            s.ip = LBS[args[0]]
    return

#tested
def blt(args):
    if s.flags[1] != s.flags[3]:
        if args[0] in LBS:
            s.ip = LBS[args[0]]
    return

#tested
def ble(args):
    if not(s.flags[0] == 0 and s.flags[1] == s.flags[3]):
        if args[0] in LBS:
            s.ip = LBS[args[0]]
    return

#tested
def bgt(args):
    if s.flags[0] == 0 and s.flags[1] == s.flags[3]:
        if args[0] in LBS:
            s.ip = LBS[args[0]]
    return

#tested
def bge(args):
    if s.flags[1] == s.flags[3]:
        if args[0] in LBS:
            s.ip = LBS[args[0]]
    return

def bhs(args):
    if s.flags[2]:
        if args[0] in LBS:
            s.ip = LBS[args[0]]
    return

def blo(args):
    if not s.flags[2]:
        if args[0] in LBS:
            s.ip = LBS[args[0]]
    return

def bls(args):
    if not(s.flags[0] == 0 and s.flags[2] == 1):
        if args[0] in LBS:
            s.ip = LBS[args[0]]
    return

def bhi(args):
    if not s.flags[0] and s.flags[2]:
        if args[0] in LBS:
            s.ip = LBS[args[0]]
    return

def bmi(args):
    if s.flags[1] == 1:
        if args[0] in LBS:
            s.ip = LBS[args[0]]
    return

def bpl(args):
    if not s.flags[1]:
        if args[0] in LBS:
            s.ip = LBS[args[0]]
    return

def bvs(args):
    if s.flags[3] == 1:
        if args[0] in LBS:
            s.ip = LBS[args[0]]
    return

def bvc(args):
    if not s.flags[3]:
        if args[0] in LBS:
            s.ip = LBS[args[0]]
    return

def bal(args):
    if args[0] in LBS:
        s.ip = LBS[args[0]]
    return

def bnv(args):
    if args[0] in LBS:
        s.ip = LBS[args[0]]
    return

#tested
def bl(args):
    REG[30].int = s.ip + 1
    if args[0] in LBS:
        s.ip = LBS[args[0]]
    return

#tested
def br(args):
    rD = int(args[0][1::])
    s.ip = REG[rD].int
    return

#tested
def cbz(args):
    rT = int(args[0][1::])
    if REG[rT].int == 0:
        if args[1] in LBS:
            s.ip = LBS[args[1]]
    return

#tested
def cbnz(args):
    rT = int(args[0][1::])
    if REG[rT].int != 0:
        if args[1] in LBS:
            s.ip = LBS[args[1]]
    return

#tested
def cmp(args):
    s.flags=[0]*4
    rN = int(args[0][1::])
    rM = int(args[1][1::])
    if REG[rN].int < REG[rM].int:
        s.flags[1] = 1
    if  REG[rN].int == REG[rM].int:
        s.flags[0] = 1
    return

#tested
def cmpi(args):
    s.flags=[0]*4
    rT = int(args[0][1::])
    iM = s64(int(args[1]))
    if REG[rT].int < iM:
        s.flags[1] = 1
    if REG[rT].int == iM:
        s.flags[0] = 1
    return

#tested
def eor(args):
    rD = int(args[0][1::])
    rN = int(args[1][1::])
    rM = int(args[2][1::])
    REG[rD].int = REG[rN].int ^ REG[rM].int
    return

#tested
def eori(args):
    rD = int(args[0][1::])
    rN = int(args[1][1::])
    iM = int(args[2])
    REG[rD].int = REG[rN].int ^ iM
    return

#tested
def ldur(args):
    rT = int(args[0][1::])
    rN = int(args[1][1::])
    iM = int(args[2])
    index = REG[rN].int + s64(iM)
    #reset rT to 0
    REG[rT].clear()
    if  index < 991:
        if rT == 28:
            for i in range(8):
                REG[rT].insert(STK[index+i], i*8)
        else:
            for i in range(8):
                REG[rT].insert(MEM[index+i], i*8)
    return

#tested
def ldurb(args):
    rT = int(args[0][1::])
    rN = int(args[1][1::])
    iM = int(args[2])

    index = REG[rN].int + s64(iM)
    REG[rT] = s.b.BitArray(length=64)
    # reset rT to 0
    if index < 991:
        if rT == 28:
            REG[rT].overwrite(STK[index], 56)
        else:
           REG[rT].overwrite(MEM[index], 56)
    return

#tested
def ldurh(args):
    rT = int(args[0][1::])
    rN = int(args[1][1::])
    iM = int(args[2])

    index = REG[rN].int + s64(iM)
    REG[rT] = s.b.BitArray(length=64)
    # reset rT to 0
    if index < 991:
        if rT == 28:
            REG[rT].overwrite(STK[index + 1], 56)
            REG[rT].overwrite(STK[index], 48)
        else:
            REG[rT].overwrite(MEM[index+1], 56)
            REG[rT].overwrite(MEM[index], 48)

    return

#tested
def ldursw(args):
    rT = int(args[0][1::])
    rN = int(args[1][1::])
    iM = int(args[2])

    index = REG[rN].int + s64(iM)
    temp = s.b.BitArray(length=32)
    # reset rT to 0
    if index < 991:
        if rT == 28:
            temp.overwrite(STK[index + 3], 24)
            temp.overwrite(STK[index + 2], 16)
            temp.overwrite(STK[index + 1], 8)
            temp.overwrite(STK[index], 0)
            REG[rT].int = s64(temp.int)
        else:
            temp.overwrite(MEM[index + 3], 24)
            temp.overwrite(MEM[index + 2], 16)
            temp.overwrite(MEM[index + 1], 8)
            temp.overwrite(MEM[index], 0)
            REG[rT].int = s64(temp.int)
    return

#tested
def lsl(args):
    rD = int(args[0][1::])
    rN = int(args[1][1::])
    iM = int(args[2])
    REG[rD].int = REG[rN].int << iM
    return

#tested
def lsr(args):
    rD = int(args[0][1::])
    rN = int(args[1][1::])
    iM = int(args[2])
    REG[rD].int = REG[rN].int >> iM
    return

def movz(args):
    rD = int(args[0][1::])
    iM = int(args[1])
    MiM = int(args[3])
    REG[rD] = (iM << MiM)
    return

def movk(args):
    rD = int(args[0][1::])
    iM = int(args[1])
    MiM = int(args[3])
    REG[rD] = (iM << MiM) | iM
    return

#tested
def orr(args):
    rD = int(args[0][1::])
    rN = int(args[1][1::])
    rM = int(args[2][1::])
    REG[rD].int = REG[rN].int | REG[rM].int
    return

#tested
def orri(args):
    rD = int(args[0][1::])
    rN = int(args[1][1::])
    iM = int(args[2])
    REG[rD].int = REG[rN].int | s64(iM)
    return

#tested
def sub(args):
    rD = int(args[0][1::])
    rN = int(args[1][1::])
    rM = int(args[2][1::])
    REG[rD].int = s64(REG[rN].int - REG[rM].int)
    return

#tested
def subi(args):
    rD = int(args[0][1::])
    rN = int(args[1][1::])
    iM = int(args[2])
    REG[rD].int = s64(REG[rN].int - s64(iM))
    return

#tested
def subs(args):
    rD = int(args[0][1::])
    rN = int(args[1][1::])
    rM = int(args[2][1::])
    s.flags = [0]*4
    REG[rD].int = s64(REG[rN].int - REG[rM].int)
    if not REG[rD].int:
        s.flags[0] = 1
    if REG[rD].int < 0:
        s.flags[1] = 1
    if(REG[rN].uint < REG[rM].uint):
            s.flags[2] = 1
    if (REG[rD].int != REG[rN].int - REG[rM].int):
        s.flags[3] = 1
    return

#tested
def subis(args):
    rD = int(args[0][1::])
    rN = int(args[1][1::])
    iM = int(args[2])
    s.flags = [0]*4
    REG[rD].int = s64(REG[rN].int - s64(iM))
    if not REG[rD].int:
        s.flags[0] = 1
    if REG[rD].int < 0:
        s.flags[1] = 1
    if(REG[rN].uint < iM):
        s.flags[2] = 1
    if (REG[rD].int != REG[rN].int - s64(iM)):
        s.flags[3] = 1
    return

#tested
def stur(args):
    rT = int(args[0][1::])
    rN = int(args[1][1::])
    iM = int(args[2])
    j = REG[rN].int + s64(iM)
    if j < 991:
        if rN == 28:
            for byte in REG[rT].cut(8):
                STK[j] = byte
                j += 1
        else:
            for byte in REG[rT].cut(8):
                MEM[j] = byte
                j += 1
    return

#tested
def sturb(args):
    rT = int(args[0][1::])
    rN = int(args[1][1::])
    iM = int(args[2])
    if REG[rN].int + s64(iM) < 1000:
        if rN == 28:
            STK[REG[rN].int + s64(iM)].int = REG[rT][56:64].int
        else:
            MEM[REG[rN].int + s64(iM)].int = REG[rT][56:64].int
    return

#tested
def sturh(args):
    rT = int(args[0][1::])
    rN = int(args[1][1::])
    iM = int(args[2])

    index = REG[rN].int + s64(iM)
    if index < 991:
        if rN == 28:
            STK[index].int = REG[rT][48:56].int
            STK[index + 1].int = REG[rT][56:64].int
        else:
            MEM[index + 1].int = REG[rT][56:64].int
            MEM[index].int = REG[rT][48:56].int
    return

#tested
def sturw(args):
    rT = int(args[0][1::])
    rN = int(args[1][1::])
    iM = int(args[2])

    index = REG[rN].int + s64(iM)
    byte = REG[rT][56:64]
    bytes = REG[rT][49:57]
    if index < 991:
        if rN == 28:
            STK[index + 3].int = REG[rT][56:64].int
            STK[index + 2].int = REG[rT][48:56].int
            STK[index + 1].int = REG[rT][40:48].int
            STK[index].int = REG[rT][32:40].int

        else:
            MEM[index + 3].int = REG[rT][56:64].int
            MEM[index + 2].int = REG[rT][48:56].int
            MEM[index + 1].int = REG[rT][40:48].int
            MEM[index ].int = REG[rT][32:40].int
    return

def setZero():
    REG[31].int = 0
