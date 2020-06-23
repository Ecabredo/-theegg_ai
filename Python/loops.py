def loop():
  #Se quiere definir una lista con varios elementos e imprimir por pantalla cada uno de los elementos.
  foods = ["apple", "bread", "cheese", "milk", "banana"]
  print(foods)

  #for food in foods: #con for se declara una variable que tomará como valor cada elemento de la lista, en cada iteración.
   # print(food)

  #Para salir de un loop:
  for i in foods:
    if i == "cheese":
      break #para la ejecución del bluque.
    print(i)

  #Para saltar a la próxima iteración:
  for a in foods:
    if a != "cheese":
      continue
    print(a) #solo imprime cheese

  #Recorrer un rango:
  for i in range(1,8):
    print(i)

  #Recorrer un string:
  for i in "Hello wordl":
    print(i)

  #Bucles mediante while:
  count = 4
  while count<=10: #aquí se debe meter un conticional.
    print(count)
    count = count+1


