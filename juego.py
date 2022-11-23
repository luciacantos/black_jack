from random import choice, sample

#diccionario de las cartas
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
#lista de las cartas con el dibujo y su valor
print("Valor de cada carta: ")
for carta in sorted(cartas.keys()):
    print("La carta {} vale {}".format(carta, cartas[carta]))

print("")
print("Inicio del juego.")
lista_cartas = list(cartas)

print("")

## hacer que la persona elija dos cartas (de una en una) y sumar su valor
## primero enseñar el dibujo de la carta y después el valor
print("Pulse Enter para obterner su primera carta: ")
input()
print("Su primera carta es:", end=" ")
carta = choice(lista_cartas)
puntuacion = cartas[carta]
print(carta, end=" ")
print("")
print("Por ahora tiene una puntación de", puntuacion,"puntos")
print("")

print("Pulse Enter para obterner su segunda carta: ")
input()
print("Su segunda carta es:", end=" ")
carta = choice(lista_cartas)
puntuacion += cartas[carta]
print(carta, end=" ")
print("")
print("Sumando las dos cartas tiene una puntuación de", puntuacion,"puntos")
print("")

#el crupier saca dos cartas
#primero enseñar el dibujo de la carta y después el valor de la suma de las dos
print("Pulse enter para otener la puntuación del Crupier:")
input()
main_crupier = sample(lista_cartas, 2)
puntuacion_crupier = sum(cartas[carta] for carta in main_crupier)
print("El crupier reparte dos cartas: {} {}  sus valores suman {}".format(main_crupier[0],main_crupier[1], puntuacion_crupier))

print("")

#quien ha ganado
if puntuacion > puntuacion_crupier:
    if puntuacion <= 21:
        print("¡HAS GANADO!")
    else:
        #si se pasa de 21 el jugador (único caso posible el 22)
        print("¡HAS PERDIDO!")
elif puntuacion < puntuacion_crupier:
    if puntuacion_crupier <= 21:
        print("¡HAS PERDIDO!")
    else:
        #si se pasa de 21 el crupier (único caso posible el 22)
        print("¡HAS GANADO!")
else:
    print("¡EMPATE! Has obtenido los mismos puntos que el crupier")
