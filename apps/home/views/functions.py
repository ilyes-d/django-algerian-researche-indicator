from django.http import Http404
from serpapi import GoogleSearch
from ..models import *
from django.db.models import Q, F
from dotenv import *
from  django.shortcuts import *
from .queries import *
import os
from django.db.models import *

load_dotenv()
api_key = os.getenv("api_key")

def serpapi_author(gs_id):
    params = serp_params(gs_id,0,"pubdate")
    search = GoogleSearch(params)
    results = search.get_dict()
    if "error" in results :
        raise Http404("api kmel")
    return results

def serp_params(gs_id,start,sort):
    return {
        "engine": "google_scholar_author",
        "author_id": gs_id,
        "api_key": api_key,
        "start": start,
        "num": 100,
        "sort": sort
    }


def serpapi_author_v2(gs_id,start):
    params = serp_params(gs_id,start,"pubdate")
    search = GoogleSearch(params)
    results = search.get_dict()
    if "error" in results :
        raise Http404("api kmel")
    return results


def load_reseacher_gs_data(researcher):
    """
    this function load a single researcher data from google scholar using SerpApi.
    The Data is : H-index, i10-index, citations, citation-graph, article-graph.
    """
    gs_id = researcher.get_google_id()
    gs_data = serpapi_author_v2(gs_id,0)
    if "cited_by" in gs_data:
        cited_by = gs_data["cited_by"]
        researcher.citations=  cited_by["table"][0]["citations"]["all"] 
        researcher.h_index = cited_by["table"][1]["h_index"]["all"]
        researcher.i10_index = cited_by["table"][2]["i10_index"]["all"]
        if 'graph' in cited_by:
            researcher.graph_citations =  gs_data["cited_by"]["graph"]
    graph_article = graph_articles(researcher.get_google_id())
    researcher.nbr_pubs = graph_article["nbr_total"]
    researcher.graph_pub = graph_article["publications"]
    researcher.save()
    
def graph_articles(gs_id):
    graph_article = {'publications':{},}
    nbr_total = 0
    start = 0
    researcher = serpapi_author_v2(gs_id,start)
    if not "articles" in researcher : 
        graph_article["no_article_message"] = "There are no articles in this profile"
    else :
        while "articles" in researcher:
            articles = researcher["articles"]
            for article in articles:
                if article["year"]:
                    year = article["year"]
                    value = article["cited_by"]["value"]
                    if year in graph_article["publications"]:
                        graph_article["publications"][year]["nbr_pub"] += 1
                        if value is not None:
                            graph_article["publications"][year]["citations"] += article["cited_by"]["value"]
                    else:
                        graph_article["publications"][year] = {}
                        if value is not None:
                            graph_article["publications"][year]= {"citations" :value}
                        else:
                            graph_article["publications"][year]["citations"] =0
                        graph_article["publications"][year]["nbr_pub"]= 1
                nbr_total +=1 
            if "serpapi_pagination" in researcher:
                start += 100
                researcher = serpapi_author_v2(gs_id,start)
                articles = researcher["articles"]
            else:
                break
    
    graph_article["nbr_total"] = nbr_total
    return graph_article





# Organisation
# Queries
def query_etablisements(qs):
    etablisements_info = {}
    for etablisement in qs:
        etablisements_info[etablisement] = {
            "logo":etablisement.logo,
            "chef_eta": etablisement.chef_etablisement.__str__() , 
            "location":etablisement.location.__str__(),
            "nbr_divisions" : eta_divs(etablisement.id).count() ,
            "nbr_equipes": eta_equipes(etablisement.id).count(),
            "nbr_researchers" : eta_chers(etablisement.id).count(),
        }
    return etablisements_info

def query_all_eta_divs(eta_id):
    div_info ={}
    for div in Division.objects.filter(etablisment=eta_id):
        div_info[div] = {
            "chef_div":div.chef_div.__str__(),
            "etablisement":Etablisment.objects.get(division=div.id).__str__(),
            "nbr_equipes":Equipe.objects.filter(division=div.id).count(),
            "nbr_chers": Researcher.objects.filter(Q(equipe__division=div.id)|Q(equipe_researchers__division=div.id)).count()
        }
    return div_info

