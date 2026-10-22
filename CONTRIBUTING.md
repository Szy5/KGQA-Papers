# Contributing

Thank you for helping maintain this KGQA reading list. Corrections, missing papers,
updated publication venues, code links, and improved categorizations are welcome.

## Scope

A paper should make a direct contribution to at least one of these areas:

- knowledge graph question answering or KBQA;
- retrieval or reasoning over structured knowledge graphs;
- agentic exploration, planning, or reinforcement learning on knowledge graphs;
- KGQA datasets, evaluation, robustness, privacy, or temporal/open-world settings;
- self-play work with a clear methodological connection to KG reasoning.

General GraphRAG, graph learning, or LLM papers without a substantive KGQA
connection are out of scope.

## Add a paper

1. Choose the single most relevant section in `README.md`.
2. Add the paper in reverse chronological order using its first public release date.
3. Link the arXiv identifier to `https://arxiv.org/abs/<id>`.
4. Keep “做了什么” and “没解决的问题” factual and concise. Prefer limitations
   explicitly stated by the authors; label your own inference when necessary.
5. Do not commit PDFs. Link to the canonical paper page, publisher page, code, or
   project page instead.
6. Check that the paper is not already listed under another title or version.

Use this row format for sections 1–9:

```markdown
| YYYY-MM-DD | Paper ([YYMM.NNNNN](https://arxiv.org/abs/YYMM.NNNNN), Venue) | One-sentence contribution | One-sentence limitation or open question |
```

In the pull request, include a short explanation of the paper's KGQA relevance.

## Quality bar

- Prefer stable, canonical links and official code repositories.
- Do not describe acceptance at a venue unless it can be verified.
- Avoid promotional language and performance claims without context.
- Preserve the table structure and keep each paper in one primary category.
- Run the repository link check when possible before submitting.

The `scripts/import_survey.py` utility is only for refreshing the collection from
the original survey format. Routine additions should edit `README.md` directly.
