# Alternativas y decisión de reutilización

| Alternativa | Qué reutilizamos | Qué no sustituye | Mantenimiento/licencia |
|---|---|---|---|
| Agent Skills | Formato abierto SKILL.md; carga progresiva | El runtime del agente que se construya | Especificación consultada; licencia de implementaciones se comprueba por separado |
| Flujos deterministas y funciones | Primera opción si la secuencia y reglas bastan | Flexibilidad cuando el caso requiere decisiones variables | Bibliotecas concretas por elegir; sin dependencia impuesta |
| LangGraph | Alternativa de orquestación con estado | Contratos de datos, autorización y evaluación | Documentación oficial consultada; revisar versión/licencia antes de incorporar código |
| MCP / OpenAPI | Contratos de integraciones | Permiso de actuar, seguridad del negocio, idempotencia | Especificaciones consultadas; cada servidor tiene licencia y límites propios |
| Motor de búsqueda con RRF | Ejemplo para comparar recuperación | Evaluación sobre consultas y ACL del caso | Se referencia Elastic, sin copiar código ni imponer servicio/licencia |
| Skills SBS previas | Experiencia sobre límites E2E, evidencia y estado | No se copian sus recursos, corpus ni defaults | Fuente interna reutilizada; estas skills nuevas no dependen de ese repo |

Comparación documental, no benchmark de productos. Costes, límites y modalidades se verifican al elegir el adaptador. No se declara un ganador universal.
