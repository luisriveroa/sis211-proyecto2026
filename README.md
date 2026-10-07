# SIS-211 Proyecto 2026 — v1

## Estudiante
- **Nombre:** Luis Fabricio Rivero Aban
- **Usuario GitHub:** luisriveroa

## Dominio
Sistema básico de taxis / delivery: recepción de pedidos, asignación a
conductores y deshacer la última asignación.

## Repo
https://github.com/luisriveroa/sis211-proyecto2026

## Mapa de estructuras (v1)

| Flujo (proceso del sistema) | Familia (estructura) | ¿Por qué encaja? |
|-----------------------------|----------------------|------------------|
| El siguiente pedido a asignar | Cola | Los pedidos se atienden en el orden en que llegaron (FIFO): entran al final y sale el más antiguo. |
| Conductor por código | Tabla hash (dict) | Necesito encontrarlo directo por su código, sin recorrer todo. |
| Deshacer la última asignación | Pila | La última asignación hecha es la primera que se revierte (LIFO). |

## Estructura del código
- `src/dominio.py` — clase `Pedido`
- `src/conductor.py` — clase `Conductor`
- `src/estructuras.py` — clases `Cola` (FIFO) y `Pila` (LIFO)
- `src/sistema_taxis.py` — `SistemaTaxis`: cola de pedidos pendientes, dict de
  conductores por código y pila de asignaciones
- `src/main.py` — demostración de uso (ejecutar desde `src/`: `python main.py`)

Al deshacer una asignación, el pedido vuelve al frente de la cola, porque era el
más antiguo cuando se asignó y así se mantiene el orden FIFO.