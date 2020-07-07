def binario(num):
  
  def calculo(num):
    l_resto = []
    l_binario = []
    while int(num)/2 >= 1: #Se continua con la operación hasta que la división sea 1.
      resto = int(num)%2   #Se calcula el resto con la división entre dos. Se guarda el valor en una lista.
      num = int(num)/2     #La operación continua con la división.
      l_resto.append(resto)
    l_resto.append(1)     #Se añade el uno a los restos.
  
    for i in reversed(l_resto): #Se recorre la lista de manera inversa y se guardan los valores en la lista resultado.
      l_binario.append(i)
    return(l_binario)   #Se muestra por pantalla todo seguido, y no como una lista.

  if num >0:
    l_result = calculo(num)
    print("La representación binaria del número positivo ", num, " es ", *l_result, sep="")
  
  elif num ==0:
    print("La representación binaria del número ", num, " es ", 0)

  else:
    #1.Representación binaria de un número negativo utilizando Módulo y Signo, en 16 bits: 
    #Se hace la representación del número positivo. Se añade un uno como primer dígito para mostrar que es negativo, esto es, se reserva un bit para el uno. 
    l_result = calculo(abs(num))
    l_result = [1]+[0]*(15-len(l_result))+l_result
    print("La representación binaria del número negativo ", num, " en Módulo y Signo, 16 bits, es ", *l_result, sep="")

    #2. Representación binaria de un número negativo utilizando Complemento a Uno.
    #Se convierte a binario el número el valor absoluto. Después, se invierten los 1 por 0 y viceversa.
    def compl_uno(num):
      l_result = calculo(abs(num)) #representación binaria del número en valor absoluto.
      l_result =[0]*(16-len(l_result))+l_result #Se añaden los ceros en la izquierda hasta completa 16 bits
      for i in range(0,len(l_result)): #Se recorre cada elemento de la lista y se convierten los ceros en unos y los unos en ceros.
        if l_result[i]==0:
          l_result[i]=int(1)
        else:
          l_result[i]=int(0)
      
      return(l_result)
      
    l_result = compl_uno(num)
    print("La representación binaria del número negativo ", num, " en Complemento a Uno, 16 bits, es ", *l_result, sep="")

    #3. Representación binaria de un número negativo en Complemento a Dos.
    #Se obtiene la representación binaria del número en Complemento a Uno y se le suma uno.
    l_result[15:16] = [1]
    print("La representación binaria del número negativo ", num, " en Complemento a Dos, 16 bits, es ", *l_result, sep="")
  
    #4. Representación binaria de un número negativo en Exceso:
    #En 16 bits, tendríamos 2^(m-1) = 2^17 = 131072. A este valor, se le resta el número negativo que se desea representar en binario.
    #El sistema en Exceso consiste en convertir dicho valor a binario
    exc = 2**(16-1)
    exc = num + exc
    l_result = calculo(abs(exc))
    print("La representación binaria del número negativo ", num, " en Exceso, 16 bits, es ", *l_result, sep="")


