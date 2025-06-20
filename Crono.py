from Vehiculo import Vehiculo
from Tiempo import Tiempo

class Crono:
    #COMPOSICION DE LOS OBJETOS TIEMPO Y SUBCLASE DE VEHICULO (Moto o Coche)
    numero_crono = 0
    def __init__(self, vehiculo, tiempo):
        Crono.numero_crono += 1
        self.vehiculo = vehiculo
        self.tiempo = tiempo
        self.id_crono = str(Crono.numero_crono)

    def __str__(self):
        return f"ID: {self.id_crono}\n\tTIEMPO: {self.tiempo}\n\t{self.vehiculo}"
    
    def to_dict(self):
        return {
            "id_crono": self.id_crono,
            "vehiculo": self.vehiculo.to_dict(),
            "tiempo": self.tiempo.to_dict()
        }

    @classmethod
    def from_dict(cls, data):
        vehiculo = Vehiculo.from_dict(data["vehiculo"])
        tiempo = Tiempo.from_dict(data["tiempo"])
        obj = cls(vehiculo, tiempo)
        obj.id_crono = data["id_crono"]  # restauramos el ID

        id_num = int(obj.id_crono)
        if id_num > cls.numero_crono:
            cls.numero_crono = id_num
            
        return obj