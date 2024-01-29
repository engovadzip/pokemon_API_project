from pathlib import Path
import json


def load_schema(filepath):
    with open(path(filepath)) as file:
        schema = json.load(file)
        return schema

def path(schema_name):
    return str(Path(__file__).parent.parent.parent.joinpath(f'schemas/{schema_name}'))