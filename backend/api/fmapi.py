from repertorio import Repertorio
from django.http import JsonResponse
import json

def get_artist_setlist(request, artist_name):
    api = Repertorio('4HgFs37ud5OQhHs48Go6mO6j6GFiqHpFaMof')
    if request.method == 'GET':
        try:
            setlists_data = api.setlists(artistName=artist_name)
            total_pages = setlists_data.get('total', 0)
            print(total_pages)

            song_counts = count_songs(setlists_data)

            print("Songs played by:", artist_name)
            for song, count in song_counts.items():
                print(f"{song}: {count}")
            return JsonResponse(song_counts, safe=False)
            # return JsonResponse(setlists_data, safe=False)

        except Exception as e:
            print(f"Error in get_artist_setlist: {e}")
            return JsonResponse({'error': str(e)}, status=500)

# def get_artist_setlist(request, artist_name):
#     api = Repertorio('4HgFs37ud5OQhHs48Go6mO6j6GFiqHpFaMof')
#     if request.method == 'GET':
#         try:
#             song_counts = {}

#             # Initial call to get the total number of pages
#             initial_data = api.setlists(artistName=artist_name)
#             total_pages = initial_data.get('total', 0)

#             # Loop over each page and accumulate song counts
#             for page in range(1, total_pages + 1):
#                 setlists_data = api.setlists(artistName=artist_name, p=page)
#                 page_song_counts = count_songs(setlists_data)

#                 # Update the overall song counts
#                 for song, count in page_song_counts.items():
#                     song_counts[song] = song_counts.get(song, 0) + count

#             print("Songs played by:", artist_name)
#             for song, count in song_counts.items():
#                 print(f"{song}: {count}")

#             # Return the final song counts
#             return JsonResponse(song_counts, safe=False)
#         except Exception as e:
#             print(f"Error in get_artist_setlist: {e}")
#             return JsonResponse({'error': str(e)}, status=500)
        
def count_songs(setlists_data):
    try:
        song_counts = {}
        setlists = setlists_data.get('setlist', [])

        if not isinstance(setlists, list):
            return {}

        for setlist in setlists:
            if 'sets' not in setlist or not isinstance(setlist['sets'], dict):
                continue

            sets = setlist['sets'].get('set', [])

            if not isinstance(sets, list):
                continue

            for set in sets:
                if 'song' not in set or not isinstance(set['song'], list):
                    continue

                for song in set['song']:
                    if 'name' not in song or not isinstance(song['name'], str):
                        print("Error: 'name' key is missing or not a string in song")
                        continue

                    song_name = song['name']
                    song_counts[song_name] = song_counts.get(song_name, 0) + 1

        return song_counts

    except Exception as e:
        print(f"Error in count_songs: {e}")
        return {}
