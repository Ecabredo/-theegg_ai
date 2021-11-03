Ejercicio:

    Para resolver el ejercicio se debe ejecutar el programa recogido en el fichero análisis_memoria.py.
    Por otro lado, el fichero functions.py contiene las funciones de comprensión, descomprención y solicitud 
    de datos de entrada al usuario.

Resultados:

    Para calcular el espacio ocupado por un objeto en memoria se utiliza el módulo asizeof. 
    De esta manera, se consideran todos los elementos guardados en un objeto de manera recursica, y no únicamente lo 
    que ocupa el objeto. La alternativa era utilizar sys.getsizeof(), el cual únicamente indica el espacio
    en memoria ocupado por el objeto primitivo.

    En el caso particular del ejecicio, al guardar el resultado de la comprensión en una lista de diccionarios (tripleta),
    la ocupación en memoria de la comprensión es superior a la ocupación de la cadena inicial.


