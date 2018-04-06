# Setup
- Instal virtualenve: `pip install virtualenv` (may need to run with sudo)
- Create a virtualenv: `virtualenv venv`
- Start the virtualenv: `source venv/bin/activate`
- Install dependencies: `pip install -r requirements.txt`
- Start up the server: `export FLASK_APP=todoapp FLASK_DEBUG=1 && flask run`


# Tips
Open browser console network tab and check the `Disable cache` option otherwise
the browser will keep returning your old static files.


The app should be running in your browser at localhost:8080