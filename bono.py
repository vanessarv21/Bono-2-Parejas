class Cliente:
    def __init__(self, nombre, apellido, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.activo = True
        
    def __str__(self):
        estado = "ACTIVO" if self.activo else "INACTIVO"
        return f"{self.nombre} {self.apellido} - Tel: {self.telefono} - Estado: {estado}"

class Nodo:
    def __init__(self, cliente):
        self.cliente = cliente
        self.anterior = None
        self.siguiente = None


class ListaDobleClientes:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamano = 0
        