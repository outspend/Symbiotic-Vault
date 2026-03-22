---
type: system
id: vault-ui
---

# Vault UI Design

Interactive element patterns for this vault. When building or modifying buttons, links, or navigation elements, follow these conventions.

---

## Two Button Modes

Interactive buttons in this vault follow one of two modes. Choose based on whether a context should have one file or many.

---

### Mode A — Single-Reference (create-or-navigate)

**When to use:** One file per context. The button creates the file if it doesn't exist, then navigates. On return, it navigates directly. Button text reflects state.

**Examples:** Today's Journal, reply to a reflection.

**Pattern:**
```javascript
const filePath = `folder/filename.md`;
const fileExists = app.vault.getAbstractFileByPath(filePath);
const linkText = fileExists ? '→ View [thing]' : '↩ Create [thing] →';

const a = dv.container.createEl('a', { text: linkText, cls: 'internal-link' });
a.addEventListener('click', async (e) => {
  e.preventDefault();
  if (!fileExists) {
    await app.vault.create(filePath, content);
  }
  app.workspace.openLinkText(filename, '', false);
});
```

**Rules:**
- Deterministic filename — no sequential numbering
- Dynamic text: action label when absent, navigation label when present
- `openLinkText(..., false)` — opens in current pane, back arrow works
- Re-clicking never creates a duplicate

**Naming convention for single-reference files:**

| Type | Convention | Example |
|---|---|---|
| Daily journal | `YYYY-MM-DD` | `_journal/2026-03-21.md` |
| Daily reflection | `YYYY-MM-DD` | `_reflection/2026-03-21.md` |
| Reflection reply | `reply-YYYY-MM-DD` | `_inbox/reply-2026-03-19.md` |

---

### Mode B — Always-Create (append-only)

**When to use:** Multiple files per context are expected. The button always creates a new file. Static text. Discovery of existing items is handled elsewhere (e.g., a dataview list), not by the button.

**Examples:** Capture. A capture session is discrete — you may capture several things in a day, each gets its own file.

**Pattern:**
```javascript
const date = moment().format("YYYY-MM-DD");
const n = dv.pages('"_inbox"').where(p => p.file.name.startsWith(date + "_")).length;
const name = `${date}_${String(n + 1).padStart(3, "0")}`;
const path = `_inbox/${name}.md`;

const a = dv.container.createEl('a', { text: '📥 Capture →', cls: 'internal-link' });
a.addEventListener('click', async (e) => {
  e.preventDefault();
  if (!app.vault.getAbstractFileByPath(path)) {
    await app.vault.create(path, content);
  }
  app.workspace.openLinkText(name, '', false);
});
```

**Rules:**
- Sequential filename — `YYYY-MM-DD_NNN`
- Static text — always signals a new action
- `openLinkText(..., false)` — opens in current pane
- Existing items surface via dataview list, not the button

**Naming convention for always-create files:**

| Type | Convention | Example |
|---|---|---|
| Inbox capture | `YYYY-MM-DD_NNN` | `_inbox/2026-03-21_001.md` |

---

## Static Wikilink (no JavaScript)

For the simplest case — navigate to a file, let Obsidian handle create-if-missing natively:

```
> `$= dv.fileLink("_journal/" + moment().format("YYYY-MM-DD"), false, "📝 Today's Journal →")`
```

Use this when there's no create logic needed and Obsidian's native behavior is sufficient. The Journal link on HOME.md uses this; the journal template handles the initial content.

---

## Navigation Convention

**Always use `openLinkText(name, '', false)`** — `false` opens in the current pane. The user can use the back arrow to return. Never use `true` (new leaf) unless explicitly opening a parallel view.

---

## Where These Patterns Are Used

| Location | Mode | Notes |
|---|---|---|
| `HOME.md` → Journal | Static wikilink | Obsidian handles create-if-missing |
| `HOME.md` → Capture | Mode B (always-create) | Sequential NNN; list on HOME.md shows unprocessed |
| `_reflection/*.md` → Reply | Mode A (single-reference) | `reply-YYYY-MM-DD`; dynamic text |
