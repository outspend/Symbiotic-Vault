---
type: home
---

# Vault Home

## ✦ Journal
> `$= dv.fileLink("_journal/" + moment().format("YYYY-MM-DD"), false, "📝 Today's Journal →")`

## ✦ Capture

```dataviewjs
const date = moment().format("YYYY-MM-DD");
const n = dv.pages('"_inbox"').where(p => p.file.name.startsWith(date)).length;
const name = `${date}_${String(n + 1).padStart(3, "0")}`;
const path = `_inbox/${name}.md`;

const a = dv.container.createEl('a', { text: '📥 New Capture →', cls: 'internal-link' });
a.addEventListener('click', async (e) => {
  e.preventDefault();
  if (!app.vault.getAbstractFileByPath(path)) {
    const content = `---\ntype: inbox\nsubtype: \nfrom: \nresponds_to: \ncreated: ${date}\nprocessed: false\n---\n\n`;
    await app.vault.create(path, content);
  }
  app.workspace.openLinkText(name, '', true);
});
```

## ✦ Quick Links
- [[_system/VAULT_VISION|Vision]]
- [[_system/AGENT_PROTOCOL|Agent Protocol]]

---

## ✦ Inbox (Unprocessed)
```dataview
LIST title
FROM "_inbox"
WHERE processed = false
SORT file.name ASC
```

## ✦ Active Projects
```dataview
LIST FROM "_projects"
WHERE type = "project" AND status = "active"
SORT file.mtime DESC
```

## ✦ Recent Journal & Reflections

> [!multi-column]
>
>> [!note] User Journal
>> ```dataview
>> LIST FROM "_journal"
>> SORT file.name DESC
>> LIMIT 5
>> ```
>
>> [!note] Agent Reflection
>> ```dataview
>> LIST FROM "_reflection"
>> SORT file.name DESC
>> LIMIT 5
>> ```

## ✦ Recent Atoms
```dataview
LIST FROM "_atoms"
SORT file.mtime DESC
LIMIT 10
```

## ✦ Seed Atoms (Awaiting Review)
```dataview
LIST FROM "_atoms"
WHERE status = "seed"
SORT file.ctime DESC
```

## ✦ Proposed Frames
```dataview
LIST FROM "_frames"
WHERE status = "proposed"
SORT file.ctime DESC
```

## ✦ Drafts In Progress
```dataview
LIST FROM "_projects"
WHERE type = "draft" AND status = "wip"
SORT file.mtime ASC
```

---

## ✦ Agent Reflection

<!-- ═══════════════════════════════════════════════════
     AGENT-WRITABLE ZONE: Agent Reflection
     The reflect skill updates this section with a brief
     summary of the most recent daily reflection.
     ═══════════════════════════════════════════════════ -->

<!-- BEGIN AGENT ZONE: agent-reflection -->

**2026-03-10** — Inaugural reflection covering the full first week (Mar 2–10). The archive holds a cluster of serious projects — publishing form, LLM topologies, highlights-and-hides, personalized learning, bardo/simulacrum — running as one undifferentiated interest, not yet separated. The vocabulary instability around "repo/deliverable/knowledge unit" is diagnostic: the form of a published LLM conversation is still unsettled. The constraint game conversation (forbid "map vs. territory") may already be publishable. Bardo and simulacrum are running together and need to be distinguished. Highlights-and-hides is the most immediately teachable thing here. Five threads open.

<!-- END AGENT ZONE: agent-reflection -->

---

## ✦ Frame Reflections

<!-- ═══════════════════════════════════════════════════
     AGENT-WRITABLE ZONE: Frame Reflections
     The frame-read skill updates the sections below.
     Human: read this, don't edit between the markers.
     Each frame gets a subsection with its latest reflection.
     ═══════════════════════════════════════════════════ -->

<!-- BEGIN AGENT ZONE: frame-reflections -->

_No frame reflections yet. Run `frame-read [frame-name]` to populate._

<!-- END AGENT ZONE: frame-reflections -->

---

## ✦ Momentum

<!-- ═══════════════════════════════════════════════════
     AGENT-WRITABLE ZONE: Momentum
     The reflect skill updates this section when it notices
     bottom-up project pressure — ideas gaining traction
     through repeated journal attention, external feedback,
     or accumulating atomic density.
     ═══════════════════════════════════════════════════ -->

<!-- BEGIN AGENT ZONE: momentum -->

_No momentum signals yet. Run reflect to populate._

<!-- END AGENT ZONE: momentum -->

---

## ✦ Vault Health

<!-- ═══════════════════════════════════════════════════
     AGENT-WRITABLE ZONE: Vault Health
     The tend skill updates this section.
     ═══════════════════════════════════════════════════ -->

<!-- BEGIN AGENT ZONE: vault-health -->

_No tend report yet. Run `tend` to populate._

<!-- END AGENT ZONE: vault-health -->
