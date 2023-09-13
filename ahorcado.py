def jugar():
  print('================================')
  print('Bienvenido al Juego del Ahorcado')
  print('================================')

  import random



  palabra_secreta ='mandarina'
  letras_acertadas =['_' for elemento in palabra_secreta]
  
  ahorcado = False
  acerto = False
  errores = 0  # contador de errores
  
  print(letras_acertadas)
  while(not ahorcado and not acerto):
    entrada = input('Ingrese una letra ...')
    entrada = entrada.strip()                 # elimina espacio en blanco a la izquierda y derecha
    entrada = entrada.lower()                 # convierte a letras minúsculas
    
    if entrada in palabra_secreta:
        indice = 0
        for letra in palabra_secreta:
            if(entrada==letra):
                letras_acertadas[indice] = letra

            indice = indice + 1
    else:
        errores += 1
    
    ahorcado = errores == 9
    acerto = "_" not in letras_acertadas
    print(letras_acertadas)

  if(acerto):
    print('Felicitaciones, ganaste!!')
  else:
    print('lo siento, perdiste!!')
  print("Fin del Juego")
    
if(__name__ == "__main__"):
    jugar()