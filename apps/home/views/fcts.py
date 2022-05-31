from pickle import NONE
from traceback import print_tb
from serpapi import GoogleSearch 
from  apps.home.models import *
from datetime import datetime, timezone


def serpapi_author(researcher_id):
    params = {
        "engine": "google_scholar_author",
        "author_id": researcher_id,
        "api_key": "bfdde7462931844d6003e1d183494fad96f1011bdd6d192179f5bae85d0e16c1"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    print(results )
    print(researcher_id)
    return results

def check_gs_id(gs_id):
    params = {
        "engine": "google_scholar_author",
        "author_id": gs_id,
        "api_key": "016c19a111a3df750b7a37250aedf532683ef08faa73e2ab7f4aba7f2f2746be"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    if "author" in results:
        return True
    return False

def get_gs_id(account):
    return account.partition("user=")[2][:12]

def ApiData(pk): # l'id du chercheur
    r  = Researcher.objects.get(pk = pk)
    params = {
    "engine": "google_scholar_author",
    "author_id": r.get_google_id(),
    "api_key": "05840cb02e8ba6f67538df2d4c51c859c362279184fdbcb7e66f308ad8115a21",
    "start": 0,
    "num": "100"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    print(results)
    if checkKey(results,'error') :
        return {}
    else:    
       articles_num = len(results["articles"])
       flag = 100
       while "articles" in results:
         params = {
           "engine": "google_scholar_author",
           "author_id": r.get_google_id(),
           "api_key": "05840cb02e8ba6f67538df2d4c51c859c362279184fdbcb7e66f308ad8115a21",
           "start": flag,
           "num": str(flag+100)
         }
         flag += 100
         search = GoogleSearch(params)
         results = search.get_dict()
         if "articles" in results:
            articles_num += len(results["articles"])
         results["articles_num"] = articles_num
         print(r.date_joined)
         results["date_joined"] = r.date_joined
         print(results)
    if checkKey(results,'error') :
        results ={}    
    return results 


def Dash_Eta_calc(pk):
   info_etablisment = Etablisment.objects.get(pk = pk)
   divisions = Division.objects.filter(etablisment = pk )
   nbr_division_etablisment = divisions.count()
   nbr_equipe_etablisment=0
   nbr_CitationL = 0
   nbr_cher_etablisment=0
   moy_indice_hL = 200
   moy_indice_i10L = 0.0
   nbr_chercheur_24=0
   for i in divisions:
       inter = Dash_Division_calc(i.id)
       if inter !={} and inter !=None :
          nbr_equipe_etablisment += inter["nbr_equipe_division"]
          nbr_CitationL += inter["nbr_Citation"]       
          moy_indice_hL += inter["moy_indice_h"]
          moy_indice_i10L += inter["moy_indice_i10"]
          nbr_cher_etablisment += inter["nbr_cher_division"]
          nbr_chercheur_24 += inter["nbr_chercheur_24"]
        
   if  nbr_division_etablisment == 0:
       moy_indice_hL = 0.0
       moy_indice_i10L = 0.0  
       nbr_chercheur_24 =0
   else: 
       moy_indice_hL=round(moy_indice_hL/nbr_division_etablisment , 2)
       moy_indice_i10L=round(moy_indice_i10L/nbr_division_etablisment,2)    
       nbr_chercheur_24 = round((nbr_chercheur_24 * 100)/nbr_cher_etablisment ,2)   
   context ={'nbr_equipe_etablisment':nbr_equipe_etablisment,
             'nbr_cher_etablisment':nbr_cher_etablisment ,
             'info_etablisment': info_etablisment,
             'nbr_division_etablisment':nbr_division_etablisment,
             'nbr_Citation':nbr_CitationL,
             'moy_indice_h':moy_indice_hL,
             'moy_indice_i10':moy_indice_i10L,
             'nbr_chercheur_24':nbr_chercheur_24}
   return context


def Dash_Division_calc(pk):
    info_division = Division.objects.get(pk = pk)
    equipes = Equipe.objects.filter(division = pk)
    nbr_equipe_division = equipes.count()
    print(nbr_equipe_division)
    nbr_CitationL = 0
    nbr_cher_division=0
    moy_indice_hL = 0.0
    moy_indice_i10L = 0.0
    nbr_chercheur_24 = 0
    nbr_chercheur_24_final =0 
    for i in equipes:
        inter = Dash_Equipe_calc(i.id)
        if inter !={} and inter !=None :
           nbr_CitationL += inter["nbr_Citation"]       
           moy_indice_hL += inter["moy_indice_h"]
           moy_indice_i10L += inter["moy_indice_i10"]
           nbr_cher_division += inter["nbr_cher_equipe"]
           nbr_chercheur_24 += inter["nbr_chercheur_24"]
    if  nbr_equipe_division == 0:
        moy_indice_hL = 0.0
        moy_indice_i10L = 0.0
    else: 
        moy_indice_hL=round(moy_indice_hL/nbr_equipe_division , 2)
        moy_indice_i10L=round(moy_indice_i10L/nbr_equipe_division, 2)
    if nbr_cher_division != 0:
        nbr_chercheur_24_final =(nbr_chercheur_24 *100)/nbr_cher_division    
     
    context ={'nbr_equipe_division':nbr_equipe_division,
               'nbr_cher_division':nbr_cher_division ,
               'nbr_chercheur_24':nbr_chercheur_24,
               'nbr_chercheur_24_final':nbr_chercheur_24_final,
               'info_division': info_division,
               'nbr_Citation':nbr_CitationL,
               'moy_indice_h':moy_indice_hL,
               'moy_indice_i10':moy_indice_i10L}
    print(nbr_chercheur_24)
    return context
 

def Dash_Equipe_calc(pk):# on fait sous form de fonction pour utulistaion direct dans les autre dash board
    
    info_equipe = Equipe.objects.get(pk = pk)
    researchers = Researcher.objects.filter(equipe_researchers = pk) # recupere les chercheur des equipe
    nbr_cher_equipe = researchers.count()
    nbr_Citation = 0
    moy_indice_h = 0.0
    moy_indice_i10 = 0.0
    nbr_chercheur_24 =0 
    for i in researchers:
        inter = ApiData(i.id)
        if inter !={} and inter !=None  :
           print(inter)
           nbr_Citation += inter["cited_by"]["table"][0]["citations"]["all"]
           moy_indice_h += inter["cited_by"]["table"][1]["h_index"]["all"]  
           moy_indice_i10 += inter["cited_by"]["table"][2]["i10_index"]["all"]
           now = datetime.now(timezone.utc)
           if len(str( now - inter["date_joined"] )) < 16:
               nbr_chercheur_24 +=1
    if nbr_cher_equipe == 0:
         moy_indice_h = 0.0
         moy_indice_i10 = 0.0  
    else:  
       moy_indice_h = moy_indice_h/nbr_cher_equipe
       moy_indice_i10 = moy_indice_i10/nbr_cher_equipe
    if nbr_cher_equipe != 0:
        nbr_chercheur_24_final =(nbr_chercheur_24 *100)/nbr_cher_equipe
           
    print(nbr_chercheur_24)  
    context ={'nbr_cher_equipe':nbr_cher_equipe,
              'nbr_chercheur_24':nbr_chercheur_24 ,
              'nbr_chercheur_24_final':nbr_chercheur_24_final ,
              'info_equipe': info_equipe,
              'nbr_Citation':nbr_Citation,
              'moy_indice_h':moy_indice_h,
              'moy_indice_i10':moy_indice_i10}
    return context
    
        
    
def get_etablisement_id(request):
    return Etablisment.objects.get(chef_etablisement=request.user.pk).id

def get_division_id(request):
    return Division.objects.get(chef_div=request.user.pk).id

def get_equipe_id(request):
    return Equipe.objects.get(chef_equipe=request.user.pk).id



def user_role(request):
    if request.user.is_superuser :
        return "organisation"
    if Etablisment.objects.filter(chef_etablisement__id=request.user.id):
        return "etablisement"
    if Division.objects.filter(chef_div__id=request.user.id):
        return "division"
    if Equipe.objects.filter(chef_equipe__id=request.user.id):
        return "equipe"
    return "membre"


def checkKey(dict, key): 
    if key in dict.keys():
        return True
    return False
  
def EquipeList_Eta(pk):
    inter = Division.objects.filter(etablisment = pk)
    researchers = Equipe.objects.none()
    i =[]
    for i1 in inter:
       researchers = Equipe.objects.filter(division = i1.id)
       i +=researchers
    return i