import re,os,sys,shutil
sys.path.insert(0,'.')
from lib import *
from data1 import ORGS
from data2 import CABINETS,SECONDAIRES,AFFAIRES,OPERATIONS
W='/home/claude/mes-cas-pratiques'
os.makedirs(W+'/front',exist_ok=True); os.makedirs(W+'/figures/logos',exist_ok=True)
for f in os.listdir('/home/claude/maletyon/logos'): shutil.copy('/home/claude/maletyon/logos/'+f,W+'/figures/logos/'+f)
for f in os.listdir('/home/claude/cours-snsd/figures/logos'): shutil.copy('/home/claude/cours-snsd/figures/logos/'+f,W+'/figures/logos/'+f)
for f in os.listdir('/home/claude/snc4/logos'): shutil.copy('/home/claude/snc4/logos/'+f,W+'/figures/logos/'+f)
sty=open('/home/claude/cours-snsd/Style_SNSD.sty',encoding='utf-8').read()
sty=sty.replace('Style_SNSD','Style_MCP')
sty=sty.replace(r"\newcommand{\titreCours}{Stratégie numérique et schéma directeur SI}",r"\newcommand{\titreCours}{Mes cas pratiques}")
sty=sty.replace(r"\newcommand{\sigleCours}{SNSD}",r"\newcommand{\sigleCours}{MaletYon}").replace(r"\newcommand{\codeUE}{MSN-2S4-MSI01}",r"\newcommand{\codeUE}{tous les cours}")
sty=sty.replace(r"\newcommand{\institutionprimaire}{Chaire UNESCO d'Afrique Centrale Accès TIC}",r"\newcommand{\institutionprimaire}{MaletYon · cours ouverts}")
sty=re.sub(r"\\newcommand\{\\tutelle\}\{[^\n]*\}",lambda m:r"\newcommand{\tutelle}{ENSPY · Chaire UNESCO ACCES-TIC · PSSFP · Université de Garoua · IAI-Cameroun}",sty)
sty=re.sub(r"\\newcommand\{\\unitepedago\}\{[^\n]*\}",lambda m:r"\newcommand{\unitepedago}{Gouvernance, audit, sécurité et investigation numérique}",sty)
sty=sty.replace(r"\fancyhead[LE]{\small\color{CouleurPrimaire}\leftmark}",r"\fancyhead[LE]{\small\color{CouleurPrimaire}Mes cas pratiques · les organisations fictives de mes cours}")
sty=sty.replace(r"\fancyfoot[LO,RE]{\small\color{CouleurAccent}\textit{\sigleCours{} · UE\,\codeUE}}",r"\fancyfoot[LO,RE]{\small\color{CouleurAccent}\textit{MaletYon · recueil commun à tous les cours}}")
open(W+'/Style_MCP.sty','w',encoding='utf-8').write(sty)
def tx(s):
    s=s.replace('\\','\\textbackslash{}')
    for a,b in [('&',r'\&'),('%',r'\%'),('#',r'\#'),('_',r'\_'),('$',r'\$')]: s=s.replace(a,b)
    s=re.sub(r'\*\*([^*]+)\*\*',r'\\textbf{\1}',s)
    s=s.replace(' :','~:').replace(' ;','~;').replace(' ?','~?').replace('« ','«~').replace(' »','~»').replace('n° ','n°~')
    return re.sub(r'(\d) (\d{3})',r'\1\\,\2',s)
L=[]
def chap(titre,marque):
    L.append(f"\\chapter{{{tx(titre)}}}\n\\chaptermark{{{tx(marque)}}}\\markright{{{tx(marque)}}}\n")
