#!/usr/bin/env python3
import os, pathlib, sys, subprocess
from openai import OpenAI

# Load env without printing secrets
env = pathlib.Path.home() / ".hermes" / ".env"
if env.exists():
    for line in env.read_text().splitlines():
        line=line.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        k,v=line.split('=',1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

client = OpenAI()
wd = pathlib.Path('/Users/jasonyim/Projects/meridian-landing')
ref = wd / 'assets/video/source_refs/doctor-photo-clean-speaking-ref-1280x720.jpg'
raw_out = wd / 'assets/video/doctor-portrait-live-sora2-4s-1280x720.mp4'
overlay_out = wd / 'assets/video/doctor-speaking-overlay-540x394.mp4'

prompt = (
    "Create a natural 4-second video from this portrait. The person remains in the same framing, looking into the camera. "
    "Add only subtle believable life: natural blinking, tiny head micro-movements, gentle breathing, and small relaxed mouth movements as if quietly speaking. "
    "Keep the camera locked and preserve the same face identity, clothing, background, lighting, and composition. "
    "No text, no captions, no logo, no new objects, no camera move, no zoom, no hand gestures, no exaggerated expression. "
    "High-end realistic product-demo footage, calm and restrained."
)
print(f"START retry ref={ref}", flush=True)
with open(ref, 'rb') as f:
    video = client.videos.create_and_poll(
        model='sora-2',
        prompt=prompt,
        input_reference=f,
        seconds='4',
        size='1280x720',
        poll_interval_ms=5000,
        timeout=1800,
    )
print(f"STATUS retry id={video.id} status={video.status}", flush=True)
if video.status != 'completed':
    print(f"FAILED retry {video}", file=sys.stderr, flush=True)
    sys.exit(1)
client.videos.download_content(video.id, variant='video', timeout=600).write_to_file(raw_out)
print(f"WROTE raw {raw_out}", flush=True)
# Crop central portrait area back to overlay aspect and size.
crop_w = round(720 * 540 / 394)
x = (1280 - crop_w) // 2
cmd = [
    'ffmpeg','-y','-i',str(raw_out),
    '-vf',f'crop={crop_w}:720:{x}:0,scale=540:394,format=yuv420p',
    '-an','-c:v','libx264','-preset','slow','-crf','18','-movflags','+faststart',
    str(overlay_out)
]
subprocess.run(cmd, check=True)
print(f"WROTE overlay {overlay_out}", flush=True)
