from __future__ import division
from django.http import Http404, HttpResponse
from serpapi import GoogleSearch
from ..models import *
from django.db.models import F, Q

def check_gs_id(gs_id):
    params = {
        "engine": "google_scholar_author",
        "author_id": gs_id,
        "api_key": "2c4f4ce6c429d7399649b280e13d0c519c0f088732d1bb9861dd514675b6374f"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    if "author" in results:
        return True
    return False

def serpapi_author(gs_id):
    params = {
        "engine": "google_scholar_author",
        "author_id": gs_id,
        "api_key": "2c4f4ce6c429d7399649b280e13d0c519c0f088732d1bb9861dd514675b6374f"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    if "error" in results :
        raise Http404("api kmel")
    return results

def serp_params(gs_id,start,sort):
    return {
        "engine": "google_scholar_author",
        "author_id": gs_id,
        "api_key": "2c4f4ce6c429d7399649b280e13d0c519c0f088732d1bb9861dd514675b6374f",
        "start": start,
        "num": str(start+100),
        "sort": sort
    }

def researcher_articles7years(researcher,start,sort):
    years = ["2022","2021","2020","2019","2018","2017","2016"]
    articles_info = {
        "per_year":{
            '2022' : {
            "nbr_articles": 0,
            "citations" : 0
            },
            '2021' : {
                "nbr_articles": 0,
                "citations" : 0
            },
            '2020' : {
                "nbr_articles": 0,
                "citations" : 0
            },
            '2019' : {
                "nbr_articles": 0,
                "citations" : 0
            },
            '2018' : {
                "nbr_articles": 0,
                "citations" : 0
            },
            '2017' : {
                "nbr_articles": 0,
                "citations" : 0
            },
            '2016' : {
                "nbr_articles": 0,
                "citations" : 0
            },
        },
        'nbr_articles_total': 0,
    }
    if sort == "pubdate":
        search = GoogleSearch(serp_params(researcher.get_google_id(), start, sort))
        results = search.get_dict() 
        nbr_articles_total = 0    
        nostop = True
        while 'articles' in results :
            nbr_articles_total += len(results["articles"])
            if nostop:
                for article in results["articles"]:
                    if article["year"] in years :
                        cited_by = article["cited_by"]["value"]
                        articles_info["per_year"][str(article["year"])]["nbr_articles"] += 1
                        if not cited_by==None: 
                            articles_info["per_year"][str(article["year"])]["citations"] += article["cited_by"]["value"]
                    else:
                        nostop = False
            start += 100
            search = GoogleSearch(serp_params(researcher.get_google_id(), start , sort))
            results = search.get_dict()
    articles_info["nbr_articles_total"] = nbr_articles_total
    return articles_info

def equipe_articles(equipe_id):
    total_equipe_articles = {
        "per_year":{
            '2022' : {
            "nbr_articles": 0,
            "citations" : 0
        },
        '2021' : {
            "nbr_articles": 0,
            "citations" : 0
        },
        '2020' : {
            "nbr_articles": 0,
            "citations" : 0
        },
        '2019' : {
            "nbr_articles": 0,
            "citations" : 0
        },
        '2018' : {
            "nbr_articles": 0,
            "citations" : 0
        },
        '2017' : {
            "nbr_articles": 0,
            "citations" : 0
        },
        '2016' : {
            "nbr_articles": 0,
            "citations" : 0
        },
        },
        'nbr_articles_total': 0,
    }
    nbr_articles_total_eq = 0
    for researcher in Researcher.objects.filter(Q(equipe=equipe_id)| Q(equipe_researchers=equipe_id)):
        print(researcher)
        researcher_articles = researcher_articles7years(researcher.get_google_id(),0,'pubdate')
        print(researcher_articles)
        for key,value in total_equipe_articles["per_year"].items():
            value['nbr_articles'] += researcher_articles["per_year"][str(key)]['nbr_articles']
            value['citations'] += researcher_articles["per_year"][str(key)]['citations']
        nbr_articles_total_eq += researcher_articles["nbr_articles_total"]
    total_equipe_articles['nbr_articles_total'] = nbr_articles_total_eq
    return total_equipe_articles


def get_researcher_citations(researcher):
    author = serpapi_author(researcher.get_google_id())
    citations = 0
    if "cited_by" in author :
        citations = author["cited_by"]["table"][0]["citations"]["all"]
    return citations


def get_etablisement_researchers(eta_id):
    return Researcher.objects.filter(Q(division__etablisment__id=eta_id) | Q(equipe__division__etablisment__id=eta_id) | Q(equipe_researchers__division__etablisment__id=eta_id) | Q(etablisment__id=eta_id))

def query_all_etablisements():
    etablisements_info = {}
    for etablisement in Etablisment.objects.all():
        etablisements_info[etablisement.__str__()] = {
            "chef_eta": etablisement.chef_etablisement.__str__() , 
            "nbr_researchers" : get_etablisement_researchers(etablisement.id).count(),
            "_citations" : get_citations_total_etablisement(etablisement.id),
            # "top_researcher_citation": top_researcher_citations(etablisement.id)["max"],
        }
    return etablisements_info

def top_researcher_citations(eta_id):
    context = {}
    researchers = get_etablisement_researchers(eta_id)
    researchers_citations = {}
    for researcher in researchers:
        researchers_citations[researcher.__str__()] = get_researcher_citations(researcher)
    context["researcher_citations"] = researchers_citations
    context["max"] = max(researchers_citations , key=researchers_citations.get)
    return context
    
    
def etas_researchers_citations():
    context = []
    researchers = list(get_etablisement_researchers(eta_id))
    etablisements = Etablisment.objects.all()
    for eta in etablisements:
        pass


# Queries
def get_etablisement_divisions(eta_id):
    return Division.objects.filter(etablisement=eta_id)

def get_division_researchers(div_id):
    return Researcher.objects.filter(division=div_id)
    
    
    
    
def get_citations_total_etablisement(eta_id):
    total_citaions = 0
    researchers = list(get_etablisement_researchers(eta_id))
    for researcher in researchers :
        print(researcher)
        total_citaions += get_researcher_citations(researcher)
    return total_citaions
    
def get_citations_of_all_etablisements():
    context = {
        "etas_citations" : [],
    }
    citations = 0
    i = 0
    for etablisement in Etablisment.objects.all():
        print(i)
        context["etas_citations"].append({
            "id": etablisement.id,
            "name": etablisement.nom,
            "total_citations" : get_citations_total_etablisement(etablisement.id),
        })
        citations += context["etas_citations"][i]["total_citations"]
        i+=1
    context["org_citations"] = citations
    return context

def final_8years_citations_eta(eta_id):
    citations_per_year = [
        {"year": 2015, "citations": 0},
        {"year": 2016, "citations": 0},
        {"year": 2017, "citations": 0},
        {"year": 2018, "citations": 0},
        {"year": 2019, "citations": 0},
        {"year": 2020, "citations": 0},
        {"year": 2021, "citations": 0},
        {"year": 2022, "citations": 0},
    ]
    researchers = get_etablisement_researchers(eta_id)
    for researcher in researchers:
        researcher_gs = serpapi_author(researcher.get_google_id())
        if not ('cited_by' in researcher_gs or 'graph' in researcher_gs["cited_by"]):
            continue
        researcher_graph = researcher_gs["cited_by"]["graph"]
        for i in range(0,8):
            year = citations_per_year[i]["year"]
            for item in researcher_graph:
                if item["year"] == year:
                    citations_per_year[i]["citations"] += item["citations"] 
                    break
    return citations_per_year

def final_8years_citations_all_etas():
    citations_per_year_total = [
        {"year": 2015, "citations": 0},
        {"year": 2016, "citations": 0},
        {"year": 2017, "citations": 0},
        {"year": 2018, "citations": 0},
        {"year": 2019, "citations": 0},
        {"year": 2020, "citations": 0},
        {"year": 2021, "citations": 0},
        {"year": 2022, "citations": 0},
    ]
    for etablisement in Etablisment.objects.all():
        eta_citations = final_8years_citations_eta(etablisement.id)
        for i in range(0,8):
            citations_per_year_total[i]["citations"] += eta_citations[i]["citations"]
    
    return citations_per_year_total

def top_10_citations_etas():
    all_etas = get_citations_of_all_etablisements()["etas_citations"]
    sorted_etas = sorted(all_etas , key=lambda x :x['total_citations'], reverse=True)
    return  sorted_etas[:10] if len(sorted_etas) >= 10  else sorted_etas

def all_researchers_citations_org():
    researchers_citations = []
    for researcher in Researcher.objects.all():
        researchers_citations.append({
            'id': researcher.id,
            'name': researcher.__str__(),
            'citations': get_researcher_citations(researcher)
        })
    return researchers_citations

def top_10_researchers_citations_org():    
    for researcher in Researcher.objects.all():
        
        pass    
    
def top_10_researchers_citations_eta(request):
    pass
def top_10_researchers_citations_div(request):
    pass


    
    
        
    
        