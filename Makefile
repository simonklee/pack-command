all: clean-pyc test

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

test:
	@nosetests -w tests

test_setup:
	@python scripts/test_setup.py

toxtest:
	@tox

pack_command/_speedups.so: pack_command/_speedups.pyx
	cython pack_command/_speedups.pyx
	python setup.py build
	cp build/*/pack_command/_speedups*.so pack_command

cybuild: pack_command/_speedups.so

.PHONY: test clean-pyc cybuild all
