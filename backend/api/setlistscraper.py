from urllib.request import urlopen
from bs4 import BeautifulSoup


# Gets the URL for the artist song stats
def getArtistStatsURL(artist_name):
    artist_name = artist_name.replace(' ', '+')
    url = f"https://www.setlist.fm/search?query={artist_name}"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    statlink = soup.find_all("a", attrs={'title': "View song statistics of all setlists"})[0]['href']
    return f"https://www.setlist.fm/{statlink}"

# Gets all artists songs along with their play counts from setlists.fm
def getSongsPlayed(artist_name):
    page = urlopen(getArtistStatsURL(artist_name))
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    stattable = soup.find_all("table",)[0].findChildren('tbody', recursive=False)[0]
    names = soup.findAll('a', attrs={'class': 'songName'})
    songs = soup.findAll('a', attrs={'class': 'chartLink'})
    counttags = soup.findAll('td', attrs={'class': 'songCount'})
    countlist = [tag.contents[0].contents[0].text for tag in counttags]
    namelist = [name.text for name in names]
    songdict = {}
    for name, count in zip(namelist, countlist):
        songdict[name] = count
    return songdict
