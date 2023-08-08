import math

por1 = float(input("Porcentaje de que ocurra el suceso (no escribas '%'): ")) # Porcentaje de que ocurra el suceso
por2 = float(input("Porcentaje de que ocurra el suceso al menos una vez (no escribas '%'): ")) # Porcentaje de que ocurra el suceso al menos una vez

if (por1 == 100):
    print("Un 100% de probabilidad siempre hará que el suceso ocurra al primer intento")
elif (por1 == 0):
    print("Un 0% hara que jamas ocurra el suceso")
elif (por2 == 100):
    print("Error: Es imposible que un suceso ocurra al 100% si su probabilidad es menor al 100%")
    print("Recomendacion: Usa 99.9% en vez de 100%")
elif (por2 == 0):
    print("Si la prob. de que ocurra al menos una vez es 0%, se necesitarán 0 tiradas")
else:
    numTirMin = math.log(1-por2/100,1-por1/100)
    print(str(round(numTirMin,5)), "=>", str(math.ceil(numTirMin)), "tiradas posibles para que el suceso ocurra al menos una vez al", str(por2) + "%")