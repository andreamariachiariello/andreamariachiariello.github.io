#!/usr/bin/env python3
"""Regenerate network, publication timeline and talk map (standard library only).
Usage: python3 build_assets.py [network timeline map]
"""
import subprocess
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent
TASKS = {'network': 'collab_net/build_network.py',
         'timeline': 'research_timeline/build_timeline.py',
         'map': 'talkmap/build_map.py'}
if __name__ == '__main__':
    targets = sys.argv[1:] or list(TASKS)
    unknown = set(targets) - set(TASKS)
    if unknown:
        sys.exit('Unknown target: ' + ', '.join(sorted(unknown)))
    for target in targets:
        subprocess.run([sys.executable, str(ROOT / TASKS[target])], check=True, cwd=ROOT)
