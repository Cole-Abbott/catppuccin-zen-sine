"""Install this local package into an explicitly chosen, closed Zen profile."""
import argparse
from datetime import datetime, timezone
import fcntl
import json
from pathlib import Path
import shutil
import tempfile
import os

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('profile', type=Path, help='Profile Folder from Zen about:support; quit Zen first')
args = parser.parse_args()
profile = args.profile.expanduser().resolve()
root = Path(__file__).resolve().parent
if not (profile / 'prefs.js').is_file() or not (profile / 'chrome/JS/sine.sys.mjs').is_file():
    parser.error('Choose an existing Zen profile with Sine installed.')

# Firefox uses an advisory fcntl lock on this file while the profile is in use.
with (profile / '.parentlock').open('a') as lock:
    try:
        fcntl.lockf(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        parser.error('This profile is running. Quit Zen completely before installing.')
    mods_dir = profile / 'chrome/sine-mods'
    registry = mods_dir / 'mods.json'
    mods = json.loads(registry.read_text()) if registry.exists() else {}
    metadata = json.loads((root / 'theme.json').read_text())
    mod_id = metadata['id']
    destination = mods_dir / mod_id
    if destination.exists() or mod_id in mods:
        parser.error('Catppuccin is already installed. Remove it through Sine before reinstalling.')
    mods_dir.mkdir(parents=True, exist_ok=True)
    if registry.exists():
        stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
        shutil.copy2(registry, mods_dir / f'mods.json.before-catppuccin-{stamp}.bak')
    destination.mkdir()
    for name in ['theme.json', 'preferences.json', 'userChrome.css', 'userContent.css', 'LICENSE', 'PROVENANCE.json']:
        shutil.copy2(root / name, destination / name)
    # This package has no published repository. Suppress update checks until published.
    metadata.update({'enabled': True, 'no-updates': True})
    mods[mod_id] = metadata
    with tempfile.NamedTemporaryFile(mode='w', dir=mods_dir, delete=False) as temp:
        json.dump(mods, temp, indent=2)
        temp.write('\n')
    os.replace(temp.name, registry)
print('Installed Catppuccin. Open Zen > Settings > Sine Mods to select flavor and accent.')
