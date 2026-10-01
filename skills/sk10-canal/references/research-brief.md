# Research brief · SK10

Consultado: 2026-09-30. Autoría mediante skill-creator-z, aplicando el mismo método de forma individual. La investigación común se reutiliza; no se repite por skill.

Capacidad: Construir canal y experiencia.

- [openapi](https://spec.openapis.org/oas/latest.html): Contrato de interfaces HTTP. Límite: La página consultada declara 3.2.1; verificar versión soportada por herramientas elegidas.
- [events](https://cloudevents.io/): Contrato interoperable de eventos. Límite: No garantiza orden, entrega única ni idempotencia de efectos.

Decisión de diseño: Web/chat es una opción, no un default obligatorio. Seleccionar por restricciones del caso.

Alternativas y licencias: se usan contratos conceptuales; no se incorpora código de terceros ni se declara compatible un proveedor sin prueba. Elegir un adaptador requiere comprobar su versión, autenticación, coste, límites y licencia.

Evaluación: caso con presión y disparadores; baseline sin skill archivado antes de esta redacción. No se presume un fallo ni una mejora respecto del baseline. Riesgos: Confundir API200 con UX completa; canal incompatible; perder contexto al cambiar filtros.
