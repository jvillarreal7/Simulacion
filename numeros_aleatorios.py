import random
from statistics import mean, variance

# Se crea una lista que alojará los números aleatorios generados.
num_list = []

# Se pide al usuario la cantidad de números a generar.
num_range = int(input('Numeros a generar:\n'))

# Dada la cantidad de números a generar:
for x in range(num_range):
    # -> Genera un número real uniformemente aleatorio entre 10 y 20 inclusive.
    n = random.uniform(10, 20)
    # -> Trunca cada número a 4 decimales.
    n_rounded = round(n, 4)
    # -> Se agrega el número a la lista.
    num_list.append(n_rounded)

# Se obtiene la media muestral y la varianza, se asignan a una variable respectivamente.
media = mean(num_list)
varianza = variance(num_list)

# Imprime media y varianza muestral así como el no. de elementos.
# Los primeros dos truncados a 4 decimales.
print('\nMedia muestral: {}'.format(round(media, 4)))
print('Varianza muestral: {}'.format(round(varianza, 4)))
print('Numero de elementos: {}\n'.format(len(num_list)))

# Comparaciones al valor de la media esperado.
if media > 15:
    print('La media muestral es mayor a 15 por {}.'.format(round(media - 15, 4)))
elif media < 15:
    print('La media muestral es menor a 15 por {}.'.format(round(15 - media, 4)))
else:
    print('La media muestral es igual a 15. O___o')
