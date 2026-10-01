---
name: sk03-ingesta
description: "Diseñar o construir adquisición y actualización de fuentes para el agente: batch, API, eventos, CDC, OCR, cursores y deduplicación. Usar en diseño o revisión del sistema, no para atender una consulta cotidiana."
metadata:
  version: "0.1.2"
  status: "provisional"
---

# SK03 · Elegir y construir la ingesta

## Contrato

Entrada: Inventario de fuentes con formato, volumen, frecuencia, permisos, SLA de frescura y cambios/borrados.
Salida: ingesta.md y manifest.json: fuentes, mecanismo, frescura, metadatos, estrategia incremental, eliminación, checkpoint, pruebas y configuración sin secretos.
Estado: provisional. Una revisión de texto o un test local no prueba el componente desplegado.

## Decisiones disponibles

- Sin ingesta: consultar fuente en vivo
- Batch de archivos
- API paginada
- Eventos/streaming
- CDC
- Crawler autorizado
- OCR para documentos escaneados

## Procedimiento

1. Antes de capturar, verifica la identidad autorizada y los permisos de lectura de cada fuente y de escritura del destino mediante preflight de mínimo alcance. Si falta autorización, bloquea esa fuente y registra el pendiente; no declares la ingesta lista.
2. Elige mecanismo por fuente, no por preferencia de plataforma; compara copiar datos con acceso federado y sus costes/permisos.
3. Preserva originales o referencias recuperables, identificador, versión, tiempo de fuente y de captura, procedencia y hash cuando aplique.
4. Implementa cursor/checkpoint, deduplicación y reintentos acotados con backoff respetando límites. Un evento repetido no debe repetir un efecto.
5. Prueba páginas incompletas, 429, reinicio, llegada tardía, borrados y cambios de esquema. OCR necesita muestras revisadas y cuarentena para extracción defectuosa.

## Ejecución y evidencia

Entrega primero la decisión y sus razones verificables; si la tarea autoriza construir, implementa el componente y ejecuta las pruebas correspondientes. Si solo pide análisis, no despliegues por inferencia. Registra versión de skill, entradas/fuentes, opciones consideradas, elección, artefactos, checks y siguiente paso. Usa `no_aplica` con motivo cuando esta capacidad no sea necesaria.

Conserva lo desconocido explícito. Reutiliza autorizaciones existentes dentro de su alcance; pregunta solo por el dato o efecto realmente pendiente. No presupongas proveedores, corpus, cuentas, modelos ni presupuesto.

## Riesgos y salida de esta etapa

Pérdida por paginación; duplicados; confundir hash con autoría; estado parcial presentado como corpus completo.

Avanza cuando el contrato esté satisfecho o el pendiente tenga impacto y siguiente acción explícitos. `bloqueado` detiene la rama dependiente, no todo el proyecto. Documentar el plan no equivale a ejecutarlo.

## Referencias y evaluación

- [Opciones y criterios](references/decision-guide.md).
- [Research brief y límites](references/research-brief.md).
- [Requisitos y riesgos](references/requirements-risks.md).
- [Casos de evaluación](evals/cases.json).
