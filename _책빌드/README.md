# 책 빌드 소스 — Gr24_핵심계산_주제별완전판.html

상위 폴더의 `Gr24_핵심계산_주제별완전판.html`을 재생성하는 재료.

- `transcribe/part1..part8_*.md` — 원전 `원본노트/Gr24_핵심계산모음.pdf`(94쪽)의 전사본 (마크다운+LaTeX, 페이지 마커 포함). **문제 원문의 진실 소스.** 오탈자를 발견하면 여기서 고치고 재빌드.
- `transcribe/lrg_selected.md` — `원본노트/Learning Riemannian Geometry.pdf`에서 네비게이터가 참조하는 22문제 + Basic Formulas 원문 발췌.
- `build_book.py` — 파서 + 주제→장 매핑(네비게이터 그대로) + HTML 조판. 실행:

```
python build_book.py    # (요구: pip install markdown)
```

출력 경로는 스크립트 하단 `OUT` (상위 폴더의 HTML). 주제 매핑을 바꾸려면 `CH = []` 블록(주제 15개 스펙)을 수정.

- `katex/` — 오프라인 수식 렌더링용 KaTeX 0.16.11 (폰트 data-URI 인라인). 인터넷 없이 열린다.
