"""Render assets/medha-work.svg from medha.json (output of medha_extract.py)."""
import json, sys, datetime as dt, collections
from pathlib import Path

data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
out = Path(sys.argv[2])

LABEL = {  # repo -> (short role, stack)
    "medha-api": ("core backend", "Go"),
    "medha-admin-panel": ("admin console", "React/TS"),
    "medha-infra": ("GitOps · k8s", "Argo CD/TF"),
    "medha-web": ("public site + i18n", "React/Astro"),
    "medha-care": ("care platform", "Rust/TS"),
    "medha-ios": ("iOS app", "SwiftUI"),
    "medha-sahayak": ("LLM booking agent", "Python"),
    "medha-ops-assistant": ("offline docs QA", "Python"),
    "medha-android": ("Android fixes", "Kotlin"),
    "medha-agent": ("specs · planning", "Markdown"),
}
repos = sorted(((k, v["commits"]) for k, v in data.items() if v["commits"]), key=lambda kv: -len(kv[1]))
allc = [c for _, cs in repos for c in cs]
days = collections.Counter(dt.date.fromisoformat(c["date"]) for c in allc)
first, last = min(days), max(days)
n_commits, n_repos, n_days = len(allc), len(repos), len(days)

W, H = 1000, 298
s = []
a = s.append
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
  f'aria-label="Medha Innovations proof of work: {n_commits} commits across {n_repos} private repositories, '
  f'{first:%b %Y} to {last:%b %Y}">')
a("<title>Medha Innovations · proof of work</title>")
a("""<defs><style>
text{font-family:'JetBrains Mono','Cascadia Code',Consolas,'Courier New',monospace}
.row{fill:#00e5ff;font-size:11px;letter-spacing:3px}
.big{fill:#e6edf3;font-size:26px;font-weight:700}
.lab{fill:#8b949e;font-size:11px;letter-spacing:1px}
.t{fill:#e6edf3;font-size:12px}
.m{fill:#8b949e;font-size:11px}
.plate{fill:#161b22;stroke:#30363d}
.br{stroke:#00e5ff;stroke-width:2;fill:none}
.dot{fill:#2bff88;animation:p 2.4s ease-in-out infinite}
@keyframes p{0%,100%{opacity:.35}50%{opacity:1}}
</style></defs>""")
a(f'<rect width="{W}" height="{H}" fill="#0d1117"/>')
a('<text x="20" y="26" class="row">// PROOF OF WORK · MEDHA INNOVATIONS</text>')
a('<circle cx="958" cy="22" r="4" class="dot"/><text x="946" y="26" class="m" text-anchor="end">founding engineer</text>')

# heatmap (weeks as columns, Mon..Sun rows)
start = first - dt.timedelta(days=first.weekday())
weeks = (last - start).days // 7 + 1
cell, gap = 13, 3
hx, hy = 20, 76
a(f'<text x="{hx}" y="54" class="row">// COMMITS PER DAY</text>')
for m in range(first.month, last.month + 1):
    d = dt.date(first.year, m, 1)
    if d < first: continue
    a(f'<text x="{hx + ((d - start).days // 7) * (cell + gap)}" y="{hy - 6}" class="m">{d:%b}</text>')
def shade(n):
    return "#161b22" if n == 0 else "#0b4a55" if n <= 2 else "#00849a" if n <= 5 else "#00c2dc" if n <= 10 else "#00e5ff"
for w in range(weeks):
    for r in range(7):
        d = start + dt.timedelta(days=w * 7 + r)
        if d > last: break
        n = days.get(d, 0)
        a(f'<rect x="{hx + w*(cell+gap)}" y="{hy + r*(cell+gap)}" width="{cell}" height="{cell}" rx="2" fill="{shade(n)}">'
          f'<title>{d:%d %b %Y}: {n} commits</title></rect>')
ly = hy + 7 * (cell + gap) + 16
a(f'<text x="{hx}" y="{ly+9}" class="m">less</text>')
for i, n in enumerate([0, 1, 3, 6, 11]):
    a(f'<rect x="{hx+40+i*15}" y="{ly}" width="{cell}" height="{cell}" rx="2" fill="{shade(n)}"/>')
a(f'<text x="{hx+40+5*15+6}" y="{ly+9}" class="m">more</text>')
busiest = max(days.items(), key=lambda kv: kv[1])
a(f'<text x="{hx}" y="{ly+34}" class="m">busiest day: {busiest[0]:%d %b %Y} · {busiest[1]} commits (frontends → k8s cutover)</text>')

# per-repo bars
bx, by, bw = 580, 76, 140
a(f'<text x="{bx}" y="54" class="row">// COMMITS BY REPO</text>')
mx = len(repos[0][1])
for i, (name, cs) in enumerate(repos):
    y = by + i * 19
    role, stack = LABEL.get(name, ("", ""))
    w = max(2, round(bw * len(cs) / mx))
    a(f'<text x="{bx}" y="{y+9}" class="t">{name.replace("medha-", "")}</text>')
    a(f'<rect x="{bx+120}" y="{y}" width="{bw}" height="11" rx="2" fill="#161b22"/>'
      f'<rect x="{bx+120}" y="{y}" width="{w}" height="11" rx="2" fill="#00e5ff" opacity="{0.45 + 0.55*len(cs)/mx:.2f}"/>')
    a(f'<text x="{bx+120+bw+8}" y="{y+9}" class="t">{len(cs)}</text>'
      f'<text x="{bx+120+bw+44}" y="{y+9}" class="m">{stack}</text>')

a(f'<path d="M20 {H-30}H980" stroke="#30363d"/>')
a(f'<text x="20" y="{H-12}" class="m">source: git log over the org\'s private repos · author = me · merges, bots &amp; co-founder commits excluded</text>')
a("</svg>")
out.write_text("\n".join(s), encoding="utf-8")
print(n_commits, n_repos, n_days, first, last, busiest)
