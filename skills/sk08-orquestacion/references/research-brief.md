# Research brief · SK08

Consultado: 2026-09-30. Autoría mediante skill-creator-z, aplicando el mismo método de forma individual. La investigación común se reutiliza; no se repite por skill.

Capacidad: Construir razonamiento y coordinación.

- [patterns](https://www.anthropic.com/engineering/building-effective-agents): Alternativa entre flujos predeterminados y agentes dinámicos. Límite: Artículo de 2024 advierte cambios de tooling; se reutiliza la distinción conceptual, no recomendaciones actuales de productos.
- [graphs](https://docs.langchain.com/oss/python/langgraph/overview): Orquestación con estado y ejecución durable. Límite: Alternativa técnica; no evaluada con un despliegue en este proyecto.
- [mcp](https://modelcontextprotocol.io/docs/2025-11-25/tutorials/security/security_best_practices): Seguridad de integraciones MCP. Límite: Documento versionado 2025-11-25; comprobar compatibilidad del servidor elegido.

Decisión de diseño: Secuencia fija es una opción, no un default obligatorio. Seleccionar por restricciones del caso.

Alternativas y licencias: se usan contratos conceptuales; no se incorpora código de terceros ni se declara compatible un proveedor sin prueba. Elegir un adaptador requiere comprobar su versión, autenticación, coste, límites y licencia.

Evaluación: caso con presión y disparadores; baseline sin skill archivado antes de esta redacción. No se presume un fallo ni una mejora respecto del baseline. Riesgos: Bucles sin límite; prompt injection; pérdida de estado; agentes autoaprobando efectos ajenos.
