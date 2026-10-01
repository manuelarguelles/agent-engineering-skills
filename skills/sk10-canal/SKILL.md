---
name: sk10-canal
description: "Diseñar o implementar la interfaz de uso del agente por web, chat, API, CLI, eventos, voz o multimodal, incluidos estados, errores y experiencia. Usar en diseño o revisión del sistema, no para atender una consulta cotidiana."
metadata:
  version: "0.1.1"
  status: "provisional"
---

# SK10 · Construir canal y experiencia

## Contrato

Entrada: Usuarios, disparadores, canales, identidad, contrato de respuesta y tiempos esperados.
Salida: canal.md y contrato de interfaz: recorridos, estados, errores, accesibilidad y evidencia del flujo probado.
Estado: provisional. Una revisión de texto o un test local no prueba el componente desplegado.

## Decisiones disponibles

- Web/chat
- API headless
- CLI
- Mensajería autorizada
- Voz/multimodal
- Eventos sin interfaz

## Procedimiento

1. Elige canal por tarea, accesibilidad, latencia e integración; no impongas chat a un proceso nocturno.
2. Define estados aceptado/en curso/completo/parcial/error y recuperación; para tareas largas considera polling o streaming según el caso.
3. Valida status y Content-Type antes de interpretar JSON; un HTML de login debe producir error accionable, no texto técnico crudo al usuario.
4. Expón fuentes, limitaciones y acciones siguientes útiles; conserva identidad y no credenciales en el cliente.
5. Prueba el flujo real: enviar, esperar, consultar resultado, error, sesión expirada y cancelación si existe. En headless verifica el consumidor del evento/API.

## Ejecución y evidencia

Entrega primero la decisión y sus razones verificables; si la tarea autoriza construir, implementa el componente y ejecuta las pruebas correspondientes. Si solo pide análisis, no despliegues por inferencia. Registra versión de skill, entradas/fuentes, opciones consideradas, elección, artefactos, checks y siguiente paso. Usa `no_aplica` con motivo cuando esta capacidad no sea necesaria.

Conserva lo desconocido explícito. Reutiliza autorizaciones existentes dentro de su alcance; pregunta solo por el dato o efecto realmente pendiente. No presupongas proveedores, corpus, cuentas, modelos ni presupuesto.

## Riesgos y salida de esta etapa

Confundir API200 con UX completa; canal incompatible; perder contexto al cambiar filtros.

Avanza cuando el contrato esté satisfecho o el pendiente tenga impacto y siguiente acción explícitos. `bloqueado` detiene la rama dependiente, no todo el proyecto. Documentar el plan no equivale a ejecutarlo.

## Referencias y evaluación

- [Opciones y criterios](references/decision-guide.md).
- [Research brief y límites](references/research-brief.md).
- [Requisitos y riesgos](references/requirements-risks.md).
- [Casos de evaluación](evals/cases.json).
