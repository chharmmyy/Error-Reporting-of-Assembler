START:  MVI A, 05H
        MVI B, 0AH
LOOP:   ADD B
        SUB C
        INR A
        DCR B
        JNZ LOOP

        MUV A, B        
LOOP:   ADD A           
        JMP END_LABEL   
        LXI H, 2000H
        MOV M, A
        IN 01H
        OUT 02H

        XYZ B           

END:    HLT