def Condicion():
    Int=0
    while Int < 3:
        Caso= input("Ingresa:  ")
        try:
            Caso=int(Caso)
            return Caso
        except ValueError:
                Int += 1
    raise ValueError ("Exedio numero de intentos")

def Hash (L,M):
    Dicc={}
    if M==1:
        #m=len(L)+1
        m=6
        j=0
        for i in range(len(L)):
            XH=L[i]-int(m*int(L[i]/m))
            if ((XH,j) in Dicc) == True:
                for j in range(len(L)):
                    if ((XH,j) in Dicc) == False:
                        Dicc[XH,j]=L[i]
                        break
            else:
                j=0
                Dicc[XH,j]=L[i]
    elif M==2:
        #m=len(L)+1
        m=6
        j=0
        #print("ingresa valor de A: ")
        #A=Condicion()
        A=0.5
        for i in range(len(L)):
            XH=int(m*(L[i]*A-int(L[i]*A)))
            if ((XH,j) in Dicc) == True:
                for j in range(len(L)):
                    if ((XH,j) in Dicc) == False:
                        Dicc[XH,j]=L[i]
                        break
            else:
                j=0
                Dicc[XH,j]=L[i]
    print("Acomodo Hash terminado, con un m =",m)
    print(Dicc)

Lista=[13579837,27528519,77665491,63153143,11234578,23537109]
#print("La lista a operar es: ",Lista)
#print("Division...............(1)")
#print("Multiplicacion.........(2)")
#Modo=Condicion()
#print("Ingresa el valor de m: ",)
#m=Condicion()
Hash(Lista,1)
