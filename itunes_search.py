import json
import requests


__version__ = 0.3
__author__ = 'Christopher Toth'
__doc__ = """Simple wrapper over the iTunes search API"""

BASE_URL = 'https://itunes.apple.com/search'

def search(term, country='US', media='all', entity=None, attribute=None, limit=50, lang='en_us', explicit='Yes'):
 params = {k:v for k, v in locals().iteritems() if v is not None}
 response = requests.get(BASE_URL, params=params)
 response.raise_for_status()
 return json.loads(response.content)['results']


