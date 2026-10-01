---
name: sk01-caso-y-valor
description: "Definir usuarios, problema, tareas, alcance, métricas de éxito y valor esperado antes de elegir mecanismos del agente. Usar en diseño o revisión del sistema, no para atender una consulta cotidiana."
metadata:
  version: "0.1.1"
  status: "provisional"
---

# SK01 · Definir el caso y las decisiones

## Contrato

Entrada: Necesidad del usuario, procesos afectados, usuarios y evidencia de la situación actual.
Salida: caso.md y decisiones.json: problema, usuarios, tareas, baseline, objetivos, límites, criterios de éxito y 12 decisiones.
Estado: provisional. Una revisión de texto o un test local no prueba el componente desplegado.

## Decisiones disponibles

- Asistencia informativa
- Análisis de datos
- Generación de contenido
- Acciones transaccionales
- Automatización determinista sin agente

## Procedimiento

1. Describe actor, tarea, disparador, entrada, resultado y error costoso con ejemplos reales o etiquetados como ficticios.
2. Define alcance y exclusiones; identifica propietario del resultado y cómo se medirá valor contra el proceso actual.
3. Completa las doce decisiones del framework o marca pendiente con impacto y responsable. No conviertas ROI deseado en resultado medido.
4. Propón una primera unidad de trabajo pequeña y pruebas de aceptación observables antes de elegir stack.

## Ejecución y evidencia

Entrega primero la decisión y sus razones verificables; si la tarea autoriza construir, implementa el componente y ejecuta las pruebas correspondientes. Si solo pide análisis, no despliegues por inferencia. Registra versión de skill, entradas/fuentes, opciones consideradas, elección, artefactos, checks y siguiente paso. Usa `no_aplica` con motivo cuando esta capacidad no sea necesaria.

Conserva lo desconocido explícito. Reutiliza autorizaciones existentes dentro de su alcance; pregunta solo por el dato o efecto realmente pendiente. No presupongas proveedores, corpus, cuentas, modelos ni presupuesto.

## Riesgos y salida de esta etapa

Inventar ahorro; automatizar decisión humana de alto impacto sin controles; saltar del deseo a una tecnología.

Avanza cuando el contrato esté satisfecho o el pendiente tenga impacto y siguiente acción explícitos. `bloqueado` detiene la rama dependiente, no todo el proyecto. Documentar el plan no equivale a ejecutarlo.

## Referencias y evaluación

- [Opciones y criterios](references/decision-guide.md).
- [Research brief y límites](references/research-brief.md).
- [Requisitos y riesgos](references/requirements-risks.md).
- [Casos de evaluación](evals/cases.json).
