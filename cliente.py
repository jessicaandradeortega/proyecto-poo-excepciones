from excepciones import ClienteInvalido, CorreoInvalido

class Cliente:
    def __init__(self, nombre, correo):
        if not nombre.strip():
            raise ClienteInvalido("Nombre vacío")

        if "@" not in correo:
            raise CorreoInvalido("Correo inválido")

        self.__nombre = nombre
        self.__correo = correo

    def get_nombre(self):
        return self.__nombre
