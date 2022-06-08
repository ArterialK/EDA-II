def Condicion():
    Int=0
    while Int < 3:
        Caso= input("Elige:  ")
        try:
            Caso=int(Caso)
            return Caso
        except ValueError:
                Int += 1
    raise ValueError ("Exedio numero de intentos")
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

def Heap(Comando,Lista):
    if Comando == 1:
        for k in range(3):
            for i in range(len(Lista)):
                if (2*i+1) <= len(Lista)-1:
                    if (2*i+2) <= len(Lista)-1:
                        if (Lista[i] > Lista[2*i+1]) and (Lista[i] > Lista[2*i+2]):
                            if Lista[2*i+1] < Lista[2*i+2]:
                                temp = Lista[2*i+1]
                                Lista[2*i+1] = Lista[2*i+2]
                                Lista[2*i+2] = temp
                        else:
                            if (Lista[2*i+1] > Lista[2*i+2]) and (Lista[2*i+1] > Lista[i]):
                                temp=Lista[i]
                                Lista[i]=Lista[2*i+1]
                                Lista[2*i+1]=temp
                            else:
                                temp=Lista[i]
                                Lista[i]=Lista[2*i+2]
                                Lista[2*i+2]=temp
        for k in range(3):                        
            for i in range(len(Lista)):
                if (i+3) <= len(Lista)-1:
                    if Lista[i+3] > Lista[i+2]:
                        temp = Lista[i+3]
                        Lista[i+3] = Lista[i+2]
                        Lista[i+2] = temp
            
        Arbol(Lista)
    
    if Comando == 2:
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
        for k in range(len(Lista)-5):                        
            for i in range(len(Lista)):
                if (i+3) <= len(Lista)-1:
                    if Lista[i+3] < Lista[i+2]:
                        temp = Lista[i+3]
                        Lista[i+3] = Lista[i+2]
                        Lista[i+2] = temp
            
        Arbol(Lista)

Lista=[1,5,9,7,3,8,6,2,4]
print("La lista Base es: ",Lista)
print("Como quieres heapearla")
print("Heap-Max........(1)")
print("Heap-Min........(2)")
Caso=Condicion()
Heap(Caso,Lista)
print("\n\nLista Ordenada: ",Lista)
