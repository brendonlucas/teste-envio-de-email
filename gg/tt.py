import random

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'g', 'h']
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
link = ''
for x in range(7):
    num_letra = random.randint(0, 10)
    link += letras[num_letra]

for i in range(6):
    num_letra = random.randint(0, 9)
    link += str(numeros[num_letra])

print(link)