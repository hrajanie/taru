# settings.md — Minds and budgets

Which model runs which role. Hannu edits freely; the next boot or cycle picks it up. Every artifact records its maker — plays and prep are attributable to the minds that drove them (DISTILL.md §1, BACKROOM.md).

| Role | Model | Effort | Notes |
|---|---|---|---|
| table (storyteller) | session model — Fable | high | set with `/model` + `/effort`; high confirmed good, xhigh too slow (2026-07-09) |
| distill | fable | high | canon fidelity is cheap to keep, expensive to lose |
| reconcile + brief | fable | high | judgment-heavy; owns screen, arc, poetics |
| scene smith (fan-out) | fable | high | try sonnet once briefing quality is established |
| critic: canon | sonnet | — | retrieval + comparison — Sonnet-workhorse trial |
| critic: player-sim | fable | high | must model Hannu from thin evidence |
| critic: poetics | fable | high | taste |
| critic: emotion | fable | high | taste |
| critic: momentum | sonnet | — | Sonnet-workhorse trial |
| quick-prep | table session | — | inline, two minutes |

**Budget levers** (cycle size): fan-out 4–6 · revision rounds 1–2 · critics 5. A full cycle ≈ 300–600k tokens as configured. To shrink: fan-out to 3 and rounds to 1 *before* dropping critics; drop the Sonnet critics last (they're nearly free).

**Effort column** applies where the harness allows it. Claude Code subagents currently take a model but not an effort; the table takes both via `/model` and `/effort`; a future table-runner wrapper takes both per call. Record `?` rather than guess.

**Reading the trial:** journal entries stamp who made what. If a Sonnet-made verdict or briefing reads as well as a Fable one, promote Sonnet to that role and bank the budget.

*Per-table file: an instance tunes its own minds and budgets here; upstream updates never overwrite it.*
