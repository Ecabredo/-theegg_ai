from functions import f_compr, f_dcompr, f_input
from pympler.asizeof import asizeof


# Se llama a la función de entrada de cadena:
v_cadena = f_input()

while f_compr(v_cadena) == None:
    v_cadena = f_input()

print("La cadena ocupa {} bytes en memoria".format(asizeof(v_cadena)))
print("El resultado de la cadena comprimida se representa en la siguiente lista de diccionarios: \n" + str(f_compr(v_cadena)[0]))
print("La cadena comprimida ocupa {} bytes memoria".format(asizeof(f_compr(v_cadena)[0])))
print("El resultado de la descompresión es: " + f_dcompr(f_compr(v_cadena)[0],f_compr(v_cadena)[1]))

