install:
	pip install virtualenv
	test -d venv || virtualenv venv
	venv/bin/pip install -r requirements.txt

test:
	venv/bin/python -m unittest discover

run:
	export FLASK_DEBUG=1 FLASK_APP=todo/__init__.py && venv/bin/python -m flask run --port 8000
