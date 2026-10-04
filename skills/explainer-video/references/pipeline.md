# Pipeline: beat-by-beat build

## Project layout
```
my-video/
  script.md        # beats: Say: (narration) + Visual: (scene notes) + measured duration
  audio/beat1.wav, beat2.wav, ...
  scenes.py        # class Beat1(Scene), Beat2(Scene), ...
  final.mp4
```

## Steps

### 1. Write `script.md`
One block per beat:
```markdown
## Beat 1 — 6.2s
Say: Your narration line here.
Visual: Title writes on, subtitle fades in below.
```

### 2. Synthesize audio (see `narration.md`)
One file per beat → `audio/beatN.wav`. Then measure and fill in the durations:
```bash
for f in audio/beat*.wav; do
  printf "%s " "$f"
  ffprobe -v error -show_entries format=duration -of csv=p=0 "$f"
done
```

### 3. Write `scenes.py`
One `Scene` per beat. Total play time per scene ≈ its audio duration (±0.5s).
See `manim-guide.md` and `examples/hello-derivative/scenes.py`.

### 4. Draft render + frame review
```bash
manim -ql scenes.py Beat1 Beat2 Beat3
ffmpeg -y -i media/videos/scenes/480p15/Beat1.mp4 -vf fps=1 frames/b1_%03d.png
```
Open the frames. Check: overlaps, text cut off at edges, colors readable on dark background, nothing static for >3s. Fix `scenes.py`, re-render. Max two fix loops, then ship the draft quality or move on.

Fast layout check without full render: `manim -ql -s scenes.py Beat1` renders only the last frame as PNG.

### 5. Final render
```bash
manim -qh scenes.py Beat1 Beat2 Beat3
```
Outputs land in `media/videos/scenes/1080p60/`.

### 6. Mux each beat with its narration
```bash
ffmpeg -y -i media/videos/scenes/1080p60/Beat1.mp4 -i audio/beat1.wav \
  -c:v copy -c:a aac -shortest voiced1.mp4
```
Repeat per beat. (`-shortest` trims whichever stream is longer; the ±0.5s tolerance from step 3 keeps this invisible.)

### 7. Concatenate
```bash
printf "file 'voiced1.mp4'\nfile 'voiced2.mp4'\nfile 'voiced3.mp4'\n" > list.txt
ffmpeg -y -f concat -safe 0 -i list.txt -c copy final.mp4
```

### 8. Optional: captions
Generate an SRT (e.g. with whisper) named `captions.srt`, then burn in:
```bash
ffmpeg -y -i final.mp4 -vf subtitles=captions.srt final_captioned.mp4
```

## Timing example
Beat audio measures 12.4s → the scene's plays must sum to ~12.4s, e.g.:
`Write (2s) + wait (0.5s) + Transform (3s) + FadeIn (1.5s) + wait (5.4s) = 12.4s`.
