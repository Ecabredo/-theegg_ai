def num():
  #Números enteros = int
  #Números decimales = float
  print(type(9))
  print(type(9.1)) #Los decimales se representan con .

  #Operaciones:
  print(2**3) #dos al cuboo 
  print(3//2) #para obtener la parte entera de una división
  print(6%2)
  print(6%4) #para obtener el residuo

  #Pedir por pantala y guardarlo en una variable:
  age = input("Insert your age: ")
  print(age)
  #¡Cuidado! Todo lo que se inserta por pantalla es un string, por ello, lo siguiente falla:
  #print(age+5) #no se puede sumar un texto con un número.
  print(type(age))
  age = int(age)+5
  print(age)


