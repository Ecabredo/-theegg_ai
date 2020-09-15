num_entradas = int(input("Escriba la cantidad de frases u oraciones a invertir: "))
cont = 0
l_result = list()
l_result_total = list()
while cont < num_entradas:
  entrada = input("Escriba una entrada: ")
  cont = cont + 1.
  #Se obtiene una lista con las palabras, separadas por espacio, con el método split()
  l_entrada=entrada.split()
  for i in reversed(l_entrada):
    l_result.append(i)
  #método para unir elementos de una lista:
  s_result=' '.join(l_result)
  l_result=[]
  l_result_total.append(s_result) 

for d in range(0,len(l_result_total)):
  print('Case'+' '+'#'+str(int(d)+1)+': '+str(l_result_total[d]))

  
  
  

  

