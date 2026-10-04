# Example: "Why the derivative of x² is 2x" (2 beats, ~25s)

A minimal complete run of the skill pipeline. Render it with:

```bash
manim -ql scenes.py Beat1Question Beat2Square   # draft
manim -qh scenes.py Beat1Question Beat2Square   # final
```

## script.md

### Beat 1 — ~7s
**Say:** The derivative of x squared is two x. But why? Let's watch it happen.
**Visual:** Title writes on; subtitle fades in below.

### Beat 2 — ~16s
**Say:** Start with a square of side x. Its area is x squared. Now let the side grow by a tiny amount. The new area is two thin strips, each x by the tiny growth, plus a negligible corner. So the growth of the area is two x times the tiny growth. That is why the derivative is two x.
**Visual:** Blue square fades in with labels; labels fade; square grows; two yellow strips fade in over the added region; red corner fades in; caption appears.

*(Durations are estimates — synthesize the audio first, then measure with ffprobe and adjust the scene's play times to match, per `references/pipeline.md`.)*

## What this demonstrates
- One `Scene` class per narration beat (`Beat1Question`, `Beat2Square`).
- House palette: BLUE main object, YELLOW the active idea, RED the negligible corner, GREY labels, dark background.
- `Transform` for continuous growth instead of a jump cut; `FadeIn`/`FadeOut` for labels.
- Total animation time per scene ≈ its narration duration.
