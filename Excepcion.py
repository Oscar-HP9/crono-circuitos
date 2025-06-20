class CircuitosNombresIguales(Exception):
    def __init__(self):
        super().__init__("Ya existe un circuito con este nombre")