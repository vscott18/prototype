import base64
import requests
#
#getThis = "https://api.mysportsfeeds.com/v1.1/pull/nfl/2017-regular/game_boxscore.json?gameid=20171008-SF-IND&teamstats=W,L,T,PF,PA&playerstats=Att,Comp,Yds,TD"
#r = requests.get(getThis)
#data = r.json()

def send_request():
    # Request

    try:
        response = requests.get(
            url= "https://api.mysportsfeeds.com/v1.1/pull/nfl/2017-regular/game_boxscore.json?gameid=20171008-SF-IND&teamstats=W,L,T,PF,PA&playerstats=Att,Comp,Yds,TD",
            params={
                "fordate": "20161121"
            },
            headers={
                "Authorization": "Basic " + base64.b64encode('{}:{}'.format(vzsn,benice2me).encode('utf-8')).decode('ascii')
            }
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

send_request()