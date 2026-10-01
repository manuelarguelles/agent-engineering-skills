# Guía de decisión · SK14

## Entrada de ejemplo

Una skill parece mejor en los mismos tres casos usados para escribirla. Queremos reemplazar todas las skills y defaults de proveedor automáticamente esta noche. Propón mejora controlada.

## Qué debe resolver

Baseline emparejado y casos nuevos; alcance de cambio; versiones; regresiones; evidencias separadas skill/componente; no universalizar proveedor.

## Opciones

- Corrección del componente
- Refinamiento de la skill
- Cambio de datos
- Cambio de configuración
- No cambiar si falta evidencia

## Contrato de salida

mejora.md: fallo→causa→cambio→prueba, baseline/candidato, holdout, regresiones, versión y decisión de promoción.

No todas las opciones deben implementarse. Compara al menos la opción sencilla viable y la alternativa que resolvería su limitación. Declara supuesto, evidencia, coste de cambio y señal para reconsiderar.
