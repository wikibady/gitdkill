import os  
import sys  
root = os.path.dirname(__file__)                                             
sys.path.insert(0, os.path.join(root, '..', 'django'))                
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bdlibsaas.settings")  
  
  
from django.core.wsgi import get_wsgi_application  
application = get_wsgi_application() 