# 1. 4*4 grid que se pueda llenar con cualquier número
# 2. Si presiona alguna tecla lo elementos de la celda se mueve en dirección a la tecla presionada
# 3. Si los números son identicos se suman.
# 4. Se añade un número en una celda vacia aleatoria después de moverse.
# 5. Si no hay una celda libre se pierde.

#Importar el paquete
import random


def empezar_juego():
    # Inicializar la matriz del juego
    mat = []
    for i in range(4):
        mat.append([0] * 4)

    print("Los comandos los siguientes: ")
    print("w: arriba")
    print("s: abajo")
    print("a: izquierda")
    print("d: derecha")

    return mat

#Funcion para agregar un nuevo 2
#En una celda aleatoria
def agregar_num(mat):

    #Elegir la fila y columna aleatoriamente
    fila = random.randint(0, 3)
    columna = random.randint(0, 3)

    #Revisar si la celda ya tiene un número
    while (mat[fila][columna] != 0):
        fila = random.randint(0, 3)
        columna = random.randint(0, 3)
    
    #Asignar el 2 en la celda disponible
    mat[fila][columna] = 2

# Función para ver el estado actual del juego
def obtener_estado_juego(mat):

    # Si alguna celda tiene 2048 se gano
    for i in range(4):
        for j in range(4):
            if(mat[i][j] == 2048):
                return "GANASTE!!!"

    