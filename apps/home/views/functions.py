from django.http import HttpResponse
from serpapi import GoogleSearch
from ..models import *
from django.db.models import F, Q

def serpapi_author(researcher_id):
    params = {
        "engine": "google_scholar_author",
        "author_id": researcher_id,
        "api_key": "016c19a111a3df750b7a37250aedf532683ef08faa73e2ab7f4aba7f2f2746be"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    if "errors" in results :
        return {"api-kmel" : "api key kmel"}
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


def get_researcher_citations(researcher):
    author = serpapi_author(researcher.get_google_id())
    citations = 0
    if "cited_by" in author :
        citations = author["cited_by"]["table"][0]["citations"]["all"]
        print(citations)
    if "api-kmel" in author : 
        return "api key kmel"
    return citations

def get_etablisement_researchers(eta_id):
    return Researcher.objects.filter(Q(division__etablisment__id=eta_id) | Q(equipe__division__etablisment__id=eta_id) | Q(equipe_researchers__division__etablisment__id=eta_id) | Q(etablisment__id=eta_id))

def get_citations_total_etablisement(eta_id):
    total_citaions = 0
    researchers = list(get_etablisement_researchers(eta_id))
    for researcher in researchers :
        print(researcher)
        total_citaions += get_researcher_citations(researcher)
    return total_citaions
    
def get_citations_all_etablisements():
    citations = 0
    for etablisement in Etablisment.objects.all():
        citations += get_citations_total_etablisement(etablisement.id)
    return citations



def final_years_citations_etablisement(eta_id):
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
        researcher_graph = serpapi_author(researcher.get_google_id())["cited_by"]["graph"]
        for i in range(0,8):
            year = citations_per_year[i]["year"]
            print(year)
            for item in researcher_graph:
                if item["year"] == year:
                    citations_per_year[i]["citations"] += item["citations"] 
                    break
    return citations_per_year
            
            

def final_years_all_etablisement():
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
        eta_citations = final_years_citations_etablisement(etablisement.id)    
        for i in range(0,8):
            citations_per_year_total[i]["citations"] += eta_citations[i]["citations"]
    
    return citations_per_year_total