#!/bin/bash
source ./env_vars.sh
echo WHERE_ON_EARTH: $WHERE_ON_EARTH
curl https://www.kickstarter.com/projects/search.json?woe_id=$WHERE_ON_EARTH | python -m json.tool > _data/sources/kickstarter.json
curl -G -d api_token=e88bd0a00305bfdfb18003a75665643b -d status=open -d city=Dayton https://api.indiegogo.com/1.1/search/campaigns.json | python -m json.tool > _data/sources/indiegogo.json
python combine_feeds.py
