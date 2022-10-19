import random


def run():
    numero_aleatorio = random.randint(1, 100)
    vida = 5
    print(' ❤️ '* vida)
    numero_elegido = int(input('Elige un número del 1 al 100: '))
    while numero_elegido != numero_aleatorio:
        if vida > 1:
            if numero_elegido < numero_aleatorio:
                vida = vida - 1
                print(' ❤️ '* vida)
                print('Busca un número más grande')
            else:
                vida = vida - 1
                print(' ❤️ '* vida)
                print('Busca un número más pequeño')
            numero_elegido = int(input('Elige otro número: '))
        else:
            print('¡Perdiste!')
            break
    if numero_elegido == numero_aleatorio:
        print('¡Ganaste!')
    


if __name__ == '__main__':
    run()