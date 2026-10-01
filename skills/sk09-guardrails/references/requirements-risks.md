# Requisitos y riesgos · SK09

| Requisito | Riesgo | Evidencia exigida |
|---|---|---|
| Elegir mecanismo por caso | Sobreajuste al piloto anterior | Opciones y razón de decisión |
| Diseñar guardrails y permisos | Aprobación indiscriminada; permisos solo visuales; sanitización como única defensa. | Autorización backend/herramientas; tenant y retrieval; egress; prompt injection; permisos explícitos para enviar; pruebas negativas. |
| Mantener alcance autorizado | Efectos externos no pedidos | Acción concreta y permiso aplicable |
| Estado honesto | Plan presentado como ejecución | Artefactos y checks observados, pendientes separados |
