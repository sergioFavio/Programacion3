def jugar():
  print('================================')
  print('Bienvenido al Juego del Ahorcado')
  print('================================')

  palabra_secreta ='mandarina'
  
  ahorcado = False
  acerto = False
  
  while(not ahorcado and not acerto):
    entrada = input('Ingrese una letra ...')
    indice = 0
    for letra in palabra_secreta:
        if(entrada==letra):
            print('Se encontro la letra {} en la posición {}'.format(letra, indice))

        indice = indice + 1
    print('jugando ...')


  print("Fin del Juego")
    
if(__name__ == "__main__"):
    jugar()