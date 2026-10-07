from estructuras import Cola, Pila
from dominio import Pedido
from conductor import Conductor


class SistemaTaxis:
    """
    Tres familias, cada una en un flujo real:
      - Cola (FIFO): pedidos pendientes, se asigna el más antiguo.
      - Tabla hash (dict): conductores por código, búsqueda directa.
      - Pila (LIFO): asignaciones hechas, se deshace la más reciente.
    """

    def __init__(self):
        self.pedidos_pendientes = Cola()
        self.conductores = {}            # código -> Conductor
        self.asignaciones = Pila()       # (pedido, conductor)

    # --- conductores (tabla hash) ---
    def registrar_conductor(self, codigo, nombre):
        if codigo in self.conductores:
            raise ValueError(f"Ya existe el conductor {codigo}")
        self.conductores[codigo] = Conductor(codigo, nombre)

    def buscar_conductor(self, codigo):
        return self.conductores.get(codigo)

    # --- pedidos (cola) ---
    def recibir_pedido(self, id_pedido, cliente, origen, destino):
        pedido = Pedido(id_pedido, cliente, origen, destino)
        self.pedidos_pendientes.encolar(pedido)
        return pedido

    def asignar_siguiente(self, codigo_conductor):
        conductor = self.buscar_conductor(codigo_conductor)
        if conductor is None:
            raise KeyError(f"No existe el conductor {codigo_conductor}")
        if not conductor.disponible:
            raise ValueError(f"El conductor {codigo_conductor} está ocupado")
        if self.pedidos_pendientes.esta_vacia():
            raise IndexError("No hay pedidos pendientes")

        pedido = self.pedidos_pendientes.desencolar()
        pedido.estado = "asignado"
        conductor.disponible = False
        self.asignaciones.apilar((pedido, conductor))
        return pedido, conductor

    # --- deshacer (pila) ---
    def deshacer_ultima_asignacion(self):
        if self.asignaciones.esta_vacia():
            raise IndexError("No hay asignaciones para deshacer")
        pedido, conductor = self.asignaciones.desapilar()
        pedido.estado = "pendiente"
        conductor.disponible = True
        # era el más antiguo cuando se asignó: vuelve al frente de la cola
        self.pedidos_pendientes.encolar_al_frente(pedido)
        return pedido, conductor
