def bubbleShort(A):
    conde=0
    for i in range (1,len(A)):
        for j in range(len(A)-1):
            conde=conde+1
            if A[j] > A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
                
    return conde
                
A = [1,3,9,0,10,13,3,43,21,1,19,87,32,2,43,56,6,1,7,91,11,2,4,22,10,24,23,15]
bubbleShort(A)
print("numero de iteraciones: ",bubbleShort(A))
print();
print("Lista ordenada: ",A)
