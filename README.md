# Agent Engineering Skills

Skills en español para **diseñar, construir y evaluar agentes según el caso**, sin exigir una industria, proveedor, framework, canal o modelo concretos.

No es un runtime ni un generador que despliegue cualquier agente con un clic. Es un método de trabajo modular: cada skill ayuda a elegir mecanismos, implementar dentro del alcance autorizado y producir evidencia. Puede concluir que una tarea se resuelve mejor sin agente.

## Empezar

1. Clona este repositorio y abre el proyecto con un asistente que pueda leer archivos.
2. Invoca `skills/sk00-contexto/SKILL.md` con el contexto del caso. Después usa SK01 y SK02 para fijar valor, decisiones y arquitectura.
3. Selecciona las skills siguientes según la arquitectura. Marca `no_aplica` con razón para los componentes innecesarios.
4. Cada invocación entrega decisión, artefactos, comprobaciones, límites y próximo paso. Construir o desplegar exige el alcance concreto correspondiente, no simplemente leer una skill.

Ejemplo de encargo: «Lee `skills/sk00-contexto/SKILL.md` y aplícala a este repo para construir un agente de soporte. Reutiliza el contexto disponible y entrega evidencia, brechas y siguiente paso». Continúa invocando SK01 y SK02 sobre esa salida.

Las skills no son pasos que se ejecutan en cada pregunta del usuario final. Dirigen el trabajo de construir y operar la solución.

## Skills en orden de uso

| Orden | Skill | Para qué sirve |
|---|---|---|
| SK00 | [sk00-contexto](skills/sk00-contexto/SKILL.md) | Recuperar contexto y evidencia |
| SK01 | [sk01-caso-y-valor](skills/sk01-caso-y-valor/SKILL.md) | Definir el caso y las decisiones |
| SK02 | [sk02-arquitectura](skills/sk02-arquitectura/SKILL.md) | Elegir arquitectura y mecanismos |
| SK03 | [sk03-ingesta](skills/sk03-ingesta/SKILL.md) | Elegir y construir la ingesta |
| SK04 | [sk04-datos-y-memoria](skills/sk04-datos-y-memoria/SKILL.md) | Preparar datos, estado y memoria |
| SK05 | [sk05-recuperacion](skills/sk05-recuperacion/SKILL.md) | Elegir recuperación y grounding |
| SK06 | [sk06-herramientas](skills/sk06-herramientas/SKILL.md) | Diseñar herramientas y acciones |
| SK07 | [sk07-modelos](skills/sk07-modelos/SKILL.md) | Elegir modelos y configuración |
| SK08 | [sk08-orquestacion](skills/sk08-orquestacion/SKILL.md) | Construir razonamiento y coordinación |
| SK09 | [sk09-guardrails](skills/sk09-guardrails/SKILL.md) | Diseñar guardrails y permisos |
| SK10 | [sk10-canal](skills/sk10-canal/SKILL.md) | Construir canal y experiencia |
| SK11 | [sk11-evaluacion](skills/sk11-evaluacion/SKILL.md) | Evaluar y comparar el agente |
| SK12 | [sk12-observabilidad](skills/sk12-observabilidad/SKILL.md) | Instrumentar y operar |
| SK13 | [sk13-despliegue](skills/sk13-despliegue/SKILL.md) | Desplegar y recuperar |
| SK14 | [sk14-mejora](skills/sk14-mejora/SKILL.md) | Mejorar skills y componentes |

El número facilita encontrarlas; **no impone una cascada rígida**. Diseña guardrails (SK09), evaluación (SK11) y observabilidad (SK12) desde la arquitectura y repítelos al integrar. SK03–SK08 y SK10 se seleccionan por necesidad; no todos los agentes requieren corpus, RAG o memoria persistente.

## Qué puede elegirse

- **Ingesta:** ninguna, batch, API, eventos, CDC, crawler autorizado u OCR.
- **Recuperación:** ninguna, SQL/API exacta, léxica, vectorial, híbrida, grafo o contexto directo. RRF y reranking se comparan cuando aportan valor.
- **Razonamiento:** reglas, una llamada a modelo, workflow, bucle acotado o varios agentes.
- **Herramientas:** funciones, SDK, HTTP, MCP o adaptadores de interfaz; su contrato no sustituye la autorización.
- **Canal:** web/chat, API, CLI, eventos, voz o multimodal.
- **Ejecución:** local, contenedor, servicio gestionado, jobs o edge según restricciones.

La plataforma se decide después de los requisitos y se encapsula en adaptadores. No se heredan datos, cuentas ni recursos de SBS Radar.

## Plantillas y ejemplos

- [Doce decisiones](docs/12-decisiones.md).
- [Capas y etapas de preparación](docs/capas-y-etapas.md).
- [Contrato de invocación](templates/invocation.json).
- [Casos de distintos tipos](examples/README.md).
- [Crear una carpeta de trabajo](scripts/new_project.py): genera plantillas; no crea servicios ni llama modelos.

```sh
python3 scripts/new_project.py soporte-interno --kind documental --output /tmp/soporte-interno
python3 scripts/validate.py
```

## Uso con un runtime de skills

Cada carpeta tiene `SKILL.md`, referencias y casos. Mantén la carpeta completa al copiarla al directorio de skills que admita tu runtime, o invoca la ruta explícitamente. La autodetección depende del runtime y no se ha certificado en todos los productos. No se instalan skills globales automáticamente.

## Validación y estado

**Paquete 0.1.1 provisional; SK03 refinada a 0.1.2.** Se aplicó `skill-creator-z` individualmente, reutilizando investigación común. Cada skill conserva brief, riesgos, casos y registro de creación. Hay salidas baseline sin skill y salidas con skill, más revisiones independientes. Consulta [el informe](evals/REPORT.md).

No se afirma mejora estadística ni preparación para producción. Los ejemplos son diseños ficticios; no son agentes desplegados. Casos especializados —por ejemplo control físico o decisiones de alto impacto— requieren adaptadores, especialistas y pruebas adicionales del dominio.

## Fuentes y licencia

Las [fuentes primarias](research/sources.json) y la [comparación de alternativas](research/alternatives.md) separan hechos, decisiones y límites. No se incluye código ni credenciales de proveedores. Código y texto originales de este repositorio: MIT; las fuentes enlazadas conservan sus propias licencias.
