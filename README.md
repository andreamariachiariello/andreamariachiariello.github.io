# Andrea Maria Chiariello — academic website

Jekyll / AcademicPages website adapted from Giorgio Nicoletti’s design.
See the Italian guide supplied alongside this website directory.

1. Replace USERNAME in _config.yml with the real GitHub username.
2. Review all text; add the portrait and complete CV.
3. Create the public repository USERNAME.github.io and upload this directory’s contents.
4. Set Settings → Pages → Deploy from a branch → main → /(root).

The four publication records, network and timeline are a selected sample, not a complete bibliography.
The West Nile entry is explicitly a preprint. Research prose is a proposed author-voice draft.

To update network, timeline and map: `python3 build_assets.py` (standard library only).
Map positions are edited in `_data/map_locations.json`.
All metadata values in publication/talk front matter should remain on one line; lists use ["a", "b"].
For local Jekyll preview: `bundle install`, then `bundle exec jekyll serve --config _config.yml,_config.dev.yml`.

See ATTRIBUTION.md and LICENSE for source credits.
