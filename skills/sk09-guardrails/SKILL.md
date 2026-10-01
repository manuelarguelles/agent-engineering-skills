---
name: sk09-guardrails
description: "Diseñar o comprobar controles de seguridad del agente: autorización, aislamiento, prompt injection, salida de datos y validación de acciones. Usar en diseño o revisión del sistema, no para atender una consulta cotidiana."
metadata:
  version: "0.1.1"
  status: "provisional"
---

# SK09 · Diseñar guardrails y permisos

## Contrato

Entrada: Identidades, datos sensibles, herramientas con efectos, fronteras y política de autorización del caso.
Salida: guardrails.md: amenaza→control→propietario→prueba, permisos y política de rechazo/escalamiento.
Estado: provisional. Una revisión de texto o un test local no prueba el componente desplegado.

## Decisiones disponibles

- RBAC/ABAC
- Aislamiento por tenant
- Validación de esquemas
- Allowlist de fuentes/destinos
- Límites de herramientas y consumo
- Escalamiento proporcional al riesgo

## Procedimiento

1. Traza fronteras usuario/canal/orquestador/herramienta/datos y amenazas concretas; asigna controles a la capa que puede hacerlos cumplir.
2. Autoriza en backend y datos usando identidad verificada; ocultar botones o filas en UI no basta.
3. Limita fuentes, destinos y secretos; no pongas credenciales en cliente ni logs. Separa contenido recuperado de instrucciones autorizadas.
4. Prueba cruces de tenant, inyección, acceso indirecto, exfiltración y argumentos manipulados. Clasificadores ayudan pero no sustituyen controles deterministas.
5. La consulta permitida no necesita una aprobación institucional genérica; identifica exactamente qué efecto sí requiere autorización adicional.

## Ejecución y evidencia

Entrega primero la decisión y sus razones verificables; si la tarea autoriza construir, implementa el componente y ejecuta las pruebas correspondientes. Si solo pide análisis, no despliegues por inferencia. Registra versión de skill, entradas/fuentes, opciones consideradas, elección, artefactos, checks y siguiente paso. Usa `no_aplica` con motivo cuando esta capacidad no sea necesaria.

Conserva lo desconocido explícito. Reutiliza autorizaciones existentes dentro de su alcance; pregunta solo por el dato o efecto realmente pendiente. No presupongas proveedores, corpus, cuentas, modelos ni presupuesto.

## Riesgos y salida de esta etapa

Aprobación indiscriminada; permisos solo visuales; sanitización como única defensa.

Avanza cuando el contrato esté satisfecho o el pendiente tenga impacto y siguiente acción explícitos. `bloqueado` detiene la rama dependiente, no todo el proyecto. Documentar el plan no equivale a ejecutarlo.

## Referencias y evaluación

- [Opciones y criterios](references/decision-guide.md).
- [Research brief y límites](references/research-brief.md).
- [Requisitos y riesgos](references/requirements-risks.md).
- [Casos de evaluación](evals/cases.json).
