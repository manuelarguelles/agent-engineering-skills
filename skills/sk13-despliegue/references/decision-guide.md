# Guía de decisión · SK13

## Entrada de ejemplo

El notebook pasa con parámetros inyectados, el endpoint responde 200 y la app aún no fue probada. Hay un cambio de esquema irreversible. Se solicita canary 10% sin saber si el destino admite split. Planifica release.

## Qué debe resolver

Probar configuración entregada/camino real; HTTP no E2E; capacidades split; rollback código/datos; IaC dueño único; separar publicación de despliegue.

## Opciones

- Proceso local
- Contenedor
- Servicio gestionado
- Job/batch
- Edge con restricciones
- IaC + pipeline CI/CD según entorno

## Contrato de salida

release.md: manifest, comandos, inventario, configuración, pruebas reales, rollback/migración, responsables y límites pendientes.

No todas las opciones deben implementarse. Compara al menos la opción sencilla viable y la alternativa que resolvería su limitación. Declara supuesto, evidencia, coste de cambio y señal para reconsiderar.
