# Guía de decisión · SK12

## Entrada de ejemplo

Hay respuestas lentas. Operaciones pide registrar prompts completos, correos y tokens de acceso para diagnosticar. Las trazas cruzan modelo, retrieval y herramientas; coste parcial. Define observabilidad.

## Qué debe resolver

IDs correlación; redacción/minimización; coste desconocido distinto cero; latencia por etapa; alertas con acción; retención.

## Opciones

- Logs estructurados
- Métricas
- Trazas distribuidas
- Auditoría de efectos
- Alertas
- Muestreo/minimización

## Contrato de salida

operacion.md: métricas/SLO, trazas, redacción, retención, presupuesto y runbooks con responsables.

No todas las opciones deben implementarse. Compara al menos la opción sencilla viable y la alternativa que resolvería su limitación. Declara supuesto, evidencia, coste de cambio y señal para reconsiderar.
