import numpy as np
import funcs as f
import state as s
import bitstring as b
import re


# To see the values stored in a registers in a certain format:
#    print(s.registers[int(values[i])].int)
# where .int is replaces with .(chosen format)

functions = {
    'ADD': f.add,
    'ADDI': f.addi,
    'ADDS': f.adds,
    'ADDIS': f.addis,
    'AND': f.aand, #needs to be spelled like this because 'and' is reserved
    'ANDI': f.andi,
    'ANDS': f.ands,
    'ANDIS': f.andis,
    'B': f.b,
    'BEQ': f.beq,
    'BNE': f.bne,
    'BLT': f.blt,
    'BLE': f.ble,
    'BGT': f.bgt,
    'BGE': f.bge,
    'BHS': f.bhs,
    'BLO': f.blo,
    'BLS': f.bls,
    'BHI': f.bhi,
    'BL': f.bl,
    'BR': f.br,
    'CBZ': f.cbz,
    'CBNZ': f.cbnz,
    'CMP': f.cmp,
    'CMPI': f.cmpi,
    'EOR': f.eor,
    'EORI': f.eori,
    'MOVZ': f.movz,
    'MOVK':f.movk,
    'LDUR': f.ldur,
    'LDURB': f.ldurb,
    'LDURH': f.ldurh,
    'LDURSW': f.ldursw,
    'LDXR': f.ldxr,
    'LSL': f.lsl,
    'LSR': f.lsr,
    'ORR': f.orr,
    'ORRI': f.orri,
    'SUB': f.sub,
    'SUBI': f.subi,
    'SUBS': f.subs,
    'SUBIS': f.subis,
    'STUR': f.stur,
    'STURB': f.sturb,
    'STURH': f.sturh,
    'STURW': f.sturw,
    'STXR': f.stxr,
}

def load_memory():
    st = input("Enter initial memory values: ")
    values = st.split()
    for i in range(0, len(values)-1, 2):
        #bitstrings don't pad with leading 0's, so to keep 64bit size limit,
        #we need to translate anygiven hex into a signed int. If number is
        #above limit, the msb's will be chopped off
        temp = values[i+1]
        temp = f.s64(int(temp, 0))
        (s.MEM[int(values[i])]).int = temp
        #print(s.MEM[int(values[i])])

LegCode = []
load_memory()


#progFile = input("Enter name of program file: ")
with open("simple_test.txt", 'r') as file:
    lines = file.readlines()
    for line in lines:
        if line != '\n':
            LegCode.append(line.rstrip())

#First pass to collect labels. It then trims the label from the beginning of
#the stored instruction so that we don't need to repeatedly check the beginning
#of each lines when we enter the execution phase.
for N in range(len(LegCode)):
    x = LegCode[N]
    x = re.sub(r'[^\w\s]','',x)
    ins_params = x.split()
    if ins_params[0] not in functions:
        s.LBS[ins_params[0]] = N
        LegCode[N] = re.sub(r'^\W*\w+\W*', '', LegCode[N])


while s.ip < len(LegCode):
    runMode = input("Run(1) or Step(2): ")
    if runMode == "1":
        while s.ip < len(LegCode):
            N = s.ip
            x = LegCode[s.ip]
            if x != "":
                x = re.sub(r'[^\w\s]','',x)
                ins_params = x.split()
                functions[ins_params[0]](ins_params[1::])
                f.setZero()
                if N == s.ip:
                    s.ip += 1
            else:
                s.ip += 1
        break;
    if runMode == "2":
        N = s.ip
        x = LegCode[s.ip]
        if x != "":
            x = re.sub(r'[^\w\s]','',x)
            ins_params = x.split()
            print("Doing Instruction: ", x)
            functions[ins_params[0]](ins_params[1::])
            f.setZero()
            if N == s.ip:
                s.ip += 1
            doPrint = input("Print Registers Y(1) / N(2): ")
            if doPrint == "1":
                s.printRegs()
        else:
            s.ip += 1

s.printRegs()
