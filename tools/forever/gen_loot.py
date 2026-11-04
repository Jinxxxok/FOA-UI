# 포에버 던전 전리품 → FOA_UI/ForeverLoot.lua
#  loot.txt : @키|영문 이름|한글 이름(모르면 비움)|권장 최소|최대|instanceID(모르면 비움)
#             보스 이름|아이템,아이템,...
import sys
src, out = sys.argv[1], sys.argv[2]
def esc(s): return s.replace('\\', '\\\\').replace('"', '\\"')
L = ['-- FOA UI · 포에버 던전 보스별 전리품 (자동 생성 · tools/forever/gen_loot.py)',
     '-- 출처: Method WoW Forever 던전 공략 (아이템 번호는 와우헤드 링크). 포에버에서 바뀐 전리품 포함',
     'local _, ns = ...', 'ns.FOREVER_LOOT = {', '\tsrc = "Method 던전 공략",', '\tlist = {']
cur = None
def flush():
    if cur:
        b = ', '.join('{ "%s", { %s } }' % (esc(n), ', '.join(ids)) for n, ids in cur['bosses'])
        L.append('\t\t{ key = "%s", en = "%s", ko = %s, lo = %s, hi = %s, inst = %s, bosses = { %s } },' % (
            cur['key'], esc(cur['en']), ('"%s"' % esc(cur['ko'])) if cur['ko'] else 'nil', cur['lo'], cur['hi'], cur['inst'] or 'nil', b))
for line in open(src, encoding='utf-8'):
    line = line.strip()
    if not line: continue
    if line.startswith('@'):
        flush()
        k, en, ko, lo, hi, inst = line[1:].split('|')
        cur = {'key': k, 'en': en, 'ko': ko, 'lo': lo, 'hi': hi, 'inst': inst, 'bosses': []}
    else:
        n, ids = line.split('|')
        cur['bosses'].append((n, [i for i in ids.split(',') if i]))
flush()
L += ['\t},', '}', '']
open(out, 'w', encoding='utf-8').write('\n'.join(L))
