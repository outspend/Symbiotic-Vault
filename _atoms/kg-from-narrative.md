---
type: atom
id: kg-from-narrative
aliases: [knowledge graph from literature, narrative KG, story as knowledge graph]
kind: method
status: seed
created: 2026-03-30
source:
  - _journal/2026-03-23.md
tags: [knowledge-graphs, narrative, NLP, formal-knowledge-design, film-production]
frames: [formal-knowledge-design, sequential-narrative]
---

Extracting a knowledge graph from a narrative text — a novel, film script, or story. MapReduce on large texts functions as an intermediate step: breaking the text into processable chunks, extracting relationships, then assembling them into a graph structure.

The questions this opens: How does a classic story appear as a KG? What types of relationships get mapped? How does temporal progression — the fact that a story changes over time — fit into a structure that's typically static? Jim White suggested this with Siddhartha (Hesse) as an example case.

An application in large production: in a film like Avatar, a KG built on the script could track the state of scenes, characters, and props across production — bridging virtual and non-virtual elements. The KG becomes a production state management tool rather than a literary analysis tool.

---
## Relations

- [[word2vec-as-humanistic-concept]]: derives from — the humanistic reading of Word2Vec motivates treating relational structure in text as meaningful and extractable
- [[llm-to-knowledge-graph-pipeline]]: extends — extends the general pipeline to specifically narrative texts, where temporal and character-state relationships add complexity
- [[vault-as-graph-not-topic-filter]]: complements — the vault's graph structure is analogous to what KG-from-narrative produces for a story; both prefer relational traversal over categorical filtering
