# Cálculos estadísticos
Varios programas útiles para hacer cálculos diversos relativos a la probabilidad de sucesos. En todos los programas me refiero a "tirar" como ejecutar la acción de probar suerte al suceso con un porcentaje dado.

## resumenEstadistica.py

![image](https://github.com/Sauleteh/calculos-estadisticos/assets/22859905/5dae6aec-68af-4cb0-a954-c95635193f2a)

Define el porcentaje de que ocurra el suceso y el número de intentos (o tiradas, llámalo como mejor lo entiendas) y el programa hará varios cálculos estadísticos para mostrar un resumen de lo pedido (las dos primeras líneas), el número de veces que se espera que ocurra el suceso y la probabilidad de que, habiendo hecho todas las tiradas, ocurra al menos una vez de forma asegurada (estadísticamente hablando) el suceso (las siguientes dos líneas).

El programa también cuenta con un simulador. Las dos últimas líneas explican cómo ha ido la simulación que se ha hecho, pudiendo observar cuántas veces se acertó el suceso y la suerte que tuviste en la ejecución de ese programa. En la imagen se puede observar que la suerte que tuve a la hora de ejecutar el programa cuando le saqué captura fue negativa pues se acertó una vez cuando estadísticamente hablando debería haber acertado al menos 3 veces, pero la estadística es la teoría de lo que podría ocurrir, cada vez que ejecutas el programa puede salirte diferentes tipos de suerte.

## numTiradasParaUnaVez.py

![image](https://github.com/Sauleteh/calculos-estadisticos/assets/22859905/cfb2e9f8-2179-4335-bb0a-2e4e8970d008)

Introduce el porcentaje de que ocurra un suceso y el porcentaje que quieres que ocurra ese suceso asegurado y te dirá el número de veces que tendrás que tirar para que ocurra el suceso asegurado al porcentaje que indicaste como segundo argumento. Si quieres saber las tiradas necesarias para asegurarte que sí o sí te tocará el suceso, no escribas 100 como porcentaje en el segundo parámetro sino 99 y un número determinado de decimales (Ej: 99.9999), esto es debido a que nunca será posible asegurar al 100% un suceso que no ocurre el 100% de las veces, es un tema estadístico y no un problema del programa.

## porcXdeCadaY.py

![image](https://github.com/Sauleteh/calculos-estadisticos/assets/22859905/4483d2da-0f34-4057-8ecb-5679339ac889)

Muy simple: Defines un valor para la X y otro para la Y y te muestra el porcentaje. Es bastante autoexplicativo además de ser un cálculo simple.
