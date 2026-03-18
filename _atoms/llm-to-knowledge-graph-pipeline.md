---
type: atom
id: llm-to-knowledge-graph-pipeline
aliases: [LLM to knowledge graph, unstructured text to KG, LLM KG extraction]
kind: method
status: seed
created: 2026-03-16
source:
  - _inbox/2026-03-10_002.md
tags: [knowledge-graph, llm-tools, information-extraction, reference]
frames: [formal-knowledge-design]
---

A method for converting unstructured text into interactive knowledge graphs using LLMs — using the model to identify entities, relationships, and structure that can then be represented as a graph.

Flagged via a Medium article shared by Jim on Discord (Robert McDermott, "From Unstructured Text to Interactive Knowledge Graphs Using LLMs"). Personal interest is specifically for policy-level rules: could LLM-assisted KG extraction enable articulation of a whole game system? The method would let a designer externalize and inspect game rules as a graph, enabling QA via simulation (running the game system against questions, worries, scenarios).

Still speculative as application; the GitHub repo linked in the article needs investigation.

## Relations
- [[vault-as-graph-not-topic-filter]] — adjacent: both concern structuring knowledge as graph; KG pipeline is an extraction method, vault-as-graph is a design principle — they could be combined
- [[game-system-articulation-via-llm]] — grounds: the KG pipeline is the likely technical mechanism for externalizing a game system as navigable structure
