# LegV8Interpreter
Johnathan Soto and Elizabeth Axworthy
Requires Python3.7.3 64-bit,
Dependencies: bitstring, numpy

Assumptions: Based on the sample input given, we assume that if the instruction
pointer equals 0, it is the equivalent of a 'return 0', meaning successful
completion. Thus, the list of instructions to execute are numbered 1 - N. We
append an arbitrary label '-END-' at the beginning of our list of instructions,
LegCode[0], to enforce this system. The first instruction to actually execute
will be at LegCode[1], which will contain the first line found in the provided
.txt file .

Important Notes for writing programs: We use line number to simulate instruction
address. Blank lines are ignored when parsing the .txt file. A jump to a
destination that resolves to 4(decimal) will mean that the next instruction to
execute will be the fourth line to actually contain text. Keep this in mind when
writing programs that require jumping between different instructions. If you need
to debug, add a 'print(LegCode)' to the main file before the while loop to see
what instruction addresses your instructions have been assigned, and calculate
which values you need to load accordingly.
