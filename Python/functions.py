def func():
  #Ya se han utilizado unas cuantas funciones:
  #print()
  #dir()
  #len()
  #type()

  #Para definir una función:
  def hello():
    print("Hello world")
  hello()#Llamada a la función

  #Función con parámetro:
  def hello_p(nombre):
    print("Hola "+nombre)
  hello_p("Ernes")#Llamada a la función

  #Colocar por defecto un parámetro a una función
  def hello_d(nombre="Adriana"):
    print("Hola " + nombre)
  hello_d("Ernes")#Se sobreescribe al definido en la función.
  hello_d()#Al no pasar parámetro, coge el definido en la función.

  #Crear función suma:
  def suma(n1,n2):
      return n1+n2
  print(suma(1,2))

  #Definir una función con lambda. Esto permite no tener que poner la expresión return.
  add = lambda n1, n2: n1+n2
  print(add(5,9))