def fiche(o):
    P=presence(o['pat'],o.get('sauf',()))
    chap(o['nom'],o['nom']+' · '+(o['nature'][0].lower()+o['nature'][1:])+(', '+o['lieu'] if o['lieu'] else ''))
    L.append(f"\\begin{{boxinfo}}\n\\textbf{{{tx(o['nature'])}{tx(', '+o['lieu']) if o['lieu'] else ''}. Organisation fictive.}}\n\n\\smallskip {tx(o['resume'])}\n\\end{{boxinfo}}\n")
    L.append("\\section{Fiche d'identité}\n\\begin{tableaucours}{L{3.6cm}L{8.6cm}}{\\tableauHeader{Élément} & \\tableauHeader{Description}}")
    for k,v in o['fiche']: L.append(f"{tx(k)} & {tx(v)} \\\\")
    L.append("\\end{tableaucours}\n")
    if o['personnes']:
        L.append("\\section{Les personnes}\n\\begin{tableaucours}{L{3.6cm}L{8.6cm}}{\\tableauHeader{Nom} & \\tableauHeader{Rôle}}")
        for k,v in o['personnes']: L.append(f"{tx(k)} & {tx(v)} \\\\")
        L.append("\\end{tableaucours}\n")
    L.append("\\section{Ce qui lui arrive}\n")
    for h in o['histoire']: L.append(tx(h)+"\n")
    L.append("\\section{Où la retrouver et pour apprendre quoi}\n")
    for s in ORDRE:
        if s not in P: continue
        rows,lb=P[s]; t,ue,et=COURS[s]
        L.append(f"\\subsection*{{{s} · {tx(t)}}}\n{{\\small\\itshape {tx(ue)}, {tx(et)}.}}\n")
        if s in o['cours']: L.append("\\textbf{Contexte.} "+tx(o['cours'][s])+"\n")
        if lb: L.append("\\textbf{Labs.} "+tx(' ; '.join(f"{a} « {b} »" for a,b in lb))+".\n")
        L.append("{\\small\\begin{longtable}{@{}p{1.5cm}p{5.0cm}p{0.9cm}p{4.6cm}@{}}\n\\toprule \\textbf{Chapitre} & \\textbf{Titre} & \\textbf{Ment.} & \\textbf{Question posée au cas} \\\\ \\midrule \\endhead")
        for lab,ti,n,qd in rows: L.append(f"{lab} & {tx(ti)} & {n} & {tx('« '+qd[0].upper()+qd[1:]+' »') if qd else ''} \\\\")
        L.append("\\bottomrule\\end{longtable}}\n")
    return P
PRES={}
L.append("\\part{Les organisations}\n")
for o in ORGS: PRES[o['cle']]=fiche(o)
L.append("\\part{Les cabinets et les experts}\n")
for o in CABINETS: PRES[o['cle']]=fiche(o)
def ou(pat):
    P=presence(pat); return ' ; '.join(f"{s} ({', '.join(r[0].replace('Chap. ','').lower() for r in P[s][0])})" for s in ORDRE if s in P)
