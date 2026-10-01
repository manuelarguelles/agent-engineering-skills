# Guía de decisión · SK05

## Entrada de ejemplo

Dos consultas: importe exacto de factura F-9081 en SQL y explicación de una política en documentos. El buscador ya fusiona lexical/vectorial con RRF. Nos proponen aplicar otro RRF y reranking a todo. Decide.

## Qué debe resolver

SQL exacto versus documental; filtros ACL antes de contexto; no doble RRF; reranking solo medido; abstención y citas.

## Opciones

- Sin recuperación externa
- SQL o API exacta
- Búsqueda léxica
- Búsqueda vectorial
- Híbrida con fusión
- Grafo
- Contexto largo directo
- Reranking opcional

## Contrato de salida

recuperacion.md: rutas, chunking si aplica, filtros, ranking, parámetros, conjunto de consultas, métricas y criterio de abstención.

No todas las opciones deben implementarse. Compara al menos la opción sencilla viable y la alternativa que resolvería su limitación. Declara supuesto, evidencia, coste de cambio y señal para reconsiderar.
