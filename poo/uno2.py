"""
Generate the uno deck of 108 cards.
Parameters: None
Return values: deck -> list

https://www.youtube.com/watch?v=7BXDcBfk-04
"""
def buildDeck():
    deck = []
    colores = ["Rojo", "Verde", "Amarillo", "Azul"]
    values = [0,1,2,3,4,5,6,7,8,9,"Roba dos", "Pasar", "Reversa"]
    wilds = ["Wild", "Wild Draw Four"]
    for color in colores:
        for value in values:
            cartaValor = "{} {}".format(color, value)
            deck.append(cartaValor)
            if value != 0:
                deck.append(cartaValor)

    for i in range(4):
        deck.append(wilds[0])
        deck.append(wilds[1])

    print(deck)
    return deck

buildDeck()