---
layout: archive
title: "More on my research"
permalink: /posts/
author_profile: true
---

{% include base_path %}
{% assign postsByYear = site.posts | group_by_exp: "post", "post.date | date: '%Y'" %}
{% for year in postsByYear %}
  <h2>{{ year.name }}</h2>
  {% for post in year.items %}
    {% include archive-single-post.html %}
  {% endfor %}
{% endfor %}

{% if site.posts.size == 0 %}
Research summaries and explanatory notes will be added here.
{% endif %}
