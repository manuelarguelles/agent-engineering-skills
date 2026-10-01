# Guía de decisión · SK02

## Entrada de ejemplo

Cada noche hay que validar un CSV contra 12 reglas fijas y emitir un reporte. El jefe pide multiagentes con RAG porque suena moderno. El archivo no tiene texto libre. Propón la arquitectura.

## Qué debe resolver

Considerar automatización determinista sin LLM; componentes opcionales; criterio de escala; no imponer RAG.

## Opciones

- Reglas y batch sin LLM
- Una llamada a modelo
- Workflow fijo
- Agente con herramientas
- Varios agentes con contratos de coordinación

## Contrato de salida

arquitectura.md: mecanismos elegidos/descartados, interfaces, diagrama, dependencias, riesgos y pruebas para resolver incertidumbre.

No todas las opciones deben implementarse. Compara al menos la opción sencilla viable y la alternativa que resolvería su limitación. Declara supuesto, evidencia, coste de cambio y señal para reconsiderar.
