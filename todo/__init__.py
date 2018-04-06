import os

from flask import Flask, send_from_directory

from todo import api


app = Flask(__name__)
app.register_blueprint(api.api)

if int(os.environ.get('FLASK_DEBUG', 0)):
    # production would serve static files from nginx/apache webserver
    basedir = os.path.join(os.path.dirname(__file__), '..')
    static_dir = os.path.join(basedir, 'static')

    @app.route('/', methods=['GET'])
    def serve_index():
        print 'SERVING STATIC'
        return send_from_directory(static_dir, 'index.html')

    @app.route('/js/<path:path>')
    def serve_js(path):
        return send_from_directory(os.path.join(static_dir, 'js'), path)

    @app.route('/css/<path:path>')
    def serve_css(path):
        return send_from_directory(os.path.join(static_dir, 'css'), path)
