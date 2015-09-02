---
layout: page
title: Crowdfunding937
tagline: Startup your city!
---
{% include JB/setup %}

# Projects

{% for project in site.data.current reverse | sort: 'project.deadline' %}
  - [{{ project.name }}]({{ project.url }}): Raise ${{ project.pledged | divided_by: 1000 | round }}K of ${{ project.goal | divided_by: 1000 | round }}K
  by {{ project.deadline | date: "%a, %b %d %Y" }}
  *{{ project.category }}* ({{ project.source|upcase|truncate: 1,'' }})

{% endfor %}
