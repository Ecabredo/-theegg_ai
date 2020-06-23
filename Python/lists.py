def lis():
  #Las listas se crean mediante los corchetes:
  lis = [1, "hello", 1.35, True, [1,2,3]]
  print(lis)

  #También se puede crear una lista con las función list():
  #La función list espera solo un argumento. Por ello, hay que pasar los valores en una tupla, dentro de ().
  colors=list(("red", "blue", "black", "white"))
  print(colors)
  print(type(colors))

  #Se pueden crear listas basadas en rangos mediante la función range. Esta función toma dos parámetros: desde, hasta
  print(list(range(1,10)))
  #Llega hasta el 9! Esto es, hasta un número antes del segundo parámetro.

  #¿Qué metodos se pueden ejecutar a partir de una lista?
  print(dir(colors))

  #Función para conocer el númerod de elementos de una lista:
  print(len(colors))
  #Para que devuelva el elemento de una posición:
  print(colors[0])
  print(colors[-1])

  #Para conocer si un determinado elemento está en una lista:
  print("green"in colors)
  print("red" in colors)

  #Para cambiar los elementos de una lista:
  colors[2] = "Yellow"
  print(colors)

  #Método para agregar un elemento a una lista:
  colors.append("violet")
  print(colors)
  #Para agregar varios elementos hay que hacerlo mediante una tupla, ya que el método append solo admite un argumento.
  colors.append(("black", "green"))
  print(colors)
  #Así, se ha introducido un elemento más como una tupla. ¿Cómo se agregarían ambos elementos por separado? Se debe utilizar otro método llamado extend.
  colors.extend(("orange", "grey")) #se puede pasar ya sea en forma de tupla o en forma de lista
  print(colors)

  #Método para agregar un elemento en una posición dada:
  colors.insert(1,"pink") #También se podría dar el orden inverso.
  colors.insert(-1, "last colour") #esto lo coloca en la penúltima posición
  colors.insert(len(colors), "last colour")
  print(colors)

  #Método para eliminar el último elemento:
  colors.pop()
  print(colors)

  #Método para eliminar a partir de un índice:
  colors.pop(1)
  print(colors)

  #Método para eliminar un valor en concreto:
  colors.remove("last colour")
  print(colors)

  #Método para quitar todos los elementos:
  #colors.clear()
  #print(colors)

  #Métedo para ordenar los elementos alfabéticamente:
  #colors.sort()
  #print(colors) #Da un error porque no puede ordenar tuplas y strings a la vez. Por lo tanto, elimino la tupla de dentro de la lista.

  colors.pop(5)
  colors.sort()
  print(colors) #¡Primero ordena las mayúsculas!
  #Para ordenador de manera inversa:
  colors.sort(reverse=True)
  print(colors)

  #Método para conocer el índice de un elemento:
  print(colors.index("violet"))

  #Método para conocer cuántas veces existe un elemento:
  print(colors.count("violet"))






