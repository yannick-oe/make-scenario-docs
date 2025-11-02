from __future__ import annotations
import json
from dataclasses import dataclass
from typing import Dict, List, Any, Tuple, Optional
from pathlib import Path

@dataclass
class Module:
    id: str
    name: str
    type: str
    notes: str = ""

@dataclass
class Connection:
    source: str
    target: str
    label: str = ""

def load_scenario(path: str | Path) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    # We support a minimal, generic structure:
    # {
    #   "name": "Scenario Name",
    #   "modules": [{"id":"1","name":"HTTP","type":"http.get","notes":""}, ...],
    #   "connections": [{"source":"1","target":"2","label":"success"}, ...],
    #   "metadata": {"owner":"", "created":"", ...}   # optional
    # }
    if "modules" not in data or "connections" not in data:
        raise ValueError("Invalid scenario JSON: expected top-level 'modules' and 'connections'.")
    return data

def parse_modules(raw_modules: List[Dict[str, Any]]) -> Dict[str, Module]:
    modules: Dict[str, Module] = {}
    for m in raw_modules:
        modules[str(m.get("id"))] = Module(
            id=str(m.get("id")),
            name=str(m.get("name", f"module_{m.get('id')}")),
            type=str(m.get("type", "unknown")),
            notes=str(m.get("notes", "")),
        )
    return modules

def parse_connections(raw_connections: List[Dict[str, Any]]) -> List[Connection]:
    conns: List[Connection] = []
    for c in raw_connections:
        conns.append(Connection(
            source=str(c.get("source")),
            target=str(c.get("target")),
            label=str(c.get("label", "")),
        ))
    return conns

def to_mermaid(modules: Dict[str, Module], connections: List[Connection]) -> str:
    lines = ["flowchart LR"]
    # nodes
    for m in modules.values():
        label = f"{m.name}\n({m.type})" if m.type else m.name
        lines.append(f'    {m.id}["{label}"]')
    # edges
    for c in connections:
        edge_label = f' |{c.label}|' if c.label else ""
        lines.append(f"    {c.source} -->{edge_label} {c.target}")
    return "\n".join(lines)

def generate_markdown(scenario: Dict[str, Any]) -> str:
    modules = parse_modules(scenario.get("modules", []))
    connections = parse_connections(scenario.get("connections", []))
    mermaid = to_mermaid(modules, connections)

    name = scenario.get("name", "Untitled Scenario")
    metadata = scenario.get("metadata", {})

    md = []
    md.append(f"# {name}\n")
    if metadata:
        md.append("## Metadata")
        for k, v in metadata.items():
            md.append(f"- **{k}**: {v}")
        md.append("")

    md.append("## Diagram")
    md.append("```mermaid")
    md.append(mermaid)
    md.append("```\n")

    md.append("## Modules")
    md.append("| ID | Name | Type | Notes |")
    md.append("|---:|------|------|-------|")
    for m in modules.values():
        notes = (m.notes or "").replace("\n", " ").strip()
        md.append(f"| {m.id} | {m.name} | {m.type} | {notes} |")

    md.append("\n## Connections")
    if connections:
        for c in connections:
            label = f" ({c.label})" if c.label else ""
            md.append(f"- {c.source} → {c.target}{label}")
    else:
        md.append("_No connections found._")

    return "\n".join(md)

def write_markdown(md: str, out_dir: str | Path, filename: Optional[str] = None) -> Path:
    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    if not filename:
        filename = "scenario.md"
    final = out_path / filename
    final.write_text(md, encoding="utf-8")
    return final
