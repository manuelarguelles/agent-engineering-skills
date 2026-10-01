---
name: sk13-despliegue
description: "Preparar o ejecutar releases y recuperación del servicio del agente: configuración, pruebas del destino, migraciones, rollback y capacidades de despliegue. Usar en diseño o revisión del sistema, no para atender una consulta cotidiana."
metadata:
  version: "0.1.1"
  status: "provisional"
---

# SK13 · Desplegar y recuperar

## Contrato

Entrada: Artefacto versionado, configuración de destino, contratos, pruebas y autorización del despliegue concreto.
Salida: release.md: manifest, comandos, inventario, configuración, pruebas reales, rollback/migración, responsables y límites pendientes.
Estado: provisional. Una revisión de texto o un test local no prueba el componente desplegado.

## Decisiones disponibles

- Proceso local
- Contenedor
- Servicio gestionado
- Job/batch
- Edge con restricciones
- IaC + pipeline CI/CD según entorno

## Procedimiento

1. Prepara un paquete reproducible con versiones, manifest/hash, dependencias, ejemplos sin secretos y comandos explícitos.
2. Asigna un solo propietario IaC a cada recurso; distingue crear, referenciar o adoptar. Inspecciona capacidades del destino antes de prometer canary/split.
3. Prueba instalación y configuración tal como se entregan, no solo parámetros ocultos del ejecutor; recorre UI o consumidor headless y verifica resultado real.
4. Define rollback de código/configuración y estrategia independiente de migración/datos. Un cambio irreversible exige plan compatible y autorización adecuada.
5. Publica/despliega solo dentro del alcance autorizado; readback y pruebas distinguen solicitud enviada, READY, respuesta funcional y aceptación. Un repo publicado no es un runtime desplegado.

## Ejecución y evidencia

Entrega primero la decisión y sus razones verificables; si la tarea autoriza construir, implementa el componente y ejecuta las pruebas correspondientes. Si solo pide análisis, no despliegues por inferencia. Registra versión de skill, entradas/fuentes, opciones consideradas, elección, artefactos, checks y siguiente paso. Usa `no_aplica` con motivo cuando esta capacidad no sea necesaria.

Conserva lo desconocido explícito. Reutiliza autorizaciones existentes dentro de su alcance; pregunta solo por el dato o efecto realmente pendiente. No presupongas proveedores, corpus, cuentas, modelos ni presupuesto.

## Riesgos y salida de esta etapa

Publicar secretos; rebuild no reproducible; doble dueño IaC; falsa aceptación por HTTP200.

Avanza cuando el contrato esté satisfecho o el pendiente tenga impacto y siguiente acción explícitos. `bloqueado` detiene la rama dependiente, no todo el proyecto. Documentar el plan no equivale a ejecutarlo.

## Referencias y evaluación

- [Opciones y criterios](references/decision-guide.md).
- [Research brief y límites](references/research-brief.md).
- [Requisitos y riesgos](references/requirements-risks.md).
- [Casos de evaluación](evals/cases.json).
