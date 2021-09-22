 # Los algoritmos a comparar deben hallar la suma de los primeros n números.
 # f_suma: se recorren todos los elemento desde 1 hasta n, sumando todos los miembros. Así, serán necesarias n operaciones.
 # f_parejas = (n/2) * (n+1). Esto es; con n/2 se obtiene el número de parejas. Por otro lado, n+1 indica el número de veces que se debe 
 # realizar la operación.
 # Llamada a las funciones: mediante un bucle, se llamará a las funciones 4 veces. En cada iteración se multiplicará el tamaño de n por 10.
 # El objetivo es hallar el tiempo que tarda cada función en devolver el resultado en cada una de las iteraciones.

import time

# Se define la función f_suma:
def f_suma(n):
    l_list = list(range(1,n+1))
    suma = 0
    for i in l_list:
        suma += i
    
    return(suma)

# Se defiene la función f_parejas:
def f_parejas(n): 
    suma = int((n/2) * (n+1))
    return(suma)

# Nota importante: el equipo no puede con la última iteración ("MemoryError")
num = 1000000
for i in range (4):

    try:
        # Comienza el primer crono:
        t0 = time.time() 
        sum_1 = f_suma(num)
        t1 = time.time() 
        # Comienza el segundo crono. La diferencia entre el primer y el segundo crono representa el tiempo requerido por la primera función.
        sum_2 = f_parejas(num)
        # Comienza el tercer crono. La diferencia entre el segundo y el tercer crono representa el tiempo requerido por la segunda función.
        t2 = time.time()

        print("{} - {}".format(sum_1, t1-t0))
        print("{} - {}".format(sum_2, t2-t1))

        num *= 10

    # Teniendo en cuenta los resultados, se puede asumir que la función que da MemoryError siempre será  f_suma.
    except MemoryError:
        t1 = time.time() 
        sum_2 = f_parejas(num)
        t2 = time.time()
        print("{} - {}".format(sum_2, t2-t1))


