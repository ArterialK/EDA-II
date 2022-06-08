def Equipos(Lista,Numero):
    NE=ceil(len(Lista)/Numero)
    i=len(Lista)-1
    conde=1
    Equipo={}
    while (conde != (NE+1)):
        Equipo[conde]=[Lista[i]]
        i=i-1
        if i-1 != -2:
            for retro in range(Numero-1):
                if i-1 != -1:
                    Equipo[conde]+=[Lista[i]]
                    i=i-1
        conde=conde+1
        
    print("Los equipos son:\n",Equipo)

A=["Juan","Pedro","Pancho","Ester","Julia","pollo","Ana","Pablo","Rosa"]
Equipos(A,2)
