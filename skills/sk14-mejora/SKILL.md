---
name: sk14-mejora
description: "Proponer y validar cambios versionados en skills o componentes a partir de fallos medidos, comparando baseline y regresiones antes de adoptarlos. Usar en diseño o revisión del sistema, no para atender una consulta cotidiana."
metadata:
  version: "0.1.1"
  status: "provisional"
---

# SK14 · Mejorar skills y componentes

## Contrato

Entrada: Fallo o brecha observado, versión estable, casos de evaluación y objetivo del cambio.
Salida: mejora.md: fallo→causa→cambio→prueba, baseline/candidato, holdout, regresiones, versión y decisión de promoción.
Estado: provisional. Una revisión de texto o un test local no prueba el componente desplegado.

## Decisiones disponibles

- Corrección del componente
- Refinamiento de la skill
- Cambio de datos
- Cambio de configuración
- No cambiar si falta evidencia

## Procedimiento

1. Reproduce y clasifica la causa: datos, modelo, integración, instrucciones o entorno; evita convertir un incidente en regla universal.
2. Guarda baseline y snapshots; ejecuta casos equivalentes con cambio mínimo y después casos nuevos/no relacionados.
3. Registra qué fallo se corrige, regresiones, coste y límites. Si el baseline ya pasa, no inventes mejora causal.
4. Versiona skill y componente por separado. Promueve con alcance explícito y conserva reversión; no reemplaces todas las skills por una mejora local.
5. Reutiliza fuentes y resultados vigentes; investiga solo la brecha. Actualiza el índice y consumidores afectados al renombrar una skill.

## Ejecución y evidencia

Entrega primero la decisión y sus razones verificables; si la tarea autoriza construir, implementa el componente y ejecuta las pruebas correspondientes. Si solo pide análisis, no despliegues por inferencia. Registra versión de skill, entradas/fuentes, opciones consideradas, elección, artefactos, checks y siguiente paso. Usa `no_aplica` con motivo cuando esta capacidad no sea necesaria.

Conserva lo desconocido explícito. Reutiliza autorizaciones existentes dentro de su alcance; pregunta solo por el dato o efecto realmente pendiente. No presupongas proveedores, corpus, cuentas, modelos ni presupuesto.

## Riesgos y salida de esta etapa

Sobreajuste; borrar evidencia fallida; afirmación de mejora no medida; dependencia accidental de proveedor.

Avanza cuando el contrato esté satisfecho o el pendiente tenga impacto y siguiente acción explícitos. `bloqueado` detiene la rama dependiente, no todo el proyecto. Documentar el plan no equivale a ejecutarlo.

## Referencias y evaluación

- [Opciones y criterios](references/decision-guide.md).
- [Research brief y límites](references/research-brief.md).
- [Requisitos y riesgos](references/requirements-risks.md).
- [Casos de evaluación](evals/cases.json).
