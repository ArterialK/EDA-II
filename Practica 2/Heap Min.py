def Arbol(Lista):
    for i in range(len(Lista)):
        if (2*i+1) <= len(Lista)-1:
            if (2*i+2) <= len(Lista)-1:
                print ("De la rama",Lista[i])
                print("Su hoja izquierda es: ",Lista[2*i+1])
                print("Y su hoja derecha es: ",Lista[2*i+2])
            else:
                print ("De la rama",Lista[i])
                print("Su hoja izquierda es: ",Lista[2*i+1])
                print("Y no tiene hoja derecha")
        else:
            i=len(Lista)
            
def HeapMin(Lista):
    for k in range(3):
        for i in range(len(Lista)):
            if (2*i+1) <= len(Lista)-1:
                if (2*i+2) <= len(Lista)-1:
                    if (Lista[i] < Lista[2*i+1]) and (Lista[i] < Lista[2*i+2]):
                        if Lista[2*i+1] > Lista[2*i+2]:
                            temp = Lista[2*i+1]
                            Lista[2*i+1] = Lista[2*i+2]
                            Lista[2*i+2] = temp
                    else:
                        if (Lista[2*i+1] < Lista[2*i+2]) and (Lista[2*i+1] < Lista[i]):
                            temp=Lista[i]
                            Lista[i]=Lista[2*i+1]
                            Lista[2*i+1]=temp
                        else:
                            temp=Lista[i]
                            Lista[i]=Lista[2*i+2]
                            Lista[2*i+2]=temp
    for k in range(len(Lista)):                        
        for i in range(len(Lista)):
            if (i+3) <= len(Lista)-1:
                if Lista[i+3] < Lista[i+2]:
                    temp = Lista[i+3]
                    Lista[i+3] = Lista[i+2]
                    Lista[i+2] = temp
            
    Arbol(Lista)

A = [1,5,9,7,3,8,6,2,4]
HeapMin(A)
print("\nLa lista ordenada es: ",A)
