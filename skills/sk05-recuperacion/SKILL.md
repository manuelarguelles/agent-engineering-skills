---
name: sk05-recuperacion
description: "Diseñar o comparar recuperación de conocimiento para las respuestas del agente: contexto directo, SQL/API, búsqueda léxica, vectorial o híbrida, filtros y grounding. Usar en diseño o revisión del sistema, no para atender una consulta cotidiana."
metadata:
  version: "0.1.1"
  status: "provisional"
---

# SK05 · Elegir recuperación y grounding

## Contrato

Entrada: Preguntas representativas, fuentes autorizadas, requisitos de exactitud/frescura y baseline de búsqueda.
Salida: recuperacion.md: rutas, chunking si aplica, filtros, ranking, parámetros, conjunto de consultas, métricas y criterio de abstención.
Estado: provisional. Una revisión de texto o un test local no prueba el componente desplegado.

## Decisiones disponibles

- Sin recuperación externa
- SQL o API exacta
- Búsqueda léxica
- Búsqueda vectorial
- Híbrida con fusión
- Grafo
- Contexto largo directo
- Reranking opcional

## Procedimiento

1. Clasifica preguntas: un importe exacto va a una consulta estructurada autorizada; una explicación documental puede necesitar pasajes citables.
2. Diseña unidad de recuperación según estructura y significado; conserva metadatos, documento, versión y localizador.
3. Aplica filtros de identidad y vigencia antes de entregar contenido al modelo. Revisa ACL también en cachés.
4. Compara baseline, lexical, vectorial, fusión y reranking con consultas/juicios separados de ajuste; no apliques RRF dos veces si ya existe fusión nativa.
5. Mide cobertura, relevancia, fidelidad, latencia y coste. Si no hay evidencia suficiente, aclara o abstente; las citas deben resolver a la fuente correcta.

## Ejecución y evidencia

Entrega primero la decisión y sus razones verificables; si la tarea autoriza construir, implementa el componente y ejecuta las pruebas correspondientes. Si solo pide análisis, no despliegues por inferencia. Registra versión de skill, entradas/fuentes, opciones consideradas, elección, artefactos, checks y siguiente paso. Usa `no_aplica` con motivo cuando esta capacidad no sea necesaria.

Conserva lo desconocido explícito. Reutiliza autorizaciones existentes dentro de su alcance; pregunta solo por el dato o efecto realmente pendiente. No presupongas proveedores, corpus, cuentas, modelos ni presupuesto.

## Riesgos y salida de esta etapa

Vectorizar todo; doble fusión; filtrar tarde; citar una fuente distinta; datos actuales sustituidos por un índice viejo.

Avanza cuando el contrato esté satisfecho o el pendiente tenga impacto y siguiente acción explícitos. `bloqueado` detiene la rama dependiente, no todo el proyecto. Documentar el plan no equivale a ejecutarlo.

## Referencias y evaluación

- [Opciones y criterios](references/decision-guide.md).
- [Research brief y límites](references/research-brief.md).
- [Requisitos y riesgos](references/requirements-risks.md).
- [Casos de evaluación](evals/cases.json).
