setup:
	rm -rf dist/*
	python setup.py sdist bdist_wheel

check: dist
	twine check dist/*

upload: check
	twine upload -u __token__ -p $(PYPI_TOKEN) dist/*
