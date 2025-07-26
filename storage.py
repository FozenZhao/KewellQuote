import json
from pathlib import Path
from typing import List, Dict

data_dir = Path(__file__).parent / 'data'

def load_json(name: str) -> List[Dict]:
    file_path = data_dir / f'{name}.json'
    if not file_path.exists():
        return []
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_json(name: str, data: List[Dict]) -> None:
    file_path = data_dir / f'{name}.json'
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
