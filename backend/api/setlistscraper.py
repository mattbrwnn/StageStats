from urllib.request import urlopen
from bs4 import BeautifulSoup

def getArtistStatsURL(artist_name):
    artist_name = artist_name.replace(' ', '+')
    url = f"https://www.setlist.fm/search?query={artist_name}"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    statlink = soup.find_all("a", attrs={'title': "View song statistics of all setlists"})[0]['href']
    return f"https://www.setlist.fm/{statlink}"
        
def getSongsPlayed(artist_name):
    page = urlopen(getArtistStatsURL(artist_name))
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    stattable = soup.find_all("table",)[0].findChildren('tbody', recursive=False)[0]
    names = soup.findAll('a', attrs={'class': 'songName'})
    counttags = soup.findAll('td', attrs={'class': 'songCount'})
    countlist = [tag.contents[0].contents[0].text for tag in counttags]
    namelist = [name.text for name in names]
    songdict = {}
    for name, count in zip(namelist, countlist):
        songdict[name] = count
    songdict['albums'] =  getAlbums(artist_name)
    return songdict
    
def getAlbums(artist_name):
    url = getArtistStatsURL(artist_name)
    url = url.replace('/stats/', '/stats/albums/')
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    stattable = soup.find_all("table",)[0].findChildren('tbody', recursive=False)[0]
    names = soup.findAll('td', attrs={'class': 'songName'})
    albums = []
    for name in names:
        try:
            albums.append(name.contents[1].contents[0].text)
        except:
            pass
    return [{'name': value} for value in albums]