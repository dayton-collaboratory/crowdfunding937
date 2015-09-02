import json
import datetime
from tzlocal import get_localzone
import pytz
import re

combined = []

def offset_aware(naive):
    return naive.replace(tzinfo=pytz.utc).astimezone(get_localzone())

with open('_data/sources/kickstarter.json') as infile:
    data = json.load(infile)
    for project in data['projects']:
        deadline = datetime.datetime.fromtimestamp(project['deadline'])
        if deadline > datetime.datetime.now():
            proj = {'name': project['name'],
                'deadline': deadline,
                'url': project['urls']['web']['project'],
                'pledged': project['pledged'],
                'goal': project['goal'],
                'source': 'kickstarter',
                'category': project['category']['name'],
                }
            combined.append(proj)

timezone_with_colon = re.compile(r'(-\d\d):(\d\d)$')

def parse_indiegogo_time(raw):
    #cooked = timezone_with_colon.sub(r'\1\2', raw)
    # discarding timezone info
    cooked = timezone_with_colon.sub('', raw)
    return datetime.datetime.strptime(cooked, '%Y-%m-%dT%H:%M:%S')

with open('_data/sources/indiegogo.json') as infile:
    data = json.load(infile)
    for project in data['response']:
        proj = {'name': project['title'],
                'deadline': parse_indiegogo_time(project['funding_ends_at']),
                'url': project['web_url'],
                'pledged': project['collected_funds'],
                'goal': project['goal'],
                'source': 'indiegogo',
                'category': project['category']['name'],
                }
        combined.append(proj)

combined.sort(key=lambda x: x['deadline'])
for proj in combined:
    proj['deadline'] = str(proj['deadline'])

with open('_data/current.json', 'w') as outfile:
    json.dump(combined, outfile, indent=2)
