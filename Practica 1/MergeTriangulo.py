def CrearSubArreglo(A,indIzq, indDer):
    return A[indIzq:indDer+1]

def Merge(A,p,q,r):
    Izq = CrearSubArreglo(A,p,q)
    Der = CrearSubArreglo(A,q+1,r)
    i = 0
    j = 0
    conde=0
    for k in range(p,r+1):
        conde=conde+1
        if(j >= len(Der)) or (i < len(Izq) and Izq[i] < Der[j]):
            A[k] = Izq[i]
            i = i + 1
        else:
            A[k] = Der[j]
            j = j + 1
    return conde
            
def MergeSort(A,p,r):
    conta=0
    conta=conta+1
    if r - p > 0:
        q = int((p+r)/2)
        MergeSort(A,p,q)
        MergeSort(A,q+1,r)
        conta=conta+Merge(A,p,q,r)
    return conta

def Merge2(A,p,q,r):
    Izq = CrearSubArreglo(A,p,q)
    Der = CrearSubArreglo(A,q+1,r)
    i = 0
    j = 0
    conde=0
    for k in range(p,r+1):
        conde=conde+1
        if(j >= len(Der)) or (i < len(Izq) and Izq[i] > Der[j]):
            A[k] = Izq[i]
            i = i + 1
        else:
            A[k] = Der[j]
            j = j + 1
    return conde
            
def MergeSort2(A,p,r):
    conta=0
    conta=conta+1
    if r - p > 0:
        q = int((p+r)/2)
        MergeSort2(A,p,q)
        MergeSort2(A,q+1,r)
        conta=conta+Merge2(A,p,q,r)
    return conta
        
def Reorde(A):
    Mitad= int(len(A)/2)
    ASD=A[:Mitad]
    DES=A[Mitad:]
    a=MergeSort(ASD,0,len(ASD)-1)
    b=MergeSort2(DES,0,len(DES)-1)
    print("Numero de iteraciones: ",a+b)
    Lista=ASD,DES
    return Lista
        
A = [1,3,9,0,10,13,3,43,21,1,19,87,32,2,43,56,6,1,7,91,11,2,4,22,10,24,23,15]
LISTA=Reorde(A)
print("\nLa lista dividida es:\n",LISTA)
