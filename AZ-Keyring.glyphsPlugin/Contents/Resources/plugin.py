# AZ Keyring entry point. The real plugin ships as version-specific sourceless
# bytecode under _pyc/pyXX (3.11 for Glyphs 3, 3.14 for Glyphs 4). Pick the tree
# for the running interpreter, put it on the path, and hand off. This file stays
# plain source on purpose: it holds no logic, only the hand-off. Importing the
# entry module registers the AZKeyring ObjC class that Info.plist names, so
# Glyphs resolves NSPrincipalClass with nothing else here.
import sys
from pathlib import Path

_tree = Path(__file__).resolve().parent / "_pyc" / f"py{sys.version_info.major}{sys.version_info.minor}"
if _tree.is_dir() and str(_tree) not in sys.path:
    sys.path.insert(0, str(_tree))

from _azkeyring_plugin import *  # noqa: E402,F401,F403
