pregunta = input("Escribe tu pregunta: ")

import random

respuesta_aleatoria = random.randint(1, 9)

if respuesta_aleatoria == 1:
    respuesta = "Sí, definitivamente."
elif respuesta_aleatoria == 2:
    respuesta = "Sin duda."
elif respuesta_aleatoria == 3:
    respuesta = "Por supuesto."
elif respuesta_aleatoria == 4:
    respuesta = "La respuesta es confusa, intenta de nuevo."
elif respuesta_aleatoria == 5:
    respuesta = "Pregunta de nuevo más tarde."
elif respuesta_aleatoria == 6:
    respuesta = "Mejor no decirte ahora."
elif respuesta_aleatoria == 7:
    respuesta = "Mis fuentes dicen que no."
elif respuesta_aleatoria == 8:
    respuesta = "Mi pronóstico no es muy bueno."
else:
    respuesta = "Muy dudoso."

print("Tu respuesta es:", respuesta)
