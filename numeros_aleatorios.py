import random
from statistics import mean, variance

# Se crea una lista que alojará los números aleatorios generados.
num_list = []

# Se asigna la cantidad de números a generar.
num_range = 100

# Contador inicializado para saltos de línea en archivo.
c = 1

# Abrimos un archivo txt para ir añadiendole los números.
with open('numeros.txt', 'w') as f:
    f.write('Números generados:\n')
    for x in range(num_range):
        # -> Genera un número real uniformemente aleatorio entre 10 y 20 inclusive.
        n = random.uniform(10, 20)

        # -> Trunca cada número a 4 decimales.
        n_rounded = round(n, 4)

        # -> Se agrega el número a la lista.
        num_list.append(n_rounded)

        # -> Se añade cada número a un archivo txt.
        f.write(str(n_rounded))
        # -> Separa con comas hasta que llega a la décima columna.
        if c < 100:
            f.write(',')
        # -> Si llega a la décima columna salta de línea.
        if c % 10 == 0:
            f.write('\n')
        # -> Si no, añade un espacio.
        else:
            f.write(' ')
        c += 1

    # Se obtiene la media muestral y la varianza, se asignan a una variable respectivamente.
    media = mean(num_list)
    varianza = variance(num_list)

    # Imprime al archivo media y varianza muestral, truncados a 4 decimales.
    f.write('\nMedia muestral: {}\n'.format(round(media, 4)))
    f.write('Varianza muestral: {}\n'.format(round(varianza, 4)))

    # Comparaciones al valor de la media esperado.
    if media > 15:
        f.write('La media muestral es mayor a 15 por {}.'.format(round(media - 15, 4)))
    elif media < 15:
        f.write('La media muestral es menor a 15 por {}.'.format(round(15 - media, 4)))
    else:
        f.write('La media muestral es igual a 15. O___o')
