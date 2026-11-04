import json, re
G = {
 'DRUID:102': ('icy', ['Enigmatic Dreamwatcher\'s Somnolent Stare','Aqirbane Reliquary','Frothing Venom Spaulders','Silken Voodoo Drape','Enigmatic Dreamwatcher\'s Lunar Raiment','Restless Spirit Shackles','Enigmatic Dreamwatcher\'s Gauntlets','Sash of the Forlorn Vessel','Enigmatic Dreamwatcher\'s Leggings','Silvermoon Agent\'s Sneakers','Band of the Swarmcaller','Charged Sandstone Band','Vile Vial of Volatile Venom','Twisted Horror\'s Tendril','Jan\'thrazet, the Soul Fang','Aln\'hara Lantern'], ['Flawless Quick Amethyst','Indecipherable Eversong Diamond'], []),
 'EVOKER:1467': ('icy', ['Calamitous Echo\'s Magmashapers','Aqirbane Reliquary','Calamitous Echo\'s Sundered Peaks','Silken Voodoo Drape','Searing Caldera of Calamity','Farstrider\'s Plated Bracers','Calamitous Echo\'s Ebon Greathorns','Serpentine Mixing Belt','Earthen Pillars of Calamity','Ferocious Scaleboots','Band of the Swarmcaller','Apex Brute\'s Claw Ring','Gebbo\'s Bottomless Bag','Twisted Horror\'s Tendril','Jan\'thrazet, the Soul Fang','Aln\'hara Lantern'], ['Flawless Quick Garnet'],
   [(1,'Empowered Rune of Avoidance'),(3,"Akil'zon's Swiftness"),(5,'Mark of the Worldsoul'),(7,'Sunfire Silk Spellthread'),(8,"Lynx's Dexterity"),(11,'Eyes of the Eagle'),(12,'Eyes of the Eagle'),(16,"Rite of the Hash'ey")]),
 'DRUID:104': ('method', ['Gaze Of The Coiled Watcher','Aqirbane Reliquary','Somber Spaulders','Silken Voodoo Drape','Chestwrap Of Palpable Terror','Fury-Fletched Armlets','Gauntlets Of Fevered Defense','Sash Of The Forlorn Vessel','Coiled Hex Legguards','Breakwater Boots','Band Of The Swarmcaller','Alluring Bubbleband','Voracious Heart Of Ula\'tek','Twisted Horror\'s Tendril','Abyssal Broodfiend\'s Bardiche',None], [], []),
 'EVOKER:1473': ('method', ['Sethraliss\' Fanged Helm','Amulet Of The Twin Fangs','Soulslither Spaulders','Silken Voodoo Drape','Awoken Dreadfang Cuirass','Farstrider\'s Plated Bracers','Aberrant Commander\'s Gauntlets','Farstrider\'s Trophy Belt','Cuisses Of The Uncoiled Union','Ferocious Scaleboots','Band Of The Swarmcaller','Vile Alchemist\'s Band','Font Of Venomous Rage','Twisted Horror\'s Tendril','Jan\'thrazet, The Soul Fang','Spine Of The Hissing Abyss'], [], []),
 'DRUID:105': ('method', ['Gaze Of The Coiled Watcher','Amulet Of The Twin Fangs','Silvermoon Agent\'s Mantle','Silken Voodoo Drape','War Trial Vestments','Silvermoon Agent\'s Deflectors','Enigmatic Dreamwatcher\'s Gauntlets','Sash Of The Forlorn Vessel','Coiled Hex Legguards','Breakwater Boots','Vile Alchemist\'s Band','Sickening Signet Of Atroxus','Wavecaller\'s Seastone','Soulcoiler Ritual Vessel','Jan\'thrazet, The Soul Fang','Spine Of The Hissing Abyss'], [], []),
 'EVOKER:1468': ('method', ['Calamitous Echo\'s Magmashapers','Aqirbane Reliquary','Calamitous Echo\'s Sundered Peaks','Silken Voodoo Drape','Awoken Dreadfang Cuirass','Rising Tide Wristguards','Aberrant Commander\'s Gauntlets','Serpentine Mixing Belt','Earthen Pillars Of Calamity','Ferocious Scaleboots','Vile Alchemist\'s Band','Band Of The Swarmcaller','Gebbo\'s Bottomless Bag','Soulcoiler Ritual Vessel','Jan\'thrazet, The Soul Fang','Luminescent Sprout'], [], []),
 'MONK:270': ('method', ['Gaze Of The Coiled Watcher','Aqirbane Reliquary','Somber Spaulders','Silken Voodoo Drape','Chestwrap Of Palpable Terror','Restless Spirit Shackles','Monkey King\'s Fighting Fists','Sash Of The Forlorn Vessel','Coiled Hex Legguards','Bespittled Slitherslippers','Apex Brute\'s Claw Ring','Alluring Bubbleband','Wavecaller\'s Seastone','Soulcoiler Ritual Vessel','Sanctified Knight\'s Phoenixblade','Aln\'hara Lantern'], [], []),
 'PALADIN:65': ('method', ['Corroded Hulk\'s Skullcap','Aqirbane Reliquary','Cinderfury Shoulderguards','Silken Voodoo Drape','Reckless Spirit Breastplate','Shellbound Bracers','Gauntlets Of The Avian Sentinel','Girdle Of Toxic Regret','Chausses Of Unbound Rancor','Scaled Fiend\'s Warboots','Vile Alchemist\'s Band','Band Of The Swarmcaller','Soulcoiler Ritual Vessel','Gebbo\'s Bottomless Bag','Baleful Hexblade','Bubblefin Splash Guard'], [], []),
 'PRIEST:256': ('method', ['Venomkeeper\'s Horrific Cowl','Aqirbane Reliquary','Brood Cleanser\'s Amice','Bloodthorn Burnous','Summoner\'s Searing Shirt','Martyr\'s Bindings','Grasps Of The Eternal Shadow','Caustic Chain-Wrapped Sash','Forest Dream Leg-Guards','Cackling Soultreads','Band Of The Amani Warlord','Sickening Signet Of Atroxus','Hex Lord\'s Dooming Idol','Wavecaller\'s Seastone','Jan\'thrazet, The Soul Fang','Aln\'hara Lantern'], [], []),
 'PRIEST:257': ('method', ['Venomkeeper\'s Horrific Cowl','Aqirbane Reliquary','Cosmic Penitent\'s Echoing Screams','Speakeasy Shroud','Tidebound Sorcereress\'s Robes','Martyr\'s Bindings','Handwraps Of Blasphemous Rites','Cincture Of The Abyssal Grotto','Voidweaver\'s Leggings','Nek\'zali\'s Spiritwalkers','Signet Of Snarling Servitude','Apex Brute\'s Claw Ring','Soulcoiler Ritual Vessel','Gebbo\'s Bottomless Bag','Jan\'thrazet, The Soul Fang','Aln\'hara Lantern'], [], []),
 'SHAMAN:264': ('method', ['Serpent Crown Of The Ophidian Oracle','Aqirbane Reliquary','Jangling Felpaulets','Adherent\'s Silken Shroud','Awoken Dreadfang Cuirass','Farstrider\'s Plated Bracers','Hexing Grips Of The Ophidian Oracle','Cursed Reliquary Cincture','Leggings Of The Ophidian Oracle','Scaled Shoes Of The Ophidian Oracle','Apex Brute\'s Claw Ring','Pilfered Precious Band','Soulcoiler Ritual Vessel','Twisted Horror\'s Tendril','Jan\'thrazet, The Soul Fang','Venom-Slashed Scuteward'], [], []),
}
INVS=[1,2,3,15,5,9,10,6,7,8,11,12,13,14,16,17]
names=json.load(open('/tmp/claude-0/bisbuild/names.json'))['names']
def norm(s): return re.sub(r'\s+',' ',s.lower().replace('’',"'")).strip()
def find(nm):
    ids=names.get(norm(nm))
    return max(ids) if ids else None
