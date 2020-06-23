def dict():
  #Permite definir datos a partir de claves y valores.
  product = {
    "name"    :"book",
    "cantidad": 3,
    "precio"  :4.99
  }
  person = {
    "first_name": "Michael",
    "last_name" : "Jordan"
  }

  print(type(person))
  print(dir(person))

  #Método para obtener solo las claves:
  print(person.keys())
  #Método para obtener cada par clave/valor dentro de una tupla, y todos dentro de una lista:
  print(person.items())

  #Para eliminar un diccionario.
  #del person
  #print(person)

  #Para limpiar los elementos del diccionario:
  person.clear()
  print(person) #se obtiene un diccionario vacío.

  #¿Y si se quiere meter más de un elemento en el diccionario? se crea una lista de deccionarios
  product =[
    {"name":"book"  , "price":10.99},
    {"name":"laptop", "price":299.98}
    ]
  print(product)
