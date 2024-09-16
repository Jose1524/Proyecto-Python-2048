# Importar la lógica
import logic

# Driver code
if __name__ = '__main__':
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
    
    
    

