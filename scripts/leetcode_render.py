"""Render assets/leetcode.svg from LeetCode's public GraphQL API: problems solved by difficulty."""
import json, sys, urllib.request
from pathlib import Path

USERNAME = "vi-nayKR"
out = Path(sys.argv[1] if len(sys.argv) > 1 else "assets/leetcode.svg")

QUERY = """query($u:String!){
  allQuestionsCount{ difficulty count }
  matchedUser(username:$u){ submitStatsGlobal{ acSubmissionNum{ difficulty count } } }
}"""
req = urllib.request.Request(
    "https://leetcode.com/graphql",
    data=json.dumps({"query": QUERY, "variables": {"u": USERNAME}}).encode(),
    headers={"Content-Type": "application/json", "Referer": "https://leetcode.com", "User-Agent": "Mozilla/5.0"},
)
data = json.load(urllib.request.urlopen(req, timeout=30))["data"]
if not data["matchedUser"]:
    sys.exit(f"LeetCode user {USERNAME!r} not found")
total = {d["difficulty"]: d["count"] for d in data["allQuestionsCount"]}
solved = {d["difficulty"]: d["count"] for d in data["matchedUser"]["submitStatsGlobal"]["acSubmissionNum"]}

W, H = 1000, 172
s = []
a = s.append
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
  f'aria-label="LeetCode: {solved["All"]} problems solved. Easy {solved["Easy"]}, Medium {solved["Medium"]}, Hard {solved["Hard"]}">')
a("<title>LeetCode · problems solved</title>")
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
a('<text x="20" y="26" class="row">// LEETCODE · PROBLEMS SOLVED</text>')
a(f'<circle cx="958" cy="22" r="4" class="dot"/><text x="946" y="26" class="m" text-anchor="end">@{USERNAME}</text>')

# total plate
pw = 232
a(f'<g transform="translate(20,40)"><rect class="plate" width="{pw}" height="100" rx="3"/>'
  f'<path class="br" d="M0 12V0H12M{pw-12} 100H{pw}V88"/>'
  f'<text x="16" y="50" class="big">{solved["All"]}<tspan class="m" font-weight="400"> / {total["All"]}</tspan></text>'
  f'<text x="16" y="76" class="lab">TOTAL SOLVED</text></g>')

# difficulty plates with progress bars
COLORS = {"Easy": "#2bff88", "Medium": "#ffb020", "Hard": "#ff4d6d"}
dw, bw = 232, 200
for i, d in enumerate(("Easy", "Medium", "Hard")):
    x = 262 + i * (dw + 10)
    fill = round(bw * solved[d] / total[d]) if total[d] else 0
    a(f'<g transform="translate({x},40)"><rect class="plate" width="{dw}" height="100" rx="3"/>'
      f'<path class="br" d="M0 12V0H12M{dw-12} 100H{dw}V88"/>'
      f'<text x="16" y="50" class="big">{solved[d]}<tspan class="m" font-weight="400"> / {total[d]}</tspan></text>'
      f'<text x="16" y="70" class="lab" style="fill:{COLORS[d]}">{d.upper()}</text>'
      f'<rect x="16" y="80" width="{bw}" height="6" rx="3" fill="#0d1117"/>'
      + (f'<rect x="16" y="80" width="{max(fill, 3)}" height="6" rx="3" fill="{COLORS[d]}"/>' if solved[d] else "")
      + "</g>")

a(f'<text x="20" y="162" class="m">source: leetcode.com/u/{USERNAME} · refreshed daily by GitHub Actions</text>')
a("</svg>")
out.write_text("\n".join(s) + "\n", encoding="utf-8")
print(f"wrote {out}: {solved['All']} solved (E{solved['Easy']} M{solved['Medium']} H{solved['Hard']})")
