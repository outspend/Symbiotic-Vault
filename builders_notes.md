# Builders Notes

Messages to me — insights that surfaced during skill runs and conversational sessions that no memory type is scoped to hold. Each entry links back to the file that brought it about.

---

## 2026-05-07 — from [[_system/_design/schematic-prompt-pattern]]

**Two precisions — a design move worth naming.** Most prompt-engineering thinking honors only one kind of precision: be specific about what you want. The session surfaced a second kind that's just as important: be specific about what should *remain open*. "Field of possibility" isn't slack — it's a deliberately bounded zone where the model is invited to contribute. Naming the field with bounds ("distinct figures, varied gestures of welcome, eyelines on Billy") is its own act of precision, distinct from over-specifying the answer. This is the move that lets the model's takes become creative input rather than just executions of your spec.

**Reactive tightening, not preemptive.** The schematic prompt iterates downstream of reconciliation, not upstream by guessing. The bar isn't "no drift" — it's "picks reconcile." When picks across takes can be stitched and reprompted into a coherent page, the prompt was loose enough; when they can't, that names the place to tighten. This flips the usual prompt-engineering posture (defensive over-specification up front) into something more like: ship the loosest prompt that meets the bar, let the model's behavior tell you where to firm up. Generalizable beyond comics.

**Test removal before assuming structure is load-bearing.** The whole arc of dropping the SVG schematic happened by you running the same prompt without it and finding the gens were equally good. Worth keeping as a habit: when an extra layer (a schematic, a guardrail, a meta-prompt) was introduced for a reason, periodically test whether removing it changes the output. If it doesn't, the layer wasn't earning its keep.

**Film-production vocabulary — take, circle take, hero panel, field of possibility.** You named these in the moment when describing how variations should function. They map cleanly: variations are takes, picks are circle takes, the slot they occupy is a hero panel, and the deliberately open zone in the prompt is the field of possibility. The vocabulary travels well — could anchor any AI-collaborative creative workflow where the human curates from a take pool. Preserved in the pattern doc; if other creative workflows in the vault start needing the same scaffolding, this language is portable.

**One stitch, not N references.** Your correction here was quick — reminded me that the reconciliation re-prompt should send *one* image (the stitch) plus optionally a style anchor, not 16 separate panel cutouts. Worth noting because it's a small piece of model-economic taste: the model handles "here's a target page" better than "here are sixteen disconnected exemplars." Same insight likely applies to other multi-element generative work.

---

## 2026-05-06 — from [[literal-honey-schematic-claude-code]]

**The vault holds the schematic; the model only renders.** This crystallized while watching GPT fail at its keeper duties — you asked it to change 5 jars to 4, it refused; you didn't ask it to widen panel 1's framing, it did anyway; you asked for a wardrobe block, it added one written entirely with `or` ("leather or suede," "sandals or boots"), and every "or" is a slot the model fills differently across panels and so defeats the block's own purpose. Plus it left `(shape only)` in the bottom note, contradicting the new wardrobe block right above it — couldn't even copy-edit its own change. From all of that: schematic = editorial, render = mechanical, two different jobs. The vault keeps the truth; the model receives and renders. The image-chase design already has this spirit (manifest + refs live in `_style/`); the schematic doc just pushes it one step further upstream — the editorial layer above the manifest.

**Three rules that fall out of the editorial frame** —
1. **The drawing obeys its own legend.** Stylized jar-shapes when the legend says rectangle is a self-contradiction. Counts become hard to glance, and the model has to reconcile drawing-vs-prose — which is where slop creeps in. Fix it upstream by drawing rectangles.
2. **No `or` anywhere in the bible.** Slack in the spec becomes drift in the output. Decisive wording or no wording at all.
3. **Direction lives in prose, not in the symbol.** The pill is direction-agnostic — "backs" lives in the composition note, never in the geometry. (You caught me reading frontality into pill-with-label-below; that was my projection, not what the symbol said.)

