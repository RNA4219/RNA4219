"""掲載作品の最新正式リリースを取得して、プロフィールREADMEを生成する。"""

import json
import os
from datetime import datetime
from html import escape
from pathlib import Path
from tempfile import NamedTemporaryFile
from urllib.parse import quote
from urllib.request import Request, urlopen


HERE = Path(__file__).resolve().parent
README = HERE.parent / "Readme.md"
PROJECTS = {
    "quality-evidence-graph": "Quality Evidence Graph",
    "llm-atelier": "LLM Atelier",
    "RanD": "RanD",
}


def latest_release(repo, title):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "RNA4219-profile"}
    if token := os.getenv("GITHUB_TOKEN"):
        headers["Authorization"] = f"Bearer {token}"
    request = Request(f"https://api.github.com/repos/RNA4219/{repo}/releases/latest", headers=headers)
    with urlopen(request, timeout=20) as response:
        release = json.load(response)
    tag = release["tag_name"]
    published = datetime.fromisoformat(release["published_at"].replace("Z", "+00:00"))
    href = f"https://github.com/RNA4219/{repo}/releases/tag/{quote(tag, safe='')}"
    row = f'- {published:%Y-%m-%d}　<a href="{href}">{escape(title)} · {escape(tag)}</a>'
    return published, row


def main():
    template = (HERE / "template.md").read_text(encoding="utf-8")
    if template.count("{{releases}}") != 1:
        raise ValueError("テンプレートには {{releases}} が1箇所必要です")
    # 全件取得してから置き換える。通信失敗時も公開済みの内容を保つ。
    ordered = sorted((latest_release(repo, title) for repo, title in PROJECTS.items()), reverse=True)
    page = template.replace("{{releases}}", "\n".join(row for _, row in ordered))
    if README.exists() and README.read_text(encoding="utf-8") == page:
        return
    with NamedTemporaryFile(dir=README.parent, mode="w", encoding="utf-8", newline="\n", delete=False) as tmp:
        tmp.write(page)
    Path(tmp.name).replace(README)


if __name__ == "__main__":
    main()
