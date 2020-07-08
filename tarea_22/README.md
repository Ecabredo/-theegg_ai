	• Razonamiento:
		○ Primera hipótesis: 
			i. Ordenar las vacas de mayor a menor en función de la producción lechera.
			ii. Suma acumulada del peso de las vacas, siguiendo el orden establecido en el paso anterior.
			iii. Cuando la suma acumulada supere el límite establecido para el peso del camión, se determinarán las vacas seleccionadas.
		Se comprueba la esta primera hipótesis utilizando la herramienta Solver, en Excel, y se demuestra que la solución encontrada por el programa no coincide con la hallada mediante esta primera hipótesis. 
		Se concluye que es necesario realizar todas las combinaciones posibles de las vacas y analizar todas ellas de forma individual; puede haber vacas que pesen mucho y apenas produzcan o vacas con muy poco peso que produzcan mucho. 
		
		○ Solución al problema: 
			Analizar todas las posibles combinaciones. Por ejemplo si se tienen tres vacas cuyos pesos son 567Kg, 450Kg, y 550Kg, las combinaciones a analizar son:
				□ 567Kg
				□ 450Kg
				□ 550Kg
				□ 567+450=1017Kg
				□ 567+550=622Kg
				□ 450+550=1.000Kg
				□ 567+450+550=1.567Kg
			Limitación de capacidad de transporte: de todas las combinaciones generadas, se debe descartar aquellas que superan el límite de peso establecido para el camión.
			Por último, de las combinaciones que sí respeten la limitación de peso del camión, se sumarán las producciones de las vacas y se seleccionará el máximo.
			
			
	• Ejecución del programa para el evaluador
	Se debe llamar a la función comb, sin introducir ningún parámetro de entradaà comb()
	
	• Pasos significativos seguidos en el programa:
		1. Generación del set de datos:
			i. Se preguntará al usuario el número de vacas en venta.
			ii. Se consultará el peso y la capacidad de producción de leche de cada una de las vacas, generando con la respuesta una lista de diccionarios. Por ejemplo, siguiendo el ejemplo arriba expuesto:
			[{'nº de vaca': 1, 'peso': 567.0, 'prod': 34.0}, {'nº de vaca': 2, 'peso': 450.0, 'prod': 23.0}, {'nº de vaca': 3, 'peso': 450, 'prod': 22.0}]
			iii. Se consultará también el peso límite del camión.
			n_vacas = int(input("Número de vacas en venta: "))
			n=1
			l_data = []
			
			while n<=n_vacas:
				d_data = {} #Diccionario vacío. Hay que meterlo dentro del while para que se vacíe cada vez.
				peso = float(input("Peso de la vaca nº " + str(n)+": "))
				prod = float(input("Producción de la vaca nº " + str(n)+": "))
				d_data["nº de vaca"] = n #Se completa el diccionario con los valores introducidos por usuario.
				d_data["peso"] = peso
				d_data["prod"] = prod
				l_data.append(d_data) #Se crea una lista de disccionarios.
				n=n+1
			print(l_data)
				c_peso = input("Peso máximo de camión: ")
			
		2. Se crea una lista para los pesos y otra para las producciones:
		peso = [d["peso"] for d in l_data] #Lista con uno de los elementos del diccionario.
		prod = [d["prod"] for d in l_data]
		print(peso)
		print(prod)
		
		
		3. Se generan todas las posibles combinaciones entre los pesos de las vacas, de manera análoga al ejemplo analizado arriba, calculando la suma de los pesos. Se descartan aquello que superen el límite del camión. 
		if sum(list(combinations(peso,i))[d]) >= int(c_peso): 
			continue 
		
		4. Se busca la producción máxima correspondiente a la combinación de vacas cuya suma de pesos respete el límite de pedo del camión:
		if sum(list(combinations(prod,i))[d]) > max_prod: #Se busca la máxima producción posible
			max_prod = sum(list(combinations(prod,i))[d])
