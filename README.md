# 
# Juego de piedra, papel y tijera

Este es un pequeño juego de piedra, papel y tijera implementado en Python. El juego consiste en que el usuario y el ordenador eligen una opción (piedra, papel o tijera) y se determina quién gana la ronda en función de las reglas habituales del juego.

## Requisitos

Este juego está implementado en Python y se necesita tener Python instalado en su computadora para poder jugar.

## Instrucciones de uso

1. Clonar o descargar el repositorio en su computadora.
2. Abrir la terminal y navegar hasta la carpeta donde se encuentra el archivo "index.py".
3. Ejecutar el siguiente comando: `python index.py`.
4. Se le pedirá que ingrese su opción (piedra, papel o tijera) para cada ronda. Ingrese su opción y presione Enter.
5. Después de tres rondas, el juego mostrará quién ganó (el usuario, el ordenador o si fue un empate).

Esperamos que disfrutes del juego. ¡Que gane el mejor!

## Como funciona el codigo 

El código comienza definiendo las opciones posibles para el usuario y el ordenador:

```python
options = ('piedra', 'papel', 'tijera')
```
Luego, se define el número de rondas que se jugarán:

```python
rounds = 3
```

A continuación, se inicia un bucle for que ejecutará el número de rondas especificado:

```python
for i in range(1, rounds+1):
```

Dentro del bucle for, se le pide al usuario que ingrese su opción y se verifica si es una opción válida:

```python
user_option = input('Ingrese su opcion (Piedra, Papel, tijera)').lower()
while user_option not in options:
    print('Opción inválida')
    user_option = input('Ingrese de nuevo su opcion (Piedra, Papel, tijera)').lower()
```

A continuación, el programa elige una opción aleatoria para el ordenador:

```python
computer_option = random.choice(options)
```

Luego, se compara la opción del usuario con la opción del ordenador para determinar quién gana la ronda:

```python
if user_options == computer_options:
        print('*' * 10)
        print('Empate')
    elif user_options == 'piedra' and computer_options == 'tijera' or \
            user_options == 'papel' and computer_options == 'piedra' or \
            user_options == 'tijera' and computer_options == 'papel':
        print('Gana Usuario')
        user_winners += 1
    else:
        print('Gana Computador')
        computer_winners += 1
```

Finalmente, el programa muestra quién ganó después de todas las rondas:

```python
print('* ' * 10)
if computer_winners > user_winners:
    print('*'*10 + ' ' + 'computador gano')
elif user_winners > computer_winners:
    print('*'*10 + ' ' + 'Gano el usuario')
else:
    print('El juago quedo en empate')
print('* ' * 10)
```

