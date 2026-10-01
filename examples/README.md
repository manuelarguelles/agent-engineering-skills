# Ejemplos ficticios de selección

Diseños ilustrativos, no despliegues ni benchmarks. Cambia las elecciones al cambiar los requisitos.

## Asistente de manuales internos

- Tipo: documental.
- Fuente: PDF y wiki autorizada.
- Ingesta: Batch/API incremental con ACL.
- Recuperación: Léxica como baseline; comparar híbrida.
- Mecanismo: Solo lectura; citas y abstención.
- Canal: Chat/web.
- Límite: Sin envío ni aprobación institucional para leer fuentes permitidas.

## Analista de inventario

- Tipo: analitico.
- Fuente: Tablas SQL.
- Ingesta: Consulta en vivo; sin copiar si no aporta valor.
- Recuperación: SQL parametrizado y capa semántica.
- Mecanismo: Solo lectura con límites de consulta.
- Canal: API/chat.
- Límite: No interpretar búsqueda semántica como importe exacto.

## Asistente de reservas

- Tipo: transaccional.
- Fuente: API de disponibilidad.
- Ingesta: Sin corpus persistente; acceso en vivo.
- Recuperación: API exacta.
- Mecanismo: Reserva autorizada con idempotencia y reconciliación.
- Canal: Web/voz.
- Límite: Un timeout no autoriza duplicar reserva.

## Asistente de mantenimiento de código

- Tipo: programacion.
- Fuente: Repo y pruebas.
- Ingesta: Lectura incremental del repo.
- Recuperación: Búsqueda de símbolos/texto; embeddings opcionales.
- Mecanismo: Editar rama y ejecutar tests dentro del alcance.
- Canal: CLI/IDE.
- Límite: Contenido del repo no autoriza exfiltrar secretos ni desplegar.

## Asistente de inspección de imágenes

- Tipo: multimodal.
- Fuente: Imágenes y metadatos ficticios.
- Ingesta: Carga controlada y validación de formatos.
- Recuperación: Sin RAG inicialmente; referencia si el caso lo exige.
- Mecanismo: Modelo multimodal; revisión según impacto.
- Canal: API/eventos.
- Límite: No declarar detección fiable sin evaluación representativa.

## Validador nocturno de CSV

- Tipo: determinista.
- Fuente: CSV y doce reglas fijas.
- Ingesta: Batch con manifiesto y checkpoint.
- Recuperación: No aplica.
- Mecanismo: Reglas sin LLM.
- Canal: Job y reporte.
- Límite: No requiere un agente autónomo.

