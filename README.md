# Sistema básico de taxis / delivery

**Autor:** Luis Fabricio Rivero Aban
**Materia:** SIS211 · Proyecto V1 (Unidad 2)

## Descripción

Sistema simple que recibe pedidos de clientes, los asigna a conductores
disponibles y permite deshacer la última asignación.

## Estructuras de datos usadas

| Flujo del dominio | Familia | La uso porque... |
| --- | --- | --- |
| El siguiente pedido a asignar | Cola | los pedidos se atienden en el orden en que llegaron (FIFO). |
| Conductor o cliente por código | Tabla hash (`dict`) | necesito encontrarlo directo por su código, sin recorrer todo. |
| Deshacer la última asignación | Pila | la última asignación hecha es la primera que se revierte (LIFO). |

## Estructura del repositorio

- `pedido.py`: clase `Pedido`.
- `conductor.py`: clase `Conductor`.
- `sistema_taxis.py`: clase `SistemaTaxis` (cola, dict y pila).
- `main.py`: programa de demostración.

## Cómo ejecutarlo

Requisitos: Python 3.10 o superior (no usa librerías externas).

```bash
git clone https://github.com/luisriveroa/sis211-proyecto2026.git
cd NOMBRE-PROYECTO
python main.py
```

## Ejemplo de uso

1. Se registran conductores y se crean pedidos.
2. Se asigna el siguiente pedido de la cola a un conductor disponible.
3. Se busca un conductor o cliente por código.
4. Se deshace la última asignación (el pedido vuelve a la cola).