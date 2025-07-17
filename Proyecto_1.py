nombre_pltaforma = input("Dale un nombre a la plataforma 😊: ")

print(
    "\n¡Bienvenido a",
    nombre_pltaforma,
    ", Aquí te ayudaremos a elegir la mejor película para ti.\n",
)

# Aqui puedes elejir tu estado de animo

estado_de_animo = int(
    input(
        """Cual es tu estado de animo hoy? 
        (ingresa el numero de tu estado de animo)            
        feliz(1), triste(2), aburrido(3), emocionado(4): 
        """
    )
)

# Aqui puedes elejir tu genero de peliculas favorito

genero_de_pelicula_favorito = int(
    input(
        """
        Cual seria tu genero de peliculas favorito?
        (ingresa el numero con el genero favorito) 
        comedia(1), terror(2), acción(3), romance(4): 
        """
    )
)

# Condicionales:

if estado_de_animo == 1:
    if genero_de_pelicula_favorito == 1:
        print("Excelente, te recomiendo que veas Como niños 1 y 2 😁")
    elif genero_de_pelicula_favorito == 2:
        print("Si te gusta el terror podrias ver scary movie 👻")
    elif genero_de_pelicula_favorito == 3:
        print("Ummm, quiza podrias ver una pelicula de Marvel, quiza los Avengers 🦸")
    else:
        print("Si te gusta el amor, podria gustarte Me before you ❤️")

elif estado_de_animo == 2:
    if genero_de_pelicula_favorito == 1:
        print("quiza esta te pueda alegrar el dia, Supercool 😎")
    elif genero_de_pelicula_favorito == 2:
        print(
            "Se que estas triste pero esto puede gustarte, te recomiendo Five Nights at Freddy's 🐻"
        )
    elif genero_de_pelicula_favorito == 3:
        print("Quiza esta pelicula te pueda animar, Guardians of the Galaxy 🚀")
    else:
        print(
            "Si tienes ganas de ver una peli de romance te recomiendo, Bajo la misma estrella 🌃"
        )

elif estado_de_animo == 3:
    if genero_de_pelicula_favorito == 1:
        print(
            "Una pelicula que me encanta ver cuando estoy aburrido es The Naked Gun 👮"
        )
    elif genero_de_pelicula_favorito == 2:
        print("Quiza te pueda gustar, Actividad Paranormal 😱")
    elif genero_de_pelicula_favorito == 3:
        print("Tal ves te guste el poderosisimo John Wick 💥")
    else:
        print("Si te aburres podrias ver Titanic 🚢")

else:
    if genero_de_pelicula_favorito == 1:
        print("Perfecto para estar emocionado, te recomiendo Deadpool 🎯")
    elif genero_de_pelicula_favorito == 2:
        print("Si quieres terror con mucha emoción, prueba La Noche del Demonio 🔮")
    elif genero_de_pelicula_favorito == 3:
        print("Para acción y emoción, ve Misión Imposible 🎬")
    else:
        print("Si quieres romance y emoción, mira La La Land 🎷")
