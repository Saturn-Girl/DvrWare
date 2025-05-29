; 6502.asm
; 6502 version with 16-bit data

    .segment "DATA"
bit:
    .word 32       ; 16-bit value 32 stored here (low byte first)

    .segment "CODE"
    .org $8000     ; start of program (example address)

_start:
    LDA bit        ; load low byte of 'bit' into A
    LDX bit+1      ; load high byte of 'bit' into X

    ; Now A = low byte, X = high byte of the 16-bit value at 'bit'
    ; You can combine or use them as needed

    ; (example: do nothing, infinite loop)
loop:
    JMP loop
