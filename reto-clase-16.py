# Juego del aahorcado
opciones_permitidas = ["piedra", "papel", "tijeras"]

print('''
------------------------------------------------
Bienvenido al juego de piedra, papel y tijeras'
__________________________________________________________
''')

print('''[JUGADOR 1]''')
opcion_jugador_1 = input("  > Elige 'Piedra', 'Papel' o 'Tijeras': ")
while opcion_jugador_1.lower() not in opciones_permitidas:
    print("    Opción '{}' no válida".format(opcion_jugador_1))
    opcion_jugador_1 = input("  > Elige 'Piedra', 'Papel' o 'Tijeras': ")

print('    ¡¡¡OÍDO COCINA!!!')

print('''
[JUGADOR 2]''')
opcion_jugador_2 = input("  > Elige 'Piedra', 'Papel' o 'Tijeras': ")
while opcion_jugador_2.lower() not in opciones_permitidas:
    print("    Opción '{}' no válida".format(opcion_jugador_2))
    opcion_jugador_2 = input("  > Elige 'Piedra', 'Papel' o 'Tijeras': ")

print('    ¡¡¡MARCHANDO!!!')

print('''
****************************************************************
''')
print("El JUGADOR 1 ha elegido {}. El JUGADOR 2 ha eligido {}".format(opcion_jugador_1.upper(), opcion_jugador_2.upper()))

opcion_jugador_1 = opcion_jugador_1.lower()
opcion_jugador_2 = opcion_jugador_2.lower()

resultado_1 = "¡¡¡El JUEGO HA ACABADO EN EMPATE!!!"
resultado_2 = "¡¡¡El JUGADOR 1 GANA!!!"
resultado_3 = "¡¡¡El JUGADOR 2 GANA!!!"

match opcion_jugador_1:
    case "piedra":
        if opcion_jugador_2 == "piedra":
            print(resultado_1)
        elif opcion_jugador_2 == "papel":
            print(resultado_3)
        else:
            print(resultado_2)
    case "papel":
        if opcion_jugador_2 == "papel":
            print(resultado_1)
        elif opcion_jugador_2 == "piedra":
            print(resultado_2)
        else:
            print(resultado_3)
    case "tijeras":
        if opcion_jugador_2 == "tijeras":
            print(resultado_1)
        elif opcion_jugador_2 == "papel":
            print(resultado_2)
        else:
            print(resultado_3)

print('''
****************************************************************
''')