# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, 'lib')
from flask import Flask, request, jsonify
app = Flask(__name__)
from google.appengine.api import urlfetch
from google.appengine.api import app_identity
import validators
import chardet

@app.route('/')
def index():
    APPID = app_identity.get_application_id()
    data = {'err': False, 'msg': 'crawler-slave', 'status_code': None, 'url': None, 'data': None, 'appid': APPID, 'Github': 'https://github.com/csrgxtu/crawler-slave'}
    return jsonify(data)

@app.route('/url')
def get_data_by_url():
    APPID = app_identity.get_application_id()
    url = request.args.get('url', '')

    data = {'err': False, 'msg': None, 'status_code': None, 'url': url, 'data': None, 'appid': APPID, 'Github': 'https://github.com/csrgxtu/crawler-slave'}

    if not validators.url(url):
        data['err'] = True
        data['msg'] = 'invalid url'
        data['status_code'] = 404
        return jsonify(data)

    # try:
    result = urlfetch.fetch(url)
    data['status_code'] = result.status_code
    data['data'] = result.content.decode(chardet.detect(result.content)['encoding'], 'ignore').encode('utf-8')
    # except:
    #     data['err'] = True
    #     data['msg'] = 'GAE Download Error'
    #     data['status_code'] = 500

    return jsonify(data)

@app.errorhandler(404)
def page_not_found(e):
    APPID = app_identity.get_application_id()
    data = {'err': False, 'msg': 'crawler-slave', 'status_code': None, 'url': None, 'data': None, 'appid': APPID, 'Github': 'https://github.com/csrgxtu/crawler-slave'}
    return jsonify(data)


@app.errorhandler(500)
def application_error(e):
    APPID = app_identity.get_application_id()
    data = {'err': False, 'msg': 'crawler-slave', 'status_code': None, 'url': None, 'data': None, 'appid': APPID, 'Github': 'https://github.com/csrgxtu/crawler-slave'}
    return jsonify(data)
