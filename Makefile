dependencies:
	@echo "May require administrative privileges"
	python3 -m pip install Pillow

test: test_dependencies
	@echo "\033[0;32mProject contains $$(cat *.py | sed -e '/^\s*#/d;/^\s*$$/d' | wc -l) lines of code\033[0m"
	@echo "Executing all tests:"
	@py.test *_test.py

test_dependencies:
	@echo "May require administrative privileges"
	python3 -m pip install pytest
