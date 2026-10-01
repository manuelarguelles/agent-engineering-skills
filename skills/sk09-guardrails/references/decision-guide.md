# Guía de decisión · SK09

## Entrada de ejemplo

Un agente de soporte de varios clientes consulta documentos y puede enviar correos. Su cuenta técnica tiene acceso global. La UI oculta datos ajenos. Hay poco tiempo: ¿eso basta y qué controles implementas?

## Qué debe resolver

Autorización backend/herramientas; tenant y retrieval; egress; prompt injection; permisos explícitos para enviar; pruebas negativas.

## Opciones

- RBAC/ABAC
- Aislamiento por tenant
- Validación de esquemas
- Allowlist de fuentes/destinos
- Límites de herramientas y consumo
- Escalamiento proporcional al riesgo

## Contrato de salida

guardrails.md: amenaza→control→propietario→prueba, permisos y política de rechazo/escalamiento.

No todas las opciones deben implementarse. Compara al menos la opción sencilla viable y la alternativa que resolvería su limitación. Declara supuesto, evidencia, coste de cambio y señal para reconsiderar.
