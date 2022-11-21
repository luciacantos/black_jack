cartas = {
    chr(0x1f0a1): 11,
    chr(0x1f0a2): 2,
    chr(0x1f0a3): 3,
    chr(0x1f0a4): 4,
    chr(0x1f0a5): 5,
    chr(0x1f0a6): 6,
    chr(0x1f0a7): 7,
    chr(0x1f0a8): 8,
    chr(0x1f0a9): 9,
    chr(0x1f0aa): 10,
    chr(0x1f0ab): 10,
    chr(0x1f0ad): 10,
    chr(0x1f0ae): 10,
}

print("Valor de cada carta: ")
for carta in sorted(cartas.keys()):
    print("La carta {} vale {}".format(carta, cartas[carta]))

print("Inicio del juego: ")
lista_cartas = list(cartas)

from random import choice, sample

## hacer que la persona elija dos cartas y sumar su valor

print("Ha seleccionado:", end=" ")
carta = choice(lista_cartas)
score = cartas[carta]
print(carta, end=" ")
carta = choice(lista_cartas)
score += cartas[carta]
print(carta, end=" ")
print(" >>> su puntuación es de", score)


main_banca = sample(lista_cartas, 2)
score_banca = sum(cartas[carta] for carta in main_banca)
print("La banca tiene: {} {}  >> su score es {}".format(main_banca[0],main_banca[1], score_banca))

## sumar los valores de la persona y de la banca y si tiene mas de 21 ha perdido y si tiene menos o 21 ha ganado
