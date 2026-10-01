# Requisitos y riesgos · SK03

| Requisito | Riesgo | Evidencia exigida |
|---|---|---|
| Elegir mecanismo por caso | Sobreajuste al piloto anterior | Opciones y razón de decisión |
| Elegir y construir la ingesta | Pérdida por paginación; duplicados; confundir hash con autoría; estado parcial presentado como corpus completo. | Elegir OCR/batch/API/eventos por fuente; checkpoint y cursor; deduplicación; reintentos acotados; permisos. |
| Mantener alcance autorizado | Efectos externos no pedidos | Acción concreta y permiso aplicable |
| Estado honesto | Plan presentado como ejecución | Artefactos y checks observados, pendientes separados |
