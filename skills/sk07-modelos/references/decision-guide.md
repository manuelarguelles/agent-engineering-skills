# Guía de decisión · SK07

## Entrada de ejemplo

Hay imágenes y texto sensible. Exigimos residencia de datos, latencia p95 menor de dos segundos y bajo coste. Nadie midió los candidatos. El modelo de mayor benchmark general es favorito. Selecciona estrategia.

## Qué debe resolver

No afirmar ganador sin medición; capacidades/modalidad; residencia; p95 real; muestras y coste; fallback seguro.

## Opciones

- Sin modelo
- Modelo local
- Servicio gestionado
- Modelo multimodal
- Clasificador especializado
- Ruteo entre modelos
- Fallback compatible

## Contrato de salida

modelos.md y configuracion.example.json: requisitos, candidatos, mediciones o pendientes, decisión, versiones y fallback.

No todas las opciones deben implementarse. Compara al menos la opción sencilla viable y la alternativa que resolvería su limitación. Declara supuesto, evidencia, coste de cambio y señal para reconsiderar.
