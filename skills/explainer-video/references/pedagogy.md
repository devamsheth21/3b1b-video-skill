# Pedagogy: the 3b1b style

What makes a 3Blue1Brown video feel like 3Blue1Brown is not the software — it is a set of visual and narrative habits. Follow them and the output reads as the genre, regardless of topic.

## The core loop
Every beat answers three questions in order: **what am I looking at → why should I care → what does it mean**. Never define before motivating.

## Rules

1. **One idea per beat.** If a beat needs the word "and" twice in its narration, split it. A 2–4 minute video is 8–16 beats.

2. **Question first.** Open with a puzzle, a paradox, or a concrete question — not with a definition. ("Why does this fail?" beats "Definition: ...".)

3. **Build, don't dump.** Animate the construction of each object step by step (`Write`, `Create`, `GrowFromCenter`). Nothing important should just appear; the viewer should watch it come into existence.

4. **The picture is the equation.** Color-code consistently across the whole video and never add a sixth color:
   - `BLUE` — the main objects under discussion
   - `YELLOW` — the active idea: the thing currently moving, changing, or being pointed at
   - `GREEN` — secondary objects, confirmed/good cases
   - `RED` — the naive attempt, the forbidden move, the counterexample
   - `GREY` — labels and scaffolding
   - Background: dark (`#1E1E1E`). Text: near-white.

5. **Show the naive attempt failing.** Before the real idea arrives, put the obvious-but-wrong approach on screen and let it visibly break. The repair then has something to repair.

6. **Narration explains the *why*, visuals show the *what*.** Never read the screen aloud verbatim. The spoken line should be the thought the viewer should be having while watching the motion.

7. **Minimal on-screen text.** Short labels, not paragraphs. If a sentence is on screen, it should be spoken too — or cut it.

8. **Morph, don't cut.** Use `Transform` / `ReplacementTransform` to carry objects between states instead of fading out and fading something new in. Continuous motion preserves the viewer's mental model.

9. **Pause after the punchline.** A `self.wait(1)` after the key insight lands gives the viewer time to feel it. Rushing past the aha kills it.

10. **Recap by reassembly.** End by rebuilding the key idea from its pieces — one short phrase per piece, nothing new introduced.

## Pacing
Aim for ~130–150 words per minute of narration. A beat is 1–3 sentences (roughly 5–20 seconds of audio). If a beat's audio runs over ~25 seconds, it is two beats.
