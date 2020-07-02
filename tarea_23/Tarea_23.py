def solitario():
  from string import ascii_uppercase #Método para importar el alfabeto.
  import random #Método para ordenar aleatoriamente los elementos de una lista o tupla.

   #Orden secuencial de las cartas de póker: A,2,3,4,5,6,7,8,9,10,J,Q,K = 1,2,3,4,5,6,7,8,9,10,11,12,13
  #Se define diccionario de equivalencia de las letras de la baraja.
  #Función para generar alfabeto con su valor numérico:
  
  d_equi = [{"letra":"A", "equi":1}, {"letra":2, "equi":2},{"letra":3, "equi":3}, {"letra":4, "equi":4}, {"letra":5, "equi":5}, {"letra":6, "equi":6}, {"letra":7, "equi":7}, {"letra":8, "equi":8}, {"letra":9, "equi":9}, {"letra":10, "equi":10}, {"letra":"J", "equi":11}, {"letra":"Q", "equi":12}, {"letra":"K", "equi":13}]

  #Se define diccionario con las correspondencias numéricas de los palos de la baraja:
  d_palo = [{"palo":"trebol", "val":0}, {"palo":"diamante", "val":13}, {"palo":"corazon", "val":26},{"palo":"pica", "val":39}]
      
  #Se genera alfabético inglés con las letras y sus valores(=posiciones) correspondientes:
  l_alphabet=[]
  for i in range(1,27):
    d_alphabet = {}
    d_alphabet["car"] = ascii_uppercase[i-1]
    d_alphabet["value"] = i
    l_alphabet.append(d_alphabet)
    
    
  # Se genera baraja con los palos, números o literales y sus valores correspondientes.
  l_baraja = []
  l_palos  = ["trebol", "diamante", "corazon", "pica"]
  l_num    = ["A", 2, 3,4,5,6,7,8,9,10,"J", "Q", "K"]
    
  #Se genera la baraja:
  for p in range(0,len(l_palos)):  
    for num in range(0, len(l_num)):
      d_baraja = {}
      d_baraja["palo"] = l_palos[p]
      d_baraja["num"]  = l_num[num]
      l_baraja.append(d_baraja)
    
  #Se introduce un nuevo campo en el diccionario de la baraja con el valor adaptado:
  for b in l_baraja:
    b["valor"] = (list(d["val"] for d in d_palo if d["palo"] == b["palo"])[0])+(list(d["equi"] for d in d_equi if d["letra"]== b["num"])[0])
    
  #Se añaden ambos Joker:
  joker_a = {"palo": "joker_a", "num": 53, "valor":53}
  l_baraja.append(joker_a)
  joker_b = {"palo": "joker_b", "num": 53, "valor":53}
  l_baraja.append(joker_b)

  #Se barajan las cartas, esto es, se da un orden aleatorio.
  
  random.shuffle(l_baraja)
  l_baraja_cifrado = l_baraja
  l_baraja_descifrado = l_baraja_cifrado
 

  #Se define función para intercambiar la posición de los elementos de una lista:
  #def swapPositions(list, pos1, pos2): 
      
    #list[pos1], list[pos2] = list[pos2], list[pos1] 
    #return list
  
  #Keystream algorithm:
  def f_keystream(p_baraja):
    #1.Encontrar el joker_a y posicionarlo debajo de la siguiente carta:
    #p_baraja[0:1] es una lista con el diccionario p_baraja[0]
    #p_baraja[0] es un diccionario.
    #Para sumarlos, hay que ponerlos o como lista o como diccionario. En el ejercicio se suman como diccionarios.
    cont_ja=0
    for j in range(0,len(p_baraja)):
      if p_baraja[j]["palo"] == "joker_a":
        if cont_ja == 53:
          cont_ja = 0 
          p_baraja = p_baraja[53:54]+p_baraja[0:53]
          break
        else:
          #swapPositions(p_baraja,cont_ja, cont_ja+1)
          p_baraja = p_baraja[0:cont_ja]+p_baraja[cont_ja+1:cont_ja+2]+p_baraja[cont_ja:cont_ja+1]+p_baraja[cont_ja+2:54] 
          break
      cont_ja=cont_ja+1
    
  
     
    #2.Encontrar el joker_b y posicionarlo dos cartas por debajo:
    cont_jb=0
    for j in range(0,len(p_baraja)):
      if p_baraja[j]["palo"] == "joker_b":
        if cont_jb == 51:
          p_baraja = p_baraja[51:52]+p_baraja[0:51]+p_baraja[52:54]
          break
        elif cont_jb == 52:
          p_baraja = p_baraja[0:1]+p_baraja[52:53]+p_baraja[1:52]+p_baraja[53:54]
          break
        elif cont_jb == 53:
          p_baraja = p_baraja[0:2]+p_baraja[52:53]+p_baraja[2:53]
          break
        else:
          p_baraja = p_baraja[0:cont_jb]+p_baraja[cont_jb+1:cont_jb+3]+p_baraja[cont_jb:cont_jb+1]+p_baraja[cont_jb+3:54] 
          break
      cont_jb=cont_jb+1
    
    

    #3.Realizar un triple corte. Se ignora el hecho de cuál sea el primero de los jokers. Se identifican todas las cartas encima del primer joker. De la misma forma, se identifican todas las cartas debajo del segundo joker. Se invierten las posiciones: las cartas por encima del primer joker pasan a estar debajo del segundo joker. Las cartas por debajo sel segundo joker pasan a estar por encima del primero.
    cont_aux_a = 0
    cont_aux_b = 0
    cont_aux   = 0
    
    for n in range(0,len(p_baraja)):
      if p_baraja[n]["palo"] == "joker_a":
        cont_aux_a=n
      if p_baraja[n]["palo"] == "joker_b":
        cont_aux_b=n
    #Se reordena:
    if cont_aux_a > cont_aux_b:
      cont_aux   = cont_aux_a
      cont_aux_a = cont_aux_b
      cont_aux_b = cont_aux
          
    p_baraja = p_baraja[cont_aux_b+1:54]+p_baraja[cont_aux_a:cont_aux_b+1]+p_baraja[0:cont_aux_a]
    
    
    #4. Realizar un corte de cuenta. Se identifica el valor de la última carta. Se cuenta el número de cartas igual al valor de la última carta, empezando por la primera. Se coloca ese número de cartas encima de la última carta. De esta manera, la última carta no cambia.
   
    ult_carta = p_baraja[53]["valor"]
    p_baraja = p_baraja[ult_carta:53]+p_baraja[0:ult_carta]+p_baraja[53:54]
    
  
    #5. Identificar el resultado. Utilizando el valor de la primera carta. Contar dicho número de cartas a partir de la primera y coger el valor de la siguiente carta.
    pri_carta = p_baraja[0]["valor"]
    return([p_baraja[pri_carta]["valor"],p_baraja]) #De esta manera, se devuelve el resultado en forma de lista
    
    
    
  #print(l_baraja)
  #print(f_keystream(l_baraja)[1])
  #print(type(f_keystream(l_baraja)[1]))
  

  f_keystream(l_baraja_cifrado)
  f_keystream(l_baraja_descifrado)

  def cifrar(p_baraja, text, l_text_num, p_ops, p_cipher):
    #Convertir el mensaje en valores numéricos: 
    l_keystream   = []
    
    for l in range(0,len(text)):
      l_text_num.append(list(d["value"] for d in l_alphabet if d["car"] == text[l])[0]) #Se busca el valor numérico correspondiente para cada letra del mensaje.
      l_keystream.append(f_keystream(p_baraja)[0])
      p_baraja = f_keystream(p_baraja)[1]
          
    #Se suman los valores de ambas listas: valor numérico del mensaje y su cifrado. Si la suma es mayor que 52, se restan 52. Si la suma es mayor que 26, se restan 26:
    for s in range(0,len(l_text_num)):
      p_ops.append(l_text_num[s]+l_keystream[s])
      if p_ops[s] > 52:
        p_ops[s] = p_ops[s]-52
      elif p_ops[s] > 26:
        p_ops[s] = p_ops[s]-26
    
    #Se reconvierte a letras:
    for c in range(0,len(p_ops)):
      p_cipher.append(list(d["car"] for d in l_alphabet if d["value"] == p_ops[c])[0]) #Se busca el mensaje cifrado
    
    return(l_text_num)
    return(p_ops)
    return(p_cipher)
  
  #Descifrar el mensaje cifrado. 
  #1. Se necesita tener el valor numérico el mensaje cifrado, que ya está guardado en la variable l_ops.
  #2. Se barajan las cartas, esto es, se da un orden aleatorio. 
  #3. Se aplica la función de cifrado para cada valor de l_ops:
  
  def descifrar(p_baraja,text_inv, l_text_num_inv, p_ops_inv, p_cipher_inv):
    l_keystream_inv   = []
    for l in range(0,len(text_inv)):
      l_text_num_inv.append(list(d["value"] for d in l_alphabet if d["car"] == text_inv[l])[0]) #Se busca el valor numérico correspondiente para cada letra del mensaje.
      l_keystream_inv.append(f_keystream(p_baraja)[0])
      p_baraja = f_keystream(p_baraja)[1]
    
  #Se suman los valores de ambas listas: valor numérico del mensaje y su cifrado. Si la suma es mayor que 52, se restan 52. Si la suma es mayor que 26, se restan 26:
    for s in range(0,len(l_text_num_inv)):
      p_ops_inv.append(l_text_num_inv[s]-l_keystream_inv[s])
      if p_ops_inv[s] < -26:
        p_ops_inv[s] = p_ops_inv[s]+52
      elif p_ops_inv[s] < 0:
        p_ops_inv[s] = p_ops_inv[s]+26
      
    
    #Se reconvierte a letras:
    for c in range(0,len(p_ops_inv)):
      p_cipher_inv.append(list(d["car"] for d in l_alphabet if d["value"] == p_ops_inv[c])[0]) 
      
      
    return(l_text_num_inv)
    return(p_ops_inv)
    return(p_cipher_inv)
  
  #Llamada a la función de cifrado:
  mensaje=input("Introduzca el mensaje a encriptar: ")
  mensaje=mensaje.replace(" ","")
  mensaje=mensaje.upper()
  
  l_mensaje_num = []
  l_mensaje_num_inv = []
  l_ops = []
  l_ops_inv = []
  l_cipher = []
  l_cipher_inv = []
  

  cifrar(l_baraja_cifrado, mensaje, l_mensaje_num, l_ops, l_cipher)
  print("El mensaje a cifrar es: ", mensaje)
  print("Los valores numéricos del mensaje a cifrar: ", l_mensaje_num)
  print("Los valores numéricos del mensaje cifrado: ", l_ops)
  print("El mensaje cifrado es: ", l_cipher)  

  descifrar(l_baraja_descifrado, l_cipher, l_mensaje_num_inv, l_ops_inv, l_cipher_inv)
  print("El mensaje a descifrar es: ", l_cipher)
  print("Los valores numéricos del mensaje a descifrar: ", l_mensaje_num_inv)
  print("Los valores numéricos del mensaje descifrado: ", l_ops_inv)
  print("El mensaje descifrado es: ", l_cipher_inv)
  
 

  
  

  
  
  

  
  
  


  
  
  
    
  


   


 
    






   

 



  
  




