.PHONY: clean build check publish

clean:
	rm -rf dist/ build/ *.egg-info

build: clean
	python -m build

check: build
	twine check dist/*

publish: check
	twine upload dist/*