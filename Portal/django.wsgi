import os
import sys

sys.path.append('/var/www/html/portal')

os.environ['PYTHON_EGG_CACHE'] = '/var/www/html/portal/.python-egg'

os.environ['DJANGO_SETTINGS_MODULE'] = 'Portal.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()