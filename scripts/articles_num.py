from serpapi import GoogleSearch
params = {
    "engine": "google_scholar_author",
    "author_id": "D0lL1r0AAAAJ",
    "api_key": "bfdde7462931844d6003e1d183494fad96f1011bdd6d192179f5bae85d0e16c1",
    "start": 0,
    "num": "100"
}
search = GoogleSearch(params)
results = search.get_dict()
articles_num = len(results["articles"])
flag = 100
while "articles" in results:
    params = {
        "engine": "google_scholar_author",
        "author_id": "D0lL1r0AAAAJ",
        "api_key": "bfdde7462931844d6003e1d183494fad96f1011bdd6d192179f5bae85d0e16c1",
        "start": flag,
        "num": str(flag+100)
    }
    flag += 100
    search = GoogleSearch(params)
    results = search.get_dict()
    if "articles" in results:
        articles_num += len(results["articles"])
print(articles_num)
