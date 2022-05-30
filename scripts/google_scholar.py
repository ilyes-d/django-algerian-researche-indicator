from serpapi import GoogleSearch


def get_gs_accounts(r):
    gs_accounts = []
    enum = {"name": "", "account": ""}
    for item in r:
        params = {
            "engine": "google_scholar_profiles",
            "mauthors": item,
            "api_key": "bfdde7462931844d6003e1d183494fad96f1011bdd6d192179f5bae85d0e16c1"
        }
        search = GoogleSearch(params)
        results = search.get_dict()
        if not "error" in results:
            account = results['profiles'][0]['link']
            enum["name"] = item
            enum["account"] = account
            gs_accounts.append(enum.copy())
    return gs_accounts

# r = ["ALIANE Hassina", "ALIRADI Rachid", "ALIOUALI Nadia", "AMRANE Abdessalam", "BADACHE Nadjib", "BERROUK Saïd", "BENMEZIANE Souad", "BESSAI Fatma", "BABAKHOUYA Abdelaziz", "BAL Kamel", "BAGAA Miloud", "BELAZZOUGHI Djamel", "BELHOUL Yacine", "BENKHELIFA Imen", "BENNA amel", "BENDJOUD Ahcène", "BOUABID Mohamed", "BOUCHAMA Nadir", "BOUDER Hadjira", "BOUDINA Abdelmadjid", "BOULKRINAT Nour El Houda", "BOULKABOUL Sahar", "BOUMELLIL Lamia-Sabéha", "BOURAI Fouzia", "BEGGAR Hassina", "BOUALOUACHE Abdelouhab", "BOUCENNA Fatah", "BOUFNISSA Amel", "BOUGHACHA Rim", "CHALABI Lydia", "DAHMANE Madjid", "DJENOURI Djamel", "DELLAL Badiaa", "DOUDOU Messaoud",
#      "DEBAH Adel", "DJEDJIG Nabil", "DJELLIOUT Toufik", "EL-MAOUHAB aouaouche", "HAMANI chouaib", "HAMOUCHE Lamia", "HARIK Hakim", "HADJAR SamIr", "HADJEDJ Zineb", "KAFI Mohamed amine", "KHIDER Hadjer", "KHELLADI Lyes", "KHIAT Abdelhamid", "KICHOU Saida", "KOUICI Salima", "KHEDIMI Amina", "LASLA Nouredine", "LADOUR Hassina", "MEZIANE Abdelkrim", "MAREDJ Azzeddine", "MELLAH Hakima", "MEDJIEK Faiza", "MEKHZOUMI Dalila", "MOHAND OUSSAÏD linda", "NOUALI Nadia", "NOUALI Omar", "NEKRI Mounira", "OUADJAOUT abderaouf", "SADALLAH Madjid", "SEBA Abderazak", "SAIDI Ahmed", "TANDJAOUI Djamel", "YAHIAOUI Said", "YALAOUI Bilal", "ZEGHACHE Lynda", "ZEGHILET Houda", ]


r = ["Abdi Radia", "Adour Rafik", "Aliane Hassina", "Ali ouali Nadia", "Bennoui Wafa", "Bouder Hadjira", "Boughacha Rim", "Bourai Fouzia", "Chaa Messaoud",
     "Chalabi Lydia", "Dahmani Samia", "Djelliout Toufik", "Khellouf Hassina", "Loukem Med El Hadi", "Mekhzoumi Dalila", "Merazka Mustapha", "Nouri Leila", "Zidani Samira"]
ac = get_gs_accounts(r)
print(ac)
