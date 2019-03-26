#TODO: Maybe switch over to using bitstrings instead of numbers
#      to make 2's complement easier so that we don't go over
#      the 8 byte size limit?
import bitstring as b
registers = [b.BitArray(int = 0, length = 64)] * 32
XZR = 31

#let 0 = Z, 1 = N, 2 = C, 3 = V
flags = [0] * 4
