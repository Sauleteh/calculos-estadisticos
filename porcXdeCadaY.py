print("El suceso ocurre X de cada Y veces")
tr1 = int(input("Introduce la X: ")) # La probabilidad es de [tr1] entre [tr2]
tr2 = int(input("Introduce la Y: "))

probF = tr1 / tr2 * 100
print("La probabilidad es del", str(probF) + "%")