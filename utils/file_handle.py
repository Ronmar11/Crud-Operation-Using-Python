import json
from pathlib import Path
from typing import List, Any
import logging

DATA_FILE = Path(__file__).resolve().parents[1] / "storage" / "data.json"


def load_data() -> List[Any]:
    try:
        if not DATA_FILE.exists():
            return []
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError) as exc:
        logging.warning("Failed loading data.json: %s", exc)
        return []


def save_data(data: List[Any]) -> None:
    try:
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except OSError as exc:
        logging.error("Failed saving data.json: %s", exc)