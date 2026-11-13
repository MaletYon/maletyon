import re,os,sys
sys.path.insert(0,'.')
from lib import *
from data1 import ORGS
from data2 import CABINETS,SECONDAIRES,AFFAIRES,OPERATIONS
OUT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.makedirs(OUT+'/organisations',exist_ok=True)
GH='https://github.com/maletyon/cours-'
def lien(s): return f"[{s}]({GH}{s.lower()})"
def page(o,groupe):
    P=presence(o['pat'],o.get('sauf',())); L=[]
    L.append(f"# {o['nom']}\n")
    L.append(f"*{o['nature']}{', '+o['lieu'] if o['lieu'] else ''}. Organisation fictive.*\n")
    L.append(o['resume']+"\n")
    L.append("## Fiche d'identité\n\n| | |\n|---|---|")
    for k,v in o['fiche']: L.append(f"| **{k}** | {v} |")
    if o['personnes']:
        L.append("\n## Les personnes\n\n| Nom | Rôle |\n|---|---|")
        for k,v in o['personnes']: L.append(f"| {k} | {v} |")
    L.append("\n## Ce qui lui arrive\n")
    for h in o['histoire']: L.append("- "+h)
    L.append("\n## Où la retrouver et pour apprendre quoi\n")
    nb=sum(len(v[0]) for v in P.values())
    L.append(f"{o['nom']} apparaît dans {len(P)} cours et {nb} chapitres. La colonne « Mentions » compte les occurrences du nom dans le chapitre : elle indique si le cas y est central ou seulement cité.\n")
    for s in ORDRE:
        if s not in P: continue
        rows,lb=P[s]; t,ue,et=COURS[s]
        L.append(f"### {s} · {t}\n\n*{ue}, {et}. Dépôt {lien(s)}.*\n")
        if s in o['cours']: L.append("**Contexte.** "+o['cours'][s]+"\n")
        if lb: L.append("**Labs.** "+' ; '.join(f"{a} « {b} »" for a,b in lb)+".\n")
        L.append("| Chapitre | Titre | Mentions | Question posée au cas |\n|---|---|---|---|")
        for lab,ti,n,qd in rows: L.append(f"| {lab} | {ti} | {n} | {('« '+qd[0].upper()+qd[1:]+' »') if qd else ''} |")
        L.append("")
    L.append("---\n\n[← Mes cas pratiques](../README.md)")
    open(f"{OUT}/organisations/{o['cle']}.md",'w',encoding='utf-8').write('\n'.join(L)+'\n')
    return P
PRES={}
for o in ORGS: PRES[o['cle']]=page(o,'org')
for o in CABINETS: PRES[o['cle']]=page(o,'cab')
def ou(pat):
    P=presence(pat); out=[]
    for s in ORDRE:
        if s in P:
            labs_=[r[0].replace('Chap. ','').lower() for r in P[s][0]]
            out.append(f"{s} ({', '.join(labs_)})")
    return ' ; '.join(out)
