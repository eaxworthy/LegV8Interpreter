# LegV8Interpreter
Johnathan Soto and Elizabeth Axworthy
Requires Python3.7.3 64-bit,
Dependencies: bitstring, numpy

For LDUR and STUR we assume that an immediate values given to signify
the shift from the base address in a d-type instruction will
be a multiple of 8, to represent that we're working with 64
bit numbers (which are 8 bytes long). This follows the book' example
For example: let x5 hold the base address of array A.
 LDUR x4 [x5, #8] would be allowed, and return A[1]
 LDUR x4 [x5, #7] would not be allowed, and would return 0
