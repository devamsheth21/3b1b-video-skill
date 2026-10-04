#!/usr/bin/env bash
# Install the explainer-video skill into every coding agent found on this machine.
# Usage: ./scripts/install.sh
# Safe to re-run: existing installs are replaced.
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILL_SRC="$REPO_DIR/skills/explainer-video"
SKILL_NAME="explainer-video"

install_to() {
  local dest="$1"
  mkdir -p "$(dirname "$dest")"
  rm -rf "$dest"
  cp -r "$SKILL_SRC" "$dest"
  echo "installed -> $dest"
}

installed_any=false

# Claude Code (global)
install_to "$HOME/.claude/skills/$SKILL_NAME" && installed_any=true

# Codex CLI (global)
install_to "$HOME/.codex/skills/$SKILL_NAME" && installed_any=true

# Generic / agent-agnostic locations
install_to "$HOME/.agents/skills/$SKILL_NAME" && installed_any=true
install_to "$HOME/skills/$SKILL_NAME" && installed_any=true

echo ""
echo "Done. The skill triggers on phrases like:"
echo '  "create a 3b1b style video explainer on <topic>"'
echo '  "make an animated explainer video about <topic>"'
echo ""
echo "Notes for project-local setups (run inside your project dir):"
echo "  Cursor:      cp -r $SKILL_SRC .cursor/skills/$SKILL_NAME"
echo "  Antigravity: cp -r $SKILL_SRC .agents/skills/$SKILL_NAME"
echo "  Aider/other: point it at $SKILL_SRC/SKILL.md"
