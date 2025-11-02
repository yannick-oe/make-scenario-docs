# make-scenario-docs 🧩
**Make.com Scenario → Auto-Documentation (Markdown + Mermaid)**

Turn a Make.com (Integromat) scenario export (JSON) into a clean, human-friendly **Markdown document** with an **auto-generated Mermaid flowchart** — perfect for audits, handovers, and playbooks.

> **Why this project?**  
> Recruiters and engineers love clear documentation. This tool demonstrates practical Python, automation know‑how, and CI/CD on GitHub — without exposing any personal data or investments.

---

## ✨ Features
- Parse a Make.com scenario JSON export (modules + connections)
- Generate a Markdown doc with:
  - **Overview & metadata**
  - **Modules table** (name, type, notes)
  - **Connections** list
  - **Mermaid flowchart** (renders natively on GitHub)
- Simple **CLI**: `make-doc <input.json> [-o docs/]`
- **No external services**, no secrets needed
- Lightweight, pure Python

---

## 🚀 Quickstart

```bash
# 1) (Optional) Create a virtual env
python -m venv .venv && . .venv/bin/activate  # Windows: .venv\Scripts\activate

# 2) Install (no external deps required)
pip install -e .

# 3) Run on the demo scenario
python -m make_doc.cli sample_scenarios/demo_scenario.json -o docs
```

After running, open the generated file in `docs/demo_scenario.md` on GitHub — Mermaid renders automatically.

---

## 📦 Project Structure
```
make-scenario-docs/
├─ src/make_doc/
│  ├─ __init__.py
│  ├─ generator.py        # core: JSON → Mermaid + Markdown
│  └─ cli.py              # argparse wrapper
├─ sample_scenarios/
│  └─ demo_scenario.json  # anonymized demo
├─ tests/
│  └─ test_generator.py
├─ docs/                  # (generated) output goes here
├─ pyproject.toml
├─ README.md
├─ LICENSE
└─ .github/workflows/ci.yml
```

---

## 🧪 CI/CD (GitHub Actions)
- Lints and runs tests on every push
- Asserts that Mermaid + Markdown generation works on the demo JSON

---

## 🧠 How to adapt for your scenarios
1. In Make.com, **export** a scenario as JSON.  
2. Drop it into `sample_scenarios/your_scenario.json`.  
3. Run: `python -m make_doc.cli sample_scenarios/your_scenario.json -o docs`  
4. Commit the resulting Markdown in `docs/` to your repo.

> **Security note:** The tool reads local JSON only. No API keys, no secret uploads.

---

## 📄 License
MIT — free to use, modify, and share.
