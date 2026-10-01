#!/usr/bin/env python3
"""Build the talk map without geocoding services or Python dependencies.

Read _talks/*.md and _data/map_locations.json. Add approximate city coordinates
in the JSON file for each location used by a talk. No coordinates are inferred.
Run: python3 build_assets.py map
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def metadata(path):
    match = re.match(r'^---\s*\n(.*?)\n---', path.read_text(encoding='utf8'), re.S)
    if not match:
        raise ValueError(f'Missing front matter: {path}')
    fields = {}
    for line in match.group(1).splitlines():
        if not line or line.startswith((' ', '#')) or ':' not in line:
            continue
        key, value = line.split(':', 1)
        value = value.strip()
        if value.startswith('"'):
            value = json.loads(value)
        else:
            value = value.strip("'")
        fields[key] = value
    return fields

locations = json.loads((ROOT / '_data/map_locations.json').read_text())
entries = []
for path in sorted((ROOT / '_talks').glob('*.md')):
    talk = metadata(path)
    place = talk.get('location', '')
    if not place or place.lower() == 'online':
        continue
    if place not in locations:
        raise ValueError(f'Add coordinates for {place!r} in _data/map_locations.json')
    lat, lon = locations[place]
    if not (-90 <= lat <= 90 and -180 <= lon <= 180):
        raise ValueError(f'Invalid coordinates for {place!r}')
    text = '<strong>' + html.escape(talk['title']) + '</strong><br>'
    text += '<br>'.join(html.escape(talk.get(key, '')) for key in ['date', 'venue', 'location'])
    link = talk.get('link', '')
    if link.startswith(('https://', 'http://')):
        text += '<br><a target="_blank" rel="noopener" href="' + html.escape(link, quote=True) + '">Event page</a>'
    entries.append({'coordinates': [lat, lon], 'text': text})

page = '''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Selected talks</title>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css">
<style>html,body,#map{height:100%;margin:0;font-family:Arial,sans-serif}
.note{position:absolute;bottom:24px;left:10px;z-index:800;padding:5px 8px;background:white;color:#333;font-size:11px;border-radius:4px}
[data-theme="dark"] .leaflet-tile-pane{filter:brightness(.7)}
[data-theme="dark"] .leaflet-popup-content-wrapper,[data-theme="dark"] .leaflet-popup-tip{background:#25292d;color:#eee}
</style></head><body>
<div id="map" aria-label="Map of selected research talks"></div><div class="note">Selected talks · approximate city locations</div>
<script src="/assets/js/embed-theme.js"></script>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script>
const entries = __DATA__;
const map = L.map('map').setView([41, 13], 5);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution:'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',maxZoom:18
}).addTo(map);
entries.forEach(e=>L.circleMarker(e.coordinates,{radius:8,color:'#1f3f7a',fillColor:'#6f92d0',fillOpacity:.9}).addTo(map).bindPopup(e.text));
if(entries.length===1) map.setView(entries[0].coordinates,6);
if(entries.length>1) map.fitBounds(entries.map(e=>e.coordinates),{padding:[30,30],maxZoom:7});
</script></body></html>'''
page = page.replace('__DATA__', json.dumps(entries, ensure_ascii=False).replace('</', '<\\/'))
(ROOT / 'talkmap/talks_map.html').write_text(page, encoding='utf8')
print(f'wrote talkmap/talks_map.html: {len(entries)} talks')
