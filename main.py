import random

plays = 0
number = random.randint(1,10)
print('Bienvenido a ¡Adivina el Numero!')
print('Por favor, ingresa tu nombre: ')
name = input()
print('Genial {}, ahora ingresa un numero entre el 1 y el 10 para comenzar a jugar: '.format(name))
option = int(input())

for i in range(5):
    plays += 1
    if option > number:
        print('El numero es mas chico, por favor ingresa otro numero')
    if option < number:
        print('El numero es mas grande, por favor ingresa otro numero')
    if option == number:
        break
    option = int(input())
        
if plays >= 5 and option != number:
    print('Ups! Ya no te quedan mas intentos :(')
else:
    print('Felicidades! Adivinaste el numero :D')
