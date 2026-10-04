# 3b1b-video-skill

An **agent-agnostic skill** that turns any topic into a narrated **3Blue1Brown-style animated explainer video** — generated as code, not diffusion.

Inspired by [Andrej Karpathy's October 2026 post](https://m.twstalker.com/brus_lattice/status/2105912733715579030): the output format he is "most bullish on" is *"fully custom / bespoke explainer videos generated on any arbitrary topic"*, e.g. *"Create a 3b1b style video explainer on X. Use my ElevenLabs API key for audio narration."* This skill is the reusable playbook for exactly that prompt — for any coding agent.

The key idea: the agent **writes a program that draws each frame** (Manim Community Edition), so equations, graphs, and labels come out exact and stay editable. Narration is synthesized per scene (ElevenLabs, or free local TTS) and muxed in with ffmpeg.

## Quickstart

```bash
git clone https://github.com/devamsheth21/3b1b-video-skill
cd 3b1b-video-skill
./scripts/install.sh
```

Then ask your agent:

> Create a 3b1b style video explainer on Bayes' theorem.

The skill takes it from there: script → voiceover → Manim scenes → render → `final.mp4`.

## What's inside

```
skills/explainer-video/
  SKILL.md                  # the skill: workflow + operating rules (agent reads this)
  references/
    pedagogy.md             # what makes a video feel 3b1b (one idea/beat, build-don't-dump, house palette)
    manim-guide.md          # Manim CE cheat sheet for agents
    narration.md            # TTS options: ElevenLabs, Piper, Coqui, macOS say, espeak-ng
    pipeline.md             # beat-by-beat build: script → audio → measure → code → render → mux
scripts/install.sh          # installs into Claude Code, Codex, .agents, ~/skills (+ notes for Cursor etc.)
examples/hello-derivative/  # complete 2-beat example: script + scenes.py — render this first
```

## Works with any agent

The skill is plain Markdown (`SKILL.md` + references) — no platform lock-in. `install.sh` covers Claude Code (`~/.claude/skills`), Codex (`~/.codex/skills`), Antigravity/generic (`.agents/skills`, `~/skills`), and prints the one-liners for project-local setups (Cursor, Windsurf, Aider, ...).

## Requirements (on the machine that renders)

- Python 3.10+, `pip install manim`, cairo/pango system libs, `ffmpeg`
- LaTeX (TinyTeX/MacTeX) — only if you want `Tex`/`MathTex` typesetting; otherwise the skill falls back to plain `Text`
- TTS: an `ELEVENLABS_API_KEY` for the best voice, or nothing at all — the skill defaults to free local engines (Piper/Coqui)

Verify with the example: `cd examples/hello-derivative && manim -ql scenes.py Beat1Question Beat2Square`

## How a run works

1. **Script** — narration written as short beats, one idea each (see `pedagogy.md`)
2. **Voiceover** — one audio clip per beat; durations measured with ffprobe
3. **Scenes** — one Manim `Scene` per beat, animation time matched to its audio
4. **Draft** — low-quality render, 1-fps frame review, fix loop
5. **Final** — 1080p render, per-beat mux, concat → `final.mp4`

## Contributing

PRs welcome — especially new examples, TTS recipes, and Manim patterns. Keep `SKILL.md` thin; put detail in `references/`.

## Credits

- Pedagogy and style: Grant Sanderson / 3Blue1Brown, via the [Manim Community Edition](https://www.manim.community/) his work inspired
- The prompt that started it: Andrej Karpathy, Oct 2026

## License

MIT — see [LICENSE](LICENSE).
