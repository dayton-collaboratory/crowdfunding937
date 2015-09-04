import json

from crawlers import indiegogo
from crawlers import kickstarter


if __name__ == '__main__':
    # Executed as a script
    convertedProjects = indiegogo.retrieve_projects();
    convertedProjects.extend(kickstarter.retrieve_projects())
    
    campaign = open('campaign.json', 'w');
    campaign.write(json.dumps(convertedProjects, separators=(',',':')))
    
    
    
    