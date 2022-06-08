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

def ParImpar(Lista):
    temp=[0]
    temp+=Lista[:len(Lista)]
    for i in range(len(temp)):
        for j in range (0,len(Lista)):
            if (i==0) or (i%2!=0):
                if (Lista[j]%2==0) and (Lista[j]!=0):
                    temp[i]=Lista[j]
                    print("Posicion: ",i," Valor",Lista[j])
                    Lista[j]=0
                    break
                if j == len(Lista)-1:
                    temp[i]=0
                    print("Posicion: ",i," Valor",Lista[j])
                    
            else:
                if (Lista[j]%2==1) and (Lista[j]!=0):
                    temp[i]=Lista[j]
                    print("Posicion: ",i," Valor",Lista[j])
                    Lista[j]=0
                    break
                if j == len(Lista)-1:
                    temp[i]=0
                    print("Posicion: ",i," Valor",Lista[j])
    Arbol(temp)
    print("\n\n",temp)

A=[1,2,3,4,5,6,7,8]
ParImpar(A)
