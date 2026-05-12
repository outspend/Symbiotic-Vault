

  Use a short mode line before the request.

  - Mode: skim
    Use when you want: quick shape, first impression, “can you read this?”, “does this make sense?”
    What I do: inspect structure, scan representative content, identify major clusters and purpose.
    What you get: fast answer, lower completeness.
  - Mode: selective
    Use when you want: a local question answered without paying for a whole-artifact read.
    What I do: read only the relevant node, cluster, file references, and nearby edges.
    What you get: focused answer, possible loss of bigger-context meaning.
  - Mode: full digestion
    Use when you want: trustworthy whole-artifact summary, chronology, interpretation, or discussion from complete context.
    What I do: read the entire artifact carefully as a whole object, not just samples.
    What you get: slower but much better global understanding.

  Useful add-ons:

  - Focus: [node/cluster/topic]
  - Goal: summarize / interpret / critique / trace provenance / answer question
  - Confidence: quick / careful / exhaustive

  Examples:

  - Mode: skim
    Tell me what this canvas is doing.
  - Mode: selective
    Focus: the chatgpt-image branch
    Explain what happened here.
  - Mode: full digestion
    Summarize the whole artifact and tell me what it reveals about the process.

  My default if you do not specify:

  - “Can you read this / does it make sense?” -> skim
  - Narrow question about one part -> selective
  - Whole-summary / interpretation / chronology -> full digestion

  Best collaboration pattern:

  - Start with skim
  - Switch to full digestion when you want real interpretation
  - Use selective for follow-up questions on one branch or node

  If you want, we can treat full digestion as meaning: “do not answer interpretively until you’ve read the whole artifact.”