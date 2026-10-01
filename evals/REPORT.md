# Evaluación 0.1.1 — provisional

## Qué se ejecutó

- 15 casos de diseño con presión sin skill y los mismos 15 con skill (procedimientos 0.1.0).
- Revisión independiente de 78 criterios con evidencia textual: baseline 67 PASS, 8 PARTIAL, 3 FAIL por omisión; con skill 77 PASS y 1 PARTIAL.
- Revisión de activación sobre catálogo y casos; se detectaron descripciones poco diferenciadas y negativos demasiado fáciles. La versión 0.1.1 precisa las descripciones y añade 30 casos de frontera, conservando el procedimiento.
- Tres diseños nuevos de generalización: voz offline, monitor por eventos sin LLM y planificación de rutas físicas. Revisión favorable con límites del dominio; no se desplegaron sistemas.
- Validación de estructura, enlaces directos de skills, contratos JSON y cuatro pruebas del generador local (incluyen no sobrescribir ni conceder autorización).

## Qué significa y qué no

El conteo refleja la cobertura juzgada de estas respuestas, no exactitud de agentes desplegados ni una garantía estadística. Una repetición por caso, contexto compartido en grupos de cinco y mismo entorno de modelo limitan la independencia. Los jueces son IA y no hubo revisión humana del dominio. Tokens, coste y latencia exacta: no disponibles, null.

Los baselines fueron competentes. El juez encontró omisiones retrospectivamente; no se fabricó un fallo RED para justificar instrucciones. Las diferencias observadas no establecen causalidad. La revisión de activación por texto no certifica el router de un producto ni la instalación automática.

Cada skill conserva casos, results.json, benchmark.json y creator-record.json. Las salidas brutas y revisiones se mantienen en este directorio. No se borran los hallazgos que originaron el refinamiento.

## Evidencia

- [Comportamiento](reviews/behavior.json).
- [Activación inicial](reviews/triggering.json).
- [Generalización y permisos](reviews/safety-generalization.json).
- [Activación refinada](reviews/triggering-refined.json): 30/30 acuerdos de selección por juez textual, no router de producto.

La entrega es un framework de construcción provisional. No es un runtime universal ni una certificación de producción.

## Refinamiento posterior

SK03 0.1.2 añade comprobación explícita de permisos de fuente y destino, motivada por el único criterio PARTIAL de las respuestas con skill. Se conserva la evaluación previa y se registran por separado el reensayo y un caso nuevo.

Resultado del reensayo SK03: 5/5 criterios completos en el caso repetido. Caso nuevo: 3 PASS y 1 PARTIAL porque la respuesta no explicita conservar eventos originales, aunque preserva tombstone y evita resurrección. Se mantiene esta limitación; no se declara cobertura perfecta. [Revisión del refinamiento](reviews/ingestion-refined.json).
