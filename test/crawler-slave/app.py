import sys
sys.path.insert(0, 'lib')
import webapp2
from google.appengine.api import urlfetch
import json
import validators

class Crawler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'application/json'

        url = self.request.get('url')

        data = {'status_code': None, 'url': url, 'err': False, 'msg': None, 'data': None}

        if not validators.url(url):
            data['err'] = True
            data['msg'] = 'invalid url'
            self.response.write(json.dumps(data))
            return

        try:
            result = urlfetch.fetch(url)
            data['status_code'] = result.status_code
            data['data'] = result.content
        except:
            data['err'] = True
            data['msg'] = 'GAE Download Error'

        self.response.write(json.dumps(data))

app = webapp2.WSGIApplication([
    ('/url', Crawler),
], debug=True)
