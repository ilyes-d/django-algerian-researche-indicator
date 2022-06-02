# Les Etablisement

CERIST
chef etablisement email="badache@mail.cerist.dz",password= "badache123"
Researcher.objects.create_user(email="badache@mail.cerist.dz",password= "badache123",last_name="BADACHE",first_name="Nadjib", grade="DR",google_scholar_account= "https://scholar.google.com/citations?hl=en&user=P77h8G8AAAAJ")

Les Division

## DSISM chef Division rachid aliradi

password = aliradi123 email = "raliradi@mail.cerist.dz"
"last_name": "",
    "first_name": "",
    "grade": "A.R",
    "division": "DSISM",
    "google_scholar_account": 
Equipe Systèmes d'information et image en Santé S2IS - (chef d'équipe) Abdelkrim MEZIANE
Equipe Systèmes d'information et image en Santé S2IS - (chef d'équipe) Abdelkrim MEZIANE
    "email": ,
Researcher.objects.create_user(email="raliradi@mail.cerist.dz",password="rachid123", last_name ="ALIRADI" ,first_name="Rachid", google_scholar_account="https://scholar.google.com/citations?hl=en&user=vLBwNvwAAAAJ")
Researcher.objects.create_user(email="meziane@gmail.com",password="abdelkrim123", last_name ="MEZIANE" ,first_name="Abdelkrim", google_scholar_account="https://scholar.google.com/citations?hl=en&user=x4OzPQcAAAAJ")
Researcher.objects.create_user(email="aouaa@gmail.com",password="noureddine123", last_name ="AOUAA" ,first_name="Noureddine", google_scholar_account="https://scholar.google.com/citations?hl=en&user=LgCh4kAAAAAJ")
Researcher.objects.create_user(email="hadjadj@gmail.com",password="zineb123", last_name ="HADJADJ" ,first_name="Zineb", google_scholar_account="https://scholar.google.com/citations?hl=en&user=o5rk7VAAAAAJ")
Researcher.objects.create_user(email="setitra@gmail.com",password="insaf123", last_name ="SETITRA" ,first_name="Insaf", google_scholar_account="https://scholar.google.com/citations?hl=en&user=FlJ2v-sAAAAJ")

Researcher.objects.create_user(email="nboulkrinat@mail.cerist.dz",password="nourelhouda123", last_name ="boulkrinat" ,first_name="Nour el houda", google_scholar_account="https://scholar.google.com/citations?hl=ar&user=pwfr0DgAAAAJ")

### Interaction et routage dans les systèmes d’information

Chef Mellah hakima email="hmellah@mail.cerist.dz"
password="hakima123"
Researcher.objects.create_user(email="hmellah@mail.cerist.dz",password="hakima123", last_name ="mellah" ,first_name="hakima", google_scholar_account="https://scholar.google.com/citations?user=WEiBJsMAAAAJ&hl=fr&oi=ao")

## Division Recherche et Développement en Sciences de l'Information et Humanités Numériques DRDHN

Chef Division hassina aliane email='haliane@mail.cerist.dz',
Researcher.objects.create_user(email='haliane@mail.cerist.dz',password="hassina123",last_name='ALIANE', first_name='Hassina', grade='M.R.B', google_scholar_account="https://scholar.google.com/citations?hl=en&user=VOkaVCMAAAAJ")

### Traitement Automatique des Langues et Contenus Numériques
Chef Aliane hassina
Les members
Researcher.objects.create_user(email="mchaa@cerist.dz",password="chaa123",last_name = "Chaa", first_name = "Messaoud", google_scholar_account = "https://scholar.google.com/citations?hl=en&user=M64Rs8UAAAAJ", equipe_researchers_id = 1)
Researcher.objects.create_user(email="lchalabi@cerist.dz",password="chalabi123",last_name = "Chalabi", first_name = "Lydia",google_scholar_account = "https://scholar.google.com/citations?hl=en&user=cQzs_JQAAAAJ", equipe_researchers_id = 1)
Researcher.objects.create_user(email="nleila@mail.cerist.dz",password="nouri123",last_name = "Nouri", first_name = "Leila",google_scholar_account = "https://scholar.google.com/citations?hl=en&user=FqKD0NcAAAAJ", equipe_researchers_id = 1)








# Etablisement CDER Dz 
 Directeur : 
  email="a.hadjarab@cder.dz" password = "amar123"
  first_name = "amar" last_name = "hadj-arab" speciality = "Energies Renouvelables"
  grade = "directeur"
  google_scholar_account = "https://scholar.google.com/citations?hl=en&user=UCrtS_oAAAAJ"

## Divisions 
1. Division Energie Solaire Thermique et Thermodynamique Solaire
* chef :
`email ="s.ouali@cder.dz" password = "salima123" ,first_name = "Salima" ,last_name = "Ouali", speciality="Géothermie",google_scholar_account = "https://scholar.google.com/citations?hl=en&user=RRyeMSoAAAAJ"`
2. Division Energie Eolienn
* chef  Ouahiba Guerri
`email="o.guerri@cder.dz", password="ouhiba123", first_name = "Ouahiba" , last_name ="Guerri", google_scholar_account="https://scholar.google.com/citations?hl=en&user=JUOmDDsAAAAJ", speciality = " Wind Energy" `


