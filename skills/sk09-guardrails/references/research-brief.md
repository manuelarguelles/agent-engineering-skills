# Research brief · SK09

Consultado: 2026-09-30. Autoría mediante skill-creator-z, aplicando el mismo método de forma individual. La investigación común se reutiliza; no se repite por skill.

Capacidad: Diseñar guardrails y permisos.

- [mcp](https://modelcontextprotocol.io/docs/2025-11-25/tutorials/security/security_best_practices): Seguridad de integraciones MCP. Límite: Documento versionado 2025-11-25; comprobar compatibilidad del servidor elegido.
- [openapi](https://spec.openapis.org/oas/latest.html): Contrato de interfaces HTTP. Límite: La página consultada declara 3.2.1; verificar versión soportada por herramientas elegidas.

Decisión de diseño: RBAC/ABAC es una opción, no un default obligatorio. Seleccionar por restricciones del caso.

Alternativas y licencias: se usan contratos conceptuales; no se incorpora código de terceros ni se declara compatible un proveedor sin prueba. Elegir un adaptador requiere comprobar su versión, autenticación, coste, límites y licencia.

Evaluación: caso con presión y disparadores; baseline sin skill archivado antes de esta redacción. No se presume un fallo ni una mejora respecto del baseline. Riesgos: Aprobación indiscriminada; permisos solo visuales; sanitización como única defensa.
