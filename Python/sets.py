def set():
  #Un set es una colección de datos desordenada y que no tiene un índice.
  colors = {"red", "blue", "green"}
  print(type(colors))

  #Se puede comprobar si un elemento está dentro de un set:
  print("blue" in colors)

  #Método para agregar un elemento a un set:
  colors.add("violet")
  print(colors) #No se ha agregado al final, ya que no tiene un índice.and

  #Método para eliminar un elemento de un set:
  colors.remove("red")
  print(colors)

  #Método para eliminar todos los elementos de un set:
  colors.clear()
  print(colors) #Devuelve un set(). Estos es, un elemento con ningún elemento.

  #Para eliminar el set (o una tupla):
  del colors
  print(colors)

  #¿Cuándo se debe utilizar set? cuando se tiene un conjunto de datos que no hace falta definirlo.