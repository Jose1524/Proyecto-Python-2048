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
            
    #Revisar si el juego continua
    for i in range(4):
        for j in range(4):
            if(mat[i][j] == 0):
                return "JUEGO EN CURSO"

    # Si el juego esta vacio
    # Pero si después de cualquier movimiento
    # Que las celdas se junten y crean una celda vacia
    # Entonces el juego no ha terminado

    for i in range(3):
        for j in range(3):
            if(mat[i][j] == mat[i+1][j] or mat[i][j] == mat[i][j+1]):
                return "JUEGO EN CURSO"

    for j in range(3):
        if(mat[3][j] == mat[3][j+1]):
            return "JUEGO EN CURSO"

    for i in range(3):
        if(mat[i][3] == mat[i+1][3]):
            return "JUEGO EN CURSO"

    return 'PERDIO'

#Función para duplicar el número
def merge(mat):

    changed = False

    for i in range(4):
        for j in range(3):

            # If la celda actual tiene el mismo valor que la siguiente celda en la fila
            # Y si no están vacíos entonces:
            if(mat[i][j] == mat[i][j + 1] and mat[i][j] != 0 ):
                
                #Duplicar el valor
                mat[i][j] = mat[i][j] * 2

                #Convertir el valor de la derecha en 0
                mat[i][j + 1] = 0
                changed = True

    return mat, changed



#Funcion para comprimir la matriz después de cada movimientos
def compress(mat):

    #Variable para determinar si hubo un cambio o no
    changed = False

    # Nueva matriz
    new_mat = []

    # Iniciar con celdas vacias
    for i in range(4):
        new_mat.append([0] * 4)

    # Loop para entrar a cada fila
    # Se van a cambiar entradas a su máxima izquierda
    for i in range(4):
        pos = 0

        # Loop para cada celda
        for j in range(4):
            if(mat[i][j] != 0):

                # Si la celda no esta vacia
                # Mover el valor una celda a la izquierda
                # Esto es denotado por la variable pos
                new_mat[i][pos] = mat[i][j]

                if(j != pos):
                    changed = True
                pos += 1

    return new_mat, changed




# Funcion para revertir las filas
def reverse(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][3 - j])
    return new_mat






# Funcion para intercambiar filas y columnas
def transpose(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat


def move_left(mat):

    # Primero comprimir
    new_mat, changed1 = compress(mat)

    # Segundo merge para ver si se pueden juntar numeros iguales
    new_mat, changed2 = merge(new_mat)

    # Ver si hubo algún cambio
    changed = changed1 or changed2

    # Después de hacer el merge volver a comprimir
    new_mat, temp = compress(new_mat)

    # Devolver la nueva matriz al mover a la izquierda
    return new_mat, changed



def move_right(mat):

    # Mover todos los valores a la derecha
    new_mat = reverse(mat)

    new_mat, changed = move_left(new_mat)

    new_mat = reverse(new_mat)

    return new_mat, changed




def move_up(mat):
    # Convertir las filas por columnas para aprovechar las funciones que ya tenemos
    new_mat = transpose(mat)

    # Simular el movimiento a la izquierda para aprovechar sus funciones
    new_mat, changed = move_left(new_mat)

    # Volvemos a hacer el transpose para retornar posición original
    new_mat = transpose(new_mat)

    return new_mat, changed


def move_down(mat):

    # Convertir las filas por las columnas
    new_mat = transpose(mat)

    # Simular el movimiento a la derecha para aprovechar sus funciones
    new_mat, changed = move_right(new_mat)

    # Retornar posición original
    new_mat = transpose(new_mat)

    return new_mat, changed
