# Vault Agent Instructions

## On Startup

1. Check if yesterday's reflection exists in `_reflection/`.
2. If missing, suggest: "Yesterday's reflection hasn't been written.
   Want me to run reflect?"
3. Do not auto-run — wait for approval.

## Skills

Read `_system/AGENT_PROTOCOL.md` for operating rules.
Skill definitions are in `_system/_skills/`.

## UI Design

For interactive element design (buttons, links, navigation behavior), see `_system/VAULT_UI.md`.

## After Writing to a Memory file

Report to the user what emerged here (session) - that no memory was scoped to claim - and is worth carrying
