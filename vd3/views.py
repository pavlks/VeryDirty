from django.shortcuts import render
from django.http import HttpResponse
import requests


def index(request, page=1, threshold_date='day'):
    prev_page = page - 1
    curr_page = page
    next_page = page + 1

    settings = {
        'prev_page': prev_page,
        'curr_page': curr_page,
        'next_page': next_page,
        'page' : curr_page,
        'sorting': 'rating',
        'per_page': 16,
        'threshold_date': threshold_date,
    }
    response = requests.get('https://d3.ru/api/posts/', params=settings).json()
    d3_posts = response["posts"]
    verified_posts = d3_posts
    post_count = len(d3_posts)
    badlist = [150, 170, 6545, 8271]  # id подсайтов politota: 170, politics: 150, polka: 6545, telega: 8271
    for i in reversed(range(post_count)):
        if d3_posts[i]["domain"]["id"] in badlist or d3_posts[i]["rating"] is None or d3_posts[i]["rating"] <= 0 or not d3_posts[i]["url_slug"]:
            del verified_posts[i]
    return render(request, 'vd3/posts.html', {'posts' : verified_posts, 'settings' : settings, })

