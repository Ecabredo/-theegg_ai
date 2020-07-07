	• Convertidor analógico-digital: dispositivo electrónico que convierte una entrada analógica de voltaje a un número digital. 
	La resolución de un conversor indica el número de valores discretos que este puede producir sobre un rango de valores de voltaje. Generalmente es expresado en bits.
	El conversor ADC (Analog-to-Digital Converter – Conversor Analógico Digital) tiene que efectuar los siguientes procesos:
		a. Muestreo de la señal analógica.
		b. Cuantización de la propia señal.
		c. Codificación del resultado de la cuantización, en código binario.

	• Frecuencia de muestreo: para convertir una señal analógica en digital, el primer paso consiste en realizar un muestreo (sampling) de ésta, o lo que es igual, tomar diferentes muestras de tensiones o voltajes en diferentes puntos de la onda senoidal. La frecuencia a la que se realiza el muestreo se denomina razón, tasa o también frecuencia de muestreo y se mide en kilohertz (kHz). En el caso de una grabación digital de audio, a mayor cantidad de muestras tomadas, mayor calidad y fidelidad tendrá la señal digital resultante.
    Para realizar el muestreo (sampling) de una señal eléctrica analógica y convertirla después en digital, el primer paso consiste en tomar valores discretos de tensión o voltaje a intervalos regulares en diferentes puntos de la onda senoidal
	  Por tanto, una señal cuyo muestreo se realice a 24 kHz, tendrá menos calidad y fidelidad que otra realizada a 48 kHz. Sin embargo, mientras mayor sea el número de muestras tomadas, mayor será también el ancho de banda necesario para transmitir una señal digital, requiriendo también un espacio mucho mayor para almacenarla.
	
	• Cuantización de la señal analógica: la cuantización representa el componente de muestreo de las variaciones de valores de tensiones o voltajes tomados en diferentes puntos de la onda sinusoidal, que permite medirlos y asignarles sus correspondientes valores en el sistema numérico decimal, antes de convertir esos valores en sistema numérico binario.
	
	• Codificación de la señal en código binario: después de realizada la cuantización, los valores de las tomas de voltajes se representan numéricamente por medio de códigos y estándares previamente establecidos. Lo más común es codificar la señal digital en código numérico binario.
	
	• Transistores bipolares: la unión de transistores forma un chip. Amplificadores, microprocesadores, tarjetas, placas, router, móvil…Todos ellos están formados por transistores. Se utilizan para dos funciones:
		○ Interruptor: on/off, abierto cerrado. Electrónica digital.
		○ Amplificador: amplifica la corriente o la tensión. Electrónica analógica. 
		
	Los transistores están formados por tres patillas:
		○ Emisor: recibe la corriente (corriente emisor = corriente colector).
		○ Colector: desde donde sale la corriente. (Va justo al revés de lo que pueda parecer).
		○ Base: la corriente que pasa por el transistor será más grande o más pequeña en función de la corriente que se enchufa por la base. La corriente que sale del colector y recoge el emisor será proporcional a la corriente que pasa por la base. Así, haciendo que la corriente enchufada de la base sea cero, se corta la corriente entre colector y emisor. Por lo tanto, un transistor se puede abrir o cerrar en función si en la base se pone corriente o no. 
			§ Si existe corriente por la base: interruptor cerrado.
			§ Si se corta corriente por la base: interruptor abierto.
		De la misma manera, variaciones en la corriente de la base se convierten en variaciones en la corriente que va desde el colector al emisor. 
		
	Los transistores tienen tres modos de trabajo:
		○ Corte: no hay circulación de corriente. La base, cuya corriente es la que se controla externamente, no enchufa corriente. Se trata como de un interruptor cerrado. Corriente de base. 
			  Intensidad base (corriente de base) = 0.
			  Tensión colector-emisor = tensión base. No existe pérdida de tensión, ya que V=I*R, siendo I = 0, la pérdida de tensión V = 0. 
			  Tensión base-emisor: está entre 0 y 0,6 voltios. Mientras esté en este rango, el transistor está en zona de corte.
		Por lo tanto, para conocer si un transistor está en zona de corte, se deberá verificar:
			  La alimentación del colector. Si no tiene alimentación, no hay corriente.
			  La tensión de base-emisor: si es menor de 0,6 voltios. 
		○ Zona activa o amplificación: 
			  Corriente proporcional. Ic = constante * Ib. Zona de amplificación. Grifo abierto. 
			  Tensión base-emisor: mayor que 0,6 voltios del diodo. 
		○ Saturación: por más que se incrementa la corriente desde la base, la corriente desde el colector al emisor no se incrementa. Ya no existe proporcionalidad y la corriente es máxima. 
	
