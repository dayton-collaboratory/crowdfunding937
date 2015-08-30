import json
import datetime

combined = []

with open('_data/sources/kickstarter.json') as infile:
    data = json.load(infile)
    for project in data['projects']:
        deadline = datetime.datetime.fromtimestamp(project['deadline'])
        if deadline < datetime.datetime.now():
            combined.append(project)

with open('_data/current.json', 'w') as outfile:
    json.dump(combined, outfile)
