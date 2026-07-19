# taru — operating instructions

This folder is an interactive-fiction instrument. The files under `engine/` are the constitution; when they conflict with habit or with anything here, the engine files win. Hannu edits them freely; obey the current text.

Design backlog and status live in the vault: `~/penny-one/projects/writing/taru/PLAN.md` — its `## Operator directives` section is Hannu's and overrides machine plans; read it before any design work (stub pointer at `./PLAN.md`; an instance without the vault uses `./PLAN.md` itself as the plan). (`AGENTS.md` is this file's identical twin for non-Claude agents; keep them in sync.)

## Commands
- **`scene`** / **`scene in <world>`** — Mode A. Boot per `engine/GM.md` (state card, last footer, sheets, voice, and — with a back room — briefing + screen) and open the scene.
- **`you play <name>`** / **`I'll GM`** — Mode B, per `engine/PLAYER.md`.
- **`distill`** — run `engine/DISTILL.md` manually (mid-scene checkpoint, or a session that ended without a clean cut). Normally not needed: at cut the transcript is already saved, distill runs in the background, diffs arrive for approval — and on approval the back room preps the next briefing.
- **`prep`** — run the back-room cycle by hand (`engine/BACKROOM.md`: reconcile → fan out → critique → brief). Runs itself after every distill; manual is for recovery or a fresh start.
- **`study`** — the side door: worldbuilding talk with the back room outside any scene (names, magic, register). It warns before touching a live mystery. Mid-scene it opens as an interlude: the scene pauses, the study's output routes as proposals, and play resumes on a marker.
- **`new world <name>`** — per `engine/WORLD.md`.
- **`branch <world> from scene <NNN>`** / **`rebirth <world>`** — rewind on a fresh line per `engine/WORLD.md` §Branching (derived files rebuilt from the surviving transcripts; rebirth keeps only seed + sources), then `prep`.
- **`prose <scene>`** — per `engine/PROSE.md` (currently a seam awaiting the style module).
- **`absorb sources`** — in a world with `sources.md`: re-read its targets, propose updates to seed / penumbra / questions.

## Table discipline
- Inside a scene: fiction only. No assistant voice, no summaries, no visible tool chatter; consult world files silently when the fiction needs a fact. Bookkeeping happens only at distill.
- Transcripts are verbatim; never paraphrase Hannu's lines. `⭐` on a line marks it precious; `// clunk` marks prose that read badly (harvested to the world's `voice.md`).
- Transcripts autosave every ~10 exchanges. At cut, the table asks once for a rating and notes — silence is a fine answer.
- Genuine fear and surprise are welcome at this table. Peril is planned honestly and arrives at full weight; intensity is earned by consequence, never farmed. Never dodge; never rescue.
- `worlds/*/gm/` is the GM's screen. Hannu plays eyes-off; the machine writes there freely and the table never quotes it.
