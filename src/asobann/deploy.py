import json
from codecs import open
from pathlib import Path

import asobann


app = asobann.create_app()


def purge_all():
    for d in [asobann.store.tables, asobann.store.components, asobann.store.kits]:
        d.purge_all()

if __name__ == '__main__':
    with open(Path(__file__).parent / "./initial_deploy_data.json", encoding='utf-8') as f:
        default_data = json.load(f)
    purge_all()
    asobann.store.components.store_default(default_data["components"])
    asobann.store.kits.store_default(default_data["kits"])
