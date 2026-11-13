import re,glob,os
ROOT=os.environ.get('COURS_DEPOTS','..')  # dossier qui contient les clones cours-<sigle>
COURS={ # sigle : (intitulé, UE, établissement)
 'SIF':("Sécurité informatique","SEC3266","ENSPY"),'ASI':("Audit des systèmes d'information","INF3226","ENSPY"),
 'ARGC':("Analyse des risques et gestion de crise","GES4062","ENSPY"),'IIN':("Introduction à l'investigation numérique","SEC4031","ENSPY"),
 'INA':("Investigation numérique avancée","SEC4052","ENSPY"),'HE2':("Hacking éthique II","SEC4062","ENSPY"),
 'GCI':("IT governance, COBIT et ITIL","MSN-2S3-MSI03","Chaire UNESCO"),'ACSI':("Audit et contrôle interne des SI","MSN-2S3-MSI05","Chaire UNESCO"),
 'SNSD':("Stratégie numérique et schéma directeur SI","MSN-2S4-MSI01","Chaire UNESCO"),'FAV':("Forensics et analyse de vulnérabilités","MSN-2S3-SEC07","Chaire UNESCO"),
 'NRAC':("Normes, gestion des risques et audit de cybersécurité","MSN-2S3-SEC08","Chaire UNESCO"),'APDC':("Audit de protection des données et conformité","MSN-2S4-SEC02","Chaire UNESCO"),
 'CASI':("Contrôle et audit des systèmes d'information","CAS3401","PSSFP"),'SAFI':("Supervision, analyse forensique et gestion des incidents","SIS589","Université de Garoua"),
 'FORN':("Forensique numérique","LPI342","Université de Garoua"),'SGSI':("Systèmes de gestion de la sécurité informatique","SIS498","Université de Garoua")}
ORDRE=['SIF','ASI','ARGC','IIN','INA','HE2','GCI','ACSI','SNSD','FAV','NRAC','APDC','CASI','SAFI','FORN','SGSI']
GARDE={'Cameroun','Afrique','Europe','Garoua','Bafoussam','Monte-Carlo','Active','Directory','Internet','Windows','Linux','Android','Locard','Risk','Manager','Privacy','Framework','Trilemme','Universel','Processus','Investigatif','Budapest','Malabo','Juin','Mars','Porter','Luftman','Venkatraman'}
MINUS={'Juin':'juin','Mars':'mars','Processus':'processus','Investigatif':'investigatif','Universel':'universel','Trilemme':'trilemme'}
def phrase(t):
    t=re.sub(r'\s+',' ',t).strip()
    out=[]
    for i,w in enumerate(t.split(' ')):
        core=re.sub(r"[^\wÀ-ÿ'/-]",'',w)
        if i==0:
            m0=re.match(r"^([DL]')([A-ZÉ])([a-zà-ÿ].*)$",w)
            out.append(m0.group(1)+m0.group(2).lower()+m0.group(3) if m0 else w); continue
        if core in MINUS: out.append(w.replace(core,MINUS[core])); continue
        if core in GARDE or (len(core)>1 and core.upper()==core and re.search(r'[A-ZÉ]',core)) or re.search(r'\d',core) or re.search(r'[a-z][A-Z]',core): out.append(w); continue
        m=re.match(r"^([dlDL]')(.*)$",w)
        if m: out.append(m.group(1).lower()+ (m.group(2) if (m.group(2) in GARDE or m.group(2).upper()==m.group(2)) else m.group(2)[:1].lower()+m.group(2)[1:])); continue
        out.append(w[:1].lower()+w[1:])
    return ' '.join(out)
def detex(s):
    s=re.sub(r'\\(?:textbf|textit|emph|texttt|textsc|sigle)\{([^}]*)\}',r'\1',s)
    s=s.replace('~',' ').replace('\\,',' ').replace('\\&','&').replace('\\%','%').replace('\\oe ','œ').replace('\\oe{}','œ').replace("’","'")
    return re.sub(r'\s+',' ',s).strip()
_cache={}
def chapitres(sig):
    if sig in _cache: return _cache[sig]
    r=f'{ROOT}/cours-{sig.lower()}'
    main=open(glob.glob(r+'/*_main.tex')[0],encoding='utf-8').read()
    main=re.sub(r'(?m)^\s*%.*$','',main)
    L=[];n=13 if sig=='INA' else 0;ann=0
    for m in re.finditer(r'\\(?:input|include)\{([^}]+)\}',main):
        p=m.group(1); f=r+'/'+p+('' if p.endswith('.tex') else '.tex')
        if not os.path.exists(f): continue
        t=open(f,encoding='utf-8').read(); t=re.sub(r'(?m)^\s*%.*$','',t)
        tm=re.search(r'\\chapter(\*)?(?:\[[^\]]*\])?\{((?:[^{}]|\{[^}]*\})*)\}',t)
        if not tm: continue
        titre=detex(tm.group(2)); d=p.split('/')[0]
        if d=='front': continue
        if d=='annexes': ann+=1; lab='Annexe '+chr(64+ann)
        elif re.search(r'P00|partie0',p) : lab='Prologue'; titre=re.sub(r'^Prologue\s*:\s*','',titre)
        else: n+=1; lab=f'Chap. {n}'
        qd=re.search(r'\\section\*\{Question directrice\s*:\s*((?:[^{}]|\{[^}]*\})*)\}',t)
        L.append(dict(lab=lab,titre=phrase(titre),t=t,qd=detex(qd.group(1)) if qd else ''))
    _cache[sig]=L; return L
def labs(sig,rx):
    r=f'{ROOT}/cours-{sig.lower()}/front/03b_labs.tex'
    if not os.path.exists(r): return []
    t=open(r,encoding='utf-8').read(); out=[]
    for row in re.split(r'\\\\',t):
        m=re.search(r'([A-Z0-9]+-LAB-\d+)\s*&\s*([^&]+)&',row)
        if m and rx.search(row): out.append((m.group(1),detex(m.group(2))))
    return out
def presence(pat,sauf=()):
    rx=re.compile(pat); res={}
    for s in ORDRE:
        if s in sauf: continue
        rows=[(c['lab'],c['titre'],len(rx.findall(c['t'])),c['qd'] if rx.search(c['qd']) else '') for c in chapitres(s)]
        rows=[x for x in rows if x[2]]
        if rows: res[s]=(rows,labs(s,rx))
    return res
