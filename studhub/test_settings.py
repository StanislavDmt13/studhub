from .settings import *

DEBUG = True
STATIC_ROOT = None

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "frontend/static/"),
]
