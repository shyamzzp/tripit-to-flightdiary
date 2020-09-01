import requests
from requests_oauthlib import OAuth1
import json

def get_trips():
    with open('creds.json') as f:
        creds = json.load(f)

    auth = OAuth1(creds['CLIENT_KEY'], creds['CLIENT_SECRET'],
        creds['OAUTH_TOKEN'], creds['OAUTH_TOKEN_SECRET'])
    return requests.get('https://api.tripit.com/v1/list/trip/'
        # 'traveler/true/past/true/format/json/'  # to get all the past trips into consideration.
        'traveler/true/past/false/format/json/'
        'page_size/500/include_objects/true', auth=auth).json()

def main():
    trips=get_trips()
    print (json.dumps(trips, indent=4))
    with open('tripit.json', 'w') as fp:
	    json.dump(trips, fp)
	    print ("DONE")


if __name__ == '__main__':
    main()
