# Guía de decisión · SK11

## Entrada de ejemplo

El agente acertó diez ejemplos elegidos durante desarrollo. El mismo autor-modelo actuó como juez. Quieren declarar 100% listo para producción. Define evaluación y conclusión.

## Qué debe resolver

Holdout por tareas/riesgos; denominadores; sesgo juez; errores/latencia/costes; muestra no certifica producción.

## Opciones

- Assertions deterministas
- Muestras con revisión humana
- Juez modelo con rúbrica
- Pruebas de integración
- Holdout por familia/tarea
- Shadow/canary si procede

## Contrato de salida

evaluacion.json: dataset/particiones, rúbrica, baseline, resultados por caso, fallos críticos, decisión y límites.

No todas las opciones deben implementarse. Compara al menos la opción sencilla viable y la alternativa que resolvería su limitación. Declara supuesto, evidencia, coste de cambio y señal para reconsiderar.
