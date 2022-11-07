from colorama import init, Fore, Back
from motor import GranOca
from sound import Sonido
from time import sleep
oca = GranOca()
from casillas import *
Ocas = Oca()

start = Sonido("sounds/start.ogg")
silvato = Sonido("sounds/silvato.ogg")
winner = Sonido("sounds/winner.ogg")
background = Sonido("sounds/background.ogg")

start.reproducir()
# construir el tablero y definir las casillas
oca.definirAccion(58,Calavera())
oca.definirAccion(6,Puente())
oca.definirAccion(12,Puente())
oca.definirAccion(19,Posada())
oca.definirAccion(42,Laberinto())
oca.definirAccion(56,Carcel())
oca.definirAccion(5,Oca())
oca.definirAccion(9,Oca())
oca.definirAccion(14,Oca())
oca.definirAccion(18,Oca())
oca.definirAccion(23,Oca())
oca.definirAccion(27,Oca())
oca.definirAccion(32,Oca())
oca.definirAccion(36,Oca())
oca.definirAccion(41,Oca())
oca.definirAccion(45,Oca())
oca.definirAccion(50,Oca())
oca.definirAccion(54,Oca())

sleep(7)

init()

print(Fore.BLUE+Back.WHITE+"¿Cuántos jugadores van a participar?")
try:
	cantidad = int(input())
except ValueError:
	print("debes ingresar un valor numérico. Cerrando el juego...")
	sleep(2.5)
	exit()

for x in range(cantidad):
	nombre = input("escriba el nombre del jugador "+str(x+1))
	oca.agregarJugador(nombre, 0, 0)

oca.desordenarLista()

silvato.reproducir()
sleep(1)
print("Hay {} participantes en el juego.".format(oca.cantidadDeJugadores()))
input("pulsa énter para iniciar la partida")

background.reproducir(continuo=True)

while oca.esJuegoActivo():
	oca.iniciarRonda()

background.detener()
winner.reproducir()
sleep(4)
print("¿Gran oca!")
sleep(3)
print("¡Felicidades {nombre}! Has ganado el juego.".format(nombre=oca.nombreGanador()))
sleep(2)
print("gracias por jugar")
sleep(2)
