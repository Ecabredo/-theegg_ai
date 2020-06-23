def tup():
  #Permiten definir listas de elementos que no se pueden modificar, inmutables. Se utiliza para mantener seguro el código o para ejecutarlo más rápido.

  #Para definir una tupla se utilizan los parentesis:
  x = (1,2,3)
  print(x)

  #Análogamente a las listas, también se pueden crear las tuplas a partir de una función. Hay que tener en cuenta que esta función también espera un solo argmento, por lo que se tendrá que pasar en forma de tupla:
  y = tuple((1,2,3))
  print(y)

  #De la misma forma que los otros tipos de datos, si se quiere conocer todos los métodos y funciones que se puede hacer con tuplas:
  print(dir(x)) #comparando con una lista, hay menos métodos y funciones disponibles, ya que una tupla no se puede modificar.

  #Para definir una tupla de un solo elemento:
  z = (1,)
  print(type(z))
  #Ya que sin la "," se hubiera interpretado como un entero:
  z = (1)
  print(type(z))

  #Igual que en las listas, se puede acceder a los elementos de una tupla utilizando []
  print(x[1])

  #Al tratar de cambiar el valor de una tupla:
  #x[1] = 10 #Da error.

  #Entonces, ¿cuándo se utilizan tuplas? Al crear, por ejemplo, un diccionario de localizaciones, ya que se sabe que son valores inmutables.
  locations ={
    (35.1234, 39.3212):"Tokio",
    (23.4543, 28.8776): "LA"
  }
  print(locations)