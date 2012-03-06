import urllib

class Sport():
    API_KEY = 'y7vepxge2vuzk592wz3x7wcf'
    ESPN_URL = 'http://api.espn.com/v1'
    BASE_URL = ESPN_URL + '/sports'
    BASKETBALL = 'basketball'
    BASEBALL = 'baseball'
    BOXING = 'boxing'
    FOOTBALL = 'football'
    GOLF = 'golf'
    HOCKEY = 'hockey'
    HORSE_RACING = 'horse-racing'
    MMA = 'mma'
    RACING = 'racing'
    SOCCER = 'soccer'
    TENNIS = 'tennis'

    SUPPORTED_SPORTS = frozenset([
        BASEBALL,
        BASKETBALL,
        BOXING,
        FOOTBALL,
        GOLF,
        HOCKEY,
        HORSE_RACING,
        MMA,
        RACING,
        SOCCER,
        TENNIS
    ])


    def __init__(self, sport=None):
        if sport not in Sport.SUPPORTED_SPORTS:
            raise KeyError ("%s is not a valid supported sport" % sport)
        self.base_url = Sport.BASE_URL + '/' + sport

    def get_news(self, date=None, headlines=False, top=False, id=None):
        url_suffix = '/news'

        if id:
            url_suffix += id
        elif date:
           url_suffix += '/dates' + date.year + date.month + date.day
        elif headlines:
            url_suffix += '/headlines'
            if top:
                url_suffix += '/top'

        fetch_url = self.base_url + url_suffix + '?apikey=' + Sport.API_KEY
        return urllib.urlopen(fetch_url)

    def get_team_news(self, id=None, date=None):
        if not id:
            raise ValueError ("Team %s is needed to request team news" % id)
        url_suffix = '/teams/%s/news' % str(id)

        if date:
            url_suffix += '/news/dates/%s%S%s' % (date.year, date.month, date.day)
        fetch_url = self.base_url + url_suffix + '?apikey=' + Sport.API_KEY
        return urllib.urlopen(fetch_url)

class League(Sport):
    LEAGUE_TO_SPORT = {
        'mlb': Sport.BASEBALL,
        'mens-college-basketball': Sport.BASKETBALL,
        'nba': Sport.BASKETBALL,
        'wnba': Sport.BASKETBALL,
        'womens-college-basketball': Sport.BASKETBALL,
        'college-football': Sport.FOOTBALL,
        'nfl': Sport.FOOTBALL,
        'nhl': Sport.HOCKEY,
        'nascar': Sport.RACING,
    }

    def __init__(self, league=None):
        if league not in League.LEAGUE_TO_SPORT.keys():
            raise KeyError ("%s is not a valid supported league" % league)
        self.base_url = Sport(sport=League.LEAGUE_TO_SPORT[league]).base_url + '/' + league
        print self.base_url

if __name__ == "__main__":
    hockey = League('nhl')
    print hockey.get_news().readlines()
