---
type: home
---

# Vault Home

## ✦ Journal
> `$= dv.fileLink("_journal/" + moment().format("YYYY-MM-DD"), false, "📝 Today's Journal →")`

## ✦ Capture

```dataviewjs
const date = moment().format("YYYY-MM-DD");
const n = dv.pages('"_inbox"').where(p => p.file.name.startsWith(date + "_")).length;
const name = `${date}_${String(n + 1).padStart(3, "0")}`;
const path = `_inbox/${name}.md`;

const a = dv.container.createEl('a', { text: '📥 Capture →', cls: 'internal-link' });
a.addEventListener('click', async (e) => {
  e.preventDefault();
  if (!app.vault.getAbstractFileByPath(path)) {
    const content = `---\ntype: inbox\nsubtype: \nfrom: \nresponds_to: \ncreated: ${date}\nprocessed: false\n---\n\n`;
    await app.vault.create(path, content);
  }
  app.workspace.openLinkText(name, '', false);
});
```

## ✦ Quick Links
- [[_system/VAULT_VISION|Vision]]
- [[_system/AGENT_PROTOCOL|Agent Protocol]]

---

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
>
>> [!note] Inbox (Unprocessed)
>> ```dataview
>> LIST FROM "_inbox"
>> WHERE processed = false
>> SORT file.name DESC
>> LIMIT 10
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

## ✦ Vault Health

<!-- ═══════════════════════════════════════════════════
     AGENT-WRITABLE ZONE: Vault Health
     The tend skill updates this section.
     ═══════════════════════════════════════════════════ -->

<!-- BEGIN AGENT ZONE: vault-health -->

_No tend report yet. Run `tend` to populate._

<!-- END AGENT ZONE: vault-health -->
