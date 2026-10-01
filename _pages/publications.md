---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% include base_path %}

This page contains a **selected bibliography**, currently four papers and preprints. For a broader publication record, see [Google Scholar]({{ site.author.googlescholar }}) and [ORCID]({{ site.author.orcid }}).

The collaboration network and the counts below use only these selected entries. Paper nodes are coloured by research area; coauthor size reflects the number of included papers.

<iframe class="embed embed--network" src="/collab_net/network.html?switch=off" title="Collaboration network"></iframe>

<div class="pub-filters" role="group" aria-label="Filter by research area">
  <button class="pub-filter is-active" type="button" data-theme="all" aria-pressed="true">All <span class="count">{{ site.publications.size }}</span></button>
  {% for t in site.data.themes %}{% assign n = site.publications | where_exp: "p", "p.theme contains t.key" %}
  <button class="pub-filter" type="button" data-theme="{{ t.key }}" aria-pressed="false" style="--area: {{ t.colour }}; --area-dark: {{ t.colour_dark | default: t.colour }}">{{ t.title }} <span class="count">{{ n.size }}</span></button>{% endfor %}
</div>

<div class="pub-list">
{% assign pubs = site.publications | sort: "date" | reverse %}
{% assign by_year = pubs | group_by_exp: "p", "p.date | date: '%Y'" %}
{% for year in by_year %}
<section class="year-group">
<h2>{{ year.name }}</h2>
{% for post in year.items %}
  {% include archive-single-publication.html %}
{% endfor %}
</section>
{% endfor %}
</div>

<script src="{{ base_path }}/assets/js/filters.js" defer></script>
