
# Función de compresión
from typing import ItemsView

def f_compr (data):
    
    l_recorrido     = []
    l_salida        = []
    l_data          = []
    l_ventana       = []
    l_offsset       = []
    l_length        = []
    l_next          = []

    cont = 0
    v_check = True

    # Se construye una lista con los strings que contienen las concatenaciondes de los caracteres: A, AB, ABR, ABRA...
    for i in data:
        l_data.append(i)     

    for i in l_data:
        cont += 1
        s_ventana = ''
        for s in range(cont, len(l_data)+1):
            s_ventana = s_ventana + l_data[s-1]
            d_recorrido = {}
            d_recorrido['pos_ini'] = cont
            d_recorrido['pos_fin'] = cont + len(s_ventana) 
            d_recorrido['ref']     = i
            d_recorrido['vent']    = s_ventana
            d_recorrido['l_vent']  = len(s_ventana)
            d_recorrido['reco']    = ''.join(l_data)[0:cont-1]
            l_ventana.append(d_recorrido)
    
    l_aux_ven = []
    for i in range(1, len(l_data)):
        d_salida = {}
        l_aux     = []
        l_aux_pos = []
        # Lista principal indexada por la posición recorrida
        l_aux = list(d for d in l_ventana if d['pos_ini']==i)
        # Lista indexada por los diccionarios donde la ventana queda contenida en el recorrido
        l_aux_pos = list(d for d in l_aux if d['vent'] in d['reco'])
        if l_aux_pos != []:
            l_aux_ven = l_aux_ven + l_aux_pos

    l_aux_ref = []
    ini_pos_aux = len(data)

    # Para cada referencia, se selecciona el que mayor ventana tenga, que será el último diccionario de la referencia analizada.
    for d in reversed(l_aux_ven):
        if d['pos_ini'] < ini_pos_aux:
            ini_pos_aux = d['pos_ini']
        else:
            continue
        l_aux_ref.append(dict(d))
   
    # Se vuelve a recorrer el orden inverso. La posición final debe ser mayor que la posición de inicio y fin del siguiente diccionario.
    l_aux_col  = []
    pos_aux = 0
    for d in reversed(l_aux_ref):
        if d['pos_ini'] > pos_aux and d['pos_fin'] > pos_aux:
            pos_aux = d['pos_fin']
        else:
            continue
        l_aux_col.append(dict(d))
        
    # Si la última posición queda fuera de rango, se corrige y se rellena la variable de referencia:
    try:
        if l_aux_col[len(l_aux_col)-1]['pos_fin'] > len(data):
            l_aux_col[len(l_aux_col)-1]['pos_fin'] = l_aux_col[len(l_aux_col)-1]['pos_fin'] - 1
            v_check = False
    except IndexError:
        print("La cadena introducida no puede comprimirse utilizando el algorítmo LZ77")
        return
        
    # Se obtiene una lista con todas las posiciones de inicio y la posición máxima final:
    l_aux_posiciones = []
    l_aux_posfin     = []
    v_aux_posmax     = 0
    # l_aux_postotal   = []
    for i in range(0, len(l_aux_col)):
        l_aux_posiciones.append(l_aux_col[i]['pos_ini'])
        l_aux_posfin.append(l_aux_col[i]['pos_fin'])
        # l_aux_postotal.append(l_aux_col[i]['pos_ini'])
        # l_aux_postotal.append(l_aux_col[i]['pos_fin'])
        if v_aux_posmax < l_aux_col[i]['pos_fin']:
            v_aux_posmax = l_aux_col[i]['pos_fin']
    # print(l_aux_posiciones)
    # print(l_aux_posfin)
    # print(v_aux_posmax)
    
    # Se debe comparar si la posición final del elemento coincide con la posición de inicio del siguiente. 
    # Si no coincide, se crea una lista con las posiciones intermedias, que serán las que habrá que crear.
    l_del     = []
    l_del_aux = []
    for i in range(0, len(l_aux_posiciones)-1):
        # print(l_aux_posfin[i])
        # print(l_aux_posiciones[i+1])
        if l_aux_posiciones[i+1] - l_aux_posfin[i] > 1:
            l_del_aux = list(range(l_aux_posfin[i]+1, l_aux_posiciones[i+1]))
            l_del.extend(l_del_aux)


    # l_del = []
    # l_del = list(x for x in range(0,len(data)) if x not in l_aux_postotal and x > l_aux_col[0]['pos_ini'])
    # print(l_del)

    # l_aux_col define los colores. No obstante, hasta llegar a la posición de inicio de los mismos, también se deben definir m, n y s.
    # Además, también hay que considerar la posibilidad de que al final también haya caracteres no repetidos.
    cont     = 0
    cont_fin = 0        
    for i in range(1, len(data)+1):
        d_salida = {}
        d_salida['i'] = i
        # Los primero caracteres no repetidos
        if l_aux_col[0]['pos_ini'] > i:
            d_salida['m'] = 0
            d_salida['n'] = 0
            d_salida['s'] = l_data[i-1]

        # Los últimos caracteres no repetidos o intermedios individuales
        elif i in l_del or i > v_aux_posmax:
            d_salida['m'] = 0
            d_salida['n'] = 0
            try:
                d_salida['s'] = data[i-1]
                cont_fin = 1 
            except IndexError:
                continue

        elif i in l_aux_posiciones:
            # Posición de la ventana en el recorrido, buscado en orden inverso.
            # print(i)
            # print(l_aux_posiciones.index(i))
            # print(l_aux_col[l_aux_posiciones.index(i)])
            # print(l_aux_col[l_aux_posiciones.index(i)]['vent'])
            # print(l_aux_col[l_aux_posiciones.index(i)]['reco'])
            # print(len(l_aux_col[l_aux_posiciones.index(i)]['reco'])-l_aux_col[l_aux_posiciones.index(i)]['reco'].rfind(l_aux_col[l_aux_posiciones.index(i)]['vent']))
            d_salida['m'] = len(l_aux_col[l_aux_posiciones.index(i)]['reco'])-l_aux_col[l_aux_posiciones.index(i)]['reco'].rfind(l_aux_col[l_aux_posiciones.index(i)]['vent'])
            d_salida['n'] = l_aux_col[l_aux_posiciones.index(i)]['l_vent']
            d_salida['s'] = data[l_aux_col[l_aux_posiciones.index(i)]['pos_fin']-1]  
            cont = cont + d_salida['n']
            cont_fin = 0 

        else:
            continue

        l_salida.append(d_salida)
    
    # Se ordena seceuncialmente:
    for i in range(0, len(l_salida)):
        l_salida[i]['i'] = i+1
    # print(l_salida)
    # print(v_check)
    return(l_salida, v_check)

