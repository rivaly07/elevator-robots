from pathlib import Path

Path("/output/entry.txt").write_text(
    "Unit B, what floor do you need? Sorry—I asked the only other elevator, and now my courtesy routine won't let me interrupt its answer.",
    encoding="utf-8",
)