L.append("\\part{Autour des cas}\n")
chap("Prestataires, clients et partenaires","Prestataires, clients et partenaires")
L.append("Ces organisations fictives gravitent autour des cas principaux. Elles portent souvent la leçon du chapitre~: un contrat mal écrit, un accès distant, un rapport rédigé par celui qu'il évalue.\n")
L.append("{\\small\\begin{longtable}{@{}p{2.6cm}p{2.2cm}p{4.6cm}p{2.9cm}@{}}\n\\toprule \\textbf{Organisation} & \\textbf{Nature} & \\textbf{Rôle dans les cas} & \\textbf{Cours (chapitres)} \\\\ \\midrule \\endhead")
for nom,pat,nat,role in SECONDAIRES: L.append(f"\\textbf{{{tx(nom)}}} & {tx(nat)} & {tx(role)} & {tx(ou(pat))} \\\\[0.6ex]")
L.append("\\bottomrule\\end{longtable}}\n")
chap("Les affaires d'investigation numérique","Les affaires d'investigation numérique")
L.append("Les cours IIN et INA ne suivent pas une seule organisation. Ils travaillent sur des affaires, chacune choisie pour une technique ou une question de droit. Les personnes et les sociétés citées sont fictives. Les schémas d'infraction sont réels.\n")
L.append("{\\small\\begin{longtable}{@{}p{2.6cm}p{2.6cm}p{4.4cm}p{2.7cm}@{}}\n\\toprule \\textbf{Affaire} & \\textbf{Organisation ou victime} & \\textbf{Ce que l'affaire enseigne} & \\textbf{Cours (chapitres)} \\\\ \\midrule \\endhead")
for nom,pat,org,res in AFFAIRES: L.append(f"\\textbf{{{tx(nom)}}} & {tx(org)} & {tx(res)} & {tx(ou(pat))} \\\\[0.6ex]")
L.append("\\bottomrule\\end{longtable}}\n")
L.append(tx("Le cours INA contient aussi un cas de rançongiciel à l'hôpital des Sept Collines, établissement fictif de Yaoundé. Il porte le nom d'« opération NTEM ».")+"\n\n"+tx("La formation OPJ-APJ, en accès réservé, reprend les affaires MBONGO, ONAMBELE, BAOBAB et MOABI. Ses dossiers propres ne sont pas décrits ici.")+"\n")
L.append("\\part{Index}\n")
chap("Qui apparaît où","Qui apparaît où")
TOUS=ORGS+CABINETS
L.append("Le chiffre est le nombre de chapitres du cours où l'organisation apparaît.\n\n{\\scriptsize\\setlength{\\tabcolsep}{2.2pt}\\begin{longtable}{@{}p{3.3cm}"+"c"*len(ORDRE)+"@{}}\n\\toprule \\textbf{Organisation} & "+' & '.join(f"\\rotatebox{{90}}{{{s}}}" for s in ORDRE)+" \\\\ \\midrule \\endhead")
for o in TOUS: L.append(f"{tx(o['nom'])} & "+' & '.join(str(len(PRES[o['cle']][s][0])) if s in PRES[o['cle']] else '' for s in ORDRE)+" \\\\")
L.append("\\bottomrule\\end{longtable}}\n")
L.append("\\section{Par cours}\n{\\small\\begin{longtable}{@{}p{4.6cm}p{2.3cm}p{2.3cm}p{3.1cm}@{}}\n\\toprule \\textbf{Cours} & \\textbf{UE} & \\textbf{Fil rouge} & \\textbf{Autres cas} \\\\ \\midrule \\endhead")
for s in ORDRE:
    sc=sorted([(sum(r[2] for r in PRES[o['cle']][s][0]),o['nom']) for o in ORGS if s in PRES[o['cle']]],key=lambda x:-x[0])
    fil=[x[1] for x in sc[:1]]; aut=[x[1] for x in sc[1:]]; cab=[o['nom'] for o in CABINETS if s in PRES[o['cle']]]
    if s in('IIN','INA'): fil=["Affaires d'investigation"]; aut=[]
    L.append(f"{s} · {tx(COURS[s][0])} & {tx(COURS[s][1])} & {tx(', '.join(fil))} & {tx(', '.join(aut+cab))} \\\\[0.4ex]")
L.append("\\bottomrule\\end{longtable}}\n")
chap("Les opérations","Les opérations")
L.append("Dans les livres, chaque épisode d'un cas porte un nom d'opération, souvent celui d'un cours d'eau ou d'une ville.\n\n{\\small\\begin{longtable}{@{}p{2.8cm}p{2.8cm}p{4.4cm}p{2.3cm}@{}}\n\\toprule \\textbf{Opération} & \\textbf{Organisation} & \\textbf{Objet} & \\textbf{Cours} \\\\ \\midrule \\endhead")
for a,b,c,d in OPERATIONS: L.append(f"{tx(a)} & {tx(b)} & {tx(c)} & {tx(d)} \\\\")
L.append("\\bottomrule\\end{longtable}}\n\\section{Un nom, une seule chose}\n"+tx("Chaque nom d'organisation, d'opération et de projet ne désigne qu'une seule chose dans tout le cursus. Quelques noms de famille courants sont encore portés par des personnes différentes : KAMGA, MBARGA, ATANGANA, NDONGO, BELLO. La fiche de chaque organisation donne les siens.")+"\n")
open(W+'/corps.tex','w',encoding='utf-8').write('\n'.join(L))
print('corps',len(L))
