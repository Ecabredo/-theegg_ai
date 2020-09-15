def esprimo(n):
  v_esprimo = True
  for d in range(2,n):
    if n%d==0:
      v_esprimo = False
      break
    else:
      continue
  return v_esprimo

N = int(input("Introduzca un número primo entre 1 y 1000000: "))
while N<=1 or N>=1000000:
  N = int(input("El número introducido no cumple el rango determinado. Introduzca un número primo entre 1 y 1000000: "))

#Con el enunciado había entendido que el número N introducido también tenía que ser primo. Viendo los ejemplos, se ve que no es así, ya que el número 456789 no es primo (es divisible por 3)
#v_esprimo = esprimo(N)
#while v_esprimo == False:
  #N = int(input("El número introducido no es primo. Introduzca un número primo entre 1 y 1000000: "))
  #v_esprimo=esprimo(N)

v_control = True
l_result=[]
while v_control == True:
  l_entrada=list(str(N))
  for l in reversed(l_entrada):
    l_result.append(l)
  int_entrada=int(''.join(l_entrada))
  int_result=int(''.join(l_result))

  if int_entrada-int_result == 0 and esprimo(N) == True:
    print("El número entero más pequeño palíndromo primo mayor que o igual a N es " + str(N))
    break
  else:
    l_result=[]
    N=N+1
 
    

  

  







