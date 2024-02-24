def primeros_auxilios():
    print("Inicio")
    respuesta = input("¿Responde a Estímulos? (Sí/No): ")
    if respuesta.lower() == "sí":
        print("Valorar la necesidad de llevarlo al hospital más cercano")
    else:
        print("Abrir la vía Aérea")
        respira = input("¿Respira? (Sí/No): ")
        if respira.lower() == "sí":
            print("Permitirle posición de suficiente ventilación")
        else:
            print("Administrar 5 Ventilaciones y llamar a Ambulancia")
            llego_ambulancia = "no"
            while llego_ambulancia.lower() == "no":
                signos_de_vida = input("¿Signos de Vida? (Sí/No): ")
                if signos_de_vida.lower() == "sí":
                    print("Reevaluar a la espera de la Ambulancia")
                else:
                    print("Administrar Compresiones Torácicas hasta que llegue ambulancia")
                llego_ambulancia = input("¿Llegó la Ambulancia? (Sí/No): ")
            print("Fin")

primeros_auxilios()