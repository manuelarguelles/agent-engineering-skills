# Research brief · SK07

Consultado: 2026-09-30. Autoría mediante skill-creator-z, aplicando el mismo método de forma individual. La investigación común se reutiliza; no se repite por skill.

Capacidad: Elegir modelos y configuración.

- [patterns](https://www.anthropic.com/engineering/building-effective-agents): Alternativa entre flujos predeterminados y agentes dinámicos. Límite: Artículo de 2024 advierte cambios de tooling; se reutiliza la distinción conceptual, no recomendaciones actuales de productos.
- [openapi](https://spec.openapis.org/oas/latest.html): Contrato de interfaces HTTP. Límite: La página consultada declara 3.2.1; verificar versión soportada por herramientas elegidas.

Decisión de diseño: Sin modelo es una opción, no un default obligatorio. Seleccionar por restricciones del caso.

Alternativas y licencias: se usan contratos conceptuales; no se incorpora código de terceros ni se declara compatible un proveedor sin prueba. Elegir un adaptador requiere comprobar su versión, autenticación, coste, límites y licencia.

Evaluación: caso con presión y disparadores; baseline sin skill archivado antes de esta redacción. No se presume un fallo ni una mejora respecto del baseline. Riesgos: Confundir precio listado con coste total; ganador no medido; salida de datos por fallback.
