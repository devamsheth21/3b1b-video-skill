# Narration (TTS)

Order of operations: **script → audio → measure durations → write scenes**. Scene timings are derived from measured audio, never guessed.

## Writing for TTS
- Short sentences. Commas and periods create natural pauses.
- Spell out symbols: "x squared", not "x^2"; "the derivative of y with respect to x", not "dy/dx".
- Expand abbreviations on first use.
- ~130–150 words per minute ≈ 750–900 characters per minute. Keep beats to ~100–300 characters (5–20 seconds).

## Option 1: ElevenLabs (best quality, paid)
Needs `ELEVENLABS_API_KEY` in the environment. Never print the key.

```bash
curl -s -X POST "https://api.elevenlabs.io/v1/text-to-speech/EXAVITQu4vr4xnSDxMaL" \
  -H "xi-api-key: $ELEVENLABS_API_KEY" -H "Content-Type: application/json" \
  -d '{"text": "Your narration line here.", "model_id": "eleven_multilingual_v2"}' \
  --output audio/beat1.mp3
```
List voices: `curl -s https://api.elevenlabs.io/v1/voices -H "xi-api-key: $ELEVENLABS_API_KEY"`.

## Option 2: Piper (free, local, good quality)
```bash
pip install piper-tts
# download a voice, e.g. en_US-lessac-medium, from https://huggingface.co/rhasspy/piper-voices
echo "Your narration line here." | piper --model en_US-lessac-medium.onnx --output_file audio/beat1.wav
```

## Option 3: Coqui TTS (free, local, heavier)
```bash
pip install TTS
tts --text "Your narration line here." --model_name tts_models/en/ljspeech/tacotron2-DDC --out_path audio/beat1.wav
```

## Option 4: macOS built-in (free)
```bash
say -v Samantha -o audio/beat1.aiff "Your narration line here."
ffmpeg -y -i audio/beat1.aiff audio/beat1.wav
```

## Option 5: espeak-ng (free, robotic fallback)
```bash
espeak-ng -v en -s 150 -w audio/beat1.wav "Your narration line here."
```

## Measure durations
```bash
ffprobe -v error -show_entries format=duration -of csv=p=0 audio/beat1.wav
```
Record each beat's duration next to its line in `script.md`. The matching `Scene`'s total play time (sum of `run_time`s + `wait`s) should equal the audio duration ±0.5s.

## Optional polish
Normalize loudness across beats: `ffmpeg -y -i in.wav -af loudnorm out.wav`.
