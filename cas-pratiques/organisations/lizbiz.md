# LiZbiZ

*Société anonyme de logistique, Douala. Organisation fictive.*

Le cas le plus utilisé du cursus. Une entreprise de logistique dont on audite les stocks, dont on subit le rançongiciel, que l'on reconstruit, que l'on teste et sur laquelle on enquête.

## Fiche d'identité

| | |
|---|---|
| **Activité** | Logistique : entreposage, transport, livraison, suivi des expéditions |
| **Siège** | Douala |
| **Implantation** | Douze agences régionales, environ 150 salariés |
| **Chiffre d'affaires** | Environ 24 milliards de FCFA par an, soit quelque 80 millions par jour ouvré |
| **Informatique** | Quatre centres de données (Douala, Yaoundé, Garoua, Bafoussam), une application intégrée (stocks, expéditions, facturation, paiements), messagerie en nuage |
| **Prestataire** | SAHEL INFOGÉRANCE exploite une partie des centres de données avec un accès distant |
| **Premier client** | PHARMACAM, distributeur de médicaments |
| **Commissaire aux comptes** | NDONGO & ASSOCIÉS |

## Les personnes

| Nom | Rôle |
|---|---|
| M. ETEME | Directeur général |
| M. KOUNOU | Responsable informatique |
| Mme NKENG | Contrôleuse interne |
| Mme MBALLA | Directrice administrative et financière |
| M. NGUELE | Directeur des opérations |
| Mme ABOMO | Chargée de communication |
| M. NANGA | Chef de l'agence de Garoua |
| Mme MOUAFO | Gestionnaire des risques, recrutée après la crise |
| Me TSALA | Avocat de la société |
| M. NDONGO | Ancien employé du site de Garoua, mis en cause dans l'opération TSANAGA |

## Ce qui lui arrive

- **Les stocks et les deux missions d'audit.** Un écart de stock de 186 millions de FCFA, des comptes d'agents partis encore actifs et une réserve du commissaire aux comptes. Une première mission d'audit échoue : quarante-cinq questions posées, aucune réponse défendable. En mai 2026, le comité de direction confie une seconde mission au cabinet AUDIX CONSEIL. Elle établit deux fraudes, dont celle du fournisseur fictif TRANSLOG SERVICES.
- **Nuit du 5 au 6 mars 2026, le rançongiciel (opération GAROUA).** Un technicien du prestataire a livré son mot de passe à une fausse page le 19 février. L'attaquant entre par la passerelle d'accès distant de Garoua, sans second facteur, puis chiffre les serveurs. La rançon demandée est de 85 000 dollars. M. ETEME décide le 8 mars de ne pas payer. La facturation reprend le 16 mars. Le 19 mars, un échantillon de données clients est publié.
- **Printemps 2026, la reconstruction (opération LIZBIZ).** Le conseil décide de recruter un responsable de la sécurité, de créer un comité de sécurité, d'adopter des politiques et de renégocier le contrat du prestataire. Une gestionnaire des risques est recrutée, un registre des risques est tenu, un audit est conduit selon l'ISO 19011.
- **Avril 2026, l'enquête (opération TSANAGA).** L'entreprise découvre qu'un ancien employé de Garoua aurait copié puis revendu le fichier des clients. Le 20 avril, sur réquisition du parquet, un ordinateur portable et une clé USB sont saisis et confiés sous scellé au cabinet NYONG SÉCURITÉ.
- **Octobre 2026, le test d'intrusion (opération LOGONE).** Le 12 octobre, M. ETEME signe la lettre qui autorise NYONG SÉCURITÉ à attaquer le système pour vérifier que les mesures prises depuis mars tiennent.
- **L'inondation (opération MOUNGO).** L'entrepôt de Bonabéri, à Douala, est inondé. Le cas sert à la continuité d'activité et à la définition d'une crise.

## Où la retrouver et pour apprendre quoi

LiZbiZ apparaît dans 9 cours et 202 chapitres. La colonne « Mentions » compte les occurrences du nom dans le chapitre : elle indique si le cas y est central ou seulement cité.

### SIF · Sécurité informatique

