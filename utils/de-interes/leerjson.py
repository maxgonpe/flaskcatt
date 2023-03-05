import json

with open('project1.json', 'r') as f:
    proyecto = json.load(f)

proyecto_pretty = json.dumps(proyecto, indent=4)

print(proyecto_pretty)
