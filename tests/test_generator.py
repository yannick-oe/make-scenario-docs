from make_doc.generator import load_scenario, generate_markdown, to_mermaid, parse_modules, parse_connections
from pathlib import Path
import json

def test_demo_json_roundtrip(tmp_path: Path):
    data = {
        "name": "X",
        "modules": [{"id":"1","name":"A","type":"alpha"},{"id":"2","name":"B","type":"beta"}],
        "connections":[{"source":"1","target":"2","label":"ok"}]
    }
    p = tmp_path / "x.json"
    p.write_text(json.dumps(data), encoding="utf-8")
    scenario = load_scenario(p)
    md = generate_markdown(scenario)
    assert "```mermaid" in md
    assert "flowchart LR" in md
    assert "| 1 | A | alpha |" in md
    assert "1 → 2 (ok)" in md