query all etablisements researcher who arent leads
Researcher.objects.filter(equipe_researchers__division__etablisment__id=1)


# Centre national de Recherche en biotechnologie 
site-web: http://www.crbt.dz/index.php/component/finder/search.html?q=email&Itemid=790
[done]chef Eta : email ='a.azioune@gmail.com' , password ='amar123',grade='DR',first_name = 'Ammar',last_name= 'AZIOUNE' , google_scholar_account='https://scholar.google.com/citations?hl=en&user=y0aXgggAAAAJ'
## Division Biotechnologie et Agriculture
site-web = http://www.crbt.dz/index.php/r-d/divisions-de-recherche/biotechnologie-agriculture.html
chef div :email='',password='boualem123' first_name ='Boualem',last_name='HARFI',google_scholar_account='https://scholar.google.com/citations?hl=en&user=ZpRVFgcAAAAJ',
1. Réponses des plantes aux stress
   * chef : ZAROURI Belkacem MRB google_scholar_account='https://scholar.google.com/citations?hl=en&user=ulaHk78AAAAJ'
   *  	KERROUM Fatima 	MRB equipe_researchers=, google_scholar_account = 'https://scholar.google.com/citations?hl=en&user=PTahZ6AAAAAJ'
        <!-- NADJEM Kamel 	AR 	equipe_researchers=, google_scholar_account = '' -->
        BOUDIAR Ridha 	AR 	equipe_researchers=, google_scholar_account = 'https://scholar.google.com/citations?hl=en&user=BWyMeRgAAAAJ'
2. Facteurs de croissance et développement des plantes
   * chef : BENAHMED Amira MRB https://scholar.google.com/citations?hl=en&user=t4fbYlgAAAAJ
   *  	HARFI Boualem 	Maitre de recherche A 	Membre 'google_scholar_account'='https://scholar.google.com/citations?hl=en&user=ZpRVFgcAAAAJ'
        KARKOUR Larbi 	Attaché de recherche 	Membre 'google_scholar_account'='https://scholar.google.com/citations?hl=en&user=LzqK75cAAAAJ'
        GAAD Djouher 	Maitre de recherche B 	Membre 'google_scholar_account'='https://scholar.google.com/citations?hl=en&user=Qv9-GxgAAAAJ'

3. Bio-contrôle des maladies des plantes et micro-organismes bénéfiques
   * chef : DEBBI Ali AR google_scholar_account = 'https://scholar.google.com/citations?hl=en&user=eZWuw8EAAAAJ'
   *  	FELLAK Ahmed 	Attaché de recherche 	Membre google_scholar_account ='https://scholar.google.com/citations?hl=en&user=KlitBpwAAAAJ'
        <!-- ZERROUMDA Med. El-Fateh 	Attaché de recherche 	Membre -->
4. Production animale 
   * chef: DOUH Mourad https://scholar.google.com/citations?hl=en&user=qHchT0gAAAAJ
   <!-- *  	REBAI Nouari 	Attaché de recherche 	Membre 
        CHACHA Fayçal 	Attaché de recherche 	Membre -->
    AHMED-LALOUI Hamza 	Attaché de recherche 	Membre 'account': 'https://scholar.google.com/citations?hl=en&user=cy-qk5IAAAAJ'
    RAHMANI Abderrahmane 	Attaché de recherche 	Membre 'account': 'https://scholar.google.com/citations?hl=en&user=YzTodV8AAAAJ'
    SMADI Mustapha Adnane 	Attaché de recherche 	Membre 'account': 'https://scholar.google.com/citations?hl=en&user=7N5qqsAAAAAJ'

# Centre national de Recherche en Biotechnologie alger 
[done]chef email='b.halima@gmail.com',password='halima123',first_name='Halima',grade='DR',speciality='AG-Biotech',last_name='Benbouza',google_scholar_account='https://scholar.google.com/citations?hl=en&user=dizpqi8AAAAJ'

# Centre de recherche en technologies industrielles -CRTI-
[done]directreur 
email='r.badji@crti.dz',password='riad123',last_name='BADJI', first_name='Riad',grade='DR',google_scholar_account ='https://scholar.google.com/citations?hl=en&user=NBHg1NYAAAAJ'

# Centre de Recherche Scientifique et Technique en Analyses Physico – Chimique
site-web https://crapc.dz/
[done]chef email='k.bachari@gmail.com',password='bachari123',grade='DR',last_name='BACHARI', first_name='Khaldoun',google_scholar_account='https://scholar.google.com/citations?hl=en&user=rViVHf8AAAAJ'


# Centre de recherche en anthropologie sociale et culturelle
[done]chef email='a.manaa@gmail.com',password='manaa123',grade='DR',last_name='MANAA',first_name='Ammar',google_scholar_account='https://scholar.google.com/citations?hl=en&user=2Wdur60AAAAJ'

# Centre de Recherche Scientifique et Technique sur les Régions Arides
Mohamed KECHEBAR https://scholar.google.com/citations?hl=en&user=N1RAvO8AAAAJ
