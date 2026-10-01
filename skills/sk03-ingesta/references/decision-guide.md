# Guía de decisión · SK03

## Entrada de ejemplo

Hay PDFs escaneados semanales, una API que pagina y devuelve 429, y eventos de pedidos que pueden repetirse o llegar fuera de orden. Diseña ingesta sin asumir cloud específico.

## Qué debe resolver

Elegir OCR/batch/API/eventos por fuente; checkpoint y cursor; deduplicación; reintentos acotados; permisos.

## Opciones

- Sin ingesta: consultar fuente en vivo
- Batch de archivos
- API paginada
- Eventos/streaming
- CDC
- Crawler autorizado
- OCR para documentos escaneados

## Contrato de salida

ingesta.md y manifest.json: fuentes, mecanismo, frescura, metadatos, estrategia incremental, eliminación, checkpoint, pruebas y configuración sin secretos.

No todas las opciones deben implementarse. Compara al menos la opción sencilla viable y la alternativa que resolvería su limitación. Declara supuesto, evidencia, coste de cambio y señal para reconsiderar.
