![Build Status](https://img.shields.io/github/actions/workflow/status/yannick-oe/make-scenario-docs/ci.yml?branch=main)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/github/license/yannick-oe/make-scenario-docs)

# make-scenario-docs 🧩
**Make.com Scenario → Auto-Documentation (Markdown + Mermaid)**

Turn a Make.com (Integromat) scenario export (JSON) into a clean, human-friendly **Markdown document** with an **auto-generated Mermaid flowchart** — perfect for audits, handovers, and process documentation.

---

## ✨ Features
- Parse a Make.com scenario JSON export (modules + connections)
- Generate a Markdown document including:
  - **Overview & metadata**
  - **Modules table** (name, type, notes)
  - **Connections list**
  - **Mermaid flowchart** (renders natively on GitHub)
- Simple CLI: `make-doc <input.json> [-o docs/]`
- No external services or secrets required
- Lightweight, pure Python

---

## 🚀 Quickstart

```bash
# 1) (Optional) Create a virtual environment
python -m venv .venv && . .venv/bin/activate
# Windows: .venv\Scripts\activate

# 2) Install (no external dependencies required)
pip install -e .

# 3) Run on the demo scenario
python -m make_doc.cli sample_scenarios/demo_scenario.json -o docs

After running, open the generated file in docs/demo_scenario.md on GitHub — the Mermaid diagram will render automatically.

📦 Project Structure

make-scenario-docs/
├─ src/make_doc/
│  ├─ __init__.py
│  ├─ generator.py        # Core: JSON → Mermaid + Markdown
│  └─ cli.py              # CLI entry point
├─ sample_scenarios/
│  └─ demo_scenario.json  # Example scenario
├─ tests/
│  └─ test_generator.py
├─ docs/                  # Generated documentation
├─ pyproject.toml
├─ README.md
├─ LICENSE
└─ .github/workflows/ci.yml

🧪 CI/CD (GitHub Actions)

Runs tests and documentation generation automatically on each push
Ensures Markdown and Mermaid output is correctly produced from sample scenarios

🧠 How to use with your own scenarios

1. In Make.com, export your scenario as a JSON file.
2. Upload it to the folder: sample_scenarios/
3. Generate documentation:
    python -m make_doc.cli sample_scenarios/your_scenario.json -o docs -n your_scenario.md
4. Commit the resulting Markdown file in docs/ to your repository.

Security note: This tool reads local JSON only.
No API keys or external connections are required.
