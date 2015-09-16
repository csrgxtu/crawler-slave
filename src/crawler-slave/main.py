"""`main` is the top level module for your Flask application."""
import sys
sys.path.insert(0, 'lib')
# Import the Flask Framework
from flask import Flask, request, jsonify
app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.
from google.appengine.api import urlfetch
import validators

@app.route('/')
def index():
    data = {'err': False, 'msg': 'crawler-slave'}
    return jsonify(data)

@app.route('/url')
def get_data_by_url():
    url = request.args.get('url', '')

    data = {'err': False, 'msg': None, 'status_code': None, 'url': url, 'data': None}

    if not validators.url(url):
        data['err'] = True
        data['msg'] = 'invalid url'
        return jsonify(data)

    try:
        result = urlfetch.fetch(url)
        data['status_code'] = result.status_code
        data['data'] = result.content
    except:
        data['err'] = True
        data['msg'] = 'GAE Download Error'

    return jsonify(data)

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
