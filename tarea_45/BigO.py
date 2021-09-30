import time
import random
from funciones_busqueda import f_nit_sec, f_nit_bin

l_data = [3,56,21,33,874,123,66,1000,23,45,65,56]

# Se añade un elemento aleatorio (entre 0 y 1000) en cada iteración. Se añaden en total 10 elementos más a la lista.
# for i in range(10):
#     n = random.randint(0,1000)
#     l_data.append(n)

#     # Comienza el primer crono:
#     t0 = time.time() 
#     num_it_sec = f_nit_sec(874, l_data)

#     t1 = time.time() 
#     # Comienza el segundo crono. La diferencia entre el primer y el segundo crono representa el tiempo requerido por la primera función.
#     num_it_bin = f_nit_bin(874, l_data)
#     # Comienza el tercer crono. La diferencia entre el segundo y el tercer crono representa el tiempo requerido por la segunda función.
#     t2 = time.time()

#     print("{} - {} - {}".format(l_data, num_it_sec, t1-t0))
#     print("{} - {} - {}".format(sorted(l_data), num_it_bin, t2-t1))


# Se busca crear listas suficientemente grandes como para apreciar que el tiempo necesario del algoritmo de 
# búsqueda binario cambia.
# Se crea una lista de 100 elementos aleatorio cuyo valor estça entre 0 y 1000.

e = 1
while e < 10:
    l_random = random.sample(range(0,10**e), 10**e)
    l_data.extend(l_random)
    t1 = time.time() 
    num_it_bin = f_nit_bin(874, l_data)
    t2 = time.time()
    print("{} - {} - {}".format(str(10**e), num_it_bin, t2-t1))
    e += 1