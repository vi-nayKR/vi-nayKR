"""Render assets/leetcode.svg: LeetCode problems solved by difficulty, plus NeetCode 150 / Blind 75 progress.

LeetCode totals come from the public GraphQL API. NeetCode progress needs the LEETCODE_SESSION
cookie (env var): every NeetCode problem is a LeetCode problem, so we check each one's solved status.
Pass --require-neetcode to fail instead of skipping the NeetCode row when the cookie is missing.
"""
import json, os, sys, urllib.request
from pathlib import Path

USERNAME = "vi-nayKR"
NEETCODE_LISTS = "https://raw.githubusercontent.com/neetcode-gh/leetcode/main/.problemSiteData.json"
args = [x for x in sys.argv[1:] if not x.startswith("--")]
out = Path(args[0] if args else "assets/leetcode.svg")
session = os.environ.get("LEETCODE_SESSION", "").strip()


def gql(query, variables=None, auth=False):
    headers = {"Content-Type": "application/json", "Referer": "https://leetcode.com", "User-Agent": "Mozilla/5.0"}
    if auth:
        headers |= {"Cookie": f"LEETCODE_SESSION={session}; csrftoken=x", "x-csrftoken": "x"}
    req = urllib.request.Request("https://leetcode.com/graphql", headers=headers,
                                 data=json.dumps({"query": query, "variables": variables or {}}).encode())
    body = json.load(urllib.request.urlopen(req, timeout=60))
    if body.get("errors"):
        sys.exit(f"LeetCode API error: {body['errors']}")
    return body["data"]


data = gql("""query($u:String!){
  allQuestionsCount{ difficulty count }
  matchedUser(username:$u){ submitStatsGlobal{ acSubmissionNum{ difficulty count } } }
}""", {"u": USERNAME})
if not data["matchedUser"]:
    sys.exit(f"LeetCode user {USERNAME!r} not found")
total = {d["difficulty"]: d["count"] for d in data["allQuestionsCount"]}
solved = {d["difficulty"]: d["count"] for d in data["matchedUser"]["submitStatsGlobal"]["acSubmissionNum"]}

# NeetCode progress: {list name: (problems, solved slugs)}
neet = None
if session:
    problems = json.load(urllib.request.urlopen(NEETCODE_LISTS, timeout=60))
    for p in problems:
        p["slug"] = p["link"].strip("/")
    me = gql("{ userStatus{ isSignedIn username } }", auth=True)["userStatus"]
    if not me["isSignedIn"]:
        sys.exit("LEETCODE_SESSION is expired or invalid: copy a fresh one from leetcode.com cookies")
    if me["username"].lower() != USERNAME.lower():
        sys.exit(f"LEETCODE_SESSION belongs to {me['username']!r}, expected {USERNAME!r}")
    slugs = sorted({p["slug"] for p in problems if p.get("neetcode150") or p.get("blind75")})
    q = "{" + " ".join(f'q{i}: question(titleSlug:{json.dumps(s)}){{ status }}' for i, s in enumerate(slugs)) + "}"
    st = gql(q, auth=True)
    done = {s for i, s in enumerate(slugs) if (st[f"q{i}"] or {}).get("status") == "ac"}
    neet = {name: ([p for p in problems if p.get(key)], done)
            for name, key in (("NEETCODE 150", "neetcode150"), ("BLIND 75", "blind75"))}
elif "--require-neetcode" in sys.argv:
    sys.exit("LEETCODE_SESSION is not set")
else:
    print("LEETCODE_SESSION not set: skipping NeetCode row")

W, H = 1000, 312 if neet else 172
s = []
a = s.append
label = f"LeetCode: {solved['All']} problems solved. Easy {solved['Easy']}, Medium {solved['Medium']}, Hard {solved['Hard']}"
if neet:
    label += "".join(f". {n.title()}: {sum(p['slug'] in d for p in ps)} of {len(ps)}" for n, (ps, d) in neet.items())
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{label}">')
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


def plate(x, y, w, value, of, lab, color=None, fill=None, extra=""):
    bw = w - 32
    g = (f'<g transform="translate({x},{y})"><rect class="plate" width="{w}" height="100" rx="3"/>'
         f'<path class="br" d="M0 12V0H12M{w-12} 100H{w}V88"/>'
         f'<text x="16" y="50" class="big">{value}<tspan class="m" font-weight="400"> / {of}</tspan></text>')
    if color is None:
        return g + f'<text x="16" y="76" class="lab">{lab}</text></g>'
    g += (f'<text x="16" y="70" class="lab" style="fill:{color}">{lab}</text>{extra}'
          f'<rect x="16" y="80" width="{bw}" height="6" rx="3" fill="#0d1117"/>')
    if value:
        g += f'<rect x="16" y="80" width="{max(round(bw * fill), 3)}" height="6" rx="3" fill="{color}"/>'
    return g + "</g>"


# LeetCode: total + difficulty plates
COLORS = {"Easy": "#2bff88", "Medium": "#ffb020", "Hard": "#ff4d6d"}
a(plate(20, 40, 232, solved["All"], total["All"], "TOTAL SOLVED"))
for i, d in enumerate(("Easy", "Medium", "Hard")):
    a(plate(262 + i * 242, 40, 232, solved[d], total[d], d.upper(), COLORS[d], solved[d] / total[d] if total[d] else 0))

# NeetCode: one wide plate per list, with an Easy/Medium/Hard split
if neet:
    a('<text x="20" y="168" class="row">// NEETCODE ROADMAP</text>')
    for i, (name, (ps, done)) in enumerate(neet.items()):
        n = sum(p["slug"] in done for p in ps)
        split = " · ".join(
            f'{d[0]} {sum(p["slug"] in done for p in ps if p["difficulty"] == d)}/{sum(p["difficulty"] == d for p in ps)}'
            for d in ("Easy", "Medium", "Hard"))
        x, w = 20 + i * 484, 474
        a(plate(x, 180, w, n, len(ps), name, "#00e5ff", n / len(ps),
                f'<text x="{w-16}" y="50" class="m" text-anchor="end">{split}</text>'))

a(f'<text x="20" y="{H-10}" class="m">source: leetcode.com/u/{USERNAME}'
  f'{" · NeetCode lists from neetcode-gh/leetcode" if neet else ""} · refreshed daily by GitHub Actions</text>')
a("</svg>")
out.write_text("\n".join(s) + "\n", encoding="utf-8")
print(f"wrote {out}: {solved['All']} solved (E{solved['Easy']} M{solved['Medium']} H{solved['Hard']})"
      + "".join(f"; {n} {sum(p['slug'] in d for p in ps)}/{len(ps)}" for n, (ps, d) in (neet or {}).items()))
