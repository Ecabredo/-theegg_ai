def comb():
  from itertools import chain, combinations

  n_vacas = int(input("Número de vacas en venta: "))
  n=1
  l_data = []
  while n<=n_vacas:
    d_data = {}  #Diccionario vacío. Hay que meterlo dentro del while para que se vacíe cada vez.
    peso = float(input("Peso de la vaca nº " + str(n)+": "))
    prod = float(input("Producción de la vaca nº " + str(n)+": "))
    d_data["nº de vaca"] = n #Se completa el diccionario con los valores introducidos por usuario.
    d_data["peso"] = peso
    d_data["prod"] = prod
    l_data.append(d_data) #Se crea una lista de disccionarios.
    n=n+1
  print(l_data)
  c_peso = input("Peso máximo de camión: ")

  peso = [d["peso"] for d in l_data] #Lista con uno de los elementos del diccionario.
  prod = [d["prod"] for d in l_data]
  print(peso)
  print(prod)

  max_prod=0
  for i in range(len(peso)+1):
    for d in range(len(list(combinations(peso,i)))): #Todas las combinaciones posibles de los elementos de una lista
      # print(list(combinations(peso,i))[d]) vuelve a hacer un loop para que devuelva cada elemento de la lista indiv.
      if sum(list(combinations(peso,i))[d]) >= int(c_peso): #La función sum() suma los elementos de de una lista. 
        continue 
      #sum(list(combinations(peso,i))[d])) Suma de pesos que quedan por debajo del límite del camión.
      #print(sum(list(combinations(prod,i))[d])) #Suma de producciones correspondientes a las vacas cuyas combinaciones no superan el límite del camión.
      if sum(list(combinations(prod,i))[d]) > max_prod: #Se busca la máxima producción posible
        max_prod = sum(list(combinations(prod,i))[d])
  print(max_prod)
      
  


    
  
