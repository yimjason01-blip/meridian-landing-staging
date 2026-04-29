#!/usr/bin/env python3
"""Generate 3 candid family-vacation hero iterations via xAI Grok Imagine Pro."""
import os, base64, pathlib, sys, time
from openai import OpenAI

for env_file in [pathlib.Path.home() / ".hermes" / ".env", pathlib.Path.home() / ".hermes" / "env"]:
    if not env_file.exists():
        continue
    for line in env_file.read_text().splitlines():
        if "=" not in line or line.startswith("#"):
            continue
        k, v = line.split("=", 1)
        v = v.strip().strip('"').strip("'")
        if not v:
            continue
        os.environ[k.strip()] = v  # last non-empty wins

client = OpenAI(api_key=os.environ["XAI_API_KEY"], base_url="https://api.x.ai/v1")

OUT = pathlib.Path("assets/hero_candid_iterations")
OUT.mkdir(parents=True, exist_ok=True)

# Shared subject + context anchor
SUBJECTS = (
    "An East Asian couple on a hike that just got rained on. "
    "Woman early 30s, long wet black hair, dark rain shell, laughing openly with mouth open and head slightly tilted back. "
    "Man late 40s, short black hair, olive green rain jacket, warm gentle smile, standing close to her. "
    "Both clearly soaked, caught off guard by the rain, genuinely amused. "
    "Candid, NOT posed, NOT a magazine shot. "
)

ITERATIONS = [
    {
        "name": "01_phone_snapshot",
        "prompt": (
            f"{SUBJECTS}"
            "Shot like a phone snapshot a friend took on a family vacation. "
            "Slightly off-center framing, natural composition, the woman in motion blur as she laughs and reacts to the sudden rain, "
            "huge old-growth Douglas fir trees towering in the background showing this hike was a real destination, "
            "wet ferns and trail underfoot, soft overcast forest light, natural color, "
            "fine rain visible across the frame, lens slightly rain-speckled, "
            "wide-ish vacation-photo perspective, no editorial styling, no studio lighting. "
            "Avoid: text, watermarks, logos, magazine retouching, posed model expressions, perfect symmetry."
        ),
    },
    {
        "name": "02_caught_in_downpour",
        "prompt": (
            f"{SUBJECTS}"
            "Composition: man and woman framed slightly to one side of the frame, the forest opening up behind them with massive towering redwood-style conifers receding into mist. "
            "The rain has clearly just started — droplets visible on their faces, jackets darkening with water, hair beginning to stick. "
            "Both are reacting in the moment: she's laughing with her hand half-raised wiping rain off her face, he's grinning at her, both looking at each other not at camera. "
            "Hand-held, slightly tilted horizon, vacation snapshot energy. "
            "Soft diffused overcast daylight under a forest canopy, deep green moss, wet bark, atmospheric haze. "
            "Avoid: text, watermarks, logos, posed catalog look, dramatic studio rim light, oversaturation."
        ),
    },
    {
        "name": "03_under_the_giants",
        "prompt": (
            f"{SUBJECTS}"
            "Wider vacation shot: the trees dominate the frame, two enormous old-growth fir or sequoia trunks anchoring the foreground at left and right, "
            "the couple smaller in the middle ground on a wet trail, both looking up and laughing as the rain comes down. "
            "Conveys destination scale — the hike clearly went somewhere big. "
            "Natural overcast light, fine misty rain in the air, wet ground reflecting muted forest colors, "
            "phone-camera perspective with slight wide angle, casual handheld feel, candid timing. "
            "Avoid: text, watermarks, logos, model poses, fashion catalog aesthetic, harsh contrast."
        ),
    },
]

def gen(prompt: str, out_path: pathlib.Path, attempt: int = 1):
    t0 = time.time()
    resp = client.images.generate(
        model="grok-imagine-image-pro",
        prompt=prompt,
        n=1,
        response_format="b64_json",
    )
    b = base64.b64decode(resp.data[0].b64_json)
    out_path.write_bytes(b)
    print(f"  wrote {out_path} ({len(b)/1024:.1f} KB) in {time.time()-t0:.1f}s")

for it in ITERATIONS:
    out = OUT / f"{it['name']}.png"
    print(f"[{it['name']}] generating...")
    try:
        gen(it["prompt"], out)
    except Exception as e:
        print(f"  ERROR: {e}", file=sys.stderr)

print(f"\nDONE -> {OUT}")
for p in sorted(OUT.glob("*.png")):
    print(f"  {p}")
