	• Razonamiento 
		a. Se genera el alfabeto inglés, posicionando cada letra en el número correspondiente. De esta forma; A=1, B=2…Se detallará el procedimiento seguido en pasos significativos seguidos en el programa. 
		b. Se deben generar dos barajas de cartas inglesas y barajarlas de la misma manera. Se detallará el procedimiento seguido en pasos significativos seguidos en el programa. 
		Cada carta tiene un valor, de acuerdo a la siguiente clasificación:
			- Trébol: +0
			- Diamante: +13
			- Corazón: +26
			- Pica: +39
			- Jokers: 53
		Las únicas cartas que tiene el mismo valor son los jokers.
	
		c. Se identificará cada joker para distinguirlos entre sí. En este caso se han nombrado como joker_a y joker_b.
		
		d. Generación de la carta resultado (se define la función f_keystream):
			1. Encontrar el joker_a y posicionarlo tras las siguiente carta.
			2. Encontrar el joker_b y posicionarlo dos cartas por detrás de su posición actual. 
			Para estos dos primeros pasos hay que tener en cuenta que la baraja se debe tratar de manera circular; esto es, si el joker_a es la última carta, se deberá posicionar como la segunda carta de la baraja, justo por detrás de la primera. Análogamente, si el joker_b es la última carta, se deberá colocar como la tercera carta de la baraja, justo por detrás de la segunda. 
			3. Triple corte: independientemente de que sea el joker_a o joker_b, se identifican todas las cartas que queden por encima del primer joker. De la misma forma, se identifican todas las cartas que queden por debajo del segundo joker. Se invierten las posiciones: las cartas por encima del primer joker pasan a estar debajo del segundo joker. Las cartas por debajo del segundo joker pasan a estar por encima del primero.
			4. Corte de cuenta: se identifica el valor de la última carta. Se cuenta el número de cartas igual al valor de la última carta, empezando por la primera. Se coloca ese número de cartas encima de la última carta. De esta manera, la última carta no cambia.
			5. Identificar la carta resultado: a partir del valor de la primera carta, se cuenta el número de cartas a partir de la primera. Se selecciona el valor de la siguiente carta. 
			
		e. Definición de la función de cifrado y descifrado, en las cuáles se utilizan como parámetros de entrada la baraja, el texto de entrada, los valores numéricos del texto obtenido del alfabeto, la suma entre dichos valores numéricos y las cartas resultado, y el resultado cifrado. Los últimos tres parámetros se introducen con el objetivo de que sean devueltos por la función.
		
			
	• Ejecución del programa para el evaluador
	Se debe llamar a la función solitario, sin utilizar ningún parámetro de entrada à solitario()
	
	• Pasos significativos seguidos en el programa:
		○ Definición de la baraja:
			- Lista de diccionarios con el valor equivalente de cada carta de la baraja:
			d_equi = [{"letra":"A", "equi":1}, {"letra":2, "equi":2},{"letra":3, "equi":3}, {"letra":4, "equi":4}, {"letra":5, "equi":5}, {"letra":6, "equi":6}, {"letra":7, "equi":7}, {"letra":8, "equi":8}, {"letra":9, "equi":9}, {"letra":10, "equi":10}, {"letra":"J", "equi":11}, {"letra":"Q", "equi":12}, {"letra":"K", "equi":13}]
			
			- Se define diccionario con las correspondencias numéricas de los palos de la baraja:
			d_palo = [{"palo":"trebol", "val":0}, {"palo":"diamante", "val":13}, {"palo":"corazon", "val":26},{"palo":"pica", "val":39}]
			
			- Se genera bajara con los palos, número o literales y sus valores correspondientes. Después se genera la baraja y se introduce un nuevo campo en cada diccionario (cada carta es un diccionario) con el valor adaptado:
			l_baraja = []
			l_palos = ["trebol", "diamante", "corazon", "pica"]
			l_num = ["A", 2, 3,4,5,6,7,8,9,10,"J", "Q", "K"]
			
			for p in range(0,len(l_palos)): 
				for num in range(0, len(l_num)):
					d_baraja = {}
					d_baraja["palo"] = l_palos[p]
					d_baraja["num"] = l_num[num]
					l_baraja.append(d_baraja)
			
			for b in l_baraja:
				b["valor"] = (list(d["val"] for d in d_palo if d["palo"] == b["palo"])[0])+(list(d["equi"] for d in d_equi if d["letra"]== b["num"])[0])
			
			- Se añaden ambos Jokers con su valor correspondiente:
			joker_a = {"palo": "joker_a", "num": 53, "valor":53}
			l_baraja.append(joker_a)
			joker_b = {"palo": "joker_b", "num": 53, "valor":53}
			l_baraja.append(joker_b)
			
			- Se barajan las cartas utilizando la función shuffle. La baraja utilizada para cifrar y descifrar deben ser barajadas de la misma forma.
			random.shuffle(l_baraja)
			l_baraja_cifrado = l_baraja
			l_baraja_descifrado = l_baraja_cifrado
			
		○ Definición de la función f_keystream, cuyo parámetro de entrada es la lista de diccionarios de cartas:
			- Encontrar el joker_a y posicionarlo tras las siguiente carta:
			cont_ja=0
			for j in range(0,len(p_baraja)):
				if p_baraja[j]["palo"] == "joker_a":
					if cont_ja == 53:
					cont_ja = 0 
					p_baraja = p_baraja[0:1]+p_baraja[53:54]+p_baraja[1:53]
					break
				else:
					p_baraja = p_baraja[0:cont_ja]+p_baraja[cont_ja+1:cont_ja+2]+p_baraja[cont_ja:cont_ja+1]+p_baraja[cont_ja+2:54] 
					break
			cont_ja=cont_ja+1
			
			- Encontrar el joker_b y posicionarlo dos cartas por debajo:
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
			
			- Triple Corte:
			cont_aux_a = 0
			cont_aux_b = 0
			cont_aux = 0
			for n in range(0,len(p_baraja)):
				if p_baraja[n]["palo"] == "joker_a":
					cont_aux_a=n
				if p_baraja[n]["palo"] == "joker_b":
					cont_aux_b=n
			#Se reordena:
			if cont_aux_a > cont_aux_b:
				cont_aux = cont_aux_a
				cont_aux_a = cont_aux_b
				cont_aux_b = cont_aux
			p_baraja = p_baraja[cont_aux_b+1:54]+p_baraja[cont_aux_a:cont_aux_b+1]+p_baraja[0:cont_aux_a]
			
			- Corte de cuenta:
			ult_carta = p_baraja[53]["valor"]
			p_baraja = p_baraja[ult_carta:53]+p_baraja[0:ult_carta]+p_baraja[53:54]
			
			- Identificar la carta resultado
			pri_carta = p_baraja[0]["valor"]
			return([p_baraja[pri_carta]["valor"],p_baraja]) #De esta manera, se devuelve el resultado en forma de lista
			
		- Definición de función de cifrado:
		def cifrar(p_baraja, text, l_text_num, p_ops, p_cipher):
		#Convertir el mensaje en valores numéricos: 
			l_keystream = []
			for l in range(0,len(text)):
				l_text_num.append(list(d["value"] for d in l_alphabet if d["car"] == text[l])[0]) #Se busca el valor numérico correspondiente para cada letra del mensaje, en el alfabeto.
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
