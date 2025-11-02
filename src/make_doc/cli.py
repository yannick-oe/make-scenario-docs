from __future__ import annotations
import argparse
from pathlib import Path
from .generator import load_scenario, generate_markdown, write_markdown

def main():
    parser = argparse.ArgumentParser(
        description="Make.com Scenario → Markdown + Mermaid auto-documentation generator"
    )
    parser.add_argument("input", help="Path to scenario JSON export")
    parser.add_argument("-o", "--output", default="docs", help="Output directory (default: docs)")
    parser.add_argument("-n", "--name", default=None, help="Output filename (e.g., demo.md)")

    args = parser.parse_args()
    scenario = load_scenario(args.input)
    md = generate_markdown(scenario)

    # Derive name from input if not provided
    name = args.name
    if name is None:
        name = Path(args.input).stem + ".md"

    out_file = write_markdown(md, args.output, name)
    print(f"✅ Generated: {out_file}")

if __name__ == "__main__":
    main()
