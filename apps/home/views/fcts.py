from serpapi import GoogleSearch 
from  apps.home.models import *

def ApiData(pk): # l'id du chercheur
    r  = Researcher.objects.get(pk = pk)
    params = {
    "engine": "google_scholar_author",
    "author_id": r.get_google_id(),
    "api_key": "5693539bbd7f27e4de0624ca01bc9ad9ecba73199cbc2ce132e589daa15f8e4a",
    "start": 0,
    "num": "100"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    if results == {'error': 'Your searches for the month are exhausted. You can upgrade plans on SerpApi.com website.'}:
        results ={}
    else:    
       articles_num = len(results["articles"])
       flag = 100
       while "articles" in results:
         params = {
           "engine": "google_scholar_author",
           "author_id": r.get_google_id(),
           "api_key": "5693539bbd7f27e4de0624ca01bc9ad9ecba73199cbc2ce132e589daa15f8e4a",
           "start": flag,
           "num": str(flag+100)
         }
         flag += 100
         search = GoogleSearch(params)
         results = search.get_dict()
         if "articles" in results:
            articles_num += len(results["articles"])
         results["articles_num"] = articles_num
    return results 


def Dash_Eta_calc(pk):
   info_etablisment = Etablisment.objects.get(pk = pk)
   divisions = Division.objects.filter(etablisment = pk )
   nbr_division_etablisment = divisions.count()
   nbr_equipe_etablisment=0
   nbr_CitationL = 0
   nbr_cher_etablisment=0
   moy_indice_hL = 0.0
   moy_indice_i10L = 0.0
   for i in divisions:
       inter = Dash_Division_calc(i.id)
       if inter !={}:
          nbr_equipe_etablisment += inter["nbr_equipe_division"]
          nbr_CitationL += inter["nbr_Citation"]       
          moy_indice_hL += inter["moy_indice_h"]
          moy_indice_i10L += inter["moy_indice_i10"]
          nbr_cher_etablisment += inter["nbr_cher_division"]
   if  nbr_division_etablisment == 0:
       moy_indice_hL = 0.0
       moy_indice_i10L = 0.0  
   else: 
       moy_indice_hL=round(moy_indice_hL/nbr_division_etablisment , 2)
       moy_indice_i10L=round(moy_indice_i10L/nbr_division_etablisment,2)    
   context ={'nbr_equipe_etablisment':nbr_equipe_etablisment,
             'nbr_cher_etablisment':nbr_cher_etablisment ,
             'info_etablisment': info_etablisment,
             'nbr_division_etablisment':nbr_division_etablisment,
             'nbr_Citation':nbr_CitationL,
             'moy_indice_h':moy_indice_hL,
             'moy_indice_i10':moy_indice_i10L}
   return context


def Dash_Division_calc(pk):
    info_division = Division.objects.get(pk = pk)
    equipes = Equipe.objects.filter(division = pk)
    nbr_equipe_division = equipes.count()
    nbr_CitationL = 0
    nbr_cher_division=0
    moy_indice_hL = 0.0
    moy_indice_i10L = 0.0
    for i in equipes:
        inter = Dash_Equipe_calc(i.id)
        if inter !={}:
           nbr_CitationL += inter["nbr_Citation"]       
           moy_indice_hL += inter["moy_indice_h"]
           moy_indice_i10L += inter["moy_indice_i10"]
           nbr_cher_division += inter["nbr_cher_equipe"]
    if  nbr_equipe_division == 0:
        moy_indice_hL = 0.0
        moy_indice_i10L = 0.0  
    else: 
        moy_indice_hL=round(moy_indice_hL/nbr_equipe_division , 2)
        moy_indice_i10L=round(moy_indice_i10L/nbr_equipe_division, 2)

        
    
def get_etablisement_id(request):
    return Etablisment.objects.get(chef_etablisement=request.user.pk).id