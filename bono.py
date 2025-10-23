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


class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamano = 0

    def esta_vacia(self):
        return self.cabeza is None
    
    def agregar_cliente(self, cliente):
        nuevo_nodo = Nodo(cliente)
        
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo
        
        self.tamano += 1
        print(f"\nCliente '{cliente.nombre} {cliente.apellido}' registrado exitosamente.")
    
    def listar_clientes(self):
        if self.esta_vacia():
            print("\nNo hay clientes registrados en el sistema.")
            return
        
        print("\n" + "="*70)
        print("LISTADO DE CLIENTES".center(70))
        print("="*70)
        
        actual = self.cabeza
        contador = 1
        
        while actual is not None:
            print(f"{contador}. {actual.cliente}")
            actual = actual.siguiente
            contador += 1
        
        print("="*70)
        print(f"Total de clientes: {self.tamano}")
    
    def eliminar_cliente_logico(self):
        if self.esta_vacia():
            print("\nNo hay clientes registrados en el sistema.")
            return
        
        print("\n" + "="*70)
        print("CLIENTES ACTIVOS".center(70))
        print("="*70)
        
        actual = self.cabeza
        clientes_activos = []
        contador = 1
        
        while actual is not None:
            if actual.cliente.activo:
                print(f"{contador}. {actual.cliente}")
                clientes_activos.append(actual)
                contador += 1
            actual = actual.siguiente
        
        if not clientes_activos:
            print("\nNo hay clientes activos para eliminar.")
            return
        
        print("="*70)
        
        try:
            opcion = int(input("\nIngrese el número del cliente a eliminar (0 para cancelar): "))
            
            if opcion == 0:
                print("\nOperación cancelada.")
                return
            
            if 1 <= opcion <= len(clientes_activos):
                nodo_eliminar = clientes_activos[opcion - 1]
                nodo_eliminar.cliente.activo = False
                print(f"\nCliente '{nodo_eliminar.cliente.nombre} {nodo_eliminar.cliente.apellido}' marcado como INACTIVO.")
            else:
                print("\nOpción inválida.")
        except ValueError:
            print("\nPor favor ingrese un número válido.")
