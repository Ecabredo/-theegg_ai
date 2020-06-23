def mod(): #modulos = bibliotecas
  #Existen tres tipos de módulos: own modules, third party modules (bibliotecas que se pueden descargar de internet) y python modules (modulos built-in de python)

  #Modules preconstridos de python:
  #Obtener fecha actual
  import datetime
  print(datetime.date.today()) #biblioteca.parámetro.método

  #Este módulo tiene también un método para pasar los minutos a horas:
  print(datetime.timedelta(minutes = 80))

  #Otra forma de importan métodos:
  from datetime import timedelta
  print(timedelta(seconds = 3600))#aquí, ahora no hace falta especifical el modulo.

  #Otra ejemplo:
  from datetime import timedelta, date
  print(date.today())

