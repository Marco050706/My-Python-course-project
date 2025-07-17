altura = int(input("cuanto mides?(cm) "))
creditos = int(input("cuantos creditos tienes? "))

if altura > 150 and creditos > 10:
    print("¡Disfruta del viaje!")

elif altura > 10 and creditos <= 150:
    print("No eres lo suficientemente pro para subir :(")

elif altura > 150 and creditos <= 10:
    print("te faltan creditos papu")

else:
    print("no cumples con ninguno de los requisitos")
