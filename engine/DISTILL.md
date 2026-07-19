# DISTILL.md — The After-Pass

Run when a scene ends, or when Hannu says "distill." This is bookkeeping: record the world, not the player. No interpretation of the session, no analysis of anyone at the table — the files hold the fiction only.

## 1. Save the transcript
`worlds/<world>/scenes/NNN-slug.md` (NNN sequential, zero-padded). The file is born at boot and autosaved through play (GM.md §Scene shape); at distill, verify it is complete. Speaker-tagged, verbatim — Hannu's lines are never paraphrased, trimmed, or corrected. A `⭐` anywhere on a line marks it precious: preserved verbatim if the scene is ever converted to prose.

Open the file with YAML frontmatter, including the **engine metadata** — every play is attributable to the minds that drove it:

```yaml
---
scene: 001
played: 2026-07-07            # real date
mode: A                       # A: Hannu plays · B: Hannu GMs
table:
  model: claude-fable-5       # model running the scene
  effort: low                 # if known
  speed: standard             # standard | fast (Opus fast mode)
  harness: claude-code        # claude-code | codex | wrapper | other
gm-prep: gm/briefings/NNN.md  # or none — bare play; the attribution field
where: <in-world time and place>
present: <characters in the scene>
---
```

Record what is actually known: in Claude Code the assistant knows its own model; it may not know the session's effort setting. Use `?` for anything uncertain — never guess — and let Hannu correct at distill.

## 2. Footer (appended to the scene file)
- **Summary** — ≤8 lines, events only.
- **New canon** — facts now fixed, one line each.
- **Threads** — opened / advanced / closed.
- **Retcons** — what the hidden world quietly became, one line each.
- **Margins** — every `//` line except clunks, verbatim, in order. Never paraphrased.
- **Clunks** — every `// clunk` line, verbatim.
- **Table feedback** — the rating (if given) and his notes at cut, verbatim. Silence is a valid answer.
- **Open questions** — raised and unanswered.

## 3. Propose diffs, apply on approval
One compact block, then apply when Hannu approves:
- `canon.md` — appends under People / Places / Things / History / Laws / Promises, cited (sc NNN)
- `threads.md` — updates, with ages (born sc NNN · last touched sc NNN)
- character sheets — **Observed truths** appends (only play writes there); world-rule costs applied (e.g. Qelán: memories struck)
- `penumbra.md` — soft facts mentioned once
- `retcons.md` — ledger lines
- margin routing (proposals only, cited sc NNN): coherence questions → `questions.md` · world-ideas → `penumbra.md` · arc-thoughts → `threads.md`. Route in Hannu's own words; never interpret beyond choosing the destination.
- `voice.md` — when clunks or style margins show a pattern, propose a ruling: the evidence verbatim, cited, then the rule.
- `state-card.md` — regenerated (below)
- `gm/journal.md` — the scene's entry (engine config · what worked · feedback verbatim · registers hit). `gm/` is the machine's side of the table, written without approval (`engine/BACKROOM.md`); everything above still requires it.

## 4. The state card (regenerate every distill; hard cap ~600 words)
The boot artifact: with `seed.md`, the active sheets, and this card, a cold model must be able to run the next scene faithfully.
- **Now** — the situation, ≤5 lines.
- **Who** — each active character, one line of current state.
- **Pressure** — the open tensions that bear on the next scene, ≤7.
- **Fixed** — recent canon that must not be contradicted, ≤10 lines.
- **Tone** — the seed's five words + grammar defaults.

Older detail lives in `canon.md`; the card trusts the files rather than repeating them. With a back room, boot also includes `voice.md`, `gm/screen.md`, and the current briefing — the card points, never repeats.

## 5. Hand off to the back room
After the diffs are approved, spawn the back-room cycle (`engine/BACKROOM.md`) in the background: reconcile → fan out → critique → revise → brief. It writes only under `gm/`, leaves `gm/briefings/<next>.md` ready, and reports one line when done — never its contents.
