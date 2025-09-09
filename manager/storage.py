import json
from pathlib import Path

STORE_FILE = Path.home() / ".mini_pw_store_gui"

def load_store():
    if not STORE_FILE.exists():
        return None
    return json.loads(STORE_FILE.read_text())

def save_store(payload):
    STORE_FILE.write_text(json.dumps(payload))
