# Guía de decisión · SK04

## Entrada de ejemplo

Un asistente conversa con dos empresas distintas. Piden guardar todo para siempre y usar conversaciones antiguas como hechos actuales. Diseña datos y memoria.

## Qué debe resolver

Aislamiento por tenant; memoria no autoridad; retención/borrado; vigencia/procedencia; evitar persistencia innecesaria.

## Opciones

- SQL/tablas
- Documentos/objetos
- Índice de búsqueda
- Grafo cuando las relaciones lo justifiquen
- Estado efímero
- Memoria persistente selectiva
- Sin memoria entre sesiones

## Contrato de salida

datos-memoria.md: esquemas, claves, calidad, políticas de acceso/retención, memoria habilitada y pruebas de aislamiento y borrado.

No todas las opciones deben implementarse. Compara al menos la opción sencilla viable y la alternativa que resolvería su limitación. Declara supuesto, evidencia, coste de cambio y señal para reconsiderar.
