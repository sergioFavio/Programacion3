def jugar():
  print('================================')
  print('Bienvenido al Juego del Ahorcado')
  print('================================')

  palabra_secreta ='mandarina'
  
  ahorcado = False
  acerto = False
  
  while(not ahorcado and not acerto):
    entrada = input('Ingrese una letra ...')
    for letra in palabra_secreta:
        if(entrada==letra):
            print(entrada)

    print('jugando ...')


  print("Fin del Juego")
    
if(__name__ == "__main__"):
    jugar()