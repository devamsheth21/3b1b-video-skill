---
name: "explainer_video"
description: "Create 3Blue1Brown-style animated explainer videos on any topic: narration script, Manim CE animation code, TTS voiceover, rendered MP4. Use when the user asks for a 3b1b-style video explainer, an animated explainer video, a narrated math/science/CS concept video, or to 'explain X as a video'."
---

# Explainer Video

## Purpose
Turn any topic into a short narrated 3Blue1Brown-style animated explainer video (MP4), generated as code: the agent writes a narration script, synthesizes voiceover audio, writes Manim Community Edition scenes timed to that audio, renders, and muxes everything into a final video.

## Workflow
1. **Clarify**: topic, audience, target length (default 2–4 minutes). If vague, pick a sensible default and proceed.
2. **Script**: write the narration as short beats (1–3 sentences each). Read `references/pedagogy.md` first — one idea per beat, motivate before defining, end with a recap.
3. **Voiceover**: synthesize one audio file per beat (ElevenLabs if an API key exists, else a free local TTS). Measure each clip's duration with ffprobe. Details: `references/narration.md`.
4. **Scenes**: write one Manim CE `Scene` per beat; total animation time per scene ≈ its audio duration. Read `references/manim-guide.md` for the API cheat sheet.
5. **Draft**: render at low quality (`manim -ql`), extract 1-fps frames, review them for layout/overlap errors, fix, repeat (max two fix loops).
6. **Final**: render at high quality (`manim -qh`), mux each scene with its audio, concatenate → `final.mp4`. Exact commands: `references/pipeline.md`.
7. **Deliver**: hand over `final.mp4` plus the narration script and the Manim source.

## Output Contract
- `final.mp4` — narrated video (1080p default).
- `script.md` — narration beats with visual notes.
- `scenes.py` — Manim CE source (editable; re-render to change the video).

## Operating Rules
1. Code, not diffusion: every frame is drawn by a program the agent writes, so equations and labels are exact and editable. Never reach for an AI video-diffusion model for this.
2. Audio drives timing: never set scene timings before the voiceover durations are measured.
3. No LaTeX on screen unless a LaTeX distribution is installed; fall back to plain `Text`.
4. Verify claims: spot-check the 2–3 most surprising statements in the script against a source before rendering.
5. Keep the artifact discardable: it is a learning aid, not a publication. Say so when delivering.
