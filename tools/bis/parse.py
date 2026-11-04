import re, json, sys, os
SIMC='/tmp/claude-0/simc'
SPEC={ 'Death_Knight_Blood':('DEATHKNIGHT',250),'Death_Knight_Frost':('DEATHKNIGHT',251),'Death_Knight_Unholy':('DEATHKNIGHT',252),
 'Demon_Hunter_Havoc':('DEMONHUNTER',577),'Demon_Hunter_Vengeance':('DEMONHUNTER',581),'Demon_Hunter_Devourer':('DEMONHUNTER',1480),
 'Druid_Feral':('DRUID',103),'Hunter_Beast_Mastery':('HUNTER',253),'Hunter_Marksmanship':('HUNTER',254),'Hunter_Survival':('HUNTER',255),
 'Mage_Arcane':('MAGE',62),'Mage_Fire':('MAGE',63),'Mage_Frost':('MAGE',64),'Monk_Brewmaster':('MONK',268),'Monk_Windwalker':('MONK',269),
 'Paladin_Protection':('PALADIN',66),'Paladin_Retribution':('PALADIN',70),'Priest_Shadow':('PRIEST',258),
 'Rogue_Assassination':('ROGUE',259),'Rogue_Outlaw':('ROGUE',260),'Rogue_Subtlety':('ROGUE',261),
 'Shaman_Elemental':('SHAMAN',262),'Shaman_Enhancement':('SHAMAN',263),'Warlock_Affliction':('WARLOCK',265),'Warlock_Demonology':('WARLOCK',266),
 'Warlock_Destruction':('WARLOCK',267),'Warrior_Arms':('WARRIOR',71),'Warrior_Fury':('WARRIOR',72),'Warrior_Protection':('WARRIOR',73)}
INV={'head':1,'neck':2,'shoulders':3,'shoulder':3,'back':15,'chest':5,'wrists':9,'wrist':9,'hands':10,'waist':6,'legs':7,'feet':8,
 'finger1':11,'finger2':12,'trinket1':13,'trinket2':14,'main_hand':16,'off_hand':17}
# item names -> ids
items={}  # token -> list of (id, qualrank)
names={}
rx=re.compile(r'^\s*\{\s*"((?:[^"\\]|\\.)*)",\s*(\d+),.*?,\s*(\d+)\s*\},?\s*$')
for line in open(SIMC+'/item_data.inc',encoding='utf-8',errors='ignore'):
    m=rx.match(line)
    if not m: continue
    nm, iid, last = m.group(1).replace('\\"','"'), int(m.group(2)), int(m.group(3))
    tok=re.sub(r'[^a-z0-9]+','_',nm.lower().replace("'",'')).strip('_')
    items.setdefault(tok,[]).append((iid,last))
    names.setdefault(nm.lower(),[]).append(iid)
ench={}
erx=re.compile(r'^\s*\{\s*(\d+),.*?(-?\d+),\s*"(.*)"\s*\},?\s*$')
for line in open(SIMC+'/ench.inc',encoding='utf-8',errors='ignore'):
    m=re.match(r'^\s*\{\s*(\d+),',line)
    if not m: continue
    nm=re.search(r'"((?:[^"\\]|\\.)*)"\s*\},?\s*$',line)
    if nm:
        txt=re.sub(r'\s*\|A:.*?\|a','',nm.group(1)).strip()
        ench[int(m.group(1))]=txt
def cons(tok):
    tok=tok.split(',')[0]
    q=None
    mm=re.match(r'(.*)_(\d)$',tok)
    base=tok
    if mm: base,q=mm.group(1),int(mm.group(2))
    cands=items.get(base) or items.get(base+'_augment_rune') or []
    if not cands: return {'name':base.replace('_',' ').title()}
    best=[c for c in cands if q is None or c[1]==q] or cands
    return {'id':max(best)[0]}
out={}
for f,(cls,sid) in SPEC.items():
    p=f'{SIMC}/prof/{f}.simc'
    if not os.path.exists(p): continue
    d={'src':'simc','gear':[],'gems':{},'ench':[],'cons':{}}
    for line in open(p):
        line=line.strip()
        k,_,v=line.partition('=')
        if k in ('potion','flask','food','augmentation'):
            if v and v!='disabled': d['cons'][{'augmentation':'rune'}.get(k,k)]=cons(v)
        elif k=='temporary_enchant':
            if v and v!='disabled':
                t=v.split('/')[0].split(':')[-1]
                d['cons']['oil']=cons(t)
        elif k in INV and ',id=' in v:
            iid=int(re.search(r',id=(\d+)',v).group(1))
            inv=INV[k]
            d['gear'].append({'inv':inv,'id':iid,'crafted':('crafted_stats=' in v or re.search(r'bonus_id=[^,]*\b(8790|8960)\b',v) is not None),'tier':'redirected_base_stats=' in v})
            g=re.search(r'gem_id=([\d/]+)',v)
            if g:
                for x in g.group(1).split('/'): d['gems'][int(x)]=d['gems'].get(int(x),0)+1
            e=re.search(r'enchant_id=(\d+)',v)
            if e: d['ench'].append({'inv':inv,'id':int(e.group(1)),'name':ench.get(int(e.group(1)),'')})
    out[f'{cls}:{sid}']=d
json.dump(out,open('/tmp/claude-0/bisbuild/simc.json','w'),ensure_ascii=False,indent=0)
json.dump({'names':{k:v for k,v in names.items()}}, open('/tmp/claude-0/bisbuild/names.json','w'))
print(len(out))
r=out['ROGUE:259']; print(json.dumps(r,ensure_ascii=False)[:1500])
