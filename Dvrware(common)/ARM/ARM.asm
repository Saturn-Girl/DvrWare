;ARM.asm
    .section .data
bit:
    .word 32          @ 32-bit data

    .section .text
    .global _start

_start:
    ldr r0, =bit      @ Load address of bit into r0
    ldr r1, [r0]      @ Load the 32-bit value stored at bit into r1

    /* 
    Now r1 contains the value 32, similar to eax in x86 
    */
