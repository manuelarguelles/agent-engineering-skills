---
name: sk12-observabilidad
description: "Instrumentar y diagnosticar el agente en ejecución con trazas, métricas, costes, correlación y alertas, minimizando datos sensibles. Usar en diseño o revisión del sistema, no para atender una consulta cotidiana."
metadata:
  version: "0.1.1"
  status: "provisional"
---

# SK12 · Instrumentar y operar

## Contrato

Entrada: Flujo, objetivos de servicio, política de datos, límites de coste y responsables operativos.
Salida: operacion.md: métricas/SLO, trazas, redacción, retención, presupuesto y runbooks con responsables.
Estado: provisional. Una revisión de texto o un test local no prueba el componente desplegado.

## Decisiones disponibles

- Logs estructurados
- Métricas
- Trazas distribuidas
- Auditoría de efectos
- Alertas
- Muestreo/minimización

## Procedimiento

1. Propaga identificadores de solicitud, sesión acotada, herramienta, versión y release sin introducir credenciales.
2. Mide tiempos de espera/recuperación/modelo/herramientas, errores y consumo; declara qué coste no se conoce.
3. Minimiza y redacta contenido; define quién puede ver telemetría y su retención. No registres tokens de acceso ni razonamiento privado.
4. Define alertas con umbral, responsable, diagnóstico y acción; distingue deriva de datos, calidad y disponibilidad.
5. Prueba trazas de una solicitud completa, caída de dependencia y fallo del propio colector; el diagnóstico no debe repetir efectos del usuario.

## Ejecución y evidencia

Entrega primero la decisión y sus razones verificables; si la tarea autoriza construir, implementa el componente y ejecuta las pruebas correspondientes. Si solo pide análisis, no despliegues por inferencia. Registra versión de skill, entradas/fuentes, opciones consideradas, elección, artefactos, checks y siguiente paso. Usa `no_aplica` con motivo cuando esta capacidad no sea necesaria.

Conserva lo desconocido explícito. Reutiliza autorizaciones existentes dentro de su alcance; pregunta solo por el dato o efecto realmente pendiente. No presupongas proveedores, corpus, cuentas, modelos ni presupuesto.

## Riesgos y salida de esta etapa

Observabilidad que filtra datos; drift interpretado como fallo; coste desconocido oculto.

Avanza cuando el contrato esté satisfecho o el pendiente tenga impacto y siguiente acción explícitos. `bloqueado` detiene la rama dependiente, no todo el proyecto. Documentar el plan no equivale a ejecutarlo.

## Referencias y evaluación

- [Opciones y criterios](references/decision-guide.md).
- [Research brief y límites](references/research-brief.md).
- [Requisitos y riesgos](references/requirements-risks.md).
- [Casos de evaluación](evals/cases.json).
