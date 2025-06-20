from Crono import Crono
class Circuito:
    contador_circuito = 0
    def __init__(self, nombre, curvas, distancia, ubicacion):
        Circuito.contador_circuito += 1
        self.nombre = nombre
        self.curvas = curvas
        self.distancia = distancia
        self.ubicacion = ubicacion
        self.id_circuito = str(Circuito.contador_circuito)
        self.cronos = {}

    def __str__(self):
        cadena = f"\tID: {self.id_circuito}\n\tNOMBRE DEL CIRCUITO: {self.nombre}\n\tCURVAS: {self.curvas}\n\tDISTANCIA: {self.distancia}\n\tUBICACION: {self.ubicacion}"
        if not self.cronos:
            cadena += "\n\tNO HAY CRONOS EN ESTE CIRCUITO"
        else:
            for crono in self.cronos.values():
                cadena += "\n------------------------------------------------------------\n"f"\n\t{crono}"
        return cadena
    
    def añadir_crono(self, crono):
        self.cronos[crono.id_crono] = crono

    def to_dict(self):
        return {
            "id_circuito": self.id_circuito,
            "nombre": self.nombre,
            "curvas": self.curvas,
            "distancia": self.distancia,
            "ubicacion": self.ubicacion,
            "cronos": {k: v.to_dict() for k, v in self.cronos.items()}
        }

    @classmethod
    def from_dict(cls, data):
        circuito = cls(
            data["nombre"],
            data["curvas"],
            data["distancia"],
            data["ubicacion"]
        )
        circuito.id_circuito = data["id_circuito"]
        circuito.cronos = {k: Crono.from_dict(v) for k, v in data["cronos"].items()}

        id_num = int(circuito.id_circuito)
        if id_num > cls.contador_circuito:
            cls.contador_circuito = id_num
            
        return circuito
