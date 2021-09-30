#Se contabiliza en número de iteraciones mediante búsqueda secuencial. 
#Si el elemento se encuentra varias veces en la lista, se selecciona el primero.
def f_nit_sec(p_int, p_lista):
    n_int_sec = 1
    for i in p_lista:
        if i != p_int:
            n_int_sec = n_int_sec + 1
        else:
            break
    return(n_int_sec)

#Se contabiliza en número de iteraciones mediante búsqueda binaria.
def f_nit_bin(p_int, p_lista):
    n_int_bin = 1
    l_sort = []
    l_sort = sorted(p_lista)
    #print("La lista ordenada es: " + str(l_sort))
    #print(len(p_lista))
    #print(p_lista[int(len(p_lista)/2)])
    middle_index = int(len(l_sort)/2)
    l_newlist = l_sort
    while p_int != l_newlist[middle_index]:
        n_int_bin = n_int_bin + 1
        if p_int > l_newlist[middle_index]:
            l_newlist = l_newlist[middle_index:]
        else:
            l_newlist = l_newlist[:middle_index]
        
        middle_index = int(len(l_newlist)/2)
        #print(l_newlist)
            
    return(n_int_bin)