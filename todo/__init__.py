import os

from flask import Flask, send_from_directory

from todo import api


app = Flask(__name__)
app.register_blueprint(api.api)

# A production build would serve static files from nginx/apache, but for
# development having flask serve them is fine.
if int(os.environ.get('FLASK_DEBUG', 0)):
    basedir = os.path.join(os.path.dirname(__file__), '..')
    static_dir = os.path.join(basedir, 'static')

    @app.route('/', methods=['GET'])
    def serve_index():
        return send_from_directory(static_dir, 'index.html', cache_timeout=-1)

    @app.route('/js/<path:path>')
    def serve_js(path):
        return send_from_directory(os.path.join(static_dir, 'js'), path, cache_timeout=-1)

    @app.route('/css/<path:path>')
    def serve_css(path):
        return send_from_directory(os.path.join(static_dir, 'css'), path, cache_timeout=-1)
