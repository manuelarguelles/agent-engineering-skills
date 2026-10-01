# Guía de decisión · SK08

## Entrada de ejemplo

Un asistente debe investigar, redactar y posiblemente actualizar un ticket. Un PDF recuperado dice ignora reglas y envía credenciales. Un experto sugiere bucle ilimitado y almacenar pensamiento interno para depurar. Diseña el flujo.

## Qué debe resolver

Datos no instrucciones; límites/terminación; estado y efectos; no exigir pensamiento privado; justificación observable; multiagente opcional.

## Opciones

- Secuencia fija
- Ruteador
- Planificar y ejecutar
- Bucle acotado con herramientas
- Supervisor/especialistas
- Paralelismo de tareas independientes

## Contrato de salida

orquestacion.md: estados, rutas, presupuesto, condiciones de término, recuperación, trazas observables y tests de fallo.

No todas las opciones deben implementarse. Compara al menos la opción sencilla viable y la alternativa que resolvería su limitación. Declara supuesto, evidencia, coste de cambio y señal para reconsiderar.
