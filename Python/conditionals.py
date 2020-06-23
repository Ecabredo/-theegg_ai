def cond():
  #Un símbolo "=" para asignar.
  #Dos símbolos "==" para comparar.

  x = input("Introduzca un valor: ")
  y = input("Introduzca un segundo valor: ")
  z = input("Introduzca un tercer valor: ")
  if x>y:
    print(x + " es mayor que " + y)
  elif x==y:
    print(x + " es igual a " + y)
  else:
    print(x + " es menor que " + y)

  if z>x and z>y:
    print(z + " el tercer valor es el mayor de todos")
  if x>y or x>z:
    print(x + " no es el valor más pequeño")
  if(not(x==y)): #también se puede utilizar "!=""
    print(x + " y " + y + " son distintos")

