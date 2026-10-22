#!/usr/bin/env python3
"""Import the curated KGQA survey into the repository's Awesome-style pages."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


SECTION_RE = re.compile(r"^## (\d+)\.\s+(.+)$")
ARXIV_RE = re.compile(r"(?<![\d./])(\d{4}\.\d{4,5})(?![\d.])")
PUBLICATION_LINKS = {
    "Interactive Semantic Parsing with Reinforcement Learning for Knowledge Graph Reasoning": "https://aclanthology.org/2026.findings-acl.1023/",
    "Exploration-and-Thinking: Agentic Reasoning over KGs via an LLM-RL Synergized Framework": "https://doi.org/10.1145/3805712.3809649",
    "Thought-Action Graph Reasoning: Faithful and Efficient Reasoning via Reusing Past Experience": "https://aclanthology.org/2026.findings-acl.1572/",
    "Faico: Faithful and Complete Knowledge Graph Augmented Reasoning": "https://madsys.cs.tsinghua.edu.cn/publication/faico-faithful-and-complete-knowledge-graph-augmented-reasoning/",
    "AGEE: A multi-dimensional process-level metric for evaluating agent exploration over KGs": "https://doi.org/10.1016/j.knosys.2026.116614",
    "PYTHIA: Universal Question Answering over Knowledge Graphs": "https://doi.org/10.1145/3770855.3817968",
    "GCA-KBQA": "https://doi.org/10.1145/3805712.3809660",
    "Hop-wise Planning with Iterative Explainable Self-Correction for KBQA": "https://doi.org/10.1145/3819823",
    "Subgraph-Guided Executable Logical Form Generation for KBQA": "https://aclanthology.org/2026.findings-acl.177/",
    "Beyond Pruning: Harnessing Off-Path Triples for KGQA with LLMs": "https://doi.org/10.1016/j.ins.2026.123915",
    "Efficient LLM-Based Subgraph Retrieval for Multi-Hop KBQA": "https://doi.org/10.1109/TKDE.2026.3679080",
    "Diagnose-Reflective Planning (LLM-Guided MCTS)": "https://cmsworkshops.com/ICASSP2026/view_paper.php?PaperNum=13553",
    "Enhancing KBQA with Reinforced Hop-Wise Logical Form Generation": "https://cmsworkshops.com/ICASSP2026/view_paper.php?PaperNum=4057",
    "Plan-Answer-Refine-on-Graph": "https://proceedings.iclr.cc/paper_files/paper/2026/hash/2bb5ad76b4f1efeed5a6afde40476614-Abstract-Conference.html",
    "CompKBQA": "https://aclanthology.org/2025.emnlp-main.16/",
}


def link_arxiv_ids(line: str) -> str:
    """Link bare modern arXiv identifiers without touching existing links."""

    pieces = re.split(r"(`[^`]*`|\[[^\]]+\]\([^)]*\))", line)
    for index in range(0, len(pieces), 2):
        pieces[index] = ARXIV_RE.sub(
            lambda match: (
                f"[{match.group(1)}](https://arxiv.org/abs/{match.group(1)})"
            ),
            pieces[index],
        )
    return "".join(pieces)


def link_publication_title(line: str) -> str:
    """Link known publisher records for papers without an arXiv source."""

    for title, url in PUBLICATION_LINKS.items():
        if title in line:
            return line.replace(title, f"[{title}]({url})", 1)
    return line


def parse_sections(text: str) -> dict[int, tuple[str, list[str]]]:
    sections: dict[int, tuple[str, list[str]]] = {}
    current: int | None = None

    for line in text.splitlines():
        match = SECTION_RE.match(line)
        if match:
            current = int(match.group(1))
            sections[current] = (match.group(2), [])
            continue
        if current is not None:
            sections[current][1].append(line)
    return sections


def sort_dated_table(lines: list[str]) -> list[str]:
    """Sort a Markdown table's ISO-dated rows newest first."""

    result = list(lines)
    dated_indexes = [
        index
        for index, line in enumerate(result)
        if re.match(r"^\|\s*\d{4}-\d{2}-\d{2}\s*\|", line)
    ]
    if not dated_indexes:
        return result

    dated_rows = [result[index] for index in dated_indexes]
    dated_rows.sort(key=lambda row: row.split("|", 2)[1].strip(), reverse=True)
    for index, row in zip(dated_indexes, dated_rows):
        result[index] = row
    return result


