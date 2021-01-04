Cálculo del número de caracteres: 
Se consideran caracteres todas aquellas letras y signos de escritura. Así, se consideran como caracteres las letras, números y signos del latín (Unicode Latin-1).
Los pasos seguidos para la obtención del número de carcateres ha sido:
  1. Se obtiene la lista de todos los carcateres especiales que se quiere considerar.
  2. Se construye un patrón con los carcateres extraños, teniendo en cuenta las expresiones regulares \\ (representación del sentido literal del caracter) y | (operando lógico or).
  3. Se añade al patrón el rango Unicode Latin-1 Supplement para cotemplar los caracteres acentuados y otros caracteres extraños.
  4. Se solicita el texto a evaluar. El texto se debe copiar desde un word, ya que desde pdf no lo cogía correctamente.
  5. Se divide el texto en una lista, donde cada elemento se forma siguiendo el patrón. 
  6. Se calcula el número de caracteres considerando los carcateres especiales.
  
Cálculo del número de palabras:
En este caso, el patrón a evaluar es mucho más sencillo. No obstante, el procedimiento es el mismo.
  1. Se construye un patrón a partir de los números y letras del latín (Unicode Latin-1).
  2. Se divide el texto en una lista, donde cada elemento se forma siguiendo el patrón. 
  3. Se calcula el número de palabras. 
  
Cálculo de raking de palabras:
Para hacer el cálculo del ranking, se define una función auxiliar:
  1. Se define un diccionario a partir de la lista.
  2. La clave representa el número de ocurrencias del valor. 
 
