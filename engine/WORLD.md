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
