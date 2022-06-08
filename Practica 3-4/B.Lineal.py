def Busqueda(Lista,Nbusc):
    conde=0
    lugar=[]
    for i in range (1,len(Lista)):
       for j in range(len(Lista)-1):
           if Lista[j] > Lista[j+1]:
               temp = Lista[j]
               Lista[j] = Lista[j+1]
               Lista[j+1] = temp
    for i in range(len(Lista)):
        if Lista[i]==Nbusc:
            print("Se encontro el elemento: ",Nbusc," en la posicion: ",i)
            conde=conde+1
            lugar+=[i]
            if Lista[i]>Nbusc:
                return
    if conde==0:
        print("El elemento: ",Nbusc," no esta en la lista") 
    else:
        print("El numero",Nbusc,"esta:", conde, "veces en la(s) posicion(es):",lugar)
A = [1,3,9,0,10,13,3,43,21,1,19,87,32,2,43,56,6,1,7,91,11,2,4,22,10,24,23,15]
Busqueda(A,10)
