#!/usr/bin/env python3
"""資料夾體積排行 CLI"""
from __future__ import annotations
import argparse
from pathlib import Path

def folder_size(path: Path) -> int:
    total = 0
    for f in path.rglob("*"):
        if f.is_file():
            try:
                total += f.stat().st_size
            except OSError:
                pass
    return total

def main() -> None:
    p = argparse.ArgumentParser(description='資料夾體積排行 CLI')
    p.add_argument("dir", type=Path)
    p.add_argument("--top", type=int, default=20)
    args = p.parse_args()
    rows = []
    for child in args.dir.iterdir():
        if child.is_dir():
            rows.append((folder_size(child), child))
    rows.sort(reverse=True)
    for size, path in rows[: args.top]:
        mb = size / (1024 * 1024)
        print(f"{mb:8.2f} MB  {path.name}")

if __name__ == "__main__":
    main()
