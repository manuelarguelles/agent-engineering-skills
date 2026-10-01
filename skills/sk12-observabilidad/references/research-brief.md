# Research brief · SK12

Consultado: 2026-09-30. Autoría mediante skill-creator-z, aplicando el mismo método de forma individual. La investigación común se reutiliza; no se repite por skill.

Capacidad: Instrumentar y operar.

- [otel](https://opentelemetry.io/docs/concepts/semantic-conventions/): Vocabulario compartido para telemetría. Límite: Fijar versión de convenciones de la instrumentación elegida; no suponer estabilidad de todo atributo GenAI.
- [mcp](https://modelcontextprotocol.io/docs/2025-11-25/tutorials/security/security_best_practices): Seguridad de integraciones MCP. Límite: Documento versionado 2025-11-25; comprobar compatibilidad del servidor elegido.

Decisión de diseño: Logs estructurados es una opción, no un default obligatorio. Seleccionar por restricciones del caso.

Alternativas y licencias: se usan contratos conceptuales; no se incorpora código de terceros ni se declara compatible un proveedor sin prueba. Elegir un adaptador requiere comprobar su versión, autenticación, coste, límites y licencia.

Evaluación: caso con presión y disparadores; baseline sin skill archivado antes de esta redacción. No se presume un fallo ni una mejora respecto del baseline. Riesgos: Observabilidad que filtra datos; drift interpretado como fallo; coste desconocido oculto.
