# -*- coding: utf-8 -*-
"""build_5b — (호환 래퍼) 걸음 5b → HTML. 실체는 common.py. 전체 재빌드: python _책빌드/site.py"""
import os
import common

path = common.build_md(
    os.path.join("정리_L0-L6", "손계산_걸음별", "5b_손노트완성본_CP1_QFIM.md"),
    "손노트완성본_CP1_QFIM.html",
    "study metric — 손계산 걸음 5b",
)
print("written:", path, os.path.getsize(path) // 1024, "KB")
