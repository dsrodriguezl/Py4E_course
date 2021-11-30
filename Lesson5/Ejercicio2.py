#
#

def calcula_calificacion(Punt):
    try:
        Punt = float(Punt)
        test = 1.0 - Punt
        if test >= 0:
            if Punt < 0:
                print("Error, la puntuación debe ser un número entre 0.0 y 1.0")
            elif Punt >= 0.9:
                print("Sobresaliente")
            elif Punt >= 0.8:
                print("Notable")
            elif Punt >= 0.7:
                print("Bien")
            elif Punt >= 0.6:
                print("Suficiente")
            else:
                print("Insuficiente")
        else:
            print("Error, la puntuación debe ser un número entre 0.0 y 1.0")
    except:
        print("Error, introduzca un número")

Punt = input("Cual fue su puntuación?")
calcula_calificacion(Punt)
