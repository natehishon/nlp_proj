import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property

import os
from app import app

app.run(port=5000)

# To Run:
# python run.py
# or
# python -m flask run
