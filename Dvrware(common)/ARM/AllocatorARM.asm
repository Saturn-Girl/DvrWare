; AllocatorARM.asm
    .section .data
x:  .word 5       @ assume x is 5
y:  .word 25      @ assume y is 25

    .section .text
    .global _start

_start:
    LDR R3, =x       @ Load address of x into R3
    LDR R3, [R3]     @ Load value at x into R3 (like ebx)

    LDR R0, =y       @ Load address of y into R0
    LDR R0, [R0]     @ Load value at y into R0 (like eax)

    /* ... further code ... */
