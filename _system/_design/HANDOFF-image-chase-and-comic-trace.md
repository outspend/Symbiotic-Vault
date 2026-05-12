---
type: handoff
created: 2026-04-30
for: implementer (fresh Opus, Sonnet, or Codex picking this up cold)
implements: comic-trace skill, then image-chase skill
---

# Handoff brief — comic-trace and image-chase skills

You're picking up the implementation of two related vault skills designed across a long conversation between the user (John) and Opus on 2026-04-29. The conversation produced two design docs and a third-party prototype canvas to play off. This brief points you at what to read, in what order, and where to start.

---

## Read these in order

1. **`_trace/2026-04-22-scroggins-manson-comic-provenance.canvas`** — the hand-built prototype canvas that defines the conventions both skills formalize. Open in Obsidian, look at the lanes, colors, node types, edge labels, the legend node in the upper-left, the cluster patterns. Treat this as the source of truth for what a comic-trace canvas should look like.

2. **`_system/_design/comic-trace-skill-design.md`** — the skill that owns canvas writing. Phase 1 (init/capture/annotate) ships first; Phase 2 (compose-sub-canvas with init/append/finalize modes, link-sub with status flag) provides the live sub-canvas integration that image-chase depends on.

3. **`_system/_design/image-chase-skill-design.md`** — the skill that does image iteration via gpt-image-2. Phase 1 (`fix`) is the request-blast capability. Depends on comic-trace Phase 2 being in place.

4. **`_trace/_notes/2026-04-29-canvas-read-exchange.md`** and **`_trace/_notes/2026-04-29-new-p3-honey-script.md`** — context on the test corpus. The new P3 script will be the smoke test target for image-chase Phase 1 once it's ready.

---

## Build order (firm)

1. **comic-trace Phase 1** — `init`, `capture`, `annotate`, plus the supporting `lib/canvas.py`, `lib/schema.py`, `lib/layout.py`, `lib/resolve.py`. No API access needed.
2. **comic-trace Phase 2** — `compose-sub-canvas` (init/append/finalize modes), `link-sub` (with status flag), `lib/events.py`. Still no API access.
3. **(Pause for user prep)** — user curates `_style/scroggins-manson/manifest.yaml` with bible/character refs from existing `_trace/_assets/`, and converts the new-P3 script into a request-blast file. ~30 min of user work.
4. **image-chase Phase 1** — `fix` capability. Depends on OpenAI API key with org verification and gpt-image-2 access.
5. **image-chase Phase 2 + style-lock** — when needed for the next comic.

Do not start image-chase until comic-trace is shipped. The dependency is hard — image-chase has no canvas-writing code; it shells out to comic-trace at every event.

---

## Smoke tests (the bars)

**comic-trace Phase 1:** see the corrected smoke test in `comic-trace-skill-design.md`. Mechanics test, not a "rebuild" of the prototype — most of the prototype's content can't be derived from current vault state.

**comic-trace Phase 2:** hand-build a fake iteration directory with the documented format, run init/append/finalize/link-sub against it, confirm the sub-canvas grows correctly and the main canvas link reflects status changes.

**image-chase Phase 1:** run `/image-chase fix P3` against the curated Scroggins manifest and the new-P3 request blast. Budget cap $0.30, time cap 30 min. Confirms the loop works, surface decisions trigger, sub-canvas grows live via comic-trace calls, decision log captures every adaptation/refusal.

---

## Key design choices, in case you're tempted to revise

These were arrived at across the conversation. Don't reverse without checking with the user.

- **Conversational scoring, not in-loop vision rubric.** The agent and user evaluate gens together. No `lib/rubric.py`, no automated structured-output scoring calls. This was an explicit simplification from an earlier draft.
- **Live append sub-canvas, not one-shot at end.** The sub-canvas exists from second one and grows event-by-event, like a chat history. The user can lean on it being there mid-run. Atomic writes (write-temp-and-rename) prevent corruption.
- **comic-trace owns canvas writing.** image-chase has no canvas knowledge. If you find yourself adding `lib/sub_canvas.py` or similar to image-chase, stop — you're duplicating capability that lives in comic-trace.
- **Request-blast format is intentionally loose.** Markdown with conventional sections (`Fight for / Harvest / Fix / Continuity`), not strict YAML. The agent parses with judgment and asks clarifying questions when ambiguous. Don't tighten this into a strict schema.
- **Two budget caps (n + USD).** Either trips the stop. Don't replace with a single cap; the dual cap prevents both compulsion and runaway costs.
- **Guardrail policy:** legitimate craft adaptation (likeness via shape-language, nudity via abstraction) is fine and logged; brute-forcing past content policy is not. Hard limit: 2 craft adaptations per refusal type per run, then surface and stop. Documented in `_shared/decision-log.md`.

---

## What the docs don't capture

A few things from the conversation that didn't land in the design docs but are worth keeping in mind:

- **The user's pain is mid-iteration cleanup, not exploration.** Phase 1 (`fix`) is targeted at where they bleed time right now. Don't optimize for the spread/study/bake workflow until Phase 2.
- **The user's voice is cartoony, iconic, popart.** The Scroggins style brief is a useful reference for how they'll speak about images. Read the canvas note `a7e722a372486b22` for their own articulation.
- **The user wants segregation between agent and user input on the canvas.** This came from the legend's "red = ai/agent provisional" note. The `annotate` command's `--by user|agent` flag honors this. Belt-and-suspenders: also prefix node text with `[AGENT]:` or `[USER]:` so the distinction never blurs.
- **Failures should be kept, not deleted.** "Sometimes serendipitous" was a recurring note. Iteration directories preserve every gen. Don't add auto-prune.
- **The user already has ChatGPT Pro and is using it for the actual image work.** The API skill is for *scale and unattended chasing*, not for replacing the chat experience for one-off panels. Frame the skill as complementary, not a replacement.

---

## Open questions for the user

If you hit any of these, surface to the user before guessing:

- **OpenAI tier.** Affects rate limit and parallelism strategy. Set in `_system/_tools/image-chase/config.yaml`. User probably tier 1 unless they've upgraded.
- **Budget defaults.** Documented placeholders ($0.30 smoke, $1.00 typical fix run). Validate against the user's actual willingness to spend before shipping.
- **Whether image-chase calls comic-trace via shell-out (slower, looser coupling) or Python import (faster, tighter coupling).** Design assumes shell-out for v1. Reasonable to revisit if shell overhead becomes a real problem.

---

## Final notes

- The user is comfortable with iterative implementation. Don't try to ship everything at once. comic-trace Phase 1 alone is a useful artifact even before Phase 2.
- The two design docs are intentionally structured for cold pickup. If you find yourself confused, that's a doc gap worth surfacing — fix the doc, not the code.
- The `builders_notes.md` entry dated 2026-04-29 captures the "load-bearing image" pattern and the "Charlie's resentment as appraisal-not-jealousy" insight from the originating exchange. Useful background but not on the critical path.
