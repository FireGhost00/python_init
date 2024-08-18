from random import shuffle

# Lista Inicial
sticks = ['-', '--', '---', '----', '-----', '------', '-------', '--------', '---------', '----------']


# mezclar palitos
def mix_sticks(list):
    """
    Shuffles the list of sticks.

    Args:
        list (list): The list of sticks to shuffle.

    Returns:
        list: The shuffled list of sticks.
    """
    shuffle(list)
    return list


# pedirle inteto al usuario
def try_luck():
    """
    Prompts the user to select a number between 1 and 10.

    Returns:
        int: The number selected by the user.
    """
    intento = 0
    while intento not in range(1, 11):
        try:
            intento = int(input('Selecciona un numero del 1 al 10: '))
        except ValueError:
            print('Por favor, introduce un número')

    return intento


# comprobar intento
def check_guess(sticks, intento):
    """
    Checks if the user's guess is the shortest stick.

    Args:
        sticks (list): The list of sticks.
        intento (int): The user's guess (index in the list).

    Prints:
        str: The result of the guess.
    """
    if sticks[intento - 1] == '-':
        print('La regaste!')
    else:
        print('Te salvaste!')

    print(f'Te ha tocado: {sticks[intento - 1]}')


print('Bienvenido al juego de los palitos')
print('Tienes que seleccionar un numero del 1 al 10 evitando que te toque el palito mas corto')

flag = 's'
while flag == 's':
    check_guess(mix_sticks(sticks), try_luck())
    flag = input('Quieres jugar de nuevo? (s/n) ').lower()
    if flag != 'n' and flag != 's':
        print('Por favor, introduce una opción válida')
        flag = input('Quieres jugar de nuevo? (s/n) ').lower()

print('Gracias por jugar!')
