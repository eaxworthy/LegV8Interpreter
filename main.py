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
    'B.EQ': f.beq,
    'B.NE': f.bne,
    'B.LT': f.blt
    'B.LE': f.ble,
    'B.GT': f.bgt,
    'B.GE': f.bge,
    'B.HS': f.bhs,
    'B.LO': f.blo,
    'B.LS': f.bls,
    'B.HI': f.bhi,
    'BL': f.bl,
    'BR': f.br,
    'CBZ': f.cbz,
    'CBNZ': f.cbnz,
    'EOR': f.eor,
    'EORI': f.eori,
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

def load_registers():
    st = input("Enter initial memory values: ")
    values = st.split()
    for i in range(0, len(values)-1, 2):
        #bitstrings don't pad with leading 0's, so to keep 64bit size limit,
        #we need to translate anygiven hex into a signed int. If number is
        #above limit, the msb's will be chopped off
        temp = values[i+1]
        temp = f.s64(int(temp, 0))
        (s.memory[int(values[i])]).int = temp

load_registers()

''' Code for a txt file

LegCode = []
with open("test.txt", 'r') as f:
    lines = f.readlines()
    LegCode.append(lines)
    
for N in range(len(LegCode)):
    x = LegCode[N]
    x = re.sub(r'[^\w\s]','',x)
    #print(x)
    values = x.split()
    # check to see if the first thing is a "label: "
    functions[values[0]](values[1::])
'''
    
x = input("Enter Instruction: ")
x = re.sub(r'[^\w\s]','',x)
#print(x)
values = x.split()
functions[values[0]](values[1::])
