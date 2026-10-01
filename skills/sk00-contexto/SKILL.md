---
name: sk00-contexto
description: "Recuperar el estado de trabajo, decisiones previas y evidencia del proyecto al iniciar o retomar su diseño o construcción; no sustituye la instrumentación de producción. Usar en diseño o revisión del sistema, no para atender una consulta cotidiana."
metadata:
  version: "0.1.1"
  status: "provisional"
---

# SK00 · Recuperar contexto y evidencia

## Contrato

Entrada: Objetivo actual, repos/artefactos autorizados, decisiones previas y evidencia disponible.
Salida: contexto.md: objetivo, fuentes, matriz de evidencia, decisiones vigentes, contradicciones, pendientes y siguiente paso verificable.
Estado: provisional. Una revisión de texto o un test local no prueba el componente desplegado.

## Decisiones disponibles

- Reutilizar inventario verificado
- Inspección acotada del repo
- Entrevista breve para un bloqueo real
- Investigación nueva solo para una brecha o dato cambiante

## Procedimiento

1. Inventaría lo disponible antes de buscar de nuevo; registra ruta/URL, fecha, hash o versión y alcance.
2. Separa observado, declarado, inferido, desconocido y contradicho. El test reciente fallido limita un README histórico.
3. Reconstruye tareas realizadas, pendientes y dependencias; no supongas que un recurso de otra sesión sigue activo.
4. Resume contexto mínimo para cada siguiente skill; pregunta solo lo que cambia una decisión y continúa lo independiente.

## Ejecución y evidencia

Entrega primero la decisión y sus razones verificables; si la tarea autoriza construir, implementa el componente y ejecuta las pruebas correspondientes. Si solo pide análisis, no despliegues por inferencia. Registra versión de skill, entradas/fuentes, opciones consideradas, elección, artefactos, checks y siguiente paso. Usa `no_aplica` con motivo cuando esta capacidad no sea necesaria.

Conserva lo desconocido explícito. Reutiliza autorizaciones existentes dentro de su alcance; pregunta solo por el dato o efecto realmente pendiente. No presupongas proveedores, corpus, cuentas, modelos ni presupuesto.

## Riesgos y salida de esta etapa

Memoria obsoleta; exploración indiscriminada; credenciales expuestas; supuesto presentado como hecho.

Avanza cuando el contrato esté satisfecho o el pendiente tenga impacto y siguiente acción explícitos. `bloqueado` detiene la rama dependiente, no todo el proyecto. Documentar el plan no equivale a ejecutarlo.

## Referencias y evaluación

- [Opciones y criterios](references/decision-guide.md).
- [Research brief y límites](references/research-brief.md).
- [Requisitos y riesgos](references/requirements-risks.md).
- [Casos de evaluación](evals/cases.json).
