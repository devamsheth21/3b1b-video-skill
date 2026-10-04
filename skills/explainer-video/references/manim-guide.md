# Manim Community Edition — agent cheat sheet

Manim CE (v0.18+) turns Python into math animations. Install: `pip install manim` (needs cairo + pango system libraries; LaTeX only required for `Tex`/`MathTex`).

## Minimal scene

```python
from manim import *

config.background_color = "#1E1E1E"  # 3b1b-style dark background

class MyScene(Scene):
    def construct(self):
        title = Text("Hello, explainer", font_size=48)
        self.play(Write(title), run_time=1.5)
        self.wait(1)
        self.play(FadeOut(title))
```

Render: `manim -ql scenes.py MyScene` (draft) → `manim -qh scenes.py MyScene` (1080p final).

## Mobjects you'll use most

- `Text("...")` — plain text. No LaTeX needed. Unicode (², π, →) works.
- `MathTex(r"\frac{dy}{dx}")`, `Tex(r"...")` — beautiful math, **requires a LaTeX distribution**. If LaTeX is missing, use `Text` instead.
- Shapes: `Circle()`, `Square()`, `Rectangle()`, `Triangle()`, `Line()`, `Arrow()`, `Dot()`, `Polygon()`
- `VGroup(*mobjects)` — treat several objects as one. `VGroup(a, b).arrange(DOWN)` stacks them.
- `Axes(x_range=[0, 5], y_range=[0, 5])`, then `ax.plot(lambda x: x**2)`, `ax.c2p(2, 4)` converts coords→pixels.
- `NumberPlane()` for grids.

Positioning: `m.next_to(other, DOWN, buff=0.4)`, `m.to_edge(UP)`, `m.shift(LEFT*2)`, `m.move_to(ORIGIN)`, `m.scale(1.5)`.

## Animations you'll use most

- `Write(m)`, `Create(m)` — draw on progressively. `Write` for text, `Create` for shapes.
- `FadeIn(m)`, `FadeOut(m)`, `GrowFromCenter(m)`
- `Transform(a, b)` — morph a into b's shape. The 3b1b workhorse: keeps continuity between states.
- `ReplacementTransform(a, b)` — like Transform, then removes a.
- `Indicate(m)`, `Circumscribe(m)`, `Wiggle(m)` — draw attention to something already on screen.
- `Rotate(m, angle)`, `m.animate.shift(RIGHT)` — the `.animate` syntax animates any method.

`self.play(*anims, run_time=2)` — run_time in seconds. `self.wait(1)` — hold the frame.

## Driven motion (ValueTracker)

For a dot tracing a curve, a growing bar, anything parameterized:

```python
t = ValueTracker(0)
dot = always_redraw(lambda: Dot(ax.c2p(t.get_value(), t.get_value()**2), color=YELLOW))
self.add(dot)
self.play(t.animate.set_value(4), run_time=3, rate_func=linear)
```

## Colors

`BLUE BLUE_C GREEN YELLOW RED TEAL PINK ORANGE PURPLE WHITE GREY GREY_B BLACK`.
Custom: `ManimColor.from_hex("#FF8800")`. House palette for this skill: BLUE (main), YELLOW (active), GREEN (secondary), RED (wrong), GREY (labels).

## CLI flags

| Flag | Meaning |
|---|---|
| `-ql` | 480p15 draft — fast iteration |
| `-qm` | 720p30 |
| `-qh` | 1080p60 final |
| `-qk` | 2160p60 |
| `-p` | preview after render |
| `-s` | render only the last frame as PNG (fast layout check) |
| `-o name.mp4` | custom output filename |
| `--format=gif` | GIF instead of MP4 |

`manim checkhealth` diagnoses missing system dependencies.

## Pitfalls

1. **Overlaps**: always position with `next_to` / `to_edge` / `arrange`, never eyeball coordinates twice.
2. **Long plays**: keep any single `run_time` under ~8s; chain plays instead.
3. **Font**: default `Text` font varies by OS — acceptable. Don't set exotic fonts.
4. **Silent output**: manim renders video with no audio track. Narration is muxed afterwards with ffmpeg (see `pipeline.md`).
5. **One Scene per beat**: each narration beat gets its own `Scene` class so durations stay independent and re-renders stay cheap.
