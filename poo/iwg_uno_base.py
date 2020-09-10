class Carta:
    ' Una carta tiene un valor entre 1 y 10, y un
    ' color (rojo, amarillo, azul o verde)
    def __init__(self, valor, color):
        self.__valor = valor
        self.__color = color
        
    ' Retorna una tupla con los datos de la
    ' carta (valor, color)
    def obtener_datos(self):
        return (self.__valor,self.__color)
        
class Jugador:
    'COMPLETAR: ademas del nombre, debe recibir una lista de 7 cartas e
    ' inicializar el atributo mano con esa lista. El atributo mano debe
    ' ser privado
    def __init__(self, nombre):
        self.__nombre = nombre

    ' Retorna el nombre del jugador
    def obtener_nombre(self):
        return self.__nombre

    ' Retorna una lista de tuplas (valor, color) de las cartas en la mano
    def mostrar_mano(self):
        cartas = []
        for c in self.__mano:
            cartas.append(c.obtener_datos())
        return cartas

    'COMPLETAR: Sacar de la mano la carta en posicion_carta, y retornarla.
    ' Antes, verificar que hay cartas en la mano y que posicion_carta es valida
    ' En caso contrario, retornar None
    def jugar_carta(self, posicion_carta):
        return None
        
    'Agrega una carta a la mano
    def tomar_carta(self, carta):
        self.__mano.append(carta)
        return True
    
    'COMPLETAR: Debe sumar el valor de las cartas en la mano
    ' y retornar la suma total
    def puntaje_actual(self):
        return 0

######### PROGRAMA PRINCIPAL ######
'IMPLEMENTE AQUI LA LOGICA DEL JUEGO UNO

'Crear dos jugadores, con sus respectivas manos de 7 cartas
' (recuerde los valores y colores validos para las cartas en este juego)
'Crear un mazo como una lista de 10 cartas
'La primera carta del mazo pasa a ser el pozo de descarte

'Ciclo principal del juego
'Repetir mientras haya cartas en el pozo o bien no hay ganador/a
    'Imprimir la carta que esta encima en el pozo
    'Imprimir el nombre de la persona que le toca jugar
    'Preguntar si desea tomar una carta del mazo o botar una carta de su mano
        'Si desea tomar la carta del mazo, sacar la carta del mazo y agregarla a la mano del jugador/a
            'Si la nueva carta cumple con las reglas, botarla al pozo
        
        'Si desea botar una carta
            'Preguntar la carta que desea botar y chequear si cumple las reglas
                'Si cumple las reglas, sacar la carta de la mano y ponerla encima del pozo
                'Si no cumple, pierde el turno
                
    'Chequear si hay ganador/a o si el pozo está vacio
        'Si hay ganador, mostrar un mensaje y terminar el juego
        'Si el pozo está vacío, chequear quien tiene menor puntaje y mostrar un mensaje indicandolo Mostrar un mensaje