**Composition-note authority is real but not the goal.** The 5-jar drawing → 4-jar render in the earlier output proved prose governs symbol when they conflict — useful as a fact about the model, but the *goal* is to remove the conflict at the source. Authoritative prose over a contradictory drawing is a recovery mechanism, not a design.

---

## 2026-04-29 — from [[_trace/_notes/2026-04-29-canvas-read-exchange]]

**Load-bearing image as a craft pattern for image-gen workflows** — the canvas is full of WISH notes about wanting agent help babysitting GPT through image-gen iterations (the "compulsive chase" you named on the upper-left mid-canvas note). One concrete answer: before any iteration round, pre-identify which single panel carries the most narrative weight, name it explicitly in the prompt with an admonition to protect it through regenerations, and specify exactly which features must survive (composition, posture, expression, shape language). Then accept refinements only when those features survive. The new P3 script does this for the Charlie-watching panel — that pattern is reusable for any sequential image-gen and is worth atomizing if the vault doesn't have it. Maps to: the "spread of style options" wish, the "agentic intermediary" wish, and the perfectionist-chase compulsion you flagged as wanting outside help with.

**Charlie's resentment is colder than jealousy** — a small but story-changing distinction surfaced when refining the user's hypothesis: Charlie watching Mike with a girl reads weakly as sexual jealousy and very strongly as a recruiter clocking a holdout. The transcript supports the second reading and not the first (Charlie was offering the deal, Mike was half-accepting, the "wrong answer" was the predictable settlement of an unpaid contract). Worth holding because the same correction applies to most cult-recruitment stories — the lure-then-collect pattern reads better when the recruiter's interest is appraisal, not desire.

---

## 2026-04-30 — from [[_system/_design/HANDOFF-image-chase-and-comic-trace]]

**Lanes are horizontal bands, not vertical.** The Scroggins canvas looks like a left-to-right timeline with three y-bands (ANNOTATIONS above, ARTIFACTS in the middle, TRANSITIONS below), not three vertical columns. The lane-label text nodes are at x=-1700 at their respective y positions, and content flows rightward from there. This matters for the layout heuristic: placement is `x = rightmost_in_lane + gap`, y is fixed to the lane's band center.

**Color "1" is red in Obsidian, not purple.** The prototype legend says "purple = annotation" but all annotation nodes use `"color": "1"` which Obsidian renders as red. The design doc inherits this naming discrepancy. The skill uses color `"1"` for annotations (faithful to the prototype) and calls them "annotation" rather than "purple" in the legend. If you want the annotations to actually render purple in Obsidian, that would be `"color": "6"`. The belt-and-suspenders `[AGENT]:` prefix is the reliable distinguisher regardless of color.

**Vault file color: design says omit field, prototype uses "5".** The design doc says `color_default: cyan # i.e., omit color field` for vault file nodes, but the Scroggins prototype has `"color": "5"` on journal/hold/inbox nodes. The current implementation follows the design (omits the field). If the default rendering in Obsidian doesn't feel right, change `COLOR_CYAN = None` to `COLOR_CYAN = "5"` in `_system/_tools/comic-trace/lib/schema.py`.

---

## 2026-04-20 — from [[_reflection/2026-04-20-holdv04test]]

**The design instinct behind the ask** — the journaler isn't just amused by the Reddit post, they're treating cultural moments as tonal raw material and immediately asking what form the moment wants to be rendered in. The move from "this feels like a labor law poster" to "make me two prompts in two registers" is a single, fast gesture. That speed and direction — tonal register as a design lever you pull deliberately — is a live creative method here, not a stray observation.

**Novel thread — frames native to their content** — the comedy of the labor-law framing works because it isn't imposed on the material; it's discovered as already native to it (the playbook IS labor relations doctrine). Highlights-and-hides is adjacent but doesn't quite capture this. There's something worth an atom here: the difference between frames applied to material and frames that emerge as the material's own correct form.