def query_divs(qs):
    div_info = {}
    for div in qs:
        div_info[div] = {
            "chef_div":div.chef_div.__str__(),
            "etablisement":Etablisment.objects.get(division=div.id).__str__(),
            "nbr_equipes":Equipe.objects.filter(division=div.id).count(),
            "nbr_chers": Researcher.objects.filter(Q(equipe__division=div.id)|Q(equipe_researchers__division=div.id)).count()
        }
    return div_info

def query_equipes(qs):
    equipe_info = {}
    for equipe in qs:
        equipe_info[equipe] = {
            "nom" : equipe.nom ,
            "chef_equipe" : equipe.chef_equipe.__str__(),
            "etablisement_associe" : Etablisment.objects.get(division__equipe=equipe.id),
            "division_associe" : Division.objects.get(equipe=equipe.id),
            "nbr_chers":Researcher.objects.filter(equipe_researchers=equipe.id).count(),
        }
    return equipe_info


def eta_total_citations(eta_id):
    context={'nom':Etablisment.objects.get(id=eta_id).nom}
    chers=eta_chers(eta_id)
    total = 0
    for cher in chers:
        total += cher.citations
    context["citations_total"] = total
    return context 

def all_etas_citations():
    context = []
    etas = Etablisment.objects.all()
    for eta in etas:
        context.append(eta_total_citations(eta.id))
    return context



def article_chers_per_year(chers):
    articles_per_year = {
        "citations":[
            {"year": 2015, "articles": 0},
            {"year": 2016, "articles": 0},
            {"year": 2017, "articles": 0},
            {"year": 2018, "articles": 0},
            {"year": 2019, "articles": 0},
            {"year": 2020, "articles": 0},
            {"year": 2021, "articles": 0},
            {"year": 2022, "articles": 0},
        ],
        "citations_total" : 0,
    }
    



# citations of a group of researchers 
def citations_researchers_8years(researchers):
    citations_per_year = {
        "citations":[
            {"year": 2015, "citations": 0},
            {"year": 2016, "citations": 0},
            {"year": 2017, "citations": 0},
            {"year": 2018, "citations": 0},
            {"year": 2019, "citations": 0},
            {"year": 2020, "citations": 0},
            {"year": 2021, "citations": 0},
            {"year": 2022, "citations": 0},
        ],
        "citations_total" : 0,
    }
    max = 0
    top_researchers = []
    top_researcher = None
    for researcher in researchers:
        print(researcher)
        researcher_graph = researcher.graph_citations
        if max == 0 :
            max =  researcher.citations 
            top_researcher = researcher
        else:
            if researcher.citations > max:
                max = researcher.citations 
                top_researcher = researcher
            elif researcher.citations == max: 
                top_researchers.append(researcher)
            
        citations_per_year["citations_total"] += researcher.citations
        if not researcher_graph == None:
            for i in range(0,8):
                year = citations_per_year["citations"][i]["year"]
                for item in researcher_graph:
                    if item["year"] == year:
                        citations_per_year["citations"][i]["citations"] += item["citations"] 
                        break
    if top_researchers:
        citations_per_year["top_researchers"] = top_researchers
    else:
        if not top_researcher == None:
            citations_per_year["top_researcher"] = top_researcher
    return citations_per_year


def researchers_citations(researchers):
    context = []
    for r in researchers :
        context.append({"nom": r , "citations" : r.citations})
    return context 
            


