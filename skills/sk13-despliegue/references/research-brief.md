# Research brief · SK13

Consultado: 2026-09-30. Autoría mediante skill-creator-z, aplicando el mismo método de forma individual. La investigación común se reutiliza; no se repite por skill.

Capacidad: Desplegar y recuperar.

- [openapi](https://spec.openapis.org/oas/latest.html): Contrato de interfaces HTTP. Límite: La página consultada declara 3.2.1; verificar versión soportada por herramientas elegidas.
- [graphs](https://docs.langchain.com/oss/python/langgraph/overview): Orquestación con estado y ejecución durable. Límite: Alternativa técnica; no evaluada con un despliegue en este proyecto.
- [skills](https://agentskills.io/specification): Formato SKILL.md y divulgación progresiva. Límite: Especificación consultada; no se probó cada runtime consumidor.

Decisión de diseño: Proceso local es una opción, no un default obligatorio. Seleccionar por restricciones del caso.

Alternativas y licencias: se usan contratos conceptuales; no se incorpora código de terceros ni se declara compatible un proveedor sin prueba. Elegir un adaptador requiere comprobar su versión, autenticación, coste, límites y licencia.

Evaluación: caso con presión y disparadores; baseline sin skill archivado antes de esta redacción. No se presume un fallo ni una mejora respecto del baseline. Riesgos: Publicar secretos; rebuild no reproducible; doble dueño IaC; falsa aceptación por HTTP200.
