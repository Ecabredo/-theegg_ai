
Se define primero la función f_suma, que suma todos los números de uno a n mediante un bucle, desde el primero hasta n.

    suma     = 0
    suma + 1 = suma
    suma + 2 = suma
    suma + 3 = suma
    ...
    suma + n = suma

Se defiene después la función f_pareja, que es válida para todos los n > 0, tanto pares como impares:

    suma = (n/2) * (n+1)

Resultados de ambas funciones para n = 1000000, 10000000, 10000000, 100000000. A continuación se detalla el tiempo requerido
para cada función:

    1. 1000000:
        f_suma (1000000): 500000500000 - 0.167555570602417
        f_parejas(10000000): 500000500000 - 0.0
    2. 10000000
        f_suma (10000000): 50000005000000 - 1.6697630882263184
        f_parejas(10000000): 50000005000000 - 0.0
    3. 100000000
        f_suma (100000000): 5000000050000000 - 14.986019134521484
        f_parejas(100000000): 5000000050000000 - 0.0
    4. 1000000000
        f_suma (1000000000): memory error
        f_parejas(1000000000): 500000000500000000 - 0.0

Conclusiones:
    f_suma: el tiempo requerido es (casi) directamente proporcional al incremento del tamaño de n. Crecimiento lineal. 
            La momeria es insuficiente para ejecutar la última iteración.
    f_parejas: a pesar del incremento de n, el tiempo requerido es inapreciable.
