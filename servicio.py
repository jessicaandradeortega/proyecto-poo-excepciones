from abc import ABC, abstractmethod

class Servicio(ABC):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def calcular_costo(self, tiempo):
        pass


class ReservaSala(Servicio):
    def calcular_costo(self, tiempo):
        return self.precio * tiempo * 1.2


class AlquilerEquipo(Servicio):
    def calcular_costo(self, tiempo):
        return self.precio * tiempo * 1.5


class Asesoria(Servicio):
    def calcular_costo(self, tiempo):
        return self.precio * tiempo * 2
