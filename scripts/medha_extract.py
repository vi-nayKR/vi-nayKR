"""Extract Vinay's authored commits from local medha-innovations clones into JSON."""
import json, re, subprocess, sys, collections
from pathlib import Path

ROOT = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(r"C:\Users\vinay\Developer\medha")
OUT = Path(sys.argv[1])
ME = re.compile(r"vinay", re.I)
EXT_LANG = {".go": "Go", ".kt": "Kotlin", ".kts": "Kotlin", ".swift": "Swift", ".ts": "TypeScript",
            ".tsx": "TypeScript", ".js": "JavaScript", ".jsx": "JavaScript", ".py": "Python",
            ".sql": "SQL", ".tf": "Terraform", ".hcl": "Terraform", ".yml": "YAML", ".yaml": "YAML",
            ".sh": "Shell", ".css": "CSS", ".html": "HTML", ".java": "Java", ".rs": "Rust", ".dart": "Dart"}
SKIP = re.compile(r"(lock\.json|\.lock$|go\.sum$|\.min\.|/vendor/|/dist/|/build/|\.pb\.go$|generated|\.svg$|\.png$|\.jpg$)", re.I)

def git(repo, *args):
    return subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True, encoding="utf-8", errors="replace").stdout

data = {}
for repo in sorted(p for p in ROOT.iterdir() if (p / ".git").exists()):
    log = git(repo, "log", "--all", "--no-merges", "--numstat", "--date=short",
              "--format=\x1e%H\x1f%an\x1f%ae\x1f%ad\x1f%s")
    total = 0
    commits, langs = [], collections.Counter()
    for chunk in log.split("\x1e")[1:]:
        head, *files = chunk.strip("\n").split("\n")
        sha, an, ae, date, subj = head.split("\x1f")
        total += 1
        if not ME.search(an) or "5star" in an.lower():
            continue
        add = dele = 0
        for f in files:
            parts = f.split("\t")
            if len(parts) != 3 or parts[0] == "-" or SKIP.search(parts[2]):
                continue
            a, d = int(parts[0]), int(parts[1])
            add += a; dele += d
            lang = EXT_LANG.get(Path(parts[2]).suffix.lower())
            if lang:
                langs[lang] += a + d
        commits.append({"sha": sha[:7], "date": date, "subject": subj, "add": add, "del": dele})
    data[repo.name] = {"total_commits": total, "commits": commits, "langs": dict(langs.most_common())}

OUT.write_text(json.dumps(data, indent=1), encoding="utf-8")
for k, v in data.items():
    c = v["commits"]
    print(f"{k:22} mine={len(c):4}/{v['total_commits']:4} +{sum(x['add'] for x in c):7} -{sum(x['del'] for x in c):7} {list(v['langs'])[:4]}")
print("TOTAL", sum(len(v["commits"]) for v in data.values()))
