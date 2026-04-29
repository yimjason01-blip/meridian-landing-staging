#!/usr/bin/env python3
import os, pathlib, sys, subprocess
from openai import OpenAI

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
wd = pathlib.Path('/Users/jasonyim/Projects/meridian-landing')
ref = wd / 'assets/video/source_refs/doctor-photo-clean-speaking-ref-1280x720.jpg'
raw_out = wd / 'assets/video/doctor-speaking-sora2-4s-1280x720.mp4'
overlay_out = wd / 'assets/video/doctor-speaking-overlay-540x394.mp4'
raw_out.parent.mkdir(parents=True, exist_ok=True)

prompt = (
    "Create a subtle realistic 4-second talking-head video from this still portrait of a physician. "
    "The doctor remains in the same composition, looking into the camera as if recording a calm voice message to a patient. "
    "Only natural facial motion: gentle lip movement, tiny jaw movement, soft blinking, very small head micro-movements, subtle breathing. "
    "Keep the camera locked. Keep the background, lighting, white coat, stethoscope, framing, and professional calm expression consistent. "
    "No UI, no captions, no new text, no logo, no zoom, no pan, no hand gestures, no body repositioning, no exaggerated emotion. "
    "Premium clinical product realism; quiet and trustworthy, like a live physician video message embedded in an app."
)

print(f"START doctor-speaking ref={ref}", flush=True)
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
print(f"STATUS doctor-speaking id={video.id} status={video.status}", flush=True)
if video.status != 'completed':
    print(f"FAILED doctor-speaking {video}", file=sys.stderr, flush=True)
    sys.exit(1)
content = client.videos.download_content(video.id, variant='video', timeout=600)
content.write_to_file(raw_out)
print(f"WROTE raw {raw_out}", flush=True)

# Crop the central Sora frame back to the exact overlay aspect (540:394), then scale to asset size.
# 1280x720 -> crop width round(720 * 540/394) = 987, centered.
crop_w = round(720 * 540 / 394)
x = (1280 - crop_w) // 2
cmd = [
    'ffmpeg', '-y', '-i', str(raw_out),
    '-vf', f'crop={crop_w}:720:{x}:0,scale=540:394,format=yuv420p',
    '-an',
    '-c:v', 'libx264', '-preset', 'slow', '-crf', '20',
    '-movflags', '+faststart',
    str(overlay_out)
]
print('FFMPEG ' + ' '.join(cmd), flush=True)
subprocess.run(cmd, check=True)
print(f"WROTE overlay {overlay_out}", flush=True)
