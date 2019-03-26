import numpy as np
import funcs as f
import state as s
import bitstring as b
import re
import sys

# To see the values stored in a registers in a certain format:
#    print(b.(s.registers[int(values[i])]).int)
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
    'B.cond': f.bcond,
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
    #TODO: tokenize string
    for i in range(0, len(values)-1, 2):

        #translate input into a hex value 2's complement
        temp = hex(int(values[i+1], 0) if int(values[i+1], 0)>0 else int(values[i+1], 0)+(2**64))
        #translate back into signed int >:(

        print(temp)
        #s.registers[int(values[i])] = b.BitArray(int = temp, length = 64)
        #print(s.registers[int(values[i])].int)


load_registers()
#print(s.registers)
#x = input("Enter Instruction: ")
#x = re.sub(r'[^\w\s]','',x)
#print(x)
#values = x.split()
#functions[values[0]](values[1::])
