# Guía de decisión · SK10

## Entrada de ejemplo

El agente se usará por web y por eventos sin UI. Una petición tarda 40s y otra devuelve HTML de login en lugar de JSON. Diseña la experiencia e integración.

## Qué debe resolver

Canal headless válido; estado asincrónico; errores contrato tipo de contenido; no exponer secretos; prueba real flujo usuario/evento.

## Opciones

- Web/chat
- API headless
- CLI
- Mensajería autorizada
- Voz/multimodal
- Eventos sin interfaz

## Contrato de salida

canal.md y contrato de interfaz: recorridos, estados, errores, accesibilidad y evidencia del flujo probado.

No todas las opciones deben implementarse. Compara al menos la opción sencilla viable y la alternativa que resolvería su limitación. Declara supuesto, evidencia, coste de cambio y señal para reconsiderar.
