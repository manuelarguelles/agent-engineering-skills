# Requisitos y riesgos · SK13

| Requisito | Riesgo | Evidencia exigida |
|---|---|---|
| Elegir mecanismo por caso | Sobreajuste al piloto anterior | Opciones y razón de decisión |
| Desplegar y recuperar | Publicar secretos; rebuild no reproducible; doble dueño IaC; falsa aceptación por HTTP200. | Probar configuración entregada/camino real; HTTP no E2E; capacidades split; rollback código/datos; IaC dueño único; separar publicación de despliegue. |
| Mantener alcance autorizado | Efectos externos no pedidos | Acción concreta y permiso aplicable |
| Estado honesto | Plan presentado como ejecución | Artefactos y checks observados, pendientes separados |
