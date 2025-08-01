import requests
from django.shortcuts import render

def home(request):
    # Top anime display
    response = requests.get("https://api.jikan.moe/v4/top/anime")
    anime_list = response.json().get("data", [])
    return render(request, 'anime/home.html', {'anime_list': anime_list})

def search(request):
    query = request.GET.get("q", "")
    anime_list = []
    if query:
        response = requests.get(f"https://api.jikan.moe/v4/anime?q={query}")
        anime_list = response.json().get("data", [])
    return render(request, 'anime/search.html', {"anime_list": anime_list, "query": query})

def detail(request, anime_id):
    response = requests.get(f"https://api.jikan.moe/v4/anime/{anime_id}")
    anime = response.json().get("data", {})
    return render(request, 'anime/detail.html', {"anime": anime})

def filter_anime(request):
    genre = request.GET.get("genre")
    season = request.GET.get("season")
    year = request.GET.get("year")
    anime_list = []

    url = "https://api.jikan.moe/v4/anime?"
    if genre:
        url += f"&genres={genre}"
    if season and year:
        url = f"https://api.jikan.moe/v4/seasons/{year}/{season.lower()}"

    response = requests.get(url)
    if response.status_code == 200:
        anime_list = response.json().get("data", [])

    return render(request, "anime/filter.html", {"anime_list": anime_list})