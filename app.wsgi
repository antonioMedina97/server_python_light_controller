#! /usr/bin/python3.8

import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/server_python_light_controller')
from app import app as application
application.secret_key = '1234'
