import os
import sys
from pathlib import Path

# Determine environment
ENVIRONMENT = os.environ.get('DJANGO_ENV', 'development')

if ENVIRONMENT == 'production':
    from .production import *
else:
    from .development import *

# Add apps directory to Python path
BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(BASE_DIR / 'apps'))