def final_8years_citations_eta(eta_id):    
    """
    citations_per_year = {
        "citations":[
            {"year": 2015, "citations": 0},
            {"year": 2016, "citations": 0},
            {"year": 2017, "citations": 0},
            {"year": 2018, "citations": 0},
            {"year": 2019, "citations": 0},
            {"year": 2020, "citations": 0},
            {"year": 2021, "citations": 0},
            {"year": 2022, "citations": 0},
        ],
        "citations_total" : 0,
    }
    max = 0
    top_researchers = []
    top_researcher = None
    researchers = eta_chers(eta_id)
    for researcher in researchers:
        print(researcher)
        researcher_graph = researcher.graph_citations
        if max == 0 :
            max =  researcher.citations 
            top_researcher = researcher
        else:
            if researcher.citations > max:
                max = researcher.citations 
                top_researcher = researcher
            elif researcher.citations == max: 
                top_researchers.append(researcher)
            
        citations_per_year["citations_total"] += researcher.citations
        if not researcher_graph == None:
            for i in range(0,8):
                year = citations_per_year["citations"][i]["year"]
                for item in researcher_graph:
                    if item["year"] == year:
                        citations_per_year["citations"][i]["citations"] += item["citations"] 
                        break
    if top_researchers:
        citations_per_year["top_researchers"] = top_researchers
    else:
        if not top_researcher == None:
            citations_per_year["top_researcher"] = top_researcher
    return citations_per_year"""
    
    researchers = eta_chers(eta_id)
    return citations_researchers_8years(researchers)
        
def final_8years_citations_all_etas():
    citations_per_year_total = {
        "citations":[
            {"year": 2015, "citations": 0},
            {"year": 2016, "citations": 0},
            {"year": 2017, "citations": 0},
            {"year": 2018, "citations": 0},
            {"year": 2019, "citations": 0},
            {"year": 2020, "citations": 0},
            {"year": 2021, "citations": 0},
            {"year": 2022, "citations": 0},
        ],
     "citations_total": 0,
     }
    max = 0
    top_etas = []
    top_eta = None
    for etablisement in Etablisment.objects.all():
        eta_citations = final_8years_citations_eta(etablisement.id)
        if max == 0 :
            print("max "+str(max))
            max = eta_citations["citations_total"]
            top_eta = etablisement
        else:
            print("max "+str(max))
            if eta_citations["citations_total"] > max:
                max = eta_citations["citations_total"]
                top_eta = etablisement
            elif eta_citations["citations_total"] == max:
                max = eta_citations["citations_total"]
                top_etas.append(etablisement)
                
        citations_per_year_total["citations_total"] += eta_citations["citations_total"]
        for i in range(0,8):
            citations_per_year_total["citations"][i]["citations"] += eta_citations["citations"][i]["citations"]
    if top_etas:
        citations_per_year_total["top_etas"] = top_etas
    else:
        if not top_eta == None:
            citations_per_year_total["top_eta"] = top_eta
    return citations_per_year_total



# etablisements dashboard for 48 wilaya 
def etablisements_dash(wilaya):
    context = {
        'nbr_etablisement':0,
        'nbr_divisions': 0 ,
        'nbr_equipes': 0 ,
        'nbr_researchers':0
    }
    etablisements= Etablisment.objects.filter(location__id=wilaya)
    if etablisements:
        for eta in etablisements:
            context['nbr_divisions'] += Division.objects.filter(etablisment__id=eta.id).count()
            context['nbr_equipes'] += Equipe.objects.filter(division__etablisment__id=eta.id).count()
            context['nbr_researchers'] += eta_chers(eta.id).count()
        context['nbr_etablisement'] = etablisements.count()
    return context

def wilaya_dash():
    for wilaya in wilaya48:
        wilaya_nbr = int(list(wilaya.keys())[0])
        etas = etablisements_dash(wilaya_nbr)
        wilaya["value"] = etas['nbr_etablisement']
        wilaya["nbr_divs"] = etas['nbr_divisions']
        wilaya["nbr_equipes"] = etas['nbr_equipes']
        wilaya["nbr_researchers"] = etas['nbr_researchers']
        wilaya_researchers  = Researcher.objects.filter(Q(etablisment__location=wilaya_nbr)| Q(division__etablisment__location=wilaya_nbr)| Q(equipe__division__etablisment__location=wilaya_nbr)) 
        
        # wilaya["wilaya_citations"] = citations_researchers_8years(wilaya_researchers)["citations_total"]
        wilaya_citations=Researcher.objects.filter(etablisment__location=wilaya_nbr).aggregate(Sum("citations"))["citations__sum"]
        if wilaya_citations == None:
            wilaya['wilaya_citations'] = 0
        else:
            wilaya['wilaya_citations'] = wilaya_citations
        wilaya_articles = Researcher.objects.filter(etablisment__location=wilaya_nbr).aggregate(Sum("nbr_pubs"))["nbr_pubs__sum"]
        if wilaya_articles == None : 
            wilaya['wilaya_articles'] = 0
        else:
            wilaya['wilaya_articles'] = wilaya_articles
        
        citations_total_8year = []
        for citation_year in citations_researchers_8years(wilaya_researchers)["citations"]:
            wilaya_array = [str(citation_year["year"]),citation_year["citations"]]
            citations_total_8year.append(wilaya_array)
        wilaya["citations_total_8year"] = citations_total_8year
    return wilaya48

