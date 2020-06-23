def frac_irre():
  
  num = float(input("Intoduce un número entre 0,0001 y 0,9999: "))
  while num<0.0001 or num>0.9999: #Continua preguntando hasta que se introduce número dentro del rango.
    num =float(input("Intoduce un número entre 0,0001 y 0,9999: "))
  
  num=int(num*10000)
  print(num)

  def f_divi(n):
    divi   = [] #Se declara lista vacía.
    for i in range(2,n+1):
      j=1
      while n%i==0 and j<=i:
        n=n/i #El siguiente número a considerar debe ser división entre n y el divisor i. Se declara j para que vaya un paso por detrás de i. 
        j=j+1
        divi.append(i)
    return(divi)
  
  print(f_divi(num))
  numerador   = f_divi(num) #Lista de divisiores del numerador.
  print(f_divi(10000))
  denominador = f_divi(10000) #Lista de divisores de 10000.

  for d in numerador: #Loop para eliminar divisores comunes.
    if d in denominador:
      numerador.remove(d)
      denominador.remove(d)
      numerador.insert(0,1) #Se sustituyen los divisores comunes por 1.
      denominador.insert(0,1)
  

  from fraction import Fraction #Librería para representar fraccciones
  import numpy #Libería que ofrece método numpy.prod para multiplicar elementos de una lista.
  print(Fraction(numpy.prod(numerador),numpy.prod(denominador)))
 

  

