def bubbleShort(A):
    Mitad=int(len(A)/2)
    conde=0
    ASD=A[Mitad:]
    DES=A[:Mitad]
    
    for i in range (1,len(ASD)):
        for j in range(len(ASD)-1):
            conde=conde+1
            if ASD[j] > ASD[j+1]:
                temp = ASD[j]
                ASD[j] = ASD[j+1]
                ASD[j+1] = temp

    for i in range (1,len(DES)):
        conde=conde+1
        for j in range(len(DES)-1):
            conde=conde+1
            if DES[j] < DES[j+1]:
                temp = DES[j]
                DES[j] = DES[j+1]
                DES[j+1] = temp
    Lista=ASD,DES
    print("\nnumero de iteraciones: ",conde)
                
    return Lista
                
A = [1,3,9,0,10,13,3,43,21,1,19,87,32,2,43,56,6,1,7,91,11,2,4,22,10,24,23,15]
print("\nLa lista dividida es: ",bubbleShort(A))
