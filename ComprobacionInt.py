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
