jugar = "si"

puntos = 0
votos_si = 0
votos_no = 0

while jugar == "si":
    print("votaron", puntos, "personas")
    print("tienes", votos_si, "si")
    print("tienes", votos_no, "no")

    voto = input("inserte (si) o (no):  ").lower()

    if voto == "si":
        votos_si += 1
        puntos += 1

    elif voto == "no":
        votos_no += 1
        puntos += 1

    else:
        print("por favor, inserte si o no")

    jugar = input("¿Quiere registrar otro voto? ")
