import webapp2
import json

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'application/json'
        data = {'name': 'archer', 'age': 22, 'err': False}
        self.response.write(json.dumps(data))

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
