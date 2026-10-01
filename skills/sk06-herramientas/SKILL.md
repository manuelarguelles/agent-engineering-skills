---
name: sk06-herramientas
description: "Diseñar o implementar contratos de herramientas y acciones del agente, incluidos entradas, efectos, errores, idempotencia y adaptadores; no equivale a ejecutar una acción cotidiana. Usar en diseño o revisión del sistema, no para atender una consulta cotidiana."
metadata:
  version: "0.1.1"
  status: "provisional"
---

# SK06 · Diseñar herramientas y acciones

## Contrato

Entrada: Operaciones necesarias, API/SDK/CLI/MCP disponibles, identidades y efectos permitidos.
Salida: herramientas.json: contratos por operación, política de efectos, identidad, idempotencia, reconciliación y pruebas.
Estado: provisional. Una revisión de texto o un test local no prueba el componente desplegado.

## Decisiones disponibles

- Función local
- API HTTP con contrato
- SDK
- Servidor MCP
- Adaptador de UI solo si es necesario

## Procedimiento

1. Define cada herramienta por propósito, entradas, salidas, precondiciones, permisos, errores y efecto: lectura, escritura reversible o acción irreversible.
2. Haz cumplir validación y autorización fuera del modelo. MCP es una integración, no una concesión automática de acceso.
3. Para escrituras, usa clave idempotente o referencia de operación y reconciliación. Un timeout significa estado desconocido hasta consultar; no repetir a ciegas.
4. Respeta las autorizaciones ya concedidas dentro de su alcance y pide solo la realmente faltante; separa preparar una acción de ejecutarla.
5. Prueba argumentos adversarios, errores transitorios, respuesta incompleta, efectos duplicados y caída después del envío.

## Ejecución y evidencia

Entrega primero la decisión y sus razones verificables; si la tarea autoriza construir, implementa el componente y ejecuta las pruebas correspondientes. Si solo pide análisis, no despliegues por inferencia. Registra versión de skill, entradas/fuentes, opciones consideradas, elección, artefactos, checks y siguiente paso. Usa `no_aplica` con motivo cuando esta capacidad no sea necesaria.

Conserva lo desconocido explícito. Reutiliza autorizaciones existentes dentro de su alcance; pregunta solo por el dato o efecto realmente pendiente. No presupongas proveedores, corpus, cuentas, modelos ni presupuesto.

## Riesgos y salida de esta etapa

Doble reserva; privilegios excesivos; token passthrough; respuesta de una tool como instrucción confiable.

Avanza cuando el contrato esté satisfecho o el pendiente tenga impacto y siguiente acción explícitos. `bloqueado` detiene la rama dependiente, no todo el proyecto. Documentar el plan no equivale a ejecutarlo.

## Referencias y evaluación

- [Opciones y criterios](references/decision-guide.md).
- [Research brief y límites](references/research-brief.md).
- [Requisitos y riesgos](references/requirements-risks.md).
- [Casos de evaluación](evals/cases.json).
