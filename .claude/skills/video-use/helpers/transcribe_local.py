"""Free, local alternative to transcribe.py (no API key, no upload).

Runs faster-whisper on the machine and writes a Scribe-shaped JSON to
<edit>/transcripts/<name>.json, so pack_transcripts.py, render.py and
timeline_view.py work unchanged.

Whisper tends to drop "um" and "uh". Three settings counter that:
  - a disfluency-heavy initial prompt, so it keeps fillers
  - VAD off, because the VAD filter clips short filler sounds
  - no conditioning on previous text, so it does not "clean up" over time

It is still less faithful than Scribe on fillers and has no speaker
diarization or audio events. Spot-check takes_packed.md against the audio
before trusting the filler count.

Usage:
    python helpers/transcribe_local.py <video> [--edit-dir DIR] [--model small.en]
        [--language en] [--audio-track N]
"""

from __future__ import annotations

import argparse
import json
import sys
import tempfile
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from transcribe import extract_audio, peak_dbfs, transcript_path  # noqa: E402

FILLER_PROMPT = (
    "Umm, uh, so, um, I was, uh, like, you know, I mean, er... "
    "Right, so, um, yeah. Hmm, ah, well, uh-huh."
)


def to_scribe_words(segments) -> list[dict]:
    """faster-whisper words -> Scribe-style word + spacing entries."""
    out: list[dict] = []
    prev_end: float | None = None
    for seg in segments:
        for w in seg.words or []:
            text = w.word.strip()
            if not text:
                continue
            if prev_end is not None and w.start > prev_end:
                out.append({"type": "spacing", "text": " ", "start": prev_end, "end": w.start})
            out.append({
                "type": "word", "text": text,
                "start": round(w.start, 3), "end": round(w.end, 3),
                "speaker_id": "speaker_0",
            })
            prev_end = w.end
    return out


def transcribe_one(video: Path, edit_dir: Path, model_name: str = "small.en",
                   language: str | None = None, audio_track: int = 0,
                   verbose: bool = True) -> Path:
    out_path = transcript_path(edit_dir, video, audio_track)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if out_path.exists():
        if verbose:
            print(f"cached: {out_path.name}")
        return out_path

    from faster_whisper import WhisperModel  # heavy import, keep lazy

    t0 = time.time()
    with tempfile.TemporaryDirectory() as tmp:
        audio = Path(tmp) / f"{video.stem}.wav"
        extract_audio(video, audio, audio_track)
        if peak_dbfs(audio) < -60.0:
            raise RuntimeError(f"audio track {audio_track + 1} of {video.name} is silent")
        if verbose:
            print(f"  transcribing {video.name} with {model_name} (local)", flush=True)
        model = WhisperModel(model_name, device="auto", compute_type="auto")
        segments, info = model.transcribe(
            str(audio),
            language=language,
            word_timestamps=True,
            vad_filter=False,
            condition_on_previous_text=False,
            initial_prompt=FILLER_PROMPT,
            beam_size=5,
        )
        words = to_scribe_words(segments)

    payload = {
        "language_code": info.language,
        "language_probability": info.language_probability,
        "text": " ".join(w["text"] for w in words if w["type"] == "word"),
        "words": words,
        "engine": f"faster-whisper:{model_name}",
    }
    out_path.write_text(json.dumps(payload, indent=2))
    if verbose:
        n = sum(1 for w in words if w["type"] == "word")
        print(f"  saved: {out_path.name}, {n} words in {time.time() - t0:.1f}s")
    return out_path


def main() -> None:
    ap = argparse.ArgumentParser(description="Local word-level transcription (faster-whisper)")
    ap.add_argument("video", type=Path)
    ap.add_argument("--edit-dir", type=Path, default=None,
                    help="Edit output directory (default: <video_parent>/edit)")
    ap.add_argument("--model", default="small.en",
                    help="faster-whisper model: tiny.en, base.en, small.en, medium.en, large-v3")
    ap.add_argument("--language", default=None)
    ap.add_argument("--audio-track", type=int, default=0)
    args = ap.parse_args()

    video = args.video.resolve()
    if not video.exists():
        sys.exit(f"video not found: {video}")
    edit_dir = (args.edit_dir or (video.parent / "edit")).resolve()
    transcribe_one(video, edit_dir, args.model, args.language, args.audio_track)


if __name__ == "__main__":
    main()
