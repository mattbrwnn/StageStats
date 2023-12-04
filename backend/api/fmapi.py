from repertorio import Repertorio
from django.http import JsonResponse
import json

def get_artist_setlist(request, artist_name):
    api = Repertorio('4HgFs37ud5OQhHs48Go6mO6j6GFiqHpFaMof')
    if request.method == 'GET':
        try:
            setlists = api.setlists(artistName=artist_name)
            print(json.dumps(setlists, indent=4))
            return JsonResponse(setlists, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        