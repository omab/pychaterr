.env:
	python3 -m venv .env
	pip install -U pip
	pip install build twine

build: .env
	./.env/bin/python3 -m build 

upload: build
	./.env/bin/python3 -m twine upload dist/*