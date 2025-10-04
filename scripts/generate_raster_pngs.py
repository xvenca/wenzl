import struct
import zlib
from pathlib import Path

def png_chunk(chunk_type: bytes, data: bytes) -> bytes:
    chunk = struct.pack('>I', len(data)) + chunk_type + data
    crc = zlib.crc32(chunk_type + data) & 0xffffffff
    chunk += struct.pack('>I', crc)
    return chunk

def write_png(path: Path, width: int, height: int, color: tuple):
    # color is (r,g,b) 0-255
    width = int(width)
    height = int(height)
    header = b"\x89PNG\r\n\x1a\n"
    # IHDR
    ihdr = struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0)
    data = b''
    # raw image data: each scanline starts with filter byte 0
    r,g,b = [int(x) & 0xff for x in color]
    row = bytes([r, g, b]) * width
    for _ in range(height):
        data += b'\x00' + row
    compressed = zlib.compress(data, level=9)
    png = header + png_chunk(b'IHDR', ihdr) + png_chunk(b'IDAT', compressed) + png_chunk(b'IEND', b'')
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'wb') as f:
        f.write(png)
    print(f'Wrote {path} ({width}x{height})')

if __name__ == '__main__':
    ROOT = Path(__file__).resolve().parents[1]
    targets = {
        ROOT / 'content' / 'no' / 'gard' / 'farm.png': (1200, 600, (6,95,70)),
        ROOT / 'content' / 'en' / 'farm' / 'farm.png': (1200, 600, (6,95,70)),
        ROOT / 'content' / 'no' / 'app' / 'app.png': (1200, 600, (55,48,163)),
        ROOT / 'content' / 'en' / 'app' / 'app.png': (1200, 600, (55,48,163)),
    }
    for p, (w,h,c) in targets.items():
        write_png(p, w, h, c)
