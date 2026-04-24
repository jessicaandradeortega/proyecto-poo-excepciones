from excepciones import *

class Reserva:
    def __init__(self, cliente, servicio, tiempo):
        if tiempo <= 0:
            raise DuracionInvalida("Tiempo inválido")

        self.cliente = cliente
        self.servicio = servicio
        self.tiempo = tiempo

    def procesar(self):
        try:
            costo = self.servicio.calcular_costo(self.tiempo)
            return costo
        except Exception as e:
            raise ReservaError("Error en reserva") from e
