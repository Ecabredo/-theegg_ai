from funciones_busqueda import f_nit_sec, f_nit_bin


#Se crea un lista de elementos que se solicitarán al usuario.
l_data = []
while True:
    try:
        n = int(input("Introduce un elemento de la lista. Si quieres cerrar la lista, introduce cualquier carácter no numérico: "))
        l_data.append(n)
    except ValueError:
        if len(l_data) == 0:
            print("La lista de elemento está vacía, por lo que volvemos a empezar.")
            True
        else:
            print("La lista de elementos a analizar es:" + str(l_data))
            break

#Se solicita al usuario cuál es el elemento que se desea buscar en la lista
n = int(input("¿Cuál es el elemento que quieres buscar en: " + str(l_data) + "? "))
while True:
    try:
        if n not in l_data:
            True
            n = int(input("El elemento no se encuentra en la lista. Introduzca un elemento que se encuentre en el arreglo: "))
        else:
            break
    except:
        n = int(input("El elemento no es válido. Introduzca un elemento que se encuentre en la lista: "))
        True



#Se llama a las funciones de búsqueda:
print("El número de iteraciones con el algorítmo de búsqueda secuencial es: " + str(f_nit_sec(n, l_data)))
print("El número de iteraciones con el algorítmo de búsqueda binario es: " + str(f_nit_bin(n, l_data)))




