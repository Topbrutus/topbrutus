from pathlib import Path
import base64
import hashlib

parts = sorted(Path("parts").glob("part-*.b64"))
if not parts:
    raise SystemExit("No parts found.")

text = "".join(p.read_text(encoding="utf-8").strip() for p in parts)
data = base64.b64decode(text)
out = Path("apf-v3-source.tar.xz.aes")
out.write_bytes(data)

sha = hashlib.sha256(data).hexdigest()
expected = "3b3a0eca6ba2079e404dec3a71dbfa853965b6878ca40b7308e227306b057bbd"
print(f"Wrote {out} ({len(data)} bytes)")
print(f"SHA-256: {sha}")
if sha != expected:
    raise SystemExit("SHA-256 mismatch")
print("SHA-256 OK")
