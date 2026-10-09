"""Check portable skill links and public-package boundaries with Python stdlib."""
from pathlib import Path
import re
import shutil
import tempfile

NAMES = ("pair-writing", "generative-research")


def check_skills(root):
    skills = root / "skills"
    assert {p.name for p in skills.iterdir()} == set(NAMES), "Expected two skills"
    for name in NAMES:
        entry = skills / name / "SKILL.md"
        text = entry.read_text(encoding="utf-8")
        assert text.startswith("---\n"), entry
        header = text.split("---", 2)[1]
        assert f"name: {name}" in header, entry
        assert "description:" in header, entry
        assert (skills / name / "agents/openai.yaml").is_file(), name
    docs = list(skills.rglob("*.md")) + [root / "README.md"]
    for doc in docs:
        text = doc.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            if re.match(r"https?://", target) or target.startswith("#"):
                continue
            destination = (doc.parent / target.split("#", 1)[0]).resolve()
            assert destination.is_relative_to(root.resolve()), (doc, target)
            assert destination.is_file(), (doc, target)
        assert not re.search(r"/Users/|KB/(?:wiki|raw|output)/|\[\[|claude写作规范_Pair_version|K-C-P 能力现状", text), doc
        assert not re.search(r"(?:ghp_|github_pat_|sk-)[A-Za-z0-9_]{20,}", text), doc
    assert not list(skills.rglob("*.zip")), "Third-party snapshots excluded"
    return len(docs)


def main():
    root = Path(__file__).resolve().parents[1]
    count = check_skills(root)
    with tempfile.TemporaryDirectory(prefix="fox-skills-install-") as directory:
        moved = Path(directory)
        shutil.copytree(root / "skills", moved / "skills")
        shutil.copy2(root / "README.md", moved / "README.md")
        assert check_skills(moved) == count
    print(f"PASS: two skills, {count} Markdown files, local links and relocated copy")


if __name__ == "__main__":
    main()
