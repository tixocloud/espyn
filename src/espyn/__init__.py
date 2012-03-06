import urllib

ESPN_URL = "http://api.espn.com/{version}/{resource}/{method}?apikey={apikey}"

if __name__ == "__main__":
    version = 'v1'
    resource = 'sports'
    method = 'news'
    print urllib.urlopen
