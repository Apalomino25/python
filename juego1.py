# JUEGO PIEDRA PAPEL O TIJERA

import random


opcionUsuario = ""
opcionMaquina = ""

opcionMaquina = random.randint(1,3)

match opcionMaquina:

    case 1 :
        opcionMaquina = "PIEDRA"
    case 2:
        opcionMaquina = "PAPEL"
    case 3:
        opcionMaquina = "TIJERA"
    case _:
        print("opcion no encontrada")


opcionUsuario = input("INGRESE PIEDRA | PAPEL | TIJERA\n").upper() 

print("el usuario eligio:" + opcionUsuario)    
print("la maquina eligio:" + opcionUsuario)   


if  opcionMaquina == "TIJERA" and opcionUsuario == "PIEDRA":
    print("usuario Gana")

elif opcionMaquina == "PIEDRA" and opcionUsuario == "PAPEL":
    print("usuario Gana")

elif opcionMaquina == "PAPEL" and opcionUsuario == "TIJERA" :
    print("usuario Gana")