class ErrorSistema(Exception):
    pass

class ClienteInvalido(ErrorSistema):
    pass

class CorreoInvalido(ErrorSistema):
    pass

class ServicioNoDisponible(ErrorSistema):
    pass

class DuracionInvalida(ErrorSistema):
    pass

class ReservaError(ErrorSistema):
    passraduc
