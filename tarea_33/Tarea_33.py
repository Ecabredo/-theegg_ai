def pokemon():

  vida_1 = int(input("Vida del Pokemos nº1: "))
  ataq_1 = int(input("Ataque del Pokemon nº1: "))
  vida_2 = int(input("Vida del Pokemos nº2: "))
  ataq_2 = int(input("Ataque del Pokemon nº2: "))

  turno = 1
  cont = 1
  while vida_1>0 and vida_2>0:
    if turno==1:
      vida_2 = vida_2-ataq_1
      print("Tras el ataque del turno "+str(cont)+" la vida del Pokemon Nº2 es "+str(vida_2))
      cont+=1
      turno=0
    else:
      vida_1 = vida_1-ataq_2
      print("Tras el ataque del turno "+str(cont)+" la vida del Pokemon Nº1 es "+str(vida_1))
      cont+=1
      turno=1
  if vida_1<=0:
    print("El ganador es el Pokemon nº2")
  else:
    print("El ganador es el Pokemon nº1")
