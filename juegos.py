import ahorcado
import adivinanza

print('================================')
print('Elija su Juego')
print('================================')

print("(1) Ahorcado (2) Adivinanza")

juego = int(input("¿Cuál juego? "))

if (juego == 1):
    print("Jugando ahorcado")
elif (juego == 2):
    print("Jugando adivinanza")