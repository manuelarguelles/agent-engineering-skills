---
name: sk02-arquitectura
description: "Elegir entre automatización determinista, una llamada a modelo, workflow o agente; decidir componentes necesarios antes de seleccionar proveedores. Usar en diseño o revisión del sistema, no para atender una consulta cotidiana."
metadata:
  version: "0.1.1"
  status: "provisional"
---

# SK02 · Elegir arquitectura y mecanismos

## Contrato

Entrada: Caso, restricciones de datos/latencia/coste, mecanismos ya existentes y entorno permitido.
Salida: arquitectura.md: mecanismos elegidos/descartados, interfaces, diagrama, dependencias, riesgos y pruebas para resolver incertidumbre.
Estado: provisional. Una revisión de texto o un test local no prueba el componente desplegado.

## Decisiones disponibles

- Reglas y batch sin LLM
- Una llamada a modelo
- Workflow fijo
- Agente con herramientas
- Varios agentes con contratos de coordinación

## Procedimiento

1. Compara la solución más sencilla viable con opciones más flexibles usando necesidad de adaptación, auditabilidad y coste.
2. Decide por separado ingesta, recuperación, herramientas, memoria, modelo y canal; marca no aplica con razón.
3. Define interfaces y propietarios; mantén contratos del dominio separados de adaptadores de proveedor.
4. Dibuja ruta de datos y efectos. Explicita criterios para cambiar la arquitectura; multiagente exige beneficio contrastable y coste de coordinación.

## Ejecución y evidencia

Entrega primero la decisión y sus razones verificables; si la tarea autoriza construir, implementa el componente y ejecuta las pruebas correspondientes. Si solo pide análisis, no despliegues por inferencia. Registra versión de skill, entradas/fuentes, opciones consideradas, elección, artefactos, checks y siguiente paso. Usa `no_aplica` con motivo cuando esta capacidad no sea necesaria.

Conserva lo desconocido explícito. Reutiliza autorizaciones existentes dentro de su alcance; pregunta solo por el dato o efecto realmente pendiente. No presupongas proveedores, corpus, cuentas, modelos ni presupuesto.

## Riesgos y salida de esta etapa

Confundir complejidad con calidad; heredar un proveedor; imponer RAG a un CSV de reglas fijas.

Avanza cuando el contrato esté satisfecho o el pendiente tenga impacto y siguiente acción explícitos. `bloqueado` detiene la rama dependiente, no todo el proyecto. Documentar el plan no equivale a ejecutarlo.

## Referencias y evaluación

- [Opciones y criterios](references/decision-guide.md).
- [Research brief y límites](references/research-brief.md).
- [Requisitos y riesgos](references/requirements-risks.md).
- [Casos de evaluación](evals/cases.json).
