import urllib2
import json

def retrieve_projects():
    response = urllib2.urlopen('https://api.indiegogo.com/1.1/search/campaigns.json?api_token=e88bd0a00305bfdfb18003a75665643b&city=Dayton&country=CTRY_US&status=open')
    projectsJson = json.loads(response.read())

    convertedProjects = []

    for project in projectsJson['response']:
        converted = {}
        converted['title'] = project['title']
        for team_member in project['team_members']:
            if team_member['owner'] == True: 
                converted['created'] = team_member['name']
        converted['goal'] = project['goal']
        converted['startDate'] = project['funding_started_at']
        converted['endDate'] = project['funding_ends_at']
        converted['pledged'] = project['collected_funds']
        converted['image'] = project['image_types']['original']
        converted['description'] = project['tagline']
        converted['link'] = project['web_url']
        convertedProjects.append(converted)
        
    return convertedProjects

if __name__ == '__main__':
    # Executed as a script
    campaign = open('indiegogo-campaign.json', 'w')
    campaign.write(json.dumps(retrieve_projects(), separators=(',',':')))
