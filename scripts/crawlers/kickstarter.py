import urllib2
import json

def retrieve_projects():
    response = urllib2.urlopen('https://www.kickstarter.com/discover/advanced.json?sort=end_date&woe_id=2389876&state=live')
    projectsJson = json.loads(response.read())

    convertedProjects = []
    for project in projectsJson['projects']:
        converted = {}
        converted['title'] = project['name']
        converted['creator'] = project['creator']['name']
        converted['goal'] = project['goal']
        converted['startDate'] = project['created_at']
        converted['endDate'] = project['deadline']
        converted['pledged'] = project['pledged']
        converted['image'] = project['photo']['full']
        converted['description'] = project['blurb']
        converted['link'] = project['urls']['web']['project']
        convertedProjects.append(converted)
        
    return convertedProjects

if __name__ == '__main__':
    # Executed as a script
    campaign = open('kickstarter-campaign.json', 'w')
    campaign.write(json.dumps(retrieve_projects(), separators=(',',':')))