wilaya48 = [
 {'01': 'Adrar', 'id': 'DZ.AR'},
 {'02': 'Chlef', 'id': 'DZ.CH'},
 {'03': 'Laghouat', 'id': 'DZ.LG'},
 {'04': 'Oum El Bouaghi', 'id':'DZ.OB'},
 {'05': 'Batna', 'id': 'DZ.BT'},
 {'06': 'Béjaïa', 'id': 'DZ.BJ'},
 {'07': 'Biskra', 'id': 'DZ.BS'},
 {'08': 'Béchar', 'id': 'DZ.BC'},
 {'09': 'Blida', 'id': 'DZ.BL'},
 {'10': 'Bouira', 'id': 'DZ.BU'},
 {'11': 'Tamanrasset', 'id':'DZ.TM'},
 {'12': 'Tébessa', 'id': 'DZ.TB'},
 {'13': 'Tlemcen', 'id': 'DZ.TL'},
 {'14': 'Tiaret', 'id': 'DZ.TR'},
 {'15': 'Tizi Ouzou', 'id': 'DZ.TO'},
 {'16': 'Alger', 'id': 'DZ.AL'},
 {'17': 'Djelfa', 'id': 'DZ.DJ'},
 {'18': 'Jijel', 'id': 'DZ.JJ'},
 {'19': 'Sétif', 'id': 'DZ.SF'},
 {'20': 'Saïda', 'id': 'DZ.SD'},
 {'21': 'Skikda', 'id': 'DZ.SK'},
 {'22': 'Sidi Bel Abbès', 'id': 'DZ.SB'},
 {'23': 'Annaba', 'id': 'DZ.AN'},
 {'24': 'Guelma', 'id': 'DZ.GL'},
 {'25': 'Constantine', 'id': 'DZ.CO'},
 {'26': 'Médéa', 'id': 'DZ.MD'},
 {'27': 'Mostaganem', 'id': 'DZ.MG'},
 {'28': "M'Sila", 'id': 'DZ.MS'},
 {'29': 'Mascara', 'id': 'DZ.MC'},
 {'30': 'Ouargla', 'id': 'DZ.OG'},
 {'31': 'Oran', 'id': 'DZ.OR'},
 {'32': 'El Bayadh', 'id': 'DZ.EB'},
 {'33': 'Illizi', 'id': 'DZ.IL'},
 {'34': 'Bordj Bou Arreridj' , 'id' : "DZ.BB"},
 {'35': 'Boumerdès', 'id': 'DZ.BM'},
 {'36': 'El Tarf', 'id': 'DZ.ET'},
 {'37': 'Tindouf', 'id': 'DZ.TN'},
 {'38': 'Tissemsilt', 'id': 'DZ.TS'},
 {'39': 'El Oued', 'id': 'DZ.1950'},
 {'40': 'Khenchela', 'id': 'DZ.KH'},
 {'41': 'Souk Ahras', 'id': 'DZ.SA'},
 {'42': 'Tipaza', 'id': 'DZ.TP'},
 {'43': 'Mila', 'id': 'DZ.ML'},
 {'44': 'Aïn Defla', 'id': 'DZ.AD'},
 {'45': 'Naâma', 'id': 'DZ.NA'},
 {'46': 'Aïn Témouchent', 'id': 'DZ.AT'},
 {'47': 'Ghardaïa', 'id': 'DZ.GR'},
 {'48': 'Relizane', 'id': 'DZ.RE'}
]

