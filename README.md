# taru

*Taru* (Finnish: tale, saga, myth) is an instrument for discovering worlds and characters by playing them, with an LLM on one side of the table. Not a game engine: a space. The good stuff comes from the world and the characters.

Two modes, one folder of state:
- **Mode A** — you play a character; the model runs the world (`engine/GM.md`).
- **Mode B** — you run the world; the model inhabits a character (`engine/PLAYER.md`).

The loop: **scene → distill → back room → next scene.** Scenes are pure fiction, no bookkeeping. Distill (`engine/DISTILL.md`) saves the verbatim transcript, fixes new canon, ages the threads, and regenerates the state card — the small artifact that lets scene 041 remember scene 003. Between scenes, the back room (`engine/BACKROOM.md`) reconciles the hidden world and preps the next director's notes behind the GM screen. Short scenes; long story.

Everything is plain Markdown, so this runs on any model: hand it `engine/GM.md` plus the world's `state-card.md`, `seed.md`, the active sheets, and the last scene's footer — that bundle *is* the engine. In Claude Code, open this folder and say **`scene in qelan`** (the commands live in `CLAUDE.md`; `AGENTS.md` is its identical twin for other agents).

## What's here

```
engine/       the constitution — GM, player, distill, back room, worlds, settings
worlds/qelan  the example play: Qelán (The Sealed Radiance) — seed, canon,
              character sheets, and the verbatim transcripts of every scene
CLAUDE.md     operating instructions (Claude Code); AGENTS.md is its twin
setup.sh      makes a fork yours — see "Your own instance" below
CHANGELOG.md  what changed between tagged versions
```

## The example play: Qelán

Seven scenes and one branch, played July 2026, Mode A. The transcripts are in `worlds/qelan/scenes/`, verbatim, each with a footer (summary, new canon, threads, open questions). Reading them in order is the best introduction to what this instrument does.

| Scene | Title | Notes |
|---|---|---|
| 001 | the man who walked out | bare play — no back room yet |
| 002 | the first night | bare play |
| 003 | the latch | first briefed scene; its **Take A** sits in `scenes/branches/` — same opening played twice, once bare and once with the back room, to decide whether the back room earned its rent (it did) |
| 004 | the rain | |
| 005 | the fourth night | |
| 006 | qam | |
| 007 | the greying | |

Conventions you'll see in the transcripts: `⭐` marks a line precious (preserved verbatim if the scene ever becomes prose); a line starting `// ` is **marginalia** — the author thinking alongside the character, which the fiction never acknowledges; `[table: …]` is the one channel where the table itself may speak.

**The GM's screen is not in this repo.** `worlds/qelan/gm/` — the hidden-world hypotheses, the arc in pencil, the director's briefings — is sealed while Hannu is still playing, and will be published as an afterword when book one cuts. What you see in `worlds/qelan/` is exactly what the player's side of the table sees. (One small redaction beyond that: character sheets travel without their `secret:` line — that framing is the screen's.) The world's scripture (the Qelán worldbible and Codex) lives in a separate writing project and is likewise not included; play never needed to read it — `canon.md` and the state card carry everything the table established.

The world's `voice.md` is worth special attention: it is the table's prose style, grown ruling by ruling from actual play — each ruling cites the margin note that earned it. The transferable core of those rulings has been folded back into `engine/GM.md`, so new worlds start with the voice this one had to learn.

## Your own instance

Instances are meant to be sovereign: your table, your worlds, your hidden state, no upstream. The fastest path:

1. **Make your own repo from this one.** On GitHub: **Use this template** → create your repo (private is sensible — your future `gm/` folders hold your story's secrets). A plain fork or a clone pushed to a fresh repo works the same.
2. **Make it yours:** `./setup.sh "Your Name"` — replaces the operator's name in the engine and operating instructions (never in the Qelán play record), so the table addresses you. The engine files are now yours to edit; they are the constitution, and the constitution is meant to be amended by its player. Adjust pronouns in `engine/GM.md`/`engine/PLAYER.md` to taste.
3. **Sit down.** Open the folder in Claude Code and pick a door:

**Door one — a world from nothing.** Say **`new world <name>`**. The birth ritual (`engine/WORLD.md`) asks for four things — one image, one law, one wrongness, five tone words — and play begins from there. Character sheets are born in play; nothing else is required.

**Door two — a world from your own pages.** If you already have material — a draft, a worldbible, fragments of a novel — the engine is built to eat it. Say `new world <name>`, then write `worlds/<name>/sources.md`: a short table pointing at your documents (paths inside the repo or anywhere on disk), each marked with a status:

- ***true*** — scripture. Physics; play never contradicts it.
- ***believed*** — an in-world text. It binds what people think, not what is; the gap between believed and true is the GM's playground.
- ***draft*** — rough scenes, sketches, fragments. Quarry: a soft pre-plot the GM mines for places, people, and beats, and that play freely retcons. Playing *through* a draft is the point — what survives contact becomes canon.

Then say **`absorb sources`** — the table reads the targets and proposes updates to the seed, the penumbra, and the open questions; scene-shaped drafts become unplayed scene seeds. (`worlds/qelan/sources.md` is the worked example of the format.)

**Door three — continue Qelán from scene 008.** Say **`prep`** first: a fresh back room will read the canon, threads, and open questions and author its *own* hidden world — which diverges from Hannu's sealed one immediately. Then **`scene in qelan`**. Two players continuing from the same seven scenes will discover two different stories. That is not a limitation; it is the instrument working.

You don't have to pick up where the played line left off, either. A world can be rewound to any scene: say **`branch qelan from scene 001`** and the table sets aside the later transcripts, rebuilds the world files from what remains, and `prep` authors a fresh hidden world from there (`engine/WORLD.md` §Branching). Or go all the way back — **`rebirth qelan`** returns the world to the morning before its first scene. The default opening is the same image the played line began with: **the Sealed One walking out of cracked Berzhár, with no memory**. Diegetically the story can't start earlier — the waking burns away the memory of it, so play begins where his remembering does. Two lines from the same first image will diverge by the second turn, and the seed lists other doors besides.

Requirements: [Claude Code](https://claude.com/claude-code) (or any agent harness that reads `AGENTS.md`). No other dependencies — the folder is the game.

If you play, Hannu would love to hear how it went — open an issue on this repo, or bring him the tale directly.

## Branching

Branch freely, at every scale:

- **Instances** are whole independent games — template/fork per person, never merged.
- **Lines** within an instance: git branches (or worktrees) fork a whole alternate continuity from any scene — Qelán's scene 003 was played twice this way, and the losing take was kept whole on its own branch.
- **What-ifs**: for a single-scene fork, a `worlds/<w>/branches/` folder with its own copies of the mutable files is enough — see `engine/WORLD.md`.

Stories don't merge; *ideas* do. When a branch dies, its good inventions are harvested with provenance into the world's `ideas.md` (the quarry), where future prep can respend them. If you and another player want to trade discoveries across instances, trade quarry, not canon.

## Versioning

Tagged releases (`v0.1.0`, …) with a human `CHANGELOG.md`. The engine keeps evolving at Hannu's table; updates are published here from the private working copy (with `gm/` and other sealed material stripped). To take an engine update into your instance without disturbing your worlds: pull or cherry-pick changes under `engine/`, `CLAUDE.md`, `AGENTS.md` — worlds are never touched by upstream.

## Provenance

The Qelán scenes were played with Claude (Fable 5) in Claude Code; every scene's YAML frontmatter records the model, effort, and prep that drove it — plays are attributable to the minds at the table. The engine itself is model-agnostic by design: same folder, different mind is an experiment, and differences are data.
