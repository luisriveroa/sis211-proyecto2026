# SIS-211 Proyecto 2026 — v1

## Estudiante
- **Nombre:** Luis Fabricio Rivero Aban 
- **Usuario GitHub:** luisriveroa

## Dominio
Sistema básico de gestión de taxis/deliverys: registro de viajes,
asignación de vehículos y control de acciones (deshacer).

## Repo
https://github.com/luisriveroa/sis211-proyecto2026

## Mapa de estructuras (v1)

| Flujo (proceso del sistema)        | Familia (estructura)         | ¿Por qué encaja? |
|------------------------------------|------------------------------|------------------|
| Historial de viajes/pedidos        | Lista enlazada               | Los viajes se registran uno tras otro y se recorren en orden; cada nodo es un viaje con cliente, origen, destino y monto. |
| Deshacer última acción (cancelar asignación) | Pila (stack)         | LIFO: la última acción realizada es la primera en revertirse, sin recorrer todo el historial. |
| Catálogo/flota de vehículos disponibles | Lista doblemente enlazada | Se recorre en ambos sentidos al buscar, reasignar o dar de baja un vehículo. |

## Estructura del código
- `src/` — clases del dominio (Viaje, Nodo, Historial, PilaAcciones, Flota)
- `tests/` — pruebas de cada estructura (caso vacío, agregar, recorrer, deshacer)