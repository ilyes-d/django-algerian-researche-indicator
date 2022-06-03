from serpapi import GoogleSearch
import requests

def get_articles_num():
    params = {
        "engine": "google_scholar_author",
        "author_id": "P77h8G8AAAAJ",
        "api_key": "2c4f4ce6c429d7399649b280e13d0c519c0f088732d1bb9861dd514675b6374f",
        "start": 0,
        "num": "100",
        "sort": "pubdate"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    if 'articles' in results:
        articles_num = len(results["articles"])
    else: articles_num = 0
    flag = 100
    while "articles" in results:
        params = {
            "engine": "google_scholar_author",
            "author_id": "TnIU-bAAAAAJ",
            "api_key": "bfdde7462931844d6003e1d183494fad96f1011bdd6d192179f5bae85d0e16c1",
            "start": flag,
            "num": str(flag+100)
        }
        flag += 100
        search = GoogleSearch(params)
        results = search.get_dict()
        if "articles" in results:
            articles_num += len(results["articles"])
    return articles_num

def serp_params(gs_id,start,sort):
    return {
        "engine": "google_scholar_author",
        "author_id": gs_id,
        "api_key": "2c4f4ce6c429d7399649b280e13d0c519c0f088732d1bb9861dd514675b6374f",
        "start": start,
        "num": str(start+100),
        "sort": sort
    }


def serpapi_articles(gs_id,start,sort):
    years = ["2022","2021","2020","2019","2018","2017","2016"]
    articles_info = {
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
        'nbr_articles': 0,
    }
    if sort == "pubdate":
        search = GoogleSearch(serp_params(gs_id, start, sort))
        results = search.get_dict() 
        nbr_articles = 0    
        nostop = True
        while 'articles' in results :
            nbr_articles += len(results["articles"])
            if nostop:
                for article in results["articles"]:
                    # print(article)
                    if article["year"] in years :
                        cited_by =article["cited_by"]["value"]
                        articles_info[str(article["year"])]["nbr_articles"] += 1
                        if not cited_by==None: 
                            articles_info[str(article["year"])]["citations"] += article["cited_by"]["value"]
                    else:
                        nostop = False
            start += 100
            search = GoogleSearch(serp_params(gs_id, start , sort))
            results = search.get_dict()
    articles_info["nbr_articles"] = nbr_articles
    return articles_info

a = serpapi_articles("P77h8G8AAAAJ",0,"pubdate")
print(a)

# here 1
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 2
# here 3



