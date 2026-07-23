# -*- coding: utf-8 -*-
"""build_page — (호환 래퍼) 범용 md → HTML.

사용: python build_page.py <src.md> <out.html> [시리즈 라벨]
실체는 common.py (공유 자산 assets/ + 내장 내비). 사이트 전체 재빌드는:
    python _책빌드/site.py
"""
import sys
import common

src = sys.argv[1] if len(sys.argv) > 1 else "다음트랙_2026-07-10.md"
out = sys.argv[2] if len(sys.argv) > 2 else "다음트랙.html"
series = sys.argv[3] if len(sys.argv) > 3 else "study metric"

path = common.build_md(src, out, series)
import os
print("written:", path, os.path.getsize(path) // 1024, "KB")
