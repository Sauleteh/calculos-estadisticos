import random
import math

arg0 = float(input("Porcentaje de que ocurra el suceso (no escribas '%'): ")) # Porcentaje de que ocurra el suceso
arg1 = int(input("Número de sucesos: ")) # Número de intentos
acertados = 0
for i in range(arg1):
    numRan = round(random.uniform(0.5,round((100/arg0)+0.49,5)))
    if (numRan == 1):
        acertados = acertados + 1

acertadosEsperados = arg1*(arg0/100)
probMinUno = 1-((1-(arg0/100))**arg1)
probMinUnoPorcentaje = probMinUno*100

if ((probMinUno > 0.1 and probMinUno < 0.9) or (((probMinUnoPorcentaje - math.floor(probMinUnoPorcentaje)) < 0.00001) and probMinUno >= 0.01)):
    probMinUno = round(probMinUno,5)
    probMinUnoPorcentaje = round(probMinUnoPorcentaje,5)

if (acertadosEsperados > 0.1):
    acertadosEsperados = round(acertadosEsperados,5)

print('\033[95m' + "- /Resultados/ -")
print("Probabilidad: " + str(round(arg0/100,5)) + " (" + str(round(arg0,5)) + "%), un acierto cada " + str(round(100/arg0,5)) + " intento/s)")
print("Número de intentos: " + str(arg1))
print()
print("Nº esperado de sucesos acertados: " + str(acertadosEsperados))
print("Prob. que el suceso ocurra mínimo una vez: " + str(probMinUno) + " (" + str(probMinUnoPorcentaje) + "%)")
print()
print('\033[94m' + "Nº de sucesos acertados en la simulación: " + str(acertados) + '\033[95m')
if (acertados > acertadosEsperados):
    print('\033[96m' + "Resultado en la simulación: suerte positiva")
elif (acertados == round(acertadosEsperados)):
    print('\033[96m' + "Resultado en la simulación: suerte neutra")
else:
    print('\033[96m' + "Resultado en la simulación: suerte negativa")
if (probMinUno*100 == 100 and arg0 != 100):
    print('\033[95m' + "ATENCIÓN: La probabilidad de que ocurra al menos una vez es tan cercana a 100% que se ha redondeado a ese porcentaje (Tiene al menos 14 nueves decimales).")
elif (probMinUno*100 == 0 and arg0 != 0):
    print('\033[95m' + "ATENCIÓN: La probabilidad de que ocurra al menos una vez es tan cercana a 0% que se ha redondeado a ese porcentaje (Tiene al menos 14 ceros decimales).")
print('\033[95m' + "- /Resultados/ -")