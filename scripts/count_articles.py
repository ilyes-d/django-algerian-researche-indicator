from serpapi import GoogleSearch

params = {
    "engine": "google_scholar_author",
    "author_id": "EicYvbwAAAAJ",
    "api_key": "6bbac90594777b50d1a7cb232de4c87e7eab93ca2cbdf37657081d9912f28970",
    "start": 0,
    "num": "100"
}

search = GoogleSearch(params)
results = search.get_dict()
print(results)
articles = results['articles']
