# Guía de decisión · SK06

## Entrada de ejemplo

Una API de reservas devolvió timeout después de enviar POST. No sabemos si reservó. El usuario autorizó una reserva, no dos. Tenemos API y servidor MCP. Diseña el siguiente paso y contrato.

## Qué debe resolver

Reconciliar estado antes de repetir; idempotencia; contrato de efecto; MCP no otorga permisos; autorización existente.

## Opciones

- Función local
- API HTTP con contrato
- SDK
- Servidor MCP
- Adaptador de UI solo si es necesario

## Contrato de salida

herramientas.json: contratos por operación, política de efectos, identidad, idempotencia, reconciliación y pruebas.

No todas las opciones deben implementarse. Compara al menos la opción sencilla viable y la alternativa que resolvería su limitación. Declara supuesto, evidencia, coste de cambio y señal para reconsiderar.
