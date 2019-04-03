import requests

#have to do error handing
def getPlaceSummary(place):
    S = requests.Session()
    
    URL = "https://en.wikipedia.org/api/rest_v1/page/summary/"+ place.replace(" ", "_")
    print(URL)
    TITLE = place

    PARAMS = {
        'action': "parse",
        'page': TITLE,
        'format': "json"
    }

    R = S.get(url=URL)
    DATA = R.json()

    print(DATA["extract"])
    return(DATA["extract"])

getPlaceSummary("Chinese Garden of Friendship")