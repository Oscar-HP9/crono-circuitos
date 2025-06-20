class Vehiculo:

    def __init__(self, nombre, traccion, neumatico):

        self.nombre = nombre
        self.traccion = traccion
        self.neumatico = neumatico

    def __str__(self):
        return f"NOMBRE VEHICULO: {self.nombre}\tTRACCION: {self.traccion}\tNEUMATICO: {self.neumatico}"
    
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "traccion": self.traccion,
            "neumatico": self.neumatico,
            "tipo": self.__class__.__name__  # "Coche" o "Moto"
        }

    @classmethod
    def from_dict(cls, data):
        if data["tipo"] == "Coche":
            return Coche(data["nombre"], data["traccion"], data["neumatico"])
        elif data["tipo"] == "Moto":
            return Moto(data["nombre"], data["neumatico"])

class Coche(Vehiculo):
    def __init__(self, nombre, traccion , neumatico):
        super().__init__(nombre, traccion, neumatico)
        self.tipo = "COCHE"

    def __str__(self):
        return super().__str__() + f"\n\tTIPO: {self.tipo}"
    
class Moto(Vehiculo):
    def __init__(self, nombre, neumatico):
        super().__init__(nombre, "RWD", neumatico)
        self.tipo = "MOTO"

    def __str__(self):
        return super().__str__() + f"\n\tTIPO: {self.tipo}"
