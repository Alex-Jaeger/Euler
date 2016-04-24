; Written By Alex Jaeger 10 30 2014

INCLUDE Irvine32.inc

.DATA
usr_array	DWORD 10 DUP(0)
perm_array	DWORD 8, 3, 5, 9, 2, 6, 0, 4, 1, 7
four		DWORD 4

.CODE
main PROC
	mov ecx, LENGTHOF usr_array
	mov ebx, 0

	; Read Loop reads 10 ints into the usr_array
	readLoop:
		call ReadInt
		mov[usr_array + ebx], eax
		add ebx, 4; Adds 4 bytes to ebx offset because of DWORD byte size
		loop readLoop

	mov ecx, LENGTHOF usr_array
	mov ebx, 0

	; Perm loop grabs values from arrays and switches them
	permLoop:
		mov	esi, [usr_array + ebx]; esi = usr_array[i]
		mov eax, [perm_array + ebx]; edx = perm_array[i]
		mov edi, [usr_array + eax * 4]; edi = usr_array[perm_array[i]]

        xchg edi, esi; exchanges usr_array[perm_array[i]] and usr_array[i]

        mov[usr_array + ebx], edi
        mov[usr_array + eax * 4], esi

        mul four
        mov ebx, eax

        loop permLoop

	mov ecx, LENGTHOF usr_array
    mov ebx, 0

	; printLoop prints all 10 ints in usr_array to stdout
	printLoop:
		mov eax, [usr_array + ebx]
			call WriteInt

		add ebx, 4 ; Adds 4 bytes to ebx offset because of DWORD byte size 
		loop printLoop

	exit
main ENDP
END main
