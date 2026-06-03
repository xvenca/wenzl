"""Convert the Bergen 2025 building-swarm clips to web MP4 using the
ffmpeg bundled with imageio-ffmpeg."""
import os
import subprocess
import imageio_ffmpeg

EXE = imageio_ffmpeg.get_ffmpeg_exe()
SRC_DIR = r"C:\Users\Martin Venclu\Videos\swarm in building Bergen 2025"
OUT_DIR = r"C:\Users\Martin Venclu\OneDrive\Documents\GitHub\wenzl\static\videos\swarm-building-bergen-2025"

FILES = [
    ("IMG_2823.MOV", "01.mp4"),
    ("IMG_2824.MOV", "02.mp4"),
    ("IMG_2825.MOV", "03.mp4"),
    ("IMG_2826.MOV", "04.mp4"),
    ("IMG_2827.MOV", "05.mp4"),
]

os.makedirs(OUT_DIR, exist_ok=True)


def convert(src_name, out_name):
    src = os.path.join(SRC_DIR, src_name)
    out = os.path.join(OUT_DIR, out_name)
    cmd = [
        EXE,
        "-y",
        "-i",
        src,
        "-vf",
        "scale='if(gt(iw,ih),min(1280,iw),-2)':'if(gt(iw,ih),-2,min(1280,ih))'",
        "-c:v",
        "libx264",
        "-profile:v",
        "high",
        "-pix_fmt",
        "yuv420p",
        "-crf",
        "28",
        "-preset",
        "medium",
        "-movflags",
        "+faststart",
        "-c:a",
        "aac",
        "-b:a",
        "96k",
        out,
    ]
    run = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    ok = run.returncode == 0 and os.path.exists(out)
    size = os.path.getsize(out) if ok else 0
    return ok, size, run.stderr[-500:]


print("ffmpeg:", EXE)
for src_name, out_name in FILES:
    ok, size, err = convert(src_name, out_name)
    print(f"{src_name} -> {out_name}: ok={ok} size_mb={size / 1024 / 1024:.2f}")
    if not ok:
        print(err)