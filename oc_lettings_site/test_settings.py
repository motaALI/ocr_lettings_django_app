# test_settings.py

# Import settings from main settings file
from settings import *

# Remove Whitenoise middleware from MIDDLEWARE list
MIDDLEWARE = [
    mw for mw in MIDDLEWARE if mw != "whitenoise.middleware.WhiteNoiseMiddleware"
]