**Nano banana gap** — the two image prompts were built from the tweet source text alone, without knowledge of what nano banana 1 looked like. If there's an established visual aesthetic or prior prompt format, the generated prompts may need calibration against it.

---

## 2026-04-25 — from [[_inbox/2026-04-25-scroggins-manson-3page-script]]

**The super-song model as comic structure** — applying the super-song atom to a 3-page comic worked cleanly because pages already function like movements: each has its own tonal register, and the challenge is exactly the one the atom names — "how you move between strikingly different registers while maintaining coherence." The transitional engine in this case is the retrospective narration caption: Mike's voice carrying foreknowledge the scene itself didn't yet have. Worth noting for future comic/sequential work that page-level tonal movement + caption-as-transition-engine is a reusable pattern the vault now has a name for.

**The suede jacket as throughline object** — in a three-page comic with no repeated location, character constellation, or through-plot, a single recurring visual object can do the coherence work. The jacket appears in every scene and carries the whole argument: the thing Mike didn't give away, the thing that let him leave. This is a note about how to solve the coherence problem in a short-form episodic comic — find the one object and hold it throughout. Might be worth an atom: the throughline object as compositional device in short-form narrative.

**The Nietzsche gap as live story hole** — the journal names a Nietzsche quotation Mike can't remember. The script leaves it blank deliberately, treating the forgetting as part of the story. But the prior hold reflection (2026-04-22) did the research and landed on Zarathustra "On the Voluntary Death" as the most likely candidate. If the user wants to add the actual quote, it's there in the reflection. This is a case where a memory-type file completed work the current collaboration could have used, but didn't import because it fell outside this session's scope.

---

## 2026-04-22 (run 2) — from [[_reflection/2026-04-22-holdv04b]]

**The Baudrillard near-miss as a useful null** — "forming a consensus reality (control)" looked like a simulacrum question on first pass: manufactured agreement replacing actual reality. But the mechanism doesn't fit. Baudrillard is about images and representation; what Manson was doing was interpersonal and ritual — not mediation but direct social manufacture of agreement through daily performance. The vault has Baudrillard but not the thing. The near-miss is itself diagnostic: the vault is strong on representation/epistemology at the image level but has no atom for the social or charismatic manufacture of consensus. That's a gap worth naming.

**Rerun perspective on the Nietzsche item** — running fresh without prior reflection, the same Zarathustra Prologue §3 candidates surfaced independently. The prior run landed there too (per builders_notes 2026-04-22). Two independent cold derivations pointing at the same passage is mild evidence the identification is right. Worth noting for Mike if this comes up again.

---

## 2026-04-22 — from [[_reflection/2026-04-22-holdv04test]]

**The jacket as atom gap** — the suede jacket item surfaced a genuine hole in the vault: no atom for quiet self-retention under totalizing pressure. The gesture (staying inside a system's logic while keeping one unrelinquished claim) is a real method — possibly the oldest one — and it doesn't map onto any existing atom. The permissive-membrane topology came closest structurally but is scoped to AI/vault systems. If this thread continues, it wants its own atom. The journaler's material is doing philosophy here, not just storytelling.

**The cross-cut shape** — "visiting and not arriving" turned out to be the through-line of the entire day's entry, not just a cross-cut observation. The jacket, the conditional answer, going home at night, Mike's sense of trouble — all the same gesture. The hold skill's cross-cut paragraph named a shape the journal itself didn't quite surface. That's a sign the pass structure is doing what it's supposed to do: the per-item work earns the cross-cut.

**Register note for asks with embedded research** — the Nietzsche item required research work (Zarathustra candidates, Heinlein mediation) but its candid section had to stay brief. The risk is that the research bulk crowds out the observation's warmth. In this case the observation IS the research — the item is a question, and the answer is the observation. The candid then notes what's uncertain about the answer. That triple structure (research as observation, candid as uncertainty envelope) worked cleanly here and may be worth making explicit in the skill definition for research-type asks.
