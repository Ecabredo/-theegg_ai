import re
import unicodedata
from string import punctuation
import string
from aux_function import contarFrec


v_char = string.printable 

#l_symbols  = list(set(punctuation)) #No se utiliza en la app, pero tambiém podría servir.
#print(v_char.translate({ord(i):None for i in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\t\n\r\x0b\x0c'}))

#Lista de carcateres especiales
l_symbols = v_char.translate({ord(i):None for i in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\t\n\r\x0b\x0c'})

#Se eliminan de la lista de caracteres extraños \t, \n, \r -- tab, newline, return
l_symbols = list(v_char.translate({ord(i):None for i in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\t\n\r\x0b\x0c'}))
l_symbols.remove(' ')

#Se añaden los caracteres extraños identificados en el texto. No obstante, esto se podría obviar, por estar incluido el Unicode Latin-1 Supplement (ver más adelante).
l_symb_aux = ['"', '«','»', '¿', '¡']

l_symbols = l_symbols + l_symb_aux
print(l_symbols)

#Se añaden los caracteres extraños identificados a la lista principal de carcateres extraños.
pattern = ''
for i in range(0,len(l_symbols)):
    pattern =  "\\" + l_symbols[i] + "|" + pattern

#Se elimina el último caracter |, ya que representa la condición OR en regex.
pattern = pattern[:-1]


'''Se añade el rango Unicode Latin-1 Supplement para contemplar los caracteres acentuados y caractres extraños. No se incluyen los caracteres "¿" y "¡" en el rango,
ya que se quieren tratar como carcateres especiales a contar aparte'''
pattern = '[A-Za-z0-9\u00C0-\u00FF]+|' + pattern
#pattern = '\?|\,|\]|\%|\_|\?|\.|\:|\'|\['
#pattern = '\»|\«|\"|\~|\}|\||\{|\`|\_|\^|\]|\\|\[|\@|\?|\>|\=|\<|\;|\:|\/|\.|\-|\,|\+|\*|\)|\(|\'|\&|\%|\$|\#|\"|\!'
print(pattern)


text = input("Introduce el texto que quieres analizar: ")
#De  la siguiente manera, se podría codificar en ascii para admitir acentos del castellano. Después, se descodifica para tratarlo como un string y no como tipo bytes. 
#text = unicodedata.normalize('NFD', text).encode('utf8', 'ignore').decode('utf8')
#Se descarta dicha solución, ya que elimina caracteres extraños.

print(text)

#Se calculan el número de carcateres teniendo el cuenta los caracteres especiales
l_char      = []
v_suma_char = 0
l_char      = re.findall(pattern, text)
v_len_char  = len(l_char)
for i in range(0, v_len_char):
    v_suma_char += len(l_char[i])
    
print(l_char)
print('El número de caracteres, considerando también los caracteres especiales, es: ' + str(v_suma_char))

pattern     = '[A-Za-z0-9\u00C0-\u00FF]+'
l_word      = []
l_word      = re.findall(pattern, text)
v_len_word = len(l_word)
print('El número de palabras es: ' + str(v_len_word))


contarFrec(l_word)