# Función descompresión
def f_dcompr (l_salida, v_check):
    v_string = ''
    v_aux    = ''
    v_pos    = ''
    for i in range(0, len(l_salida)):
        if l_salida[i]['n'] == 0:
            v_string = v_string + l_salida[i]['s']
        else:
            v_pos    = l_salida[i]['m'] - l_salida[i]['n'] 
            v_aux    = v_string[-(l_salida[i]['m']):-(v_pos)]
            if v_aux == "":
                v_aux = l_salida[i-1]['s']
            if v_check == True:
                v_string = v_string + v_aux + l_salida[i]['s']
            else:
                if i < len(l_salida)-1:
                    v_string = v_string + v_aux + l_salida[i]['s']
                else:
                    v_string = v_string + v_aux 
    #print(v_string)
    return(v_string)

# Pruebas:
# test = 'ABRACADABRARRAY'
# test = 'HOLAEO'
# test = 'ernestomartinez'
# test = 'AKERRAKADARRAKOKERRAKDITU'
# f_dcompr(f_compr(test)[0],f_compr(test)[1])



# Funcion para solicitar al usuario que introduzca una cadena de caracteres cuya longitud no exceda 30 posiciones.
def f_input():
    n = 31
    while n > 30:
        v_string = str(input("Introduce una cadena con un máximo de 30 caracteres: "))
        n = len(v_string)
        if n > 30:
            print("La cadena contiene más de 30 caracteres: {} . Por favor, Introduce una cadena con un máximo de 30 caracteres: ".format(n))
        else:
            break

    #print(v_string.upper())
    return(v_string.upper())