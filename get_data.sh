#!/bin/bash
source ./env_vars.sh
echo WHERE_ON_EARTH: $WHERE_ON_EARTH
curl https://www.kickstarter.com/projects/search.json?woe_id=$WHERE_ON_EARTH | python -m json.tool > _data/sources/kickstarter.json

# cd crowdscraper
# scrapy runspider crowdscraper/spiders/indiegogo_spider.py
