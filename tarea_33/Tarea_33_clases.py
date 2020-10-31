class Pokemon:
    def __init__(self, vida, ataque):
        self.vida   = vida
        self.ataque = ataque

"""         self.vida   = int(input("Vida del Pokemon  ")) Otra alternativa sería definir la clase Pokemon sin argumento e introducirlos desde la consola.
        self.ataque = int(input("Ataque del Pokemon "+))      
 """
Pok_1 = Pokemon(int(input("Vida del Pokemon nº1: ")),int(input("Ataque del Pokemon nº1: ")))
Pok_2 = Pokemon(int(input("Vida del Pokemon nº2: ")),int(input("Ataque del Pokemon nº2: ")))

turno = 1
cont = 1
while Pok_1.vida>0 and Pok_2.vida>0:
    if turno==1:
        Pok_2.vida = Pok_2.vida-Pok_1.ataque
        print("Tras el ataque del turno "+str(cont)+" la vida del Pokemon Nº2 es "+str(Pok_2.vida))
        cont+=1
        turno=0
    else:
        Pok_1.vida = Pok_1.vida-Pok_2.ataque
        print("Tras el ataque del turno "+str(cont)+" la vida del Pokemon Nº1 es "+str(Pok_1.vida))
        cont+=1
        turno=1
if Pok_1.vida<=0:
    print("El ganador es el Pokemon nº2")
else:
    print("El ganador es el Pokemon nº1")
