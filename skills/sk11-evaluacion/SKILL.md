---
name: sk11-evaluacion
description: "Diseñar o ejecutar evaluación del agente y sus variantes con tareas, riesgos, baseline, holdout, métricas de calidad, latencia y coste. Usar en diseño o revisión del sistema, no para atender una consulta cotidiana."
metadata:
  version: "0.1.1"
  status: "provisional"
---

# SK11 · Evaluar y comparar el agente

## Contrato

Entrada: Caso, criterios de aceptación, población de tareas, candidato versionado y presupuesto de pruebas.
Salida: evaluacion.json: dataset/particiones, rúbrica, baseline, resultados por caso, fallos críticos, decisión y límites.
Estado: provisional. Una revisión de texto o un test local no prueba el componente desplegado.

## Decisiones disponibles

- Assertions deterministas
- Muestras con revisión humana
- Juez modelo con rúbrica
- Pruebas de integración
- Holdout por familia/tarea
- Shadow/canary si procede

## Procedimiento

1. Diseña la evaluación antes de optimizar: particiones de ajuste y holdout, casos positivos/negativos/límite y presión por urgencia.
2. Compara baseline y candidato con entradas equivalentes. Conserva salida bruta, versión, configuración, errores, latencia y coste; desconocido es null, no cero.
3. Usa assertions de contrato junto a juicio de calidad; controla sesgo del autor/juez, calibración y desacuerdos.
4. Reporta denominadores, resultados por segmento y límites de la muestra; una media no tapa fallos críticos.
5. Separa aprobado para una demo, calidad del componente, evaluación de la skill y listo para producción. No generes un PASS por solo validar archivos.

## Ejecución y evidencia

Entrega primero la decisión y sus razones verificables; si la tarea autoriza construir, implementa el componente y ejecuta las pruebas correspondientes. Si solo pide análisis, no despliegues por inferencia. Registra versión de skill, entradas/fuentes, opciones consideradas, elección, artefactos, checks y siguiente paso. Usa `no_aplica` con motivo cuando esta capacidad no sea necesaria.

Conserva lo desconocido explícito. Reutiliza autorizaciones existentes dentro de su alcance; pregunta solo por el dato o efecto realmente pendiente. No presupongas proveedores, corpus, cuentas, modelos ni presupuesto.

## Riesgos y salida de esta etapa

Sobreajuste; juez complaciente; métricas sin denominador; muestra pequeña presentada como garantía.

Avanza cuando el contrato esté satisfecho o el pendiente tenga impacto y siguiente acción explícitos. `bloqueado` detiene la rama dependiente, no todo el proyecto. Documentar el plan no equivale a ejecutarlo.

## Referencias y evaluación

- [Opciones y criterios](references/decision-guide.md).
- [Research brief y límites](references/research-brief.md).
- [Requisitos y riesgos](references/requirements-risks.md).
- [Casos de evaluación](evals/cases.json).
