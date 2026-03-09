# pythonanywhere_wsgi.py
#
# INSTRUCTIONS
# ────────────────────────────────────────────────────────────────────────────
# On PythonAnywhere:
#   1. Open the "Web" tab → click your web app → scroll to "Code" section.
#   2. Click the WSGI configuration file link (e.g.
#      /var/www/yourusername_pythonanywhere_com_wsgi.py).
#   3. REPLACE the entire contents of that file with the code below,
#      substituting your PythonAnywhere username where shown.
#
# This file is here for reference only — it is NOT used locally.
# ────────────────────────────────────────────────────────────────────────────

import os
import sys

# ── 1. Add the project root to Python path ──────────────────────────────────
# Replace "yourusername" with your actual PythonAnywhere username.
PROJECT_ROOT = '/home/yourusername/InstaCode'
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# ── 2. Load environment variables from .env ─────────────────────────────────
from dotenv import load_dotenv
load_dotenv(os.path.join(PROJECT_ROOT, '.env'))

# ── 3. Point Django at the settings module ──────────────────────────────────
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'instacode.settings')

# ── 4. Create the WSGI application ──────────────────────────────────────────
from django.core.wsgi import get_wsgi_application  # noqa: E402
application = get_wsgi_application()
