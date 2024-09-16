# Importar la lógica
import logic

# Driver code
if __name__ == '__main__':
    mat = logic.empezar_juego()

while(True):

    # Agarrar el input del usuario
    x = input("Presione el comando: ")

    # Cuando se quiere mover hacia arriba
    if(x == 'W' or x == 'w'):
        # Llamar función hacia arriba
        mat, flag = logic.move_up(mat)

        # Mostrar estado actual del juego
        status = logic.obtener_estado_juego(mat)
        print(status)

        # Si el juego no termina continuar
        if(status == 'JUEGO EN CURSO'):
            logic.agregar_num(mat)
    
        else: 
            break

    # Cuando se quiere mover hacia abajo
    if (x== "S" or x =="s"):
        mat, flag = logic.move_down(mat)
        mostrar = logic.obtener_estado_juego(mat)
        print(mostrar)
        if(mostrar=="JUEGO EN CURSO"):
            logic.agregar_num(mat)
        else:
            break

    #Cuando se quiere mover a la derecha
    if (x =="D" or x == "d"):
        mat, flag =logic.move_right(mat)
        mover = logic.obtener_estado_juego(mat)
        print(mover)
        if(mover=="JUEGO EN CURSO"):
            logic.agregar_num(mat)
        else:
            break

    #Cuando se quiere mover a la izquierda
    if (x =="A" or x == "a"):
        mat, flag =logic.move_left(mat)
        mover = logic.obtener_estado_juego(mat)
        print(mover)
        if(mover=="JUEGO EN CURSO"):
            logic.agregar_num(mat)
        else:
            break
    #Se quiere imprimir la matriz
    print(mat)
    
