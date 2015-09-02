import json
import datetime

combined = []

with open('_data/sources/kickstarter.json') as infile:
    data = json.load(infile)
    for project in data['projects']:
        import ipdb; ipdb.set_trace()
        deadline = datetime.datetime.fromtimestamp(project['deadline'])
        if deadline > datetime.datetime.now():
            project['source'] = 'kickstarter'
            combined.append(project)

with open('_data/current.json', 'w') as outfile:
    json.dump(combined, outfile, indent=2)
