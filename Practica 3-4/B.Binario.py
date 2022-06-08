from math import ceil
def BuscadorB(Lista,Nbusc):
    pivote=0
    conde=0
    lugar=[]
    for i in range (1,len(Lista)):
       for j in range(len(Lista)-1):
           if Lista[j] > Lista[j+1]:
               temp = Lista[j]
               Lista[j] = Lista[j+1]
               Lista[j+1] = temp
    
    for x in range(1,ceil(len(Lista)/4)+1):
        if ((x*4)-1) < (len(Lista)-1): 
            Subl=Lista[pivote:(x*4)]
        else:
            Subl=Lista[pivote:len(Lista)]
        if Subl[len(Subl)-1] >= Nbusc :
            print("Del arreglo: ",x,"  ",Subl)
            for i in range(len(Subl)):
                if Subl[i]==Nbusc:
                    conde=conde+1
                    lugar+=[i]
                    if Subl[i]>Nbusc:
                        break
        if conde!=0:
            break
        pivote=pivote+4
    if conde==0:
        print("El elemento: ",Nbusc," no esta en la lista")
    else:
        print("El numero",Nbusc,"esta:", conde, "veces en la(s) posicion(es):",lugar)
            
Lista = [1,3,9,0,10,13,3,43,21,1,19,87,32,2,43,56,6,1,7,91,11,2,4,22,10,24,23,15]
BuscadorB(Lista,91)
