from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
errors = []
for path in root.rglob('*.md'):
    if '.git' in path.parts:
        continue
    for link in re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
        if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', link) or link.startswith('#'):
            continue
        target = (path.parent / link.split('#')[0]).resolve()
        if not target.is_relative_to(root) or not target.exists():
            errors.append(f'{path.relative_to(root)}: {link}')
if errors:
    raise SystemExit('\n'.join(errors))
print('Enlaces relativos correctos. Esta comprobación sólo valida documentación.')
