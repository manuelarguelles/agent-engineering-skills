# Requisitos y riesgos · SK04

| Requisito | Riesgo | Evidencia exigida |
|---|---|---|
| Elegir mecanismo por caso | Sobreajuste al piloto anterior | Opciones y razón de decisión |
| Preparar datos, estado y memoria | Contaminación entre clientes; hechos obsoletos; persistencia por defecto sin necesidad. | Aislamiento por tenant; memoria no autoridad; retención/borrado; vigencia/procedencia; evitar persistencia innecesaria. |
| Mantener alcance autorizado | Efectos externos no pedidos | Acción concreta y permiso aplicable |
| Estado honesto | Plan presentado como ejecución | Artefactos y checks observados, pendientes separados |
