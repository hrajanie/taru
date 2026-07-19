# WORLD.md — Worlds

A world is a folder under `worlds/`. Everything the fiction has established lives there in plain Markdown; the engine is model-agnostic because the folder *is* the game.

```
worlds/<name>/
  seed.md         one image, one law, one wrongness, five tone words;
                  grammar defaults; "how this world plays" (world-rules)
  sources.md      (optional) scripture — external source docs; true vs believed
  canon.md        facts established through play, cited by scene
  penumbra.md     soft canon — said once, still revisable
  questions.md    the deliberately unwritten; may stay open forever
  threads.md      open loops, with ages — the long story's granary
  retcons.md      ledger of what the hidden world quietly became
  state-card.md   the boot artifact (see DISTILL.md §4)
  voice.md        the table voice guide — rulings grown from clunks and margins (cap: one page)
  ideas.md        (optional) the quarry — unplayed material harvested from
                  branches and asides, with provenance; binds nothing until played
  characters/     <name>.md sheets; <name>.hidden.md interiors (mode B)
  scenes/         NNN-slug.md transcripts with footers
  gm/             the back room — screen, arc, poetics, journal, ledger, briefings.
                  Eyes-off for the player; see engine/BACKROOM.md
```

## Birthing a world ("new world <name>")
Ask for — or derive from whatever Hannu gives — the seed: **one image** (what you'd see on the cover), **one law** (the physics that makes this world itself), **one wrongness** (what is already broken or beginning), **five tone words**. Create the folder and empty files; write an initial state card ("no scenes played; …"). Do not create character sheets — sheets are born in play.

## Branching
A world forks at three scales: a whole **instance** (a fork of the repo — sovereign, never merged), a **line** (a git branch or worktree carrying an alternate continuity), and a **what-if** (`worlds/<w>/branches/<name>/` with its own copies of the mutable files and its own scenes numbered from the fork point; seed, sources, and questions inherit from trunk).

And a world can be **rewound**: everything except `seed.md`, `sources.md`, and the transcripts is derived state, so any earlier table can be rebuilt. On `branch <world> from scene NNN` — always on a fresh line, never in place on trunk — set aside the scenes past NNN, prune every entry cited past NNN from canon, threads, penumbra, retcons, and the sheets' observed truths, regenerate the state card from what remains, and let `prep` author a fresh hidden world. Keep `voice.md` whole: its rulings are craft, not plot. On `rebirth <world>`, keep only seed and sources — the world returns to the morning before its first scene, with any unplayed openings still standing.

Stories don't merge; ideas do. Harvest a dead branch's inventions into `ideas.md` with provenance, and let prep respend them.

## Precedence
1. **Scripture is physics.** If `sources.md` names sources marked *true*, play never contradicts them; only Hannu edits scripture.
2. **In-world documents may lie.** A source marked *believed* (an in-universe text) binds what NPCs think, not what is true. The gap between believed and true is the GM's playground.
3. **Play-canon binds play.** `canon.md` outranks memory and invention; `penumbra.md` bends before it breaks.
4. **Questions stay open.** Items in `questions.md` are materialized lazily or never; resist resolving them just because a scene brushes one.
5. **Drafts bind nothing.** A source marked *draft* (Hannu's rough scenes, sketches, fragments) is quarry: a soft pre-plot the GM mines for places, people, and beats — and that play freely retcons. Playing through a draft is the point; what survives contact becomes canon at distill, and the draft-vs-played delta goes in the ledger. On `absorb sources`, scene-shaped drafts become unplayed scene seeds in `threads.md`; fact-shaped material is proposed for seed / penumbra / questions.

## Character sheets
```
# <Name>
wound: · desire: · mask: · secret: · body:        (five lines)

## Voice             a short first-person monologue; the sound of them thinking
## Bonds             how they treat three specific people
## Memories          (worlds with costs) what the self still holds
## Observed truths   append-only; only play writes here, cited (sc NNN)
```
A world's rules may extend the sheet — Qelán strikes Memories as tolls are paid.
