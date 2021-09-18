import json
import urllib.request as url

response = url.urlopen('https://data.covid19india.org/states_daily.json')
data = json.load(response)
states = data['states_daily']

confirmed = []
recovered = []
deceased = []

for i in range(len(states)):
    if states[i]['status'] == 'Confirmed':
        confirmed.append(states[i])
    elif states[i]['status'] == 'Recovered':
        recovered.append(states[i])
    else:
        deceased.append(states[i])


state = 'up'
cases = 0
for i in range(len(confirmed)):
    for key in confirmed[i]:
        if key == state:
            cases += int(confirmed[i][key])

print("Total cases in Delhi ::",cases)

#Print dates on which total cases was more than 2 lacs

for i in range(len(confirmed)):
    if int(confirmed[i]['tt']) > 200000:
        print(confirmed[i]['date'])