def clean_body(lines: list[str], *, sort_by_date: bool = False) -> list[str]:
    body = list(lines)
    while body and (not body[0].strip() or body[0].strip() == "---"):
        body.pop(0)
    while body and (not body[-1].strip() or body[-1].strip() == "---"):
        body.pop()
    if sort_by_date:
        body = sort_dated_table(body)
    return [
        link_publication_title(link_arxiv_ids(line)).replace(
            "与你的 Evolve on Graph 撞名", "与 Evolve on Graph 重名"
        )
        for line in body
    ]


def count_table_rows(lines: list[str]) -> int:
    return sum(
        1
        for line in lines
        if line.startswith("|")
        and not line.startswith("|---")
        and not line.startswith("| 日期")
        and not line.startswith("| 论文")
    )


def render_readme(sections: dict[int, tuple[str, list[str]]]) -> str:
    main_count = sum(count_table_rows(sections[number][1]) for number in range(1, 10))
    related_count = count_table_rows(sections[12][1])
    offline_count = count_table_rows(sections[10][1])

    output = [
        "# Awesome Knowledge Graph Question Answering (KGQA)",
        "",
        "> A curated list of recent papers on knowledge graph question answering, "
        "KG-RAG, graph reasoning, and agentic KG exploration.",
        ">",
        "> 知识图谱问答、KG-RAG、图推理与智能体图探索的近期论文清单。",
        "",
        "This repository currently focuses on work released from **2025-01-01 to "
        "2026-10-01**. Entries are grouped by research direction and ordered "
        "newest first within each section. Paper binaries are intentionally not "
        "tracked; arXiv identifiers link to the canonical abstract pages.",
        "",
        f"- **{main_count}** core KGQA papers across nine topics",
        f"- **{related_count}** related self-play and self-evolution papers",
        f"- **{offline_count}** additional conference/journal papers without an "
        "available arXiv PDF in the original survey",
        "- Survey last updated: **2026-10-09**",
        "",
        "The **★** marker is inherited from the source survey and identifies "
        "priority reading. Summaries and open-problem notes are concise research "
        "annotations; verify claims against the paper before citing them.",
        "",
        "## Contents",
        "",
    ]

    for number in range(1, 10):
        title = sections[number][0]
        output.append(f"- [{title}](#topic-{number})")
    output.extend(
        [
            "- [Published work without an arXiv PDF](#topic-10)",
            "- [Related: self-play and self-evolution](#topic-12)",
            "- [Research gaps](docs/research-gaps.md)",
            "- [Contributing](CONTRIBUTING.md)",
            "",
            "## Paper list",
            "",
        ]
    )

    for number in range(1, 11):
        title, lines = sections[number]
        output.extend(
            [
                f'<a id="topic-{number}"></a>',
                "",
                f"### {number}. {title}",
                "",
                *clean_body(lines, sort_by_date=number != 10),
                "",
            ]
        )

    title, lines = sections[12]
    output.extend(
        [
            '<a id="topic-12"></a>',
            "",
            "### 12. 自博弈 / 自进化相关",
            "",
            *clean_body(lines, sort_by_date=True),
            "",
            "## Contributing",
            "",
            "Suggestions and corrections are welcome. Please read "
            "[CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request, or "
            "use the paper-suggestion issue template.",
            "",
            "## Scope and provenance",
            "",
            "The initial collection was assembled using arXiv keyword searches, "
            "citation chasing from representative KGQA systems, and manual "
            "screening. Each annotation is based on the abstract and, when "
            "available, the paper's limitations/conclusion sections; it is not a "
            "substitute for a full-paper review.",
            "",
        ]
    )
    return "\n".join(output)


def render_gaps(sections: dict[int, tuple[str, list[str]]]) -> str:
    _, lines = sections[11]
    body = clean_body(lines)
    return "\n".join(
        [
            "# Open research gaps in KGQA",
            "",
            "These cross-paper observations were imported from the source survey "
            "and last reviewed on 2026-10-09. They are working research notes, not "
            "claims of exhaustive novelty; re-check the current literature before "
            "using them in a paper.",
            "",
            *body,
            "",
            "[Back to the paper list](../README.md)",
            "",
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path, help="source survey Markdown file")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="repository root (default: inferred from this script)",
    )
    args = parser.parse_args()

    source_text = args.source.read_text(encoding="utf-8")
    sections = parse_sections(source_text)
    required = set(range(1, 13))
    missing = required.difference(sections)
    if missing:
        raise SystemExit(f"source survey is missing sections: {sorted(missing)}")

    output_dir = args.output_dir.resolve()
    (output_dir / "docs").mkdir(parents=True, exist_ok=True)
    (output_dir / "README.md").write_text(
        render_readme(sections), encoding="utf-8"
    )
    (output_dir / "docs" / "research-gaps.md").write_text(
        render_gaps(sections), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
