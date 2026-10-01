"""Validate package contracts; this is not a behavioral or runtime certification."""
import hashlib
import json
import re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def validate(root=ROOT):
    errors=[]
    plan=json.loads((root/'plan.json').read_text())
    if len(plan)!=15: errors.append('Expected 15 planned skills')
    for item in plan:
        folder=root/'skills'/item['name'];skill=folder/'SKILL.md'
        if not skill.is_file(): errors.append(str(skill)+': missing');continue
        text=skill.read_text();parts=text.split('---',2)
        if len(parts)!=3: errors.append(str(skill)+': missing frontmatter');continue
        fields=dict(re.findall(r'^([a-z]+):\s*(.+)$',parts[1],re.M))
        if fields.get('name')!=folder.name:errors.append(str(skill)+': name mismatch')
        if not fields.get('description') or len(fields['description'])>1024:errors.append(str(skill)+': description invalid')
        if len(text.splitlines())>=500: errors.append(str(skill)+': too long')
        if re.search(r'/Users/|databricksapps\.com|7474657121564806|gsk_[A-Za-z0-9]{20}',text):errors.append(str(skill)+': origin binding or secret marker')
        for rel in re.findall(r'\]\(([^)]+)\)',text):
            if '://' not in rel and not (folder/rel.split('#')[0]).is_file():errors.append(str(skill)+': broken '+rel)
        cases=json.loads((folder/'evals/cases.json').read_text())['cases']
        if len(cases)<3:errors.append(str(skill)+': missing eval dimensions')
        record=json.loads((folder/'evals/creator-record.json').read_text())
        if record['skill_sha256']!=hashlib.sha256(skill.read_bytes()).hexdigest():errors.append(str(skill)+': creator hash stale')
    return errors
if __name__=='__main__':
    errors=validate()
    print(json.dumps({'pass':not errors,'skills':15,'scope':'Package structure and selected portability constraints only','errors':errors},ensure_ascii=False,indent=2))
    raise SystemExit(bool(errors))
