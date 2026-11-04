# 포에버 BIS · 준비물 데이터 → FOA_UI/ForeverBIS.lua
#  method_bis.txt : @CLASS:spec / PRE|부위|이름|아이템번호|획득처 / ALT|... / STATS|...
#  cons.txt       : @키 키 ... / E|부위|item=번호 또는 spell=번호 / C|종류|item=번호
import sys, re
src_dir, out = sys.argv[1], sys.argv[2]
INV = {'head':[1],'neck':[2],'shoulder':[3],'cloak':[15],'back':[15],'chest':[5],'wrist':[9],'hands':[10],'gloves':[10],
       'waist':[6],'belt':[6],'legs':[7],'feet':[8],'boots':[8],'ring':[11,12],'ring 1':[11],'ring 2':[12],
       'trinket':[13,14],'trinket 1':[13],'trinket 2':[14],'1h weapon':[16],'weapon':[16],'2h weapon':[16],
       'off hand':[17],'shield':[17],'main hand':[16],'ranged':[18],'libram':[18],'idol':[18],'totem':[18]}
def esc(s): return s.replace('\\','\\\\').replace('"','\\"')
specs = {}
cur = None
for line in open(src_dir + '/method_bis.txt', encoding='utf-8'):
    line = line.strip()
    if not line: continue
    if line.startswith('@'):
        cur = line[1:]; specs.setdefault(cur, {'pre': [], 'alt': [], 'stats': '', 'E': [], 'C': []}); continue
    p = line.split('|')
    if p[0] == 'STATS':
        specs[cur]['stats'] = '' if p[1] == '-' else p[1]
    elif p[0] in ('PRE', 'ALT') and len(p) >= 5 and p[3].isdigit():
        specs[cur]['pre' if p[0] == 'PRE' else 'alt'].append((p[1].lower(), int(p[3]), p[4]))
for line in open(src_dir + '/cons.txt', encoding='utf-8'):
    line = line.strip()
    if not line: continue
    if line.startswith('@'):
        keys = line[1:].split()
        for k in keys: specs.setdefault(k, {'pre': [], 'alt': [], 'stats': '', 'E': [], 'C': []})
        continue
    kind, slot, ref = line.split('|')
    t, n = ref.split('=')
    for k in keys: specs[k][kind].append((slot, t, int(n)))
L = ['-- FOA UI · 포에버 BIS · 준비물 (자동 생성 · tools/forever/gen_bis.py)',
     '-- 출처: Method WoW Forever 공략 (패치 1.60.1, 2026-11-04) · 아이템 번호는 와우헤드 포에버 링크',
     '-- g = BIS { [칸] = 아이템 } · alt = 대체 { 칸, 아이템 } (공략 순서) · src = 획득처 · en = 마부 · co = 소모품',
     'local _, ns = ...', 'ns.BIS_FOREVER = {', '\tsrc = "Method 공략",', '\tspecs = {']
for key in sorted(specs):
    d = specs[key]
    g, alt, srcs = {}, [], {}
    used = {}
    for slot, iid, s in d['pre']:
        invs = INV.get(slot)
        if not invs: continue
        n = used.get(slot, 0); used[slot] = n + 1
        inv = invs[min(n, len(invs) - 1)]
        if inv in g:  # 같은 칸 두 번째 (진영별 등) → 대체 1순위로
            alt.insert(0, (inv, iid))
        else:
            g[inv] = iid
        srcs[iid] = s
    for slot, iid, s in d['alt']:
        invs = INV.get(slot)
        if not invs or iid in g.values(): continue
        alt.append((invs[0], iid)); srcs.setdefault(iid, s)
    gs = ', '.join(f'[{k}] = {v}' for k, v in sorted(g.items()))
    als = ', '.join(f'{{ {a}, {b} }}' for a, b in alt)
    ss = ', '.join(f'[{k}] = "{esc(v)}"' for k, v in srcs.items())
    en = ', '.join(f'{{ "{esc(s)}", "{t}", {n} }}' for s, t, n in d['E'])
    co = ', '.join(f'{{ "{esc(s)}", {n} }}' for s, t, n in d['C'])
    L.append(f'\t\t["{key}"] = {{ stats = "{esc(d["stats"])}", g = {{ {gs} }}, alt = {{ {als} }}, src = {{ {ss} }}, en = {{ {en} }}, co = {{ {co} }} }},')
L += ['\t},', '}', '']
open(out, 'w', encoding='utf-8').write('\n'.join(L))
print(len(specs), 'specs')
