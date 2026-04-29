#!/usr/bin/env python3
import os, pathlib, sys
from openai import OpenAI
from PIL import Image

# Load Hermes env without printing secrets
env = pathlib.Path.home() / ".hermes" / ".env"
if env.exists():
    for line in env.read_text().splitlines():
        line=line.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        k,v=line.split('=',1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

client = OpenAI()

jobs = [
    {
        "name": "hero-swimmer_c-sora2-4s-1280x720",
        "input": "/Users/jasonyim/.hermes/cache/images/openai_gpt-image-2-medium_20260428_142527_5b9c9072.png",
        "output": "/Users/jasonyim/Projects/meridian-landing/assets/video/hero-swimmer_c-sora2-4s-1280x720.mp4",
        "prompt": "Create a natural 4-second documentary video from this still. A younger athletic woman in a full zipped black wetsuit has just finished a cold ocean swim and walks naturally out of the surf toward the beach at a slight diagonal. Keep the same low beach-level three-quarter composition, empty shoreline, muted overcast morning light, wet sand reflections, small waves. Subtle handheld realism: water drips from the wetsuit, hair moves slightly in wind, small waves roll behind her, her expression stays relaxed and real. No towel, no robe, no glamour posing, no model stare, no dramatic smile change, no camera zoom-out, no added people, no text or logos. Premium candid vacation/accomplishment feeling, not fashion editorial.",
    },
    {
        "name": "hero-mountain_bike_original_track-sora2-4s-1280x720",
        "input": "/Users/jasonyim/.hermes/cache/images/openai_gpt-image-2-medium_20260428_131331_a71aca65.png",
        "output": "/Users/jasonyim/Projects/meridian-landing/assets/video/hero-mountain_bike_original_track-sora2-4s-1280x720.mp4",
        "prompt": "Create a natural 4-second documentary video from this still. Preserve the original mountain bike composition and the three-generation destination ride feeling. The camera should track and pan laterally with the riders so the lead rider/family group stays large and prominent in frame for the whole clip. They move smoothly along the trail, with small wheel motion, body balance, dust or tire texture, trees/background parallax. Do not let the rider shrink into the distance, do not zoom out, do not cut to a tiny rider at the end, do not make it an extreme action shot. Keep it candid, premium outdoor family-vacation realism, natural expressions, no text or logos.",
    },
]

def make_16x9_1280x720(src):
    src = pathlib.Path(src)
    out = pathlib.Path('/Users/jasonyim/Projects/meridian-landing/assets/video/source_refs') / (src.stem + '_1280x720.png')
    out.parent.mkdir(parents=True, exist_ok=True)
    im = Image.open(src).convert('RGB')
    w, h = im.size
    target = 16 / 9
    if w / h > target:
        new_w = int(h * target)
        left = (w - new_w) // 2
        crop = im.crop((left, 0, left + new_w, h))
    else:
        new_h = int(w / target)
        top = (h - new_h) // 2
        crop = im.crop((0, top, w, top + new_h))
    crop.resize((1280, 720), Image.LANCZOS).save(out)
    return out

for job in jobs:
    out = pathlib.Path(job["output"])
    out.parent.mkdir(parents=True, exist_ok=True)
    ref_path = make_16x9_1280x720(job["input"])
    print(f"START {job['name']} ref={ref_path}", flush=True)
    with open(ref_path, "rb") as f:
        video = client.videos.create_and_poll(
            model="sora-2",
            prompt=job["prompt"],
            input_reference=f,
            seconds="4",
            size="1280x720",
            poll_interval_ms=5000,
            timeout=1800,
        )
    print(f"STATUS {job['name']} id={video.id} status={video.status}", flush=True)
    if video.status != "completed":
        print(f"FAILED {job['name']} {video}", file=sys.stderr, flush=True)
        continue
    content = client.videos.download_content(video.id, variant="video", timeout=600)
    content.write_to_file(out)
    print(f"WROTE {out}", flush=True)
