from colorama import init, Fore, Back
from motor import GranOca
from sound import Sonido
from time import sleep

ohNo = Sonido("sounds/ohNo.ogg")
posada = Sonido("sounds/posada.ogg")
up = Sonido("sounds/up.ogg")
jail = Sonido("sounds/jail.ogg")
labyrinth = Sonido("sounds/labyrinth.ogg")
bridge = Sonido("sounds/bridge.ogg")

init()
print(Fore.GREEN+Back.WHITE)

class Calavera():
	def aplicar(self,jugador):
		jugador.posicion = 0
		ohNo.reproducir()
		sleep(0.5)
		print("¡Calavera!")
		sleep(0.3)
		print("Al comienzo otra vez...")
		sleep(1)

class Puente():
	def aplicar(self,jugador):
		bridge.reproducir()
		print("¡Puente!")
		sleep(0.5)
		Posada().aplicar(jugador)

class Posada():
	def aplicar(self,jugador):
		posada.reproducir()
		print("Bienvenido a la posada. Es hora de descansar. Pierdes un turno")
		jugador.posicion = 19
		jugador.restarTurno()

class Carcel():
	def aplicar(self,jugador):
		jail.reproducir()
		sleep(0.5)
		print("¡Cárcel!")
		sleep(0.8)
		print("pierdes 2 turnos...")
		sleep(0.5)
		jugador.posicion = jugador.posicion + jugador.lastRun
		jugador.restarTurno()
		jugador.restarTurno()

class Laberinto():
	def aplicar(self,jugador):
		jugador.posicion = 30
		labyrinth.reproducir()
		sleep(0.5)
		print("¡Laberinto!")
		sleep(0.3)
		print("Del laberinto al 30...")

class Oca():
	def __init__(self,dados=0):
		self.ocas = [5,9,14,18,23,27,32,36,41,45,50,54,59]

	def aplicar(self,jugador):
		if jugador.posicion + jugador.lastRun >59:
			posicion = GranOca().casillaFinal - (jugador.posicion + jugador.lastRun - GranOca().casillaFinal)
		else:
			posicion = jugador.posicion + jugador.lastRun
			index = self.ocas.index(posicion)
			jugador.posicion = self.ocas[index + 1]
			up.reproducir()
			sleep(0.5)
			print("De Oca a Oca y tiro porque me toca. Vuelve a tirar...")
			sleep(0.3)
			jugador.darTurno()