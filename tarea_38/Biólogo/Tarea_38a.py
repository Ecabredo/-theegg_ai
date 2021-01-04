#El ADN debe estar formado por conjuntos ordenados de bases de nucleótidos: adenina (abreviado A), citosina (C), guanina (G) y timina (T). Cualqueir otro carácter, incluido minúsculas, no será adminito por el programa.
import re

ADN_1 = input("Introduce la primera secuencia de ADN: ")
#print(re.search('[^ACGT]', ADN_1))
#print(ADN_1.find('A'))
#print(ADN_1.find('C'))
#print(ADN_1.find('G'))
#print(ADN_1.find('T'))

while (ADN_1.find('A') == -1 or ADN_1.find('C') == -1 or ADN_1.find('G') == -1 or ADN_1.find('T') == -1 or re.search('[^ACGT]', ADN_1) != None):
#  print(re.search('[^ACGT]', ADN_1))
#  print(ADN_1.find('A'))
#  print(ADN_1.find('C'))
#  print(ADN_1.find('G'))
#  print(ADN_1.find('T'))
  ADN_1 = input("La secuencia de ADN no es correcta. Introdúzcala de nuevo: ")

ADN_2 = input("Introduce la segunda secuencia de ADN: ")
while (ADN_2.find('A') == -1 or ADN_2.find('C') == -1 or ADN_2.find('G') == -1 or ADN_2.find('T') == -1 or re.search('[^ACGT]', ADN_2) != None):
  ADN_2 = input("La secuencia de ADN no es correcta. Introdúzcala de nuevo: ")

ADN_sec = str()
ADN_bases = list()
#Se debe recorrer la cadena hasta el último carácter. Además, se debe comenzar a recorrer la cadena primero desde el primer carácter hasta el último. Después, se debe recorrer la cadena desde el segundo carácter hasta el último y así sucesivamente. Por lo tanto, se necesitan dos loops.
for d in range(0,len(ADN_1)):
  for i in ADN_1[d:len(ADN_1)]:
    #Se debe concatenar hasta el último carácter de la cadena. Después, se vacía la variable ADN_sec (que es donde se van guardando las sucesivas concatenaciones) y se comienza de nuevo.
    if len(ADN_sec) > len(ADN_1)- d:
      ADN_sec = ''
    ADN_sec =  ADN_sec+i
    #Se comprueba si la concatenación está embebida en la segunda secuencia de ADN. Si es así, se guarda el valor en la lista ADN_bases.
    if ADN_2.find(ADN_sec) != -1:
      ADN_bases.append(ADN_sec)

#Se busca el elemento de la lista con el mayor número de carácteres.
max = 0
for t in range(0, len(ADN_bases)):
  if max < len(ADN_bases[t]):
    max = len(ADN_bases[t])
    result = ADN_bases[t]

print(result)



  