# prestataires
L=["# Prestataires, clients et partenaires\n","Ces organisations fictives gravitent autour des cas principaux. Elles portent souvent la leçon du chapitre : un contrat mal écrit, un accès distant, un rapport rédigé par celui qu'il évalue.\n","| Organisation | Nature | Rôle dans les cas | Cours (chapitres) |\n|---|---|---|---|"]
for nom,pat,nat,role in SECONDAIRES: L.append(f"| **{nom}** | {nat} | {role} | {ou(pat)} |")
L.append("\n---\n\n[← Mes cas pratiques](README.md)")
open(OUT+'/prestataires.md','w',encoding='utf-8').write('\n'.join(L)+'\n')
# affaires
L=["# Les affaires d'investigation numérique\n","Les cours IIN et INA ne suivent pas une seule organisation. Ils travaillent sur des affaires, chacune choisie pour une technique ou une question de droit. Les personnes et les sociétés citées sont fictives. Les schémas d'infraction sont réels.\n","| Affaire | Organisation ou victime | Ce que l'affaire enseigne | Cours (chapitres) |\n|---|---|---|---|"]
for nom,pat,org,res in AFFAIRES: L.append(f"| **{nom}** | {org} | {res} | {ou(pat)} |")
L.append("\nLe cours INA contient aussi un cas de rançongiciel à l'hôpital des Sept Collines, établissement fictif de Yaoundé. Il porte le nom d'« opération NTEM ».\n")
L.append("La formation OPJ-APJ, en accès réservé, reprend les affaires MBONGO, ONAMBELE, BAOBAB et MOABI. Ses dossiers propres ne sont pas décrits ici.\n")
L.append("---\n\n[← Mes cas pratiques](README.md)")
open(OUT+'/affaires-investigation.md','w',encoding='utf-8').write('\n'.join(L)+'\n')
# index
TOUS=ORGS+CABINETS
L=["# Mes cas pratiques\n","[Livre (PDF)](Mes_cas_pratiques.pdf) · [télécharger](https://github.com/maletyon/maletyon/raw/main/cas-pratiques/Mes_cas_pratiques.pdf) · [← Tous les cours de MaletYon](../README.md)\n",
"Tous mes cours travaillent sur les mêmes organisations fictives. Une entreprise attaquée dans le cours de sécurité est auditée dans le cours d'audit, reconstruite dans le cours de gestion des risques, testée dans le cours de hacking éthique. L'étudiant qui suit plusieurs cours retrouve donc des lieux, des personnes et des chiffres qu'il connaît déjà.\n",
"Ce document présente chaque organisation en entier, puis indique dans quel cours et dans quel chapitre elle apparaît et ce que l'on y apprend.\n",
"> **Tout est fictif.** Les organisations, les personnes, les faits, les dates et les montants de ces cas ont été inventés à des fins pédagogiques. Ils s'inspirent de situations que l'on rencontre réellement dans le métier, mais toute ressemblance avec des personnes, des faits ou des entreprises réels serait purement fortuite.\n",
"> Les normes, les méthodes et les textes de loi cités dans les cours sont exacts. Les institutions réelles (ANTIC, COBAC, Chambre des comptes, Contrôle Supérieur de l'État) n'y apparaissent que dans leur rôle légal.\n",
"## Comment lire une fiche\n",
"Chaque fiche suit le même plan : une fiche d'identité, les personnes, ce qui arrive à l'organisation, puis un tableau par cours. Le paragraphe « Contexte » dit ce que le cas sert à enseigner dans ce cours. Le tableau donne les chapitres et la question que le chapitre pose au cas, quand il en pose une.\n",
"Aucune fiche ne donne la solution d'un exercice ou d'un laboratoire.\n",
"## Les organisations\n","| Organisation | Nature | En une phrase | Cours |\n|---|---|---|---|"]
for o in ORGS: L.append(f"| [**{o['nom']}**](organisations/{o['cle']}.md) | {o['nature']}{', '+o['lieu'] if o['lieu'] else ''} | {o['resume']} | {', '.join(s for s in ORDRE if s in PRES[o['cle']])} |")
L+=["\n## Les cabinets et les experts\n","| Cabinet | Nature | En une phrase | Cours |\n|---|---|---|---|"]
for o in CABINETS: L.append(f"| [**{o['nom']}**](organisations/{o['cle']}.md) | {o['nature']}{', '+o['lieu'] if o['lieu'] else ''} | {o['resume']} | {', '.join(s for s in ORDRE if s in PRES[o['cle']])} |")
L+=["\n## Les autres pages\n","- [Prestataires, clients et partenaires](prestataires.md) : quinze organisations qui gravitent autour des cas principaux.","- [Les affaires d'investigation numérique](affaires-investigation.md) : les affaires des cours IIN et INA.\n",
"## Qui apparaît où\n","Le chiffre est le nombre de chapitres du cours où l'organisation apparaît.\n",
"| Organisation | "+' | '.join(ORDRE)+" |\n|---|"+'---|'*len(ORDRE)]
for o in TOUS: L.append(f"| {o['nom']} | "+' | '.join(str(len(PRES[o['cle']][s][0])) if s in PRES[o['cle']] else '' for s in ORDRE)+" |")
L+=["\n## Par cours\n","| Cours | UE | Fil rouge | Autres cas |\n|---|---|---|---|"]
for s in ORDRE:
    sc=sorted([(len(PRES[o['cle']][s][0]),sum(r[2] for r in PRES[o['cle']][s][0]),o['nom']) for o in ORGS if s in PRES[o['cle']]],key=lambda x:(-x[1]))
    fil=[x[2] for x in sc[:1]] ; aut=[x[2] for x in sc[1:]]
    cab=[o['nom'] for o in CABINETS if s in PRES[o['cle']]]
    if s in('IIN','INA'): fil=["[Affaires d'investigation](affaires-investigation.md)"]; aut=[x[2] for x in sc]
    L.append(f"| {lien(s)} · {COURS[s][0]} | {COURS[s][1]} | {', '.join(fil)} | {', '.join(aut+cab)} |")
L+=["\n## Les opérations\n","Dans les livres, chaque épisode d'un cas porte un nom d'opération, souvent celui d'un cours d'eau ou d'une ville. Ce tableau les rattache à leur organisation.\n","| Opération | Organisation | Objet | Cours |\n|---|---|---|---|"]
for a,b,c,d in OPERATIONS: L.append(f"| {a} | {b} | {c} | {d} |")
L+=["\n## Un nom, une seule chose\n",
"Chaque nom d'organisation, d'opération et de projet ne désigne qu'une seule chose dans tout le cursus. Quelques noms de famille courants sont encore portés par des personnes différentes : KAMGA, MBARGA, ATANGANA, NDONGO, BELLO. La fiche de chaque organisation donne les siens.\n",
"---\n","[← Tous les cours de MaletYon](../README.md)"]
open(OUT+'/README.md','w',encoding='utf-8').write('\n'.join(L)+'\n')
print('pages',len(TOUS)+3)
