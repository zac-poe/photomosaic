dependencies:
	@echo "May require administrative privileges"
	python3 -m pip install Pillow

test: test_dependencies
	@echo "\033[0;32mProject contains $$(\
		find . -name '*.py' -a -not -name '*_test.py' \
			| xargs cat \
			| sed -e '/^\s*#/d;/^\s*$$/d' \
			| wc -l) lines of non-test code\033[0m"
	@echo "Executing all tests:"
	@py.test test/*.py

test_dependencies:
	@echo "May require administrative privileges"
	python3 -m pip install pytest
