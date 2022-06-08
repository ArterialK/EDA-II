import numpy as np
def Condicion():
    Int=0
    while Int < 3:
        Caso= input("Ingresa:  ")
        try:
            Caso=int(Caso)
            return Caso
        except ValueError:
                Int += 1
                print("Numero de intentos restantes:",3-Int)
    raise ValueError ("Exedio numero de intentos")

#def CrearM(): 
#    print("Intresa el numero de columnas")
#    col=Condicion()
#    print("Ingresa el numero de renglones")
#    ren=Condicion()
#    matriz= np.empty((col,ren))
#    for i in range(col):
#        for j in range(ren):
#            print("ingresa el valor de la posicion ",i+1,",",j+1)
#            matriz[(i,j)]=Condicion()
#    lim=[ren,col]
#    return matriz,lim

def CMatriz (Lista):
    print("Ingresa las dimenciones de la matriz")
    print("\nFilas: ")
    ren=Condicion()
    print("\nColumnas: ")
    col=Condicion()
    matriz= np.empty((col,ren))
    for j in range(ren):
        for i in range(col):
            if len(Lista)!=0:
                matriz[(j,i)]=int(Lista[0])
                Lista.pop(0)
    lim=[ren,col]
    return matriz,lim

Lista=[1,2,1,5,0,3,0,9,1,9,3,1,1,1,3,6,8,9,1,3,8,5,1,0]
Matriz,lim=CMatriz(Lista)
Ini=0
Fin=0
#Matriz=CrearM()
print("Que distancia quieres?")
while (Ini>lim[0]) or (Ini<=0):
    print("\nInicio")
    Ini=Condicion()
while (Fin>lim[1]) or (Fin<=0):
    print("\nFinal")
    Fin=Condicion()
print("La distancia entre ",Ini," y ",Fin," es:",int(Matriz[Ini-1,Fin-1]))
if int(Matriz[Ini-1,Fin-1])==0:
    print("No exixte camino entre ",Ini,"Y",Fin)
if int(Matriz[Ini-1,Ini-1])!= 0:
    print("El nodo ",Ini,"Tiene realimentacion")
else:
    print("El nodo ",Ini,"No tiene realimentacion")
if int(Matriz[Fin-1,Fin-1])!= 0:
    print("El nodo ",Fin,"Tiene realimentacion")
else:
    print("El nodo ",Fin,"No tiene realimentacion")
