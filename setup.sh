#!/usr/bin/env bash
# taru — make this instance yours.
#
# Usage: ./setup.sh "Your Name"
#
# Replaces the operator's name in the engine and operating instructions —
# never in worlds/, where the Qelán play record keeps its author — and resets
# PLAN.md to a fresh instance plan. Run once, in your own fork or copy.
set -euo pipefail
cd "$(dirname "$0")"

NAME="${1:-}"
if [ -z "$NAME" ]; then
  printf 'Player name: '
  read -r NAME
fi
if [ -z "$NAME" ]; then
  echo "A name is required." >&2
  exit 1
fi

if ! grep -q 'Hannu' CLAUDE.md 2>/dev/null; then
  echo "Already personalized (no 'Hannu' left in CLAUDE.md). Nothing to do."
  exit 0
fi

export TARU_NAME="$NAME"
for f in CLAUDE.md AGENTS.md engine/*.md; do
  perl -pi -e 's/\bHannu\b/$ENV{TARU_NAME}/g' "$f"
done

cat > PLAN.md <<'EOF'
# taru — PLAN

Living roadmap and design backlog for this instance. The `## Operator directives`
section is the operator's: never machine-rewritten, and it overrides machine plans.
Read this file before any design work.

## Operator directives

*(none yet)*
EOF

echo "Done. This table now answers to ${NAME}."
echo
echo "Next:"
echo "  1. Skim engine/ — it is the constitution, and it is yours to amend."
echo "  2. Open this folder in Claude Code (or any AGENTS.md-reading agent) and say:"
echo "       rebirth qelan      — the recommended first play: Qelán again from its"
echo "                            first image, with a hidden world all your own"
echo "                            (README: door one; to continue from scene 008"
echo "                            instead, say 'prep' then 'scene in qelan')"
echo "       new world <name>   — or birth your own world (engine/WORLD.md); have"
echo "                            pages already? point worlds/<name>/sources.md at"
echo "                            them and say 'absorb sources' (README: door two)"
echo
echo "Pronouns: engine/GM.md and engine/PLAYER.md refer to the player in the third"
echo "person; adjust to taste — they are your files now."