*SEC3266, ENSPY. Dépôt [SIF](https://github.com/maletyon/cours-sif).*

**Contexte.** Fil rouge du cours. Le prologue raconte la nuit de Garoua heure par heure, puis chaque chapitre remonte de l'incident vers une notion : propriétés de sécurité, cryptographie, gouvernance, risques, réseaux, identités, continuité.

**Labs.** SIF-LAB-01 « Empreintes et HMAC : retrouver les fichiers modifiés » ; SIF-LAB-02 « Certificats : lire une chaîne, repérer les défauts » ; SIF-LAB-03 « Analyse de risques EBIOS simplifiée » ; SIF-LAB-04 « Classer les actifs et coter les besoins » ; SIF-LAB-08 « Durcissement Linux ».

| Chapitre | Titre | Mentions | Question posée au cas |
|---|---|---|---|
| Prologue | Une nuit à Garoua | 22 |  |
| Chap. 1 | La sécurité de l'information : objets et propriétés | 10 |  |
| Chap. 2 | Menaces, vulnérabilités et attaques | 5 |  |
| Chap. 3 | Cryptographie (1) : symétrique, hachage, intégrité | 4 |  |
| Chap. 4 | Cryptographie (2) : asymétrique, signatures, infrastructures à clés publiques | 4 |  |
| Chap. 5 | Histoire des grandes attaques | 6 | « L'Opération GAROUA était-elle prévisible ? » |
| Chap. 6 | Gouvernance de la sécurité | 11 | « Qui était responsable de la sécurité de LiZbiZ ? » |
| Chap. 7 | Analyser et traiter les risques de sécurité | 12 |  |
| Chap. 8 | Sécurité des actifs et des données | 6 | « Quelles données ont quitté LiZbiZ, et le savait-on ? » |
| Chap. 9 | Le facteur humain | 4 |  |
| Chap. 10 | Normes et référentiels de sécurité | 8 | « Par où LiZbiZ doit-elle commencer ? » |
| Chap. 11 | Le droit de la sécurité au Cameroun et en Afrique | 7 |  |
| Chap. 12 | Éthique et responsabilité | 8 |  |
| Chap. 13 | Modèles formels de sécurité | 7 |  |
| Chap. 14 | Architecture de sécurité | 11 |  |
| Chap. 15 | Sécurité des réseaux (1) : protocoles et attaques | 4 |  |
| Chap. 16 | Sécurité des réseaux (2) : équipements et protocoles sûrs | 5 | « Les pare-feu de LiZbiZ servaient-ils à quelque chose ? » |
| Chap. 17 | Identités et accès | 5 | « Qui pouvait se connecter au système de LiZbiZ ? » |
| Chap. 18 | Sécurité des systèmes | 5 |  |
| Chap. 19 | Sécurité des applications | 2 |  |
| Chap. 20 | Sécurité du nuage et des mobiles | 7 | « La messagerie de LiZbiZ était-elle à l'abri parce qu'elle était dans le nuage ? » |
| Chap. 21 | Évaluer la sécurité | 4 |  |
| Chap. 22 | Opérations de sécurité et incidents | 9 |  |
| Chap. 23 | Continuité et reprise | 8 |  |
| Chap. 24 | Premiers pas en investigation numérique | 4 |  |
| Chap. 25 | IA, objets connectés et post-Quantique | 7 |  |
| Chap. 26 | Mesurer la sécurité | 7 | « LiZbiZ est-elle mieux protégée six mois après ? » |

### ASI · Audit des systèmes d'information

*INF3226, ENSPY. Dépôt [ASI](https://github.com/maletyon/cours-asi).*

**Contexte.** Cas principal. Le cabinet AUDIX CONSEIL y conduit deux cycles d'audit. On y apprend le contrôle interne, la fraude, la planification d'une mission, la cotation OUI, NON, NEK et le suivi des recommandations.

**Labs.** ASI-LAB-01 « Construire la cartographie des risques » ; ASI-LAB-02 « Analyser la matrice des droits » ; ASI-LAB-03 « Coter les documents sollicités, dimensionner les échantillons » ; ASI-LAB-04 « Contrôler une décomposition du domaine D » ; ASI-LAB-05 « Mesurer, situer et comparer les domaines » ; ASI-LAB-07 « Tests substantifs sur les données » ; ASI-LAB-08 « Audit d'infrastructure des quatre centres ».

| Chapitre | Titre | Mentions | Question posée au cas |
|---|---|---|---|
| Prologue | Quarante-Cinq questions et aucune réponse fiable | 15 |  |
| Chap. 1 | Auditer, contrôler, donner une assurance : du métier à l'auditologie | 23 |  |
| Chap. 2 | Grandes défaillances et naissance de l'audit des SI | 11 |  |
| Chap. 3 | Le contrôle interne et ses composantes | 19 |  |
| Chap. 4 | Le risque, notions et mesure | 15 |  |
| Chap. 5 | Gérer les risques des systèmes d'information | 16 |  |
| Chap. 6 | La fraude dans et par les systèmes d'information | 9 |  |
| Chap. 7 | La mission d'audit : principes et cycle | 10 |  |
| Chap. 8 | Préparer et planifier la mission | 12 |  |
| Chap. 9 | Décomposer l'espace d'audit : gabarit canonique et fiche d'assertion | 6 |  |
| Chap. 10 | Collecter la preuve : l'instrument OUI/NON/NEK | 5 |  |
| Chap. 11 | Conclure et rédiger : mesures, quadrant, observation, rapport | 12 |  |
| Chap. 12 | Suivre : recommandations, cycles et maturité | 9 |  |
| Chap. 13 | Les normes professionnelles de l'audit | 7 |  |
| Chap. 14 | Les référentiels de contrôle | 8 |  |
| Chap. 15 | Le cadre juridique camerounais et africain | 10 |  |
| Chap. 16 | Déontologie et profession de l'auditeur | 4 |  |
| Chap. 17 | Auditer la gouvernance et la fonction informatique | 12 | « L'informatique de LiZbiZ est-elle bien gouvernée ? » |
| Chap. 18 | Auditer une application en service | 9 |  |
| Chap. 19 | Auditer les projets informatiques | 1 |  |
| Chap. 20 | Auditer un système de management de la sécurité | 1 |  |
| Chap. 21 | Auditer la sécurité technique de l'infrastructure | 7 |  |
| Chap. 22 | Tests d'intrusion et audit de code | 7 |  |
| Chap. 23 | Auditer la production et la continuité | 3 |  |
| Chap. 24 | Auditer les tiers et le nuage | 4 |  |
| Chap. 25 | Auditer la conformité | 4 |  |
| Chap. 26 | Études de cas intégratrices | 11 |  |
| Chap. 27 | Audit continu, analyse de données et outils | 7 |  |
| Chap. 28 | Auditer l'intelligence artificielle, auditer avec elle | 4 |  |
| Chap. 29 | De l'audit à la preuve judiciaire | 3 |  |
| Chap. 30 | L'auditologie : objet, axiomes et piliers | 9 |  |
| Chap. 31 | Mesurer l'incertitude et la stratégie | 5 |  |

### ARGC · Analyse des risques et gestion de crise

*GES4062, ENSPY. Dépôt [ARGC](https://github.com/maletyon/cours-argc).*

**Contexte.** Le cours reprend la crise de mars du point de vue de la direction : qui décide, avec quelle information, puis le programme de gestion des risques, l'audit, la continuité et la communication de crise. L'opération MOUNGO y ajoute l'inondation de l'entrepôt.

**Labs.** ARGC-LAB-01 « Matrice et registre des risques » ; ARGC-LAB-02 « EBIOS RM : menace des parties prenantes » ; ARGC-LAB-05 « Indicateurs de risque et tableau de bord » ; ARGC-LAB-06 « Échantillonnage et constats d'audit ».

| Chapitre | Titre | Mentions | Question posée au cas |
|---|---|---|---|
| Prologue | le matin du 6 mars | 11 |  |
| Chap. 1 | Risque, incertitude et décision | 9 |  |
| Chap. 2 | Percevoir le risque : biais et culture | 5 |  |
| Chap. 3 | Gouvernance des risques | 10 | « Qui, chez LiZbiZ, répondait du risque du prestataire ? » |
| Chap. 4 | Les cadres de management des risques | 8 | « Quelle méthode adopter pour que les risques de LiZbiZ soient comparables ? » |
| Chap. 5 | Obligations juridiques et responsabilités | 10 | « LiZbiZ avait-elle respecté la loi avant l'attaque ? » |
| Chap. 6 | Identifier les risques | 8 |  |
| Chap. 7 | Estimer : échelles et matrices | 9 |  |
| Chap. 8 | ISO/IEC 27005 et EBIOS Risk Manager | 6 |  |
| Chap. 9 | L'analyse quantitative : FAIR et pertes annuelles | 4 | « Combien le risque de rançongiciel coûtait-il à LiZbiZ chaque année ? » |
| Chap. 10 | Simuler : Monte-Carlo et sensibilité | 4 | « LiZbiZ respecte-t-elle son appétence « neuf ans sur dix » ? » |
| Chap. 11 | Traiter, suivre et rendre compte | 6 |  |
| Chap. 12 | L'audit selon l'ISO 19011 | 8 | « Que fallait-il auditer, et quand, chez LiZbiZ ? » |
| Chap. 13 | Conduire l'audit : preuves, échantillons, constats | 2 |  |
| Chap. 14 | Auditer la gestion des risques et le SMSI | 5 | « Le registre de LiZbiZ dit-il vrai ? » |
| Chap. 15 | Le rapport et le suivi des actions | 1 |  |
| Chap. 16 | Gérer les incidents de sécurité | 5 |  |
| Chap. 17 | L'analyse d'impact sur l'activité | 2 |  |
| Chap. 18 | Stratégies et plans de continuité | 8 | « Comment LiZbiZ a-t-elle livré pendant l'inondation de Bonabéri ? » |
| Chap. 19 | Reprise informatique et résilience | 6 |  |
| Chap. 20 | Exercer et tester les plans | 4 |  |
| Chap. 21 | Qu'est-ce qu'une crise ? | 3 |  |
| Chap. 22 | La cellule de crise | 6 |  |
| Chap. 23 | Décider en situation de crise | 6 |  |
| Chap. 24 | Communiquer en crise | 11 | « Pourquoi la photographie du 6 mars a-t-elle parlé avant LiZbiZ ? » |
| Chap. 25 | Les exercices de crise | 5 | « La cellule de crise de LiZbiZ ferait-elle mieux aujourd'hui qu'en mars ? » |
| Chap. 26 | Retour d'expérience, résilience et mesure | 6 | « LiZbiZ est-elle plus résiliente en octobre qu'en mars, et le sait-elle ? » |

### HE2 · Hacking éthique II

*SEC4062, ENSPY. Dépôt [HE2](https://github.com/maletyon/cours-he2).*

**Contexte.** Sept mois après la crise, l'entreprise commande un test d'intrusion. Le cours suit la mission de la lettre d'autorisation au rapport et au contre-test.

| Chapitre | Titre | Mentions | Question posée au cas |
|---|---|---|---|
| Prologue | la lettre d'autorisation | 17 |  |
| Chap. 1 | Le hacking éthique : définitions, métiers, types de tests | 5 | « De quoi LiZbiZ avait-elle besoin : un balayage, un audit ou un test d'intrusion ? » |
| Chap. 2 | Le cadre juridique camerounais | 4 |  |
| Chap. 3 | Règles d'engagement et éthique de la mission | 2 |  |
| Chap. 4 | Méthodologies et référentiels | 3 |  |
| Chap. 5 | Reconnaissance passive et OSINT | 7 | « Que voyait-on de LiZbiZ depuis Internet, sans rien toucher ? » |
| Chap. 6 | Balayage et énumération | 5 | « Combien de portes ouvertes comptait vraiment LiZbiZ ? » |
| Chap. 7 | Analyser et prioriser les vulnérabilités | 3 |  |
| Chap. 8 | L'exploitation : principes et cadres | 1 |  |
| Chap. 9 | Attaques réseau et authentification | 4 |  |
| Chap. 10 | Active Directory | 5 |  |
| Chap. 11 | Élévation de privilèges | 2 |  |
| Chap. 12 | Post-Exploitation, mouvement latéral, persistance | 6 |  |
| Chap. 13 | Mots de passe : attaques et défenses | 5 | « Combien de mots de passe de LiZbiZ un attaquant retrouverait-il en un jour ? » |
| Chap. 14 | Tester une application web | 4 |  |
| Chap. 15 | Injections et contrôle d'accès | 1 |  |
| Chap. 16 | Interfaces de programmation et applications mobiles | 4 | « L'application mobile de LiZbiZ est-elle plus sûre que son portail web ? » |
| Chap. 17 | Tester le nuage et les conteneurs | 4 |  |
| Chap. 18 | Sans-Fil et objets connectés | 1 |  |
| Chap. 19 | Ingénierie sociale | 3 | « Combien de salariés de LiZbiZ cliquent sur un lien piégé, et qu'en conclure ? » |
| Chap. 20 | Équipe rouge et équipe violette | 2 |  |
| Chap. 21 | Se faire détecter : le point de vue du défenseur | 2 |  |
| Chap. 22 | Le rapport de test d'intrusion | 4 |  |
| Chap. 23 | Le contre-Test | 2 | « Les corrections de LiZbiZ ont-elles vraiment fermé les failles ? » |
| Chap. 24 | La divulgation coordonnée | 4 |  |
| Chap. 26 | Mesurer la sécurité offensive | 4 | « LiZbiZ est-elle « sûre » après le test ? » |

### ACSI · Audit et contrôle interne des SI

*MSN-2S3-MSI05, Chaire UNESCO. Dépôt [ACSI](https://github.com/maletyon/cours-acsi).*

**Contexte.** Cas principal, comme dans ASI, traité au niveau master : écart de stock, séparation des tâches dans l'application intégrée, fraude du fournisseur fictif, puis les mesures de l'auditologie.

**Labs.** ACSI-LAB-01 « Construire la cartographie des risques » ; ACSI-LAB-02 « Analyser la matrice des droits » ; ACSI-LAB-03 « Coter les documents sollicités, dimensionner les échantillons » ; ACSI-LAB-04 « Contrôler une décomposition du domaine D » ; ACSI-LAB-05 « Mesurer, situer et comparer les domaines » ; ACSI-LAB-07 « Tests substantifs sur les données » ; ACSI-LAB-08 « Audit d'infrastructure des quatre centres ».

| Chapitre | Titre | Mentions | Question posée au cas |
|---|---|---|---|
| Prologue | Quarante-Cinq questions et aucune réponse fiable | 8 |  |
| Chap. 1 | Auditer, contrôler, donner une assurance : du métier à l'auditologie | 11 |  |
| Chap. 2 | Le contrôle interne et ses composantes | 10 |  |
| Chap. 3 | Le risque, de la définition à la cartographie | 11 |  |
| Chap. 4 | La fraude dans et par les systèmes d'information | 6 |  |
| Chap. 5 | La mission d'audit : principes et cycle | 7 |  |
| Chap. 6 | Préparer et planifier la mission | 5 |  |
| Chap. 7 | Décomposer l'espace d'audit : gabarit canonique et fiche d'assertion | 5 |  |
| Chap. 8 | Collecter la preuve : l'instrument OUI/NON/NEK | 3 |  |
| Chap. 9 | Conclure : conformité, incertitude et observation | 6 |  |
| Chap. 10 | Les normes professionnelles de l'audit | 6 |  |
| Chap. 11 | Les référentiels de contrôle | 4 |  |
| Chap. 12 | Le cadre juridique camerounais et africain | 7 |  |
| Chap. 13 | Auditer la gouvernance et la fonction informatique | 8 | « L'informatique de LiZbiZ est-elle bien gouvernée ? » |
| Chap. 14 | Auditer une application en service | 7 |  |
| Chap. 15 | Auditer les projets informatiques | 1 |  |
| Chap. 16 | Auditer la sécurité et l'infrastructure | 5 |  |
| Chap. 17 | Auditer la production, la continuité et les tiers | 1 |  |
| Chap. 18 | Études de cas intégratrices | 11 |  |
| Chap. 19 | Audit continu, analyse de données et outils | 6 |  |
| Chap. 20 | Auditer l'intelligence artificielle, auditer avec elle | 3 |  |
| Chap. 21 | L'auditologie : objet, axiomes et piliers | 7 |  |
| Chap. 22 | Mesurer l'incertitude, la stratégie et la trajectoire | 3 |  |

### SNSD · Stratégie numérique et schéma directeur SI

*MSN-2S4-MSI01, Chaire UNESCO. Dépôt [SNSD](https://github.com/maletyon/cours-snsd).*

**Contexte.** Cas d'appui pour la stratégie d'entreprise : les cinq forces, la chaîne de valeur et le coût complet d'un projet y sont appliqués.

**Labs.** SNSD-LAB-01 « Cinq forces et chaîne de valeur » ; SNSD-LAB-07 « Coût complet sur cinq ans ».

| Chapitre | Titre | Mentions | Question posée au cas |
|---|---|---|---|
| Prologue | Le schéma directeur dort dans un tiroir | 1 |  |
| Chap. 1 | Stratégie, système d'information, numérique | 4 |  |
| Chap. 2 | Les théories de la stratégie | 9 |  |
| Chap. 3 | L'alignement et la valeur | 1 |  |
| Chap. 5 | Doctrines et stratégies numériques dans le monde et en Afrique | 1 |  |
| Chap. 7 | Le cadre juridique d'un schéma directeur | 3 |  |
| Chap. 8 | Cadrer et gouverner la démarche | 1 |  |
| Chap. 10 | Fixer la cible | 2 |  |
| Chap. 14 | Risques, sécurité, continuité, conformité | 1 |  |
| Chap. 15 | Données, intelligence artificielle, plateformes, sobriété | 3 |  |

### NRAC · Normes, gestion des risques et audit de cybersécurité

*MSN-2S3-SEC08, Chaire UNESCO. Dépôt [NRAC](https://github.com/maletyon/cours-nrac).*

**Contexte.** Cas secondaire. Il porte l'atelier EBIOS Risk Manager, lancé à la demande du client PHARMACAM, et plusieurs exercices sur les trois lignes de maîtrise et l'audit technique.

**Labs.** NRAC-LAB-02 « EBIOS Risk Manager : cadrage et sources de risque » ; NRAC-LAB-03 « EBIOS Risk Manager : écosystème et scénario opérationnel » ; NRAC-LAB-09 « Audit technique sur exports figés ».

| Chapitre | Titre | Mentions | Question posée au cas |
|---|---|---|---|
| Prologue | Certifiée, et pourtant compromise | 1 |  |
| Chap. 1 | Gouverner la cybersécurité : du contrôle à la GRC | 2 |  |
| Chap. 2 | Le risque cyber : notions, mesure, incertitude | 2 |  |
| Chap. 3 | Gérer les risques : ISO 31000 et ISO/IEC 27005 | 2 |  |
| Chap. 4 | EBIOS Risk Manager | 14 |  |
| Chap. 5 | Quantifier le risque cyber : FAIR | 2 |  |
| Chap. 6 | Conduire un audit de cybersécurité | 2 |  |
| Chap. 7 | Décomposer, coter, conclure | 2 |  |
| Chap. 8 | La famille ISO/IEC 27000 | 4 |  |
| Chap. 9 | Les autres référentiels et leurs correspondances | 4 |  |
| Chap. 10 | Le cadre camerounais et africain, la déontologie | 5 |  |
| Chap. 11 | Mettre en œuvre et auditer un SMSI | 3 |  |
| Chap. 12 | L'audit technique de sécurité | 9 |  |
| Chap. 13 | La GRC en pratique | 1 |  |
| Chap. 14 | Études de cas intégratrices | 7 |  |
| Chap. 15 | Risques émergents et nouveaux objets d'audit | 4 |  |
| Chap. 16 | Mesurer ce que l'on ne sait pas | 5 |  |

### SAFI · Supervision, analyse forensique et gestion des incidents

*SIS589, Université de Garoua. Dépôt [SAFI](https://github.com/maletyon/cours-safi).*

**Contexte.** Fil rouge du cours. Le matin du 6 mars est relu par la supervision : ce que les journaux contenaient depuis onze jours, puis l'analyse forensique et la réponse à l'incident, avec l'appui du cabinet NYONG SÉCURITÉ.

| Chapitre | Titre | Mentions | Question posée au cas |
|---|---|---|---|
| Prologue | la découverte | 9 |  |
| Chap. 1 | Pourquoi superviser | 3 |  |
| Chap. 2 | L'architecture d'un SOC | 6 | « De quelle équipe LiZbiZ a-t-elle besoin pour voir venir la prochaine attaque ? » |
| Chap. 3 | Gouvernance et indicateurs de la supervision | 3 | « Comment savoir si la supervision de LiZbiZ s'améliore vraiment ? » |
| Chap. 4 | Les journaux | 2 | « Parmi tous les journaux de LiZbiZ, lesquels auraient révélé l'intrusion ? » |
| Chap. 5 | Le SIEM | 2 |  |
| Chap. 6 | La détection d'intrusion (IDS/IPS) | 3 |  |
| Chap. 7 | Écrire et éprouver une règle de détection | 1 |  |
| Chap. 8 | Normes de la gestion d'incident et de la preuve | 3 | « Quelles normes encadrent ce que LiZbiZ doit faire, du constat à la preuve ? » |
| Chap. 9 | Le cadre juridique | 11 | « Qu'est-ce que la loi impose à LiZbiZ le 6 mars au matin ? » |
| Chap. 10 | L'admissibilité de la preuve numérique | 3 | « La preuve recueillie chez LiZbiZ tiendrait-elle devant un tiers ? » |
| Chap. 11 | Fondements du forensique et chaîne de custody | 1 |  |
| Chap. 13 | Forensique mémoire | 1 |  |
| Chap. 15 | Le cycle de réponse à incident | 3 |  |
| Chap. 16 | Le CSIRT et le CERT | 8 | « Qui décide, qui agit, qui parle pendant l'incident de LiZbiZ ? » |
| Chap. 17 | Le renseignement sur la menace | 3 | « L'attaque de LiZbiZ ressemble-t-elle à d'autres, et qu'en déduire ? » |
| Chap. 18 | Confinement, éradication, rétablissement | 7 | « Comment remettre LiZbiZ en marche sans rouvrir la porte ? » |
| Chap. 19 | Retour d'expérience et amélioration continue | 4 | « Qu'a appris LiZbiZ, et comment éviter que cela se reproduise ? » |
| Chap. 20 | Mesurer la supervision et la réponse | 5 | « LiZbiZ est-elle « prête » pour le prochain incident ? » |

### FORN · Forensique numérique

*LPI342, Université de Garoua. Dépôt [FORN](https://github.com/maletyon/cours-forn).*

**Contexte.** Le cours suit une seule enquête, l'opération TSANAGA, de la saisie des supports à la présentation devant le tribunal.

| Chapitre | Titre | Mentions | Question posée au cas |
|---|---|---|---|
| Prologue | la scène numérique | 10 |  |
| Chap. 1 | Qu'est-ce que la forensique numérique | 3 |  |
| Chap. 2 | La démarche d'enquête | 2 |  |
| Chap. 3 | Éthique, neutralité, impartialité | 3 |  |
| Chap. 4 | Le droit de la preuve numérique | 2 |  |
| Chap. 5 | La chaîne de possession | 1 |  |
| Chap. 6 | Recevabilité et admissibilité | 2 |  |
| Chap. 7 | Identifier et préserver les sources | 2 |  |
| Chap. 8 | Duplication et hachage | 2 |  |
| Chap. 9 | Ordre de volatilité et acquisition à chaud | 2 |  |
| Chap. 10 | Forensique disque et systèmes de fichiers | 3 |  |
| Chap. 11 | Fichiers supprimés, fragments et artefacts | 2 |  |
| Chap. 12 | Forensique mémoire | 4 |  |
| Chap. 13 | Forensique réseau | 5 | « Le fichier clients a-t-il quitté le réseau de LiZbiZ, et vers où ? » |
| Chap. 14 | Forensique mobile | 3 |  |
| Chap. 15 | Forensique du nuage et des applications | 3 |  |
| Chap. 16 | L'anti-Forensique et le chiffrement | 4 |  |
| Chap. 17 | Corrélation et reconstitution chronologique | 3 |  |
| Chap. 18 | Le rapport forensique | 3 |  |
| Chap. 19 | La présentation devant un tribunal | 2 |  |
| Chap. 20 | Mesurer et progresser | 4 | « L'enquête TSANAGA était-elle « bonne » ? » |

---

[← Mes cas pratiques](../README.md)
