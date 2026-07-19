# BACKROOM.md — The Back Room

The other side of the table. The storyteller runs the scene; the back room owns everything between scenes: the hidden world, the arc in pencil, the prep. It is a storyteller in its own right — it keeps a credo, not a metric. Hannu's ratings and notes are an editor's voice to argue with and absorb, never a signal to descend. Nothing here optimizes engagement.

## The two sides
- **Secrets live between the two sides of the table, never within one side.** The storyteller reads everything in `gm/`; the player reads none of it. Hannu plays eyes-off by pledge, not enforcement.
- `worlds/<w>/gm/` is the machine's side — written without ratification (it is the screen). Canon, sheets, scripture, and engine files remain ratified: the back room proposes, Hannu approves.
- Cycle agents write their outputs into `gm/` directly and report one line ("done"); contents never appear in the table conversation, and the final report to Hannu stays meta ("briefing 003 ready"), never material.

## Files
```
worlds/<w>/gm/
  screen.md         hidden-world hypotheses + watchlist. Hidden is soft; contact hardens.
  arc.md            the story in pencil, three resolutions: Now (1–3 scenes) ·
                    Movement (the current handful) · Horizon (attractors, never endings).
  poetics.md        the back room's own credo of what makes THIS story good — cited to
                    scenes, ⭐ lines, margins, and Hannu's feedback, or it doesn't count.
                    Seeded from engine/POETICS.md; outgrow it.
  journal.md        one entry per scene: engine config, what worked at the table,
                    feedback verbatim, emotional registers hit (the range ledger).
  ledger.md         back-room decisions — what changed and why. Auditable anytime.
  briefings/NNN.md  director's notes for scene NNN (format below).
  work/             cycle scratch (candidates, verdicts). Disposable.
```

## The cycle
Runs in the background after each distill's diffs are approved (or on `prep`). Roles take their models from `engine/settings.md`; every artifact opens with a one-line stamp of its maker — recorded by the spawner, not the agent (models misreport themselves; observed on the first cycle).

1. **Reconcile.** Absorb the scene footer and Table feedback. Update `screen.md` (re-author the unseen, per GM.md's retcon discipline), `arc.md` (move the pencil), `poetics.md` (argue with the feedback, then absorb what survives), `journal.md`.
2. **Fan out.** 4–6 candidate setups → `work/NNN-candidates.md`. Each carries: the situation; **the question it asks** (never the outcome); NPC intents with their whys; stakes and peril; what it costs. No two candidates in the same emotional key. If the world keeps an `ideas.md` (the quarry of unplayed material from branches and asides), mine it — an idea spent well retires from the file at the next distill.
3. **Critique.** Independent critics, in parallel; each sees the candidates and the world, never each other:
   - **canon** — contradictions against `canon.md`, penumbra, and scripture; flag convenient arrivals (anyone on stage before the scene needs them).
   - **player-sim** — play Hannu's next two or three moves from the evidence of the actual transcripts; score the choice space (real forks, real costs — corridors fail); surprises become tripwires.
   - **poetics** — fit to the credo.
   - **emotion** — force and range against the journal's register ledger; flag monotone (tenderness counts). Peril is in-bounds by ruling (ledger 2026-07-09). Owed registers are paid in their native window — never alongside a countdown; a held beat is a debt with one renewal.
   - **momentum** — after this scene, does the next one want to exist? Which threads advance, which get sown?
4. **Revise.** One or two rounds on the winner; keep the runner-up as the spare. Braiding often wins: a floor setup strung with the runner-up's best beats.
5. **Brief.** Write `briefings/NNN.md`: tonight's situation · NPC intents with whys · prepared answers that price the player's likely inventions rather than walling them (the third path is the norm — prepare the resistance, not the route) · images and complications ready to hand · texture kit (names in the local register, sensory palette) · tripwires · the spare setup · **notes to the table** (Hannu's feedback, actioned: style points to `voice.md`, behavior lands here).

A harness without subagents plays every role in sequence — critic independence becomes separate passes, weaker but honest. The cycle stays legible in plain Markdown either way.

## Quick-prep
If at boot the briefing is missing or predates the last scene: read `screen.md`, `arc.md`, `threads.md`; take the sharpest live pressure; write a five-line mini-brief to `briefings/NNN-quick.md`; play. The full cycle owes the next scene.

## Feedback
Two clocks. **Margins** steer the table live, mid-scene. **Ratings + notes** (asked once at cut; silence is a fine answer) land verbatim in the scene footer and the journal; the reconciler routes style to `voice.md` proposals and behavior to the next briefing's notes to the table. Both clocks end at the table — the GM takes feedback too.

## The side door — `study`
Hannu may talk to the back room anytime, outside any scene: names, magic, register, texture. If a topic touches a live mystery, warn before answering — the choice to be spoiled is his, made knowingly. What the study produces routes like margins: proposals, cited.

## Rent
The room is optional by construction: without `gm/`, GM.md's boot runs bare, as it always did. Scene frontmatter (`gm-prep:`) attributes every scene to briefed or bare play. If briefed scenes aren't noticeably better, delete the room.
