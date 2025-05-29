; AllocatorX86.asm
[BITS 32]

section .data
	x dd 5 ; <---- asume x is 5
	y dd 25; <--- asume y is 25

section .text
	global _start

_start:
	mov ebx,[x]
	mov eax.[y]



