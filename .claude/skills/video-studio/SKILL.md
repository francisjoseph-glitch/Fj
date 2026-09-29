---
name: video-studio
description: "Full video editing pipeline for raw footage: transcribe, cut, remove filler words and dead air, then add motion graphics (lower-thirds, callouts, kinetic titles), audio and export. Use when the user hands over a raw video file and says edit it, cut it, remove the ums, clean it up, add motion graphics, make it a Reel, or run the full pipeline. Orchestrates video-use (the cut) and the hyperframes skills (the graphics). For generating videos from scratch with no footage, see video."
metadata:
  version: 1.0.0
---

# Video Studio

Raw file in, finished video out. Two engines, run in order:

1. **Cut** with `video-use` (`.claude/skills/video-use/SKILL.md`). Transcribe, remove fillers and dead air, grade, produce a clean `final.mp4`.
2. **Graphics** with HyperFrames (`/hyperframes` router, then `/talking-head-recut` or `/motion-graphics`). Designed overlays go on top of the already-cut video, so every timestamp matches the final timeline.

Read `video-use/SKILL.md` before starting, in particular its 12 Hard Rules. They are correctness rules, not taste. Everything else in these skills is a worked example, not a mandate.

## Layout

One folder per video, all git-ignored:

```
videos/<project>/
├── <raw file>               untouched
├── edit/                    video-use output (project.md, takes_packed.md, edl.json, transcripts/, final.mp4)
└── graphics/                HyperFrames work dir (public/index.html, cards/, output.mp4)
```

Helpers live at `.claude/skills/video-use/helpers/`. Never write outputs inside the skill directories.

## Setup check (every cold start, don't reinstall)

- `ffmpeg` and `ffprobe` on PATH.
- Python 3.10+ with `requests librosa matplotlib pillow numpy` (`pip install -e .claude/skills/video-use` does it; add `faster-whisper` for local transcription).
- Node 22+ (HyperFrames is run with `npx --yes hyperframes ...`; `npx hyperframes doctor` checks the render deps).
- Transcription engine, one of:
  - **Local, free (default when no key):** `helpers/transcribe_local.py` (faster-whisper, `pip install faster-whisper`). No key, no upload. Output is Scribe-shaped, so every other helper works unchanged. Weaker on fillers: Whisper tends to drop um/uh, so the helper prompts for them and disables VAD, but still spot-check `takes_packed.md` against the audio. No speaker labels. Model `small.en` is fine on a laptop, `medium.en` if fillers are being missed. The first run downloads the model.
  - **ElevenLabs Scribe (paid, most faithful on fillers):** `helpers/transcribe.py` and `transcribe_batch.py`. Needs `ELEVENLABS_API_KEY` in the environment or in `.claude/skills/video-use/.env` (git-ignored). Never commit it and never put it in `videos/`.
  - Ask which the user wants if unclear. Both write to the same `edit/transcripts/` cache, so never mix engines on one source.
  - `transcribe_batch.py` is Scribe only. For several local takes, loop `transcribe_local.py`.

The HyperFrames `hyperframes transcribe` (local Whisper) is for the graphics pass on the already-cleaned video, where fillers no longer matter.

## Pipeline

1. **Inventory.** `ffprobe` the raw file, transcribe with `helpers/transcribe_local.py` or `helpers/transcribe.py` (see Setup), build `takes_packed.md` with `helpers/pack_transcripts.py --edit-dir videos/<project>/edit`.
2. **Ask before cutting.** Shape the questions around the material. Always settle: target platform and aspect (Instagram Reels is 1080x1920@30, ask before assuming), target length, how aggressive the filler removal is, brand palette and fonts for graphics, whether captions are wanted.
3. **Propose the plan in plain English** (4 to 8 sentences: cuts, filler policy, graphics plan, grade, length) and **wait for approval**. No cutting before that (Hard Rule 11).
4. **Cut.** Write `edl.json`, render a `--preview`, then the final with `helpers/render.py`.
   - Fillers to cut by default: um, uh, er, ah, false starts, repeated words, dead air over about 0.4s. Judgement calls, confirm in the plan: "like", "you know", "so", "right", "basically". Speaker tics that carry rhythm stay.
   - Every cut lands on a word boundary with 30 to 200ms padding and 30ms audio fades (Hard Rules 3, 6, 7).
   - Extend past laughs and punchlines. The reaction is part of the beat.
5. **Self-eval the cut** per video-use step 7 (cut boundaries, loudness with `ebur128`, `ffprobe` duration). Cap at 3 passes. You cannot listen, so say so and report the measured numbers.
6. **Graphics pass.** Take `edit/final.mp4` as the input to `/talking-head-recut`, work dir `videos/<project>/graphics/`. Routing:
   - Overlays timed to speech over the whole video (lower-third, data callout, pull-quote, kinetic title, side panel, PiP): `/talking-head-recut`.
   - A standalone animated hit under about 10s (stat, chart, logo sting, hook), or a transparent overlay: `/motion-graphics`, then place the render via the `overlays` field in `edl.json` and re-run `render.py` (PTS-shifted, Hard Rule 4).
   - For several independent animations, build them in parallel sub-agents (Hard Rule 10).
   - Fonts fail silently. Assert the font loaded before rendering.
7. **Captions.** If wanted, either use video-use subtitles (applied last, output-timeline offsets, Hard Rules 1 and 5) in the cut pass, or `/embedded-captions` in the graphics pass. Never both. Do not burn captions before overlays are composed. `embedded-captions` is not installed by default; install with `npx hyperframes skills update embedded-captions` when needed.
8. **Audio.** Music ducked 12 to 15 dB under speech, effects tied to visible events, then loudnorm to -14 LUFS with true peak at or under -1 dBTP. Music taste is the user's call, offer two beds. `/media-use` sources music and SFX.
9. **Final QA.** `ffprobe` duration, dimensions and fps against the plan. Sample frames at the first 2s, last 2s and each graphic. For anything to be published, spawn one critic sub-agent briefed to find problems, not praise.
10. **Persist.** Append a session to `videos/<project>/edit/project.md`. Never re-transcribe a cached source.

## Rules that override defaults

- Confirm the plan before cutting. Confirm palette and fonts before building graphics.
- Match source fps and aspect unless told otherwise.
- Say plainly what was measured versus assumed. Do not claim it sounds or looks good from the numbers alone.
- Optional engines stay optional: Manim (formal diagrams, not vendored here), Remotion (only if the user asks for React).
