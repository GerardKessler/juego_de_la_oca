from colorama import init, Fore, Back
from random import randint
from random import sample
from time import sleep
from sound import Sonido

dado = Sonido("sounds/dado.ogg")
init()
print(Fore.RED+Back.WHITE)

class Jugador():
	def __init__(self, nombre, posicion,lastRun):
		self.nombre = nombre
		self.posicion = posicion
		self.turno = 0
		self.lastRun = lastRun

	def darTurno(self):
		self.turno+=1

	def restarTurno(self):
		self.turno-=1

	def tieneTurno(self):
		return self.turno > 0

class GranOca():
	def __init__(self):
		self.jugadores = []
		self.activo = True
		self.ganador  = None
		self.casillaFinal = 63
		self.tablero = {}
		self.esElTurnoDe = ""
		self.apuntador = 0
		self.ronda = 0
		
	def definirAccion(self,casilla,accion):
		self.tablero[casilla] = accion

	def esJuegoActivo(self):
		return self.activo
		self.ronda = 0

	def nombreGanador(self):
		return self.ganador.nombre

	def agregarJugador(self, nombre, posicion, lastRun):
		jugador = Jugador(nombre, posicion, lastRun)
		self.jugadores.append(jugador)

	def cantidadDeJugadores(self):
		return len(self.jugadores)

	def desordenarLista(self):
		self.jugadores = sample(self.jugadores,len(self.jugadores))

	def iniciarRonda(self):
		while self.activo:
			if self.apuntador == 0:
				self.ronda+=1
				print("Ronda {}".format(self.ronda))
				sleep(0.8)
			jugador = self.obtenerJugador()
			self.activarTurno(jugador)

	def activarTurno(self,jugador):
		jugador.darTurno()
		if jugador.turno < 1:
			print("Salteando a {}... ¡Que pase el que sigue!".format(jugador.nombre))
			sleep(0.5)
		while jugador.tieneTurno():
			print("es el turno de {}.".format(jugador.nombre))
			self.esElTurnoDe = jugador.nombre
			conmutador = input()
			if conmutador == "s":
				print("Saliendo del juego...")
				sleep(0.5)
				print("Gracias por jugar")
				sleep(2)
				exit()
			elif conmutador == "p":
				self.puntaje(jugador)
			else:
				num = self.lanzarDados()
				jugador.lastRun = num
				print("; {}.".format(num))
				sleep(0.5)
				self.avanzarJugador(jugador,num)
				self.verificarSiGano(jugador)
				print("Casilla {}.".format(jugador.posicion))
				jugador.restarTurno()

	def puntaje(self,jugador):
		for jugador in self.jugadores:
			print("{}, {}".format(jugador.nombre,jugador.posicion))
			sleep(0.5)
		sleep(0.3)

	def verificarSiGano(self, jugador):
		if jugador.posicion == self.casillaFinal:
			self.activo = False
			self.ganador = jugador

	def avanzarJugador(self, jugador, x):
		if (jugador.posicion + x) <= self.casillaFinal:
			posicion = jugador.posicion + x
		else:
			posicion = self.casillaFinal - (jugador.posicion + x - self.casillaFinal)
		try:
			self.tablero[posicion].aplicar(jugador)
		except KeyError:
			jugador.posicion = posicion

	def lanzarDados(self):
		dado.reproducir()
		sleep(1)
		result = randint(1,6)
		return result
	
	def obtenerJugador(self):
		self.apuntador = (self.apuntador + 1) % len(self.jugadores)
		return self.jugadores[self.apuntador]
