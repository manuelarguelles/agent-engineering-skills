"""Create local planning artifacts only; never overwrite or provision resources."""
import argparse
import json
import re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def create(name, kind, output):
    if not re.fullmatch(r'[a-z0-9][a-z0-9-]{0,62}', name):
        raise ValueError('Use a lowercase project name with letters, digits and hyphens')
    options = {x['kind']: x for x in json.loads((ROOT/'examples/archetypes.json').read_text())}
    if kind not in options:
        raise ValueError('Unknown project kind')
    dest = Path(output)
    if dest.exists():
        raise FileExistsError('Destination already exists; refusing to overwrite')
    # Atomic directory reservation prevents a competing invocation from overwriting it.
    dest.mkdir(parents=True, exist_ok=False)
    example = options[kind]
    (dest/'contexto.md').write_text(f'# {name}\n\nEstado: planificación. Tipo propuesto: {kind}.\n\n## Hechos observados\nPendientes de aportar.\n\n## Hipótesis ilustrativa\n{example["title"]}. No es evidencia del caso real.\n\n## Siguiente paso\nAplicar SK00 con fuentes autorizadas y después SK01/SK02.\n')
    decisions=json.loads((ROOT/'templates/decisiones.json').read_text())
    decisions.update(project=name, archetype=kind)
    (dest/'decisiones.json').write_text(json.dumps(decisions,ensure_ascii=False,indent=2)+'\n')
    invocation=json.loads((ROOT/'templates/invocation.json').read_text())
    invocation.update(task_id=name+'-context', skill_id='SK00')
    (dest/'invocation.json').write_text(json.dumps(invocation,ensure_ascii=False,indent=2)+'\n')
    (dest/'README.md').write_text('# Carpeta de trabajo\n\nPlantillas únicamente. No se crearon servicios, índices, modelos ni agentes. Completa las decisiones con evidencia; no uses el arquetipo como requisito universal.\n')
    return dest

if __name__ == '__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('name');p.add_argument('--kind',default='documental',choices=['documental','analitico','transaccional','programacion','multimodal','determinista'])
    p.add_argument('--output',required=True)
    args=p.parse_args()
    try: print(create(args.name,args.kind,args.output))
    except (ValueError, FileExistsError) as exc: p.exit(2,str(exc)+'\n')
