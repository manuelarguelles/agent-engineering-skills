# Capas, etapas y skills

Mapa didáctico de este framework; no se presenta como una taxonomía universal. Una capa describe una responsabilidad y una etapa describe trabajo de preparación. Las skills son procedimientos para hacer ese trabajo.

| Nueve capas | Skills relacionadas |
|---|---|
| Canal e interacción | SK10 |
| Identidad, permisos y guardrails | SK09, SK06 |
| Orquestación y razonamiento | SK02, SK08 |
| Modelos e inferencia | SK07 |
| Herramientas y acciones | SK06 |
| Recuperación y evidencia | SK05 |
| Datos, conocimiento y memoria | SK04 |
| Fuentes e ingesta | SK03 |
| Evaluación, operación y ciclo de vida | SK11, SK12, SK13, SK14 |

Una capa puede no necesitar implementación propia: un agente headless tiene contrato de API/evento como canal; una calculadora determinista puede no necesitar modelo ni recuperación.

| Nueve etapas de preparación | Qué resuelve |
|---|---|
| 1. Contexto | Recuperar evidencia y brechas (SK00) |
| 2. Caso | Fijar valor, alcance y decisiones (SK01) |
| 3. Arquitectura | Elegir mecanismos y diseñar controles, pruebas y trazas (SK02, SK09, SK11, SK12) |
| 4. Fuentes | Diseñar ingesta cuando haga falta (SK03) |
| 5. Datos | Preparar calidad, permisos y memoria (SK04) |
| 6. Capacidades | Elegir recuperación, herramientas y modelos (SK05–SK07) |
| 7. Integración | Orquestar y exponer el canal (SK08–SK10) |
| 8. Aceptación | Evaluar flujo completo y preparar release (SK11–SK13) |
| 9. Operación | Observar, recuperar y mejorar (SK12–SK14) |

Se puede iterar o paralelizar ramas con contratos estables. Los permisos, las decisiones de arquitectura, las acciones con efectos y la aceptación no se aprueban automáticamente al terminar una cola.
