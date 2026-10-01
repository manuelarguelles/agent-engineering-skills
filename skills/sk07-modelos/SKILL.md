---
name: sk07-modelos
description: "Seleccionar modelos y parámetros según capacidades, modalidad, residencia, coste y latencia, mediante medición en tareas representativas. Usar en diseño o revisión del sistema, no para atender una consulta cotidiana."
metadata:
  version: "0.1.1"
  status: "provisional"
---

# SK07 · Elegir modelos y configuración

## Contrato

Entrada: Tareas/modalidades, restricciones duras, dataset de evaluación y proveedores permitidos.
Salida: modelos.md y configuracion.example.json: requisitos, candidatos, mediciones o pendientes, decisión, versiones y fallback.
Estado: provisional. Una revisión de texto o un test local no prueba el componente desplegado.

## Decisiones disponibles

- Sin modelo
- Modelo local
- Servicio gestionado
- Modelo multimodal
- Clasificador especializado
- Ruteo entre modelos
- Fallback compatible

## Procedimiento

1. Filtra candidatos por capacidad necesaria, residencia, tratamiento de datos, contexto, herramientas, disponibilidad y licencia.
2. Evalúa con el mismo conjunto representativo; mide calidad, errores, p50/p95, tokens/coste y límites. No elijas por benchmark general solamente.
3. Fija modelo/versión cuando exista, parámetros, prompt, configuración y dependencias; documenta cambios silenciosos del servicio si no permite fijar versión.
4. Un fallback debe conservar permisos, residencia y contrato; declara degradación. Si no hay mediciones, entrega plan de selección y candidatos, no un ganador inventado.

## Ejecución y evidencia

Entrega primero la decisión y sus razones verificables; si la tarea autoriza construir, implementa el componente y ejecuta las pruebas correspondientes. Si solo pide análisis, no despliegues por inferencia. Registra versión de skill, entradas/fuentes, opciones consideradas, elección, artefactos, checks y siguiente paso. Usa `no_aplica` con motivo cuando esta capacidad no sea necesaria.

Conserva lo desconocido explícito. Reutiliza autorizaciones existentes dentro de su alcance; pregunta solo por el dato o efecto realmente pendiente. No presupongas proveedores, corpus, cuentas, modelos ni presupuesto.

## Riesgos y salida de esta etapa

Confundir precio listado con coste total; ganador no medido; salida de datos por fallback.

Avanza cuando el contrato esté satisfecho o el pendiente tenga impacto y siguiente acción explícitos. `bloqueado` detiene la rama dependiente, no todo el proyecto. Documentar el plan no equivale a ejecutarlo.

## Referencias y evaluación

- [Opciones y criterios](references/decision-guide.md).
- [Research brief y límites](references/research-brief.md).
- [Requisitos y riesgos](references/requirements-risks.md).
- [Casos de evaluación](evals/cases.json).
