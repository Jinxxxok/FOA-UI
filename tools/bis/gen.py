import json
s=json.load(open('/tmp/claude-0/bisbuild/simc.json'))
g=json.load(open('/tmp/claude-0/bisbuild/guides.json'))
allspec={**s,**g}
crafted=set(); tier=set()
for d in s.values():
    for it in d['gear']:
        if it['crafted']: crafted.add(it['id'])
        if it['tier']: tier.add(it['id'])
SRC={'simc':'SimC 프로필','method':'Method 가이드','icy':'Icy Veins 가이드'}
def esc(t): return t.replace('\\','\\\\').replace('"','\\"')
L=['-- FOA UI · 전문화별 BIS 자료 (자동 생성 파일: 직접 고치지 마세요)',
   '--  장비 / 보석 / 마법부여 / 소모품: SimulationCraft MID2 프로필 (12.1.5 · 한밤 시즌 2)',
   '--  SimC 프로필이 없는 전문화(일부 탱커 · 힐러)는 Method / Icy Veins 가이드의 BIS 목록',
   '--  키: "직업:전문화ID",  g = { [캐릭터 창 칸 번호] = 아이템 ID }',
   'local _, ns = ...',
   'ns.BIS = {',
   '\tver = "12.1.5 · 한밤 시즌 2",',
   '\tcrafted = { '+', '.join(f'[{i}] = true' for i in sorted(crafted))+' },',
   '\ttier = { '+', '.join(f'[{i}] = true' for i in sorted(tier))+' },',
   '\tspecs = {']
MANUAL_IDS = {'Thalassian Phoenix Oil': 243734}
for key in sorted(allspec):
    d=allspec[key]
    gear=', '.join(f'[{it["inv"]}] = {it["id"]}' for it in d['gear'])
    gems=', '.join(str(k) for k in d['gems'])
    en=', '.join(f'{{ {e["inv"]}, {e["id"]}, "{esc(e["name"])}" }}' for e in d['ench'])
    co=[]
    for k in ('flask','potion','food','rune','oil'):
        c=d['cons'].get(k)
        if not c: continue
        # SimC 아이템 표에 없는 소모품은 직접 번호 (wowhead)
        if 'id' not in c and c.get('name') in MANUAL_IDS: c = {'id': MANUAL_IDS[c['name']]}
        co.append(f'{k} = {c["id"]}' if 'id' in c else f'{k} = "{esc(c["name"])}"')
    L.append(f'\t\t["{key}"] = {{ src = "{SRC[d["src"]]}", g = {{ {gear} }}, gem = {{ {gems} }}, en = {{ {en} }}, co = {{ {", ".join(co)} }} }},')
L+=['\t},','}','']
open('/home/claude/FOA_UI/BISData.lua','w').write('\n'.join(L))
print(len(allspec), 'specs', len(crafted),'crafted', len(tier),'tier')
