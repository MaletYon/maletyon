# Mes cas pratiques

Tous mes cours travaillent sur les mêmes organisations fictives. Une entreprise attaquée dans le cours de sécurité est auditée dans le cours d'audit, reconstruite dans le cours de gestion des risques, testée dans le cours de hacking éthique. L'étudiant qui suit plusieurs cours retrouve donc des lieux, des personnes et des chiffres qu'il connaît déjà.

Ce document présente chaque organisation en entier, puis indique dans quel cours et dans quel chapitre elle apparaît et ce que l'on y apprend.

> Les organisations, les personnes, les dates et les montants sont fictifs. Les normes, les méthodes et les textes de loi cités dans les cours sont exacts. Les institutions réelles (ANTIC, COBAC, Chambre des comptes, Contrôle Supérieur de l'État) y gardent leur rôle légal.

## Comment lire une fiche

Chaque fiche suit le même plan : une fiche d'identité, les personnes, ce qui arrive à l'organisation, puis un tableau par cours. Le paragraphe « Contexte » dit ce que le cas sert à enseigner dans ce cours. Le tableau donne les chapitres et la question que le chapitre pose au cas, quand il en pose une.

Aucune fiche ne donne la solution d'un exercice ou d'un laboratoire.

## Les organisations

| Organisation | Nature | En une phrase | Cours |
|---|---|---|---|
| [**LiZbiZ**](organisations/lizbiz.md) | Société anonyme de logistique, Douala | Le cas le plus utilisé du cursus. Une entreprise de logistique dont on audite les stocks, dont on subit le rançongiciel, que l'on reconstruit, que l'on teste et sur laquelle on enquête. | SIF, ASI, ARGC, HE2, ACSI, SNSD, NRAC, SAFI, FORN |
| [**BANQUE SANAGA**](organisations/banque-sanaga.md) | Établissement de crédit, Douala | Une banque de trente-huit agences sous le regard de la COBAC. Elle rate une bascule informatique en mars 2026, puis subit un rançongiciel dans ses agences en septembre 2026 alors qu'elle est certifiée. | SIF, ASI, ARGC, HE2, GCI, ACSI, SNSD, NRAC, SAFI |
| [**ANPP**](organisations/anpp.md) | Établissement public, Yaoundé | Une agence publique de paiement. On y audite les paiements et la conformité, on y gouverne un portefeuille de projets, on y teste un portail, on y rédige un schéma directeur. | SIF, ASI, ARGC, HE2, GCI, ACSI, SNSD, NRAC |
| [**NYANGA CRÉDIT**](organisations/nyanga-credit.md) | Établissement de microfinance de deuxième catégorie, Bafoussam | Une microfinance victime d'une intrusion en mars 2025. Le cours FAV conduit l'enquête. Le cours APDC audite, un an plus tard, ce que l'établissement fait des données de ses clients. | FAV, APDC |
| [**NOUN PAY**](organisations/noun-pay.md) | Société de technologie financière, Bafoussam | Une jeune entreprise de paiement mobile dont tout le système est hébergé à l'étranger et qui note ses clients avec un modèle automatique. | GCI, APDC |
| [**CENTRE MÉDICAL MBOLO**](organisations/centre-medical-mbolo.md) | Établissement de santé privé, Bertoua | Un établissement de 120 lits qui traite des données de santé. Il lance une téléconsultation et découvre que le dossier d'une patiente a été consulté sans raison. | APDC |
| [**KRIBILOG SA**](organisations/kribilog.md) | Opérateur logistique portuaire, Kribi et Douala | Un opérateur portuaire de 1 200 salariés qui dépend d'un infogérant pour son suivi des conteneurs. | GCI |
| [**SOLITRANS LOGISTIQUE**](organisations/solitrans-logistique.md) | Transitaire et logisticien du port | Le second cas du cours FAV. Il sert à la gestion des vulnérabilités, sans attaque. | FAV |
| [**MINÉQUIR**](organisations/minequir.md) | Ministère imaginaire de l'Équipement rural, Yaoundé | Un ministère imaginaire où une facture est payée deux fois par l'application de dépense. | CASI |
| [**CAPNO**](organisations/capno.md) | Caisse publique de prévoyance, Garoua | Une caisse publique dont le fichier de paie contient des agents qui n'existent pas. | CASI |
| [**Recette des finances de Bafoussam**](organisations/recette-bafoussam.md) | Service public (dossier fictif), Bafoussam | Un petit service de trois agents qui reçoit une application de dématérialisation sans que personne n'ait vérifié les sauvegardes. | SNSD, CASI |
| [**Mairie d'Eséka**](organisations/mairie-eseka.md) | Commune (dossier fictif), Eséka, Nyong-et-Kéllé | Une mairie qui, après un incident, bâtit un système de management de la sécurité de l'information et le conduit jusqu'à la certification. | SGSI |

## Les cabinets et les experts

| Cabinet | Nature | En une phrase | Cours |
|---|---|---|---|
| [**AUDIX CONSEIL**](organisations/audix-conseil.md) | Cabinet d'audit et de conseil | Le cabinet qui conduit les missions d'audit des cours ASI et ACSI, puis la mission de schéma directeur du cours SNSD. | SIF, ASI, ARGC, ACSI, SNSD, NRAC |
| [**NYONG SÉCURITÉ**](organisations/nyong-securite.md) | Cabinet de sécurité, de réponse à incident et d'expertise | Le cabinet technique du cursus. Il assiste LiZbiZ pendant l'incident, expertise les supports saisis et conduit le test d'intrusion. | HE2, SAFI, FORN |
| [**KORO AUDIT & CONFORMITÉ**](organisations/koro-audit.md) | Cabinet d'audit de conformité, Yaoundé | Le cabinet qui audite la protection des données chez NYANGA CRÉDIT, au CENTRE MÉDICAL MBOLO et chez NOUN PAY. | APDC |
| [**SANKOFA EXPERTISE**](organisations/sankofa-expertise.md) | Cabinet de réponse à incident, Yaoundé | Le cabinet mandaté par NYANGA CRÉDIT le jour de l'intrusion. | FAV |

## Les autres pages

- [Prestataires, clients et partenaires](prestataires.md) : quinze organisations qui gravitent autour des cas principaux.
- [Les affaires d'investigation numérique](affaires-investigation.md) : les affaires des cours IIN et INA.

## Qui apparaît où

Le chiffre est le nombre de chapitres du cours où l'organisation apparaît.

| Organisation | SIF | ASI | ARGC | IIN | INA | HE2 | GCI | ACSI | SNSD | FAV | NRAC | APDC | CASI | SAFI | FORN | SGSI |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LiZbiZ | 27 | 32 | 27 |  |  | 26 |  | 23 | 10 |  | 17 |  |  | 19 | 21 |  |
| BANQUE SANAGA | 17 | 25 | 13 |  |  | 5 | 20 | 15 | 11 |  | 17 |  |  | 2 |  |  |
| ANPP | 10 | 18 | 1 |  |  | 6 | 17 | 12 | 19 |  | 8 |  |  |  |  |  |
| NYANGA CRÉDIT |  |  |  |  |  |  |  |  |  | 17 |  | 19 |  |  |  |  |
| NOUN PAY |  |  |  |  |  |  | 12 |  |  |  |  | 15 |  |  |  |  |
| CENTRE MÉDICAL MBOLO |  |  |  |  |  |  |  |  |  |  |  | 14 |  |  |  |  |
| KRIBILOG SA |  |  |  |  |  |  | 17 |  |  |  |  |  |  |  |  |  |
| SOLITRANS LOGISTIQUE |  |  |  |  |  |  |  |  |  | 8 |  |  |  |  |  |  |
| MINÉQUIR |  |  |  |  |  |  |  |  |  |  |  |  | 13 |  |  |  |
| CAPNO |  |  |  |  |  |  |  |  |  |  |  |  | 10 |  |  |  |
| Recette des finances de Bafoussam |  |  |  |  |  |  |  |  | 5 |  |  |  | 8 |  |  |  |
| Mairie d'Eséka |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 21 |
| AUDIX CONSEIL | 1 | 26 | 1 |  |  |  |  | 20 | 2 |  | 5 |  |  |  |  |  |
| NYONG SÉCURITÉ |  |  |  |  |  | 8 |  |  |  |  |  |  |  | 6 | 5 |  |
| KORO AUDIT & CONFORMITÉ |  |  |  |  |  |  |  |  |  |  |  | 8 |  |  |  |  |
| SANKOFA EXPERTISE |  |  |  |  |  |  |  |  |  | 6 |  |  |  |  |  |  |

## Par cours

| Cours | UE | Fil rouge | Autres cas |
|---|---|---|---|
| [SIF](https://github.com/maletyon/cours-sif) · Sécurité informatique | SEC3266 | LiZbiZ | ANPP, BANQUE SANAGA, AUDIX CONSEIL |
| [ASI](https://github.com/maletyon/cours-asi) · Audit des systèmes d'information | INF3226 | LiZbiZ | BANQUE SANAGA, ANPP, AUDIX CONSEIL |
| [ARGC](https://github.com/maletyon/cours-argc) · Analyse des risques et gestion de crise | GES4062 | LiZbiZ | BANQUE SANAGA, ANPP, AUDIX CONSEIL |
| [IIN](https://github.com/maletyon/cours-iin) · Introduction à l'investigation numérique | SEC4031 | [Affaires d'investigation](affaires-investigation.md) |  |
| [INA](https://github.com/maletyon/cours-ina) · Investigation numérique avancée | SEC4052 | [Affaires d'investigation](affaires-investigation.md) |  |
| [HE2](https://github.com/maletyon/cours-he2) · Hacking éthique II | SEC4062 | LiZbiZ | BANQUE SANAGA, ANPP, NYONG SÉCURITÉ |
| [GCI](https://github.com/maletyon/cours-gci) · IT governance, COBIT et ITIL | MSN-2S3-MSI03 | BANQUE SANAGA | KRIBILOG SA, ANPP, NOUN PAY |
| [ACSI](https://github.com/maletyon/cours-acsi) · Audit et contrôle interne des SI | MSN-2S3-MSI05 | LiZbiZ | BANQUE SANAGA, ANPP, AUDIX CONSEIL |
| [SNSD](https://github.com/maletyon/cours-snsd) · Stratégie numérique et schéma directeur SI | MSN-2S4-MSI01 | ANPP | LiZbiZ, BANQUE SANAGA, Recette des finances de Bafoussam, AUDIX CONSEIL |
| [FAV](https://github.com/maletyon/cours-fav) · Forensics et analyse de vulnérabilités | MSN-2S3-SEC07 | NYANGA CRÉDIT | SOLITRANS LOGISTIQUE, SANKOFA EXPERTISE |
| [NRAC](https://github.com/maletyon/cours-nrac) · Normes, gestion des risques et audit de cybersécurité | MSN-2S3-SEC08 | BANQUE SANAGA | LiZbiZ, ANPP, AUDIX CONSEIL |
| [APDC](https://github.com/maletyon/cours-apdc) · Audit de protection des données et conformité | MSN-2S4-SEC02 | NYANGA CRÉDIT | NOUN PAY, CENTRE MÉDICAL MBOLO, KORO AUDIT & CONFORMITÉ |
| [CASI](https://github.com/maletyon/cours-casi) · Contrôle et audit des systèmes d'information | CAS3401 | MINÉQUIR | Recette des finances de Bafoussam, CAPNO |
| [SAFI](https://github.com/maletyon/cours-safi) · Supervision, analyse forensique et gestion des incidents | SIS589 | LiZbiZ | BANQUE SANAGA, NYONG SÉCURITÉ |
| [FORN](https://github.com/maletyon/cours-forn) · Forensique numérique | LPI342 | LiZbiZ | NYONG SÉCURITÉ |
| [SGSI](https://github.com/maletyon/cours-sgsi) · Systèmes de gestion de la sécurité informatique | SIS498 | Mairie d'Eséka |  |

## Les opérations

Dans les livres, chaque épisode d'un cas porte un nom d'opération, souvent celui d'un cours d'eau ou d'une ville. Ce tableau les rattache à leur organisation.

| Opération | Organisation | Objet | Cours |
|---|---|---|---|
| GAROUA | LiZbiZ | Le rançongiciel de la nuit du 5 au 6 mars 2026 | SIF, ARGC, HE2 |
| LIZBIZ | LiZbiZ | Les missions d'audit, puis le programme de gestion des risques | ASI, ACSI, ARGC, SIF |
| LOGONE | LiZbiZ | Le test d'intrusion d'octobre 2026 (HE2). Le cours SAFI donne ce nom à la journée du 6 mars | HE2, SAFI |
| BÉNOUÉ, FARO, MAYO | LiZbiZ | Les trois temps du cours : supervision, analyse forensique, réponse | SAFI |
| TSANAGA | LiZbiZ | L'enquête sur le fichier des clients | FORN |
| MOUNGO | LiZbiZ | L'inondation de l'entrepôt de Bonabéri | ARGC |
| SANAGA | BANQUE SANAGA | La bascule manquée du projet HORIZON | GCI, ASI, ACSI |
| WOURI | BANQUE SANAGA | La continuité d'activité et la sensibilisation | ARGC, SIF, SNSD |
| MBAM | BANQUE SANAGA | L'exercice d'équipe rouge | HE2, SAFI |
| MEFOU | ANPP | La gouvernance, l'audit et le test du portail | GCI, ASI, ACSI, SIF, HE2 |
| KRIBI | KRIBILOG SA | La gestion des services | GCI |
| NOUN | NOUN PAY | La gouvernance d'une petite structure | GCI |
| NYANGA | NYANGA CRÉDIT | L'enquête sur l'intrusion du 14 mars 2025 | FAV |
| SOLITRANS | SOLITRANS LOGISTIQUE | La gestion des vulnérabilités | FAV |
| NYONG, KELLÉ, MAKAK, MATOMB | Mairie d'Eséka | Les quatre phases du système de management | SGSI |

## Homonymes à connaître

- **WOURI** désigne la continuité de la BANQUE SANAGA dans les cours ARGC, SIF et SNSD. Dans les cours IIN et INA, c'est une affaire de fraude au faux fournisseur.
- **SANAGA** désigne la banque partout, sauf dans un cas intégrateur du cours INA, où c'est le nom d'une opération sans rapport avec elle.
- **LOGONE** désigne le test d'intrusion d'octobre 2026 dans le cours HE2. Le cours SAFI donne ce nom à la journée du 6 mars 2026.
- **e-RECETTES** est l'application de la recette des finances de Bafoussam dans le cours CASI. Le cours SNSD donne ce nom à un projet de l'ANPP.
- Plusieurs personnes portent le même nom de famille sans être la même personne : KAMGA, MBARGA, NKENG, ATANGANA, NDONGO, BELLO. La fiche de chaque organisation donne les siens.

---

[← Tous les cours de MaletYon](../README.md)
