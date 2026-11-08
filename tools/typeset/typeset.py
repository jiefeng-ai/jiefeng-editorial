"""Markdown -> 微信公众号可粘贴的内联样式 HTML。

排版引擎来自 wewrite (MIT, 见 wechat_typeset/LICENSE-wewrite)，只取了 converter 和 theme。

用法:
    tools/.venv/bin/python tools/typeset/typeset.py articles/<dir>/draft.md [--theme NAME] [--list]

输出到 md 同目录:
    final.html    粘贴用（make_paste_safe 处理过的正文）
    preview.html  本地浏览器预览
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from wechat_typeset.converter import WeChatConverter, make_paste_safe, preview_html  # noqa: E402
from wechat_typeset.theme import load_theme  # noqa: E402

THEMES_DIR = str(Path(__file__).parent / "wechat_typeset" / "themes")
DEFAULT_THEME = "sspai"


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("markdown", nargs="?")
    p.add_argument("--theme", default=DEFAULT_THEME)
    p.add_argument("--list", action="store_true", help="列出可用主题")
    a = p.parse_args()

    if a.list:
        for f in sorted(Path(THEMES_DIR).glob("*.yaml")):
            print(f.stem)
        return
    if not a.markdown:
        p.error("需要 markdown 文件路径")

    src = Path(a.markdown)
    theme = load_theme(a.theme, themes_dir=THEMES_DIR)
    result = WeChatConverter(theme=theme).convert(src.read_text(encoding="utf-8"))

    (src.parent / "final.html").write_text(make_paste_safe(result.html), encoding="utf-8")
    (src.parent / "preview.html").write_text(preview_html(result.html, theme), encoding="utf-8")
    print(f"标题: {result.title}\n摘要: {result.digest}\n图片: {result.images}")
    print(f"输出: {src.parent / 'final.html'} / preview.html")


if __name__ == "__main__":
    main()
