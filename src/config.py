from pathlib import Path
import yaml


DEFAULTS = {
"base_url": "https://eg.indeed.com/jobs",
"user_agents": [],
"sleep_min": 1.0,
"sleep_max": 3.0,
"results_per_page": 10,
}




def load_config(path: str | Path = None):
    if path is None:
        return DEFAULTS
    p = Path(path)
    if not p.exists():
        return DEFAULTS
    with open(p, "r", encoding="utf8") as f:
        data = yaml.safe_load(f) or {}
    return {**DEFAULTS, **data}