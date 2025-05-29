        .org $8000          ; start address

; Data section (little endian 32-bit values)
x:      .byte 5, 0, 0, 0    ; x = 5 (0x00000005)
y:      .byte 25, 0, 0, 0   ; y = 25 (0x00000019)

; Code section
_start:
        ; Load low byte of x into A
        LDA x

        ; Store it somewhere (for example, zero page $00)
        STA $00

        ; Load low byte of y into A
        LDA y

        ; Store it somewhere (for example, zero page $01)
        STA $01

        ; (your code here)

        ; Infinite loop to end program
loop:
        JMP loop
