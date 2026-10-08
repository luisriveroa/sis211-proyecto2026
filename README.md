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

- `src/dominio.py`: clase `Pedido`.
- `src/conductor.py`: clase `Conductor`.
- `src/estructuras.py`: implementación de `Cola` y `Pila`.
- `src/sistema_taxis.py`: clase `SistemaTaxis` (usa cola, dict y pila).
- `src/main.py`: programa de demostración.
- `tests/test_limites.py`: pruebas de casos límite.

## Cómo ejecutarlo

Requisitos: Python 3.10 o superior (sin librerías externas).

```bash
git clone https://github.com/luisriveroa/sis211-proyecto2026.git
cd sis211-proyecto2026
python src/main.py
```

## Pruebas

```bash
pip install pytest
python -m pytest tests
```

## Ejemplo de uso

1. Se registran conductores y se crean pedidos.
2. Se asigna el siguiente pedido de la cola a un conductor disponible.
3. Se busca un conductor por código.
4. Se deshace la última asignación (el pedido vuelve al frente de la cola).
