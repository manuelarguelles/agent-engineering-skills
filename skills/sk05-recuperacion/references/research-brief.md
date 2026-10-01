# Research brief · SK05

Consultado: 2026-09-30. Autoría mediante skill-creator-z, aplicando el mismo método de forma individual. La investigación común se reutiliza; no se repite por skill.

Capacidad: Elegir recuperación y grounding.

- [rrf](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/reciprocal-rank-fusion): RRF combina listas de resultados. Límite: Ejemplo de implementación, no requisito de usar Elastic ni promesa de calidad.
- [mcp](https://modelcontextprotocol.io/docs/2025-11-25/tutorials/security/security_best_practices): Seguridad de integraciones MCP. Límite: Documento versionado 2025-11-25; comprobar compatibilidad del servidor elegido.

Decisión de diseño: Sin recuperación externa es una opción, no un default obligatorio. Seleccionar por restricciones del caso.

Alternativas y licencias: se usan contratos conceptuales; no se incorpora código de terceros ni se declara compatible un proveedor sin prueba. Elegir un adaptador requiere comprobar su versión, autenticación, coste, límites y licencia.

Evaluación: caso con presión y disparadores; baseline sin skill archivado antes de esta redacción. No se presume un fallo ni una mejora respecto del baseline. Riesgos: Vectorizar todo; doble fusión; filtrar tarde; citar una fuente distinta; datos actuales sustituidos por un índice viejo.
