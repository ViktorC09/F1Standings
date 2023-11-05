import requests
import json
def ergast_retrieve(api_endpoint: str):
    url = f'https://ergast.com/api/f1/{api_endpoint}.json'
    response = requests.get(url).json()
    
    return response['MRData']
last = ergast_retrieve('current/last')
l = last['RaceTable']['round']
q = "current/"
w = str(l)
e = "/driverStandings"
r=q+w+e
data = ergast_retrieve(r)

for a in range(22):
    datab = data['StandingsTable']['StandingsLists'][0]['DriverStandings'][int(a)]['Driver']['code']
    datac = data['StandingsTable']['StandingsLists'][0]['DriverStandings'][int(a)]['points']
    print(datab,"   ",datac)