ench={}
for line in open('/tmp/claude-0/simc/ench.inc',encoding='utf-8',errors='ignore'):
    m=re.match(r'^\s*\{\s*(\d+),',line); n=re.search(r'"((?:[^"\\]|\\.)*)"\s*\},?\s*$',line)
    if m and n: ench.setdefault(re.sub(r'\s*\|A:.*?\|a','',n.group(1)).strip().lower(),[]).append(int(m.group(1)))
def find_ench(nm):
    nm=nm.lower()
    best=None
    for k,v in ench.items():
        if k.endswith(' - '+nm) or k==nm:
            best=max(v) if best is None else max(best,max(v))
    return best
out={}; miss=[]
for key,(src,gear,gems,enc) in G.items():
    d={'src':src,'gear':[],'gems':{},'ench':[],'cons':{}}
    for inv,nm in zip(INVS,gear):
        if not nm: continue
        iid=find(nm)
        if iid: d['gear'].append({'inv':inv,'id':iid,'crafted':False,'tier':False})
        else: miss.append((key,nm))
    for g in gems:
        iid=find(g)
        if iid: d['gems'][iid]=1
        else: miss.append((key,'GEM '+g))
    for inv,nm in enc:
        eid=find_ench(nm)
        d['ench'].append({'inv':inv,'id':eid or 0,'name':nm})
        if not eid: miss.append((key,'ENCH '+nm))
    out[key]=d
json.dump(out,open('/tmp/claude-0/bisbuild/guides.json','w'),ensure_ascii=False)
print('missing',len(miss)); [print(' ',m) for m in miss]
