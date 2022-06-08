def CrearSubArreglo(A,indIzq,indDer):
    return A[indIzq:indDer+1]

def Merge (A,p,q,r):
    izq = CrearSubArreglo(A,p,q)
    print("\nLista 1: ",izq)
    der = CrearSubArreglo(A,q+1,r)
    print("lista 2: ",der)
    i=0
    j=0
    k=0
    for k in range(p,r+1):
        if (j >= len(der)) or (i < len (izq) and izq[i] < der[j]):
            A[k] = izq[i]
            i = i + 1
        else:
            A[k] = der[j]
            j = j + 1 

def MergeSort(A,p,r):
    if r - p > 0:
        q = int ((p+r)/2)
        MergeSort(A,p,q)
        MergeSort(A,q+1,r)
        Merge(A,p,q,r)        
A = [1,3,9,0,10,13,3,43,21,1,19,87,32,2,43,56,6,1,7,91,11,2,4,22,10,24,23,15]
MergeSort(A,0,len(A)-1)
print("\nLista ordenada: ",A)
