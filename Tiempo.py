class Tiempo:
    def __init__(self, minutos, segundos, fraciones_segundo):
        self.minutos = minutos
        self.segundos = segundos
        self.fracciones_segundo = fraciones_segundo
        self.tiempo = self.minutos * 60 + self.segundos + self.fracciones_segundo

    def __str__(self):
        return f"{self.minutos}:{self.segundos + self.fracciones_segundo}"
    
    def to_dict(self):
        return {
            "minutos": self.minutos,
            "segundos": self.segundos,
            "fracciones_segundo": self.fracciones_segundo
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["minutos"], data["segundos"], data["fracciones_segundo"])