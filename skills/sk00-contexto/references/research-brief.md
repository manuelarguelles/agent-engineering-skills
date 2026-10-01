# Research brief · SK00

Consultado: 2026-09-30. Autoría mediante skill-creator-z, aplicando el mismo método de forma individual. La investigación común se reutiliza; no se repite por skill.

Capacidad: Recuperar contexto y evidencia.

- [skills](https://agentskills.io/specification): Formato SKILL.md y divulgación progresiva. Límite: Especificación consultada; no se probó cada runtime consumidor.
- [patterns](https://www.anthropic.com/engineering/building-effective-agents): Alternativa entre flujos predeterminados y agentes dinámicos. Límite: Artículo de 2024 advierte cambios de tooling; se reutiliza la distinción conceptual, no recomendaciones actuales de productos.

Decisión de diseño: Reutilizar inventario verificado es una opción, no un default obligatorio. Seleccionar por restricciones del caso.

Alternativas y licencias: se usan contratos conceptuales; no se incorpora código de terceros ni se declara compatible un proveedor sin prueba. Elegir un adaptador requiere comprobar su versión, autenticación, coste, límites y licencia.

Evaluación: caso con presión y disparadores; baseline sin skill archivado antes de esta redacción. No se presume un fallo ni una mejora respecto del baseline. Riesgos: Memoria obsoleta; exploración indiscriminada; credenciales expuestas; supuesto presentado como hecho.
