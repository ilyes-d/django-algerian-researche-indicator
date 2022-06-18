"""

def serpapi_config(gs_id):
    params = serp_params(gs_id,0,"pubdate")
    search = GoogleSearch(params)
    results = search.get_dict()
    if "author" in results:
        return True
    return False
def top_researcher_citations(eta_id):
    context = {}
    researchers = chercheurs_of_eta(eta_id)
    researchers_citations = {}
    for researcher in researchers:
        print(researcher)
        researchers_citations[researcher.__str__()] = get_researcher_citations(researcher)
    context["researcher_citations"] = researchers_citations
    context["max"] = max(researchers_citations , key=researchers_citations.get)
    return context
def get_citations_total_etablisement(eta_id):
    total_citaions = 0
    researchers = list(chercheurs_of_eta(eta_id))
    for researcher in researchers :
        print(researcher)
        total_citaions += get_researcher_citations(researcher)
    return total_citaions

def top_10_citations_etas():
    all_etas = get_citations_of_all_etablisements()["etas_citations"]
    sorted_etas = sorted(all_etas , key=lambda x :x['total_citations'], reverse=True)
    return  sorted_etas[:10] if len(sorted_etas) >= 10  else sorted_etas
def get_researcher_citations(researcher):
    author = serpapi_author(researcher.get_google_id())
    citations = 0
    if "cited_by" in author :
        citations = author["cited_by"]["table"][0]["citations"]["all"]
    return citations
def all_researchers_citations_org():
    researchers_citations = []
    for researcher in Researcher.objects.all():
        researchers_citations.append({
            'id': researcher.id,
            'name': researcher.__str__(),
            'citations': get_researcher_citations(researcher)
        })
    return researchers_citations
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
        researcher_articles = researcher_articles7years(researcher,0,'pubdate')
        print(researcher_articles)
        for key,value in total_equipe_articles["per_year"].items():
            value['nbr_articles'] += researcher_articles["per_year"][str(key)]['nbr_articles']
            value['citations'] += researcher_articles["per_year"][str(key)]['citations']
        nbr_articles_total_eq += researcher_articles["nbr_articles_total"]
    total_equipe_articles['nbr_articles_total'] = nbr_articles_total_eq
    return total_equipe_articles


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
    def query_all_researchers():
    chers_info = {}
    for cher in Researcher.objects.all():
        div_info[div.__str__()] = {
            "nom":cher.nom,
            "etablisement":,
            "division":,
            "etablisement":Etablisment.objects.get(division=div.id).__str__(),
            "nbr_equipes":Equipe.objects.filter(division=div.id).count(),
            "nbr_chers": Researcher.objects.filter(Q(equipe__division=div.id)|Q(equipe_researchers__division=div.id)).count()
        }
    return div_info

"""
