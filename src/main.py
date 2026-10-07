from sistema_taxis import SistemaTaxis
 
s = SistemaTaxis()
s.registrar_conductor("C1", "Ana")
s.registrar_conductor("C2", "Luis")
 
s.recibir_pedido(1, "Marta", "Plaza 25 de Mayo", "Terminal")
s.recibir_pedido(2, "Jorge", "Mercado", "Hospital")
s.recibir_pedido(3, "Rosa", "Universidad", "Aeropuerto")
 
print("Buscar C2:", s.buscar_conductor("C2"))
 
print("\n-- Asignaciones (sale el pedido más antiguo) --")
print(s.asignar_siguiente("C1"))
print(s.asignar_siguiente("C2"))
 
print("\n-- El operador se equivocó: deshacer la más reciente --")
pedido, conductor = s.deshacer_ultima_asignacion()
print("Revertido:", pedido, "|", conductor)
 
print("\n-- Pendientes ahora (el pedido 2 vuelve al frente) --")
for p in s.pedidos_pendientes:
    print(p)
 