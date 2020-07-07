	• Razonamiento 
		○ Representación binaria de un número positivo (ejemplo con el número decimal 24):
			• Para la representación binaria de un número decimal se calculan los restos de la división de dicho número decimal (y sucesivos resultados) entre dos. 
			• Una vez hecha la primera división, se divide el resultado de la primera división entre dos. Se continua con el mismo procedimiento, anotando los restos de cada división. 
			• Por último, se añade el resultado de la última división (3/2=1).
			• La representación binaria consiste en unir este último resultado con todos los restos obtenidos.
			
			24	2	 	 	 
			0	12	2	 	 
			 	0	6	2	 
			 	 	0	3	2
			 	 	 	1	1
			
			Así, la representación binaria del número 24 es 11000
		
		○ Representación binaria de un número negativo (para la representación de los números negativos se han utilizado 16 bits):
			i. Módulo y Signo: primero se representa en binario el valor absoluto del número negativo. Después, se añaden ceros por la izquierda hasta completar los bits requeridos. Se reserva el primer bit para el signo, poniendo en este caso un uno para representar que el número es negativo. 
			ii. Complemento a Uno: de la misma forma, primero se obtiene la representación binaria del valor absoluto del número negativo. Después, se añaden ceros por la izquierda hasta completar los bits requeridos. A continuación, se cambian los ceros obtenidos por unos y los unos obtenidos por ceros. A esto se le conoce como complementar el número.
			iii. Complemento a Dos: análogo a la representación en Complemento a Uno, sumándole un uno al mismo.
			iv. Exceso: primero se obtiene el siguiente valor: 2^(m-1), siendo m el número de bits que se esté utilizando. Después, se suma dicho valor al número decimal del cual se quiere obtener la representación binaria. A continuación, se convierte dicho valor a binario (es positivo, por lo tanto se sigue el razonamiento expuesto anteriormente).
			
	• Ejecución del programa para el evaluador
	Se debe llamar a la función binario, introduciendo como parámetro el número decimal del cual se desea obtener a representación binaria. Ejemplos:
		○ binario(24)
		○ binario(0)
		○ binario(-24)
	
	• Pasos significativos seguidos en el programa:
		○ Definición de una función que devuelva el número binario de un número decimal positivo (parámetro de entrada). Se opta por crear una función ya que es un paso necesario también para la representación binaria de un número decimal negativo, evitando así suplicar innecesariamente el código.
			i. Definición de una lista donde se guardan los restos (l_resto).
			ii. Una vez guardados los restos en una lista, se recorre la lista de manera inversa y se le da la vuelta.
			iii. Se guarda el resultado el otra lista (l_result)
		○ Módulo y Signo: se completa la lista resultado (l_result) con un uno y los ceros correspondientes, hasta completar los 16 bits.
		○ Complemento a Uno: se define una función, ya que también se utiliza en la representación a Dos.
			i. Representación binaria del número en valor absoluto, utilizando la función definida para los números decimales positivos.
			ii. Se completa la lista resultado (l_result) con ceros hasta los 16 bits.
			iii. Se recorre cada elemento de la lista y se convierten los ceros en unos y los unos en ceros.
		○ Complemento a Dos: se utiliza la función definida para Complemento a Uno.
		○ Exceso: se calcula primero el valor 2^(16-1)=32768. Después, se suma dicho valor al número negativo del cual se quiere obtener la representación binaria. A continuación, se pasa dicha suma como parámetro de entrada a la función definida para los números positivos.
