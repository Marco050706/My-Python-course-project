i = 0
saldo_actual = 1000
while i < 3:

    contraseña_correcta = "Señor1234"

    contraseña = str(input("ingrese la contraseña: "))

    if contraseña == contraseña_correcta:
        print("Bienvenido")
        while True:

            print(
                """
                        = MENÚ DEL CAJERO =
                        (1) Consultar saldo  
                        (2) Retirar dinero
                        (3) Depositar dinero
                        (4) Salir del cajero
                        """
            )

            accion = int(input("Inserte que quiere realizar: "))

            Consultar_saldo = 1
            Retirar_saldo = 2
            Depositar_dinero = 3
            Salir_del_cajero = 4

            match accion:
                case 1:
                    print(f"Tu saldo actual es de: {saldo_actual} colones")

                case 2:
                    cantidad = int(input("¿Cuando deseas retirar? "))
                    if cantidad > saldo_actual:
                        print("Saldo insuficiente. :(")
                    else:
                        saldo_actual -= cantidad
                        print(
                            f"El retiro esta siendo procesado... , su saldo actual es de: {saldo_actual} colones"
                        )

                case 3:
                    cantidad = int(input("¿Cuanto dinero desea depositar? "))
                    saldo_actual += cantidad
                    print(
                        f"Tu deposito esta siendo procesado... , su saldo actual es de: {saldo_actual} colones"
                    )

                case 4:
                    print("Gracias por usar este cajero, tenga un buen dia :)")
                    break

                case _:
                    print("Te equivocaste de acción, intenta denuevo")

    else:
        print("Contraseña incorrecta...")

    i += 1
