import requests, os
from django.http import JsonResponse
from datetime import datetime

def top_rated_games(request):
    
    url = f"{os.environ['IGDB_BASE_URL']}/games"
    headers = {
        'Client-ID': f"{os.environ['IGDB_CLIENT_ID']}",
        'Authorization': f"Bearer {os.environ['IGDB_ACCESS_TOKEN']}"
    }
    params = {
        'fields': 'name,genres.name,platforms.name,url,summary,cover.url,first_release_date,release_dates.date,rating,screenshots.url',
        'order': 'total_rating_count desc',
        'limit': 10,
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        top_rated_games_data = response.json()
        return JsonResponse({'games': top_rated_games_data})
    else:
        return JsonResponse({'error': 'Failed to fetch'}, status=response.status_code)


def top_anticipated_games(request):
    
    url = f"{os.environ['IGDB_BASE_URL']}/games"
    headers = {
        'Client-ID': f"{os.environ['IGDB_CLIENT_ID']}",
        'Authorization': f"Bearer {os.environ['IGDB_ACCESS_TOKEN']}"
    }
    
    current_time = int(datetime.now().timestamp())
    timestamp_2024 = int(datetime(2024, 1, 1).timestamp())
    timestamp_2027 = int(datetime(2027, 1, 1).timestamp())
    
    params = {
        'fields': 'name,genres.name,platforms.name,url,summary,cover.url,first_release_date,release_dates.date,rating,screenshots.url', 
        'where': f'date > {timestamp_2024} & date < {timestamp_2027}',
        'order': 'aggregated_rating desc',
        'limit': 10,
    }

    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        top_anticipated_games_data = response.json()
        return JsonResponse({'games': top_anticipated_games_data})
    else:
        return JsonResponse({'error': 'Failed to fetch'}, status=response.status_code)

def search_games(request):
    query = request.GET.get('query')
    if query:
        url = f"{os.environ['IGDB_BASE_URL']}/games"
        headers = {
            'Client-ID': f"{os.environ['IGDB_CLIENT_ID']}",
            'Authorization': f"Bearer {os.environ['IGDB_ACCESS_TOKEN']}"
        }
        params = {
            'search': query,
            'fields': 'name,genres.name,platforms.name,url,summary,cover.url,first_release_date,release_dates.date,rating,screenshots.url',
            'limit': 3,
        }

        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            search_results_data = response.json()
            return JsonResponse({'games': search_results_data})
        else:
            return JsonResponse({'error': 'Failed to fetch search results'}, status=response.status_code)
    else:
        return JsonResponse({'error': 'No query provided'}, status=400)