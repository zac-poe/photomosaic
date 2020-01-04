dependencies:
	@echo "May require administrative privileges"
	python3 -m pip install Pillow
	python3 -m pip install requests

test: test_dependencies
	@code_line_filter='/^\s*#/d;/^\s*$$/d'
	@echo "\033[0;32mProject contains $$(\
		find . -maxdepth 1 -name '*.py' \
			| xargs cat \
			| sed -e "$$code_line_filter" \
			| wc -l) lines of non-test/non-build code"
	@echo "    and $$(\
		find . -name '*.py' -or -name '*.sh' -or -name Makefile \
			| xargs cat \
			| sed -e "$$code_line_filter" \
			| wc -l) total lines of code\033[0m"
	@echo "Executing all tests:"
	@py.test test/*.py

test_dependencies: dependencies
	@echo "May require administrative privileges"
	python3 -m pip install pytest

sample: dependencies
	@echo "Generating sample photomosaics..."
	@test/photomosaic_test.sh
