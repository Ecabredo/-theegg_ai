def greet():

  #Para saber todo lo que se puede hacer con la variable
  #se utiliza dir(). Devuelve una lista de métodos.
  my_str = "Hello World"
  print(dir(my_str))

  #Por ejemplo, se puede utilizar el método upper/lower para para poner el string en mayúscula/minúscula.all
  print(my_str.upper())
  print(my_str.lower())

  #Método para reemplazar texto:
  print(my_str.replace("Hello", "By"))

  #Se puede colocar un método dentro de otro:
  print(my_str.replace("Hello", "By").upper())

  #Método para contar cuántas veces se repite un carácter dentro de una cadena:
  print(my_str.count("l"))

  #Método para conocer si un string empieza/acaba con una determinada letra (booleano):
  print(my_str.startswith("By"))
  print(my_str.endswith("d"))

  #Método para separar el texto en una lista:
  print(my_str.split()) #Por defecto, lo separa basado en el espcio.
  #También se puede separar a partir de cualquier carácter:
  print(my_str.split("o"))

  #Método para buscar la posición de un carácter en una cadena: ¡Vemos que empieza en cero!
  print(my_str.find("H"))

  #Función para conocer el tamaño de una cadena:
  print(len(my_str))

  #Método para conocer el índice de un carácter dentro de una cadena: ¿cuál es la diferencia con find?
  print(my_str.index("l"))

  #Métodos para conocer si una variable es numérica/alfanumérica:
  print(my_str.isnumeric())
  print(my_str.isalpha())

  #Para imprimir alguna posición en particular:
  print(my_str[4])
  #Para imprimir en el orden inverso:
  print(my_str[-1])

  #Imprimir cadena unida a variable utilizando concatenación:
  print("Hola mundo "+ my_str)
  #Sin utilizar concatenación: se debe colocar antes una letra f. La f significa que se va a imprimir un texto con una variable.
  print(f"Hola mundo {my_str}") #Opción disponible a partir de 3.6
  #Otra manera de hacerlo:
  print("Hola mundo {0}".format(my_str))



