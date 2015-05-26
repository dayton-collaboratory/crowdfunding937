# Architecture

## Scraper

- Only non-static component
- Consumes API from Kickstarter, ...
- Scrapes Indiegogo, ...
- Checks crowdfunding937.json to determine which ones are new
- Creates Jekyll blog posts (`_posts/blahblah.md`) 
- Creates new version of crowdfunding937.json
- pushes to github

## Jekyll blog posts

- Generate RSS through jekyll-rss-feeds (http://joelglovier.com/writing/rss-for-jekyll/)

## Jekyll blog

- Link to RSS
- Link to crowdfunding937.json
- Posts 

## Static JSON file

- in lieu of API
- data store to check whether campaigns require new posts

# Data sources

## Indiegogo

Doesn't seem to have RSS for search results, or an API.
May need to simply scrape
https://www.indiegogo.com/explore?filter_title=dayton

not sure how much will load directly via Requests, though

## Kickstarter

https://github.com/markolson/kickscraper

http://stackoverflow.com/questions/12907133/does-kickstarter-have-a-public-api

http://www.kickstarter.com/projects/search.json?search=&term=dayton


