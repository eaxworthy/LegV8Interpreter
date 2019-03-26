import numpy as np
import funcs as f
import state as s
import re


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
    str = input("Enter initial memory values: ")
    values = str.split()
    #TODO: tokenize string
    for i in range(0, len(values)-1, 2):
        s.registers[int(values[i])] = int(values[i+1])

#
x = input("Enter Instruction: ")
x = re.sub(r'[^\w\s]','',x)
print(x)
values = x.split()
functions[values[0]](values[1::])
#load_registers()
#print(s.registers)
