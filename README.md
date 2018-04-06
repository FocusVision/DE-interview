# Setup
- Install virtualenv: `pip install virtualenv` (may need to run with sudo)
- Create a virtualenv: `virtualenv venv`
- Start the virtualenv: `source venv/bin/activate`
- Install dependencies: `pip install -r requirements.txt`
- Start up the server: `export FLASK_APP=todo/__init__.py FLASK_DEBUG=1 && flask run`


# Running Unit Tests
- Make sure your virtualenv is running
- From the project directory run `python -m unittest discover`


# Tips
Open browser console network tab and check the `Disable cache` option otherwise
the browser will keep returning your old static files.


# Resources
- Flask API docs http://flask.pocoo.org/docs/0.12/api/
- JQuery API docs https://api.jquery.com/
- Python unittest docs https://docs.python.org/2/library/unittest.html
