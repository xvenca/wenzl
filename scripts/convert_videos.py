"""Convert the yellow-hive .MOV clips to web-optimized MP4 using the
ffmpeg bundled with imageio-ffmpeg (no system ffmpeg needed)."""
import os, subprocess, re, sys
import imageio_ffmpeg

EXE = imageio_ffmpeg.get_ffmpeg_exe()
SRC_DIR = r"C:\Users\Martin Venclu\OneDrive\Pictures\zluty_lezan"
OUT_DIR = r"C:\Users\Martin Venclu\OneDrive\Documents\GitHub\wenzl\static\videos"
os.makedirs(OUT_DIR, exist_ok=True)

def probe(path):
    p = subprocess.run([EXE, "-hide_banner", "-i", path],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    info = p.stderr
    dur = re.search(r"Duration: ([\d:.]+)", info)
    vid = re.search(r"Video: .*?(\d{3,5})x(\d{3,5})", info)
    return (dur.group(1) if dur else "?",
            (vid.group(1) + "x" + vid.group(2)) if vid else "?")

def convert(src_name, out_name):
    src = os.path.join(SRC_DIR, src_name)
    out = os.path.join(OUT_DIR, out_name)
    # Scale so the longest side <= 1280, keep aspect, even dimensions; H.264, web-friendly.
    cmd = [EXE, "-y", "-i", src,
           "-vf", "scale='if(gt(iw,ih),min(1280,iw),-2)':'if(gt(iw,ih),-2,min(1280,ih))'",
           "-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p",
           "-crf", "28", "-preset", "medium", "-movflags", "+faststart",
           "-c:a", "aac", "-b:a", "96k",
           out]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    ok = r.returncode == 0 and os.path.exists(out)
    size = os.path.getsize(out) if ok else 0
    return ok, out, size, (r.stderr[-500:] if not ok else "")

print("ffmpeg:", EXE)
for v in ["IMG_8635.MOV", "IMG_8637.MOV"]:
    d, res = probe(os.path.join(SRC_DIR, v))
    print(f"PROBE {v}: duration={d} resolution={res}")

ok, out, size, err = convert("IMG_8635.MOV", "zluty-lezan.mp4")
print(f"CONVERT IMG_8635 -> {out}: ok={ok} size={size/1024/1024:.2f} MB")
if not ok:
    print("ERR:", err)
