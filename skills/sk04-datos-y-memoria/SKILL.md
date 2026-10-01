---
name: sk04-datos-y-memoria
description: "Diseñar representación de datos, estado de ejecución y memoria persistente, con procedencia, vigencia, aislamiento y retención. Usar en diseño o revisión del sistema, no para atender una consulta cotidiana."
metadata:
  version: "0.1.1"
  status: "provisional"
---

# SK04 · Preparar datos, estado y memoria

## Contrato

Entrada: Fuentes, identidades, requisitos de consulta, política de retención y estado de sesiones.
Salida: datos-memoria.md: esquemas, claves, calidad, políticas de acceso/retención, memoria habilitada y pruebas de aislamiento y borrado.
Estado: provisional. Una revisión de texto o un test local no prueba el componente desplegado.

## Decisiones disponibles

- SQL/tablas
- Documentos/objetos
- Índice de búsqueda
- Grafo cuando las relaciones lo justifiquen
- Estado efímero
- Memoria persistente selectiva
- Sin memoria entre sesiones

## Procedimiento

1. Separa conocimiento fuente, datos transaccionales, estado de tarea y memoria conversacional. Una memoria es una hipótesis contextual, no autoridad actual.
2. Define esquema, identificadores, procedencia, calidad, relaciones y versionado; documenta unidades y fechas.
3. Aplica alcance por usuario/tenant desde acceso, índices y cachés hasta logs. Minimiza qué se recuerda y por cuánto tiempo.
4. Implementa revisión, expiración, exportación y borrado según política del caso; prueba contaminación entre sesiones y restablecimiento.

## Ejecución y evidencia

Entrega primero la decisión y sus razones verificables; si la tarea autoriza construir, implementa el componente y ejecuta las pruebas correspondientes. Si solo pide análisis, no despliegues por inferencia. Registra versión de skill, entradas/fuentes, opciones consideradas, elección, artefactos, checks y siguiente paso. Usa `no_aplica` con motivo cuando esta capacidad no sea necesaria.

Conserva lo desconocido explícito. Reutiliza autorizaciones existentes dentro de su alcance; pregunta solo por el dato o efecto realmente pendiente. No presupongas proveedores, corpus, cuentas, modelos ni presupuesto.

## Riesgos y salida de esta etapa

Contaminación entre clientes; hechos obsoletos; persistencia por defecto sin necesidad.

Avanza cuando el contrato esté satisfecho o el pendiente tenga impacto y siguiente acción explícitos. `bloqueado` detiene la rama dependiente, no todo el proyecto. Documentar el plan no equivale a ejecutarlo.

## Referencias y evaluación

- [Opciones y criterios](references/decision-guide.md).
- [Research brief y límites](references/research-brief.md).
- [Requisitos y riesgos](references/requirements-risks.md).
- [Casos de evaluación](evals/cases.json).
