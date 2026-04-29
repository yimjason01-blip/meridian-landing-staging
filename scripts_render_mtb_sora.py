#!/usr/bin/env python3
import os, pathlib, sys
from openai import OpenAI
from PIL import Image

env = pathlib.Path.home() / ".hermes" / ".env"
if env.exists():
    for line in env.read_text().splitlines():
        line=line.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        k,v=line.split('=',1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

client = OpenAI()

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

name = "hero-mountain_bike_original_track-sora2-4s-1280x720"
src = "/Users/jasonyim/.hermes/cache/images/openai_gpt-image-2-medium_20260428_131331_a71aca65.png"
out = pathlib.Path("/Users/jasonyim/Projects/meridian-landing/assets/video/hero-mountain_bike_original_track-sora2-4s-1280x720.mp4")
prompt = "Create a natural 4-second documentary video from this still. Preserve the original mountain bike composition and the three-generation destination ride feeling. The camera tracks and pans laterally with the riders so the lead rider and family group stay large and prominent in frame the entire time. Smooth trail riding, small wheel motion, body balance, tire texture, background tree parallax. Do not let the rider shrink into the distance. Do not zoom out. Do not cut to a tiny rider at the end. Do not make it an extreme action shot. Candid premium outdoor family-vacation realism, natural expressions, no text or logos."

out.parent.mkdir(parents=True, exist_ok=True)
ref = make_16x9_1280x720(src)
print(f"START {name} ref={ref}", flush=True)
with open(ref, "rb") as f:
    video = client.videos.create_and_poll(
        model="sora-2",
        prompt=prompt,
        input_reference=f,
        seconds="4",
        size="1280x720",
        poll_interval_ms=5000,
        timeout=1800,
    )
print(f"STATUS {name} id={video.id} status={video.status}", flush=True)
if video.status != "completed":
    print(f"FAILED {name} {video}", file=sys.stderr, flush=True)
    sys.exit(1)
content = client.videos.download_content(video.id, variant="video", timeout=600)
content.write_to_file(out)
print(f"WROTE {out}", flush=True)
