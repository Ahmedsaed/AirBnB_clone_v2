entry_point = console.py
PY_FILES := $(shell find . -type d -name 'tests' -prune -o -type f -name '*.py' -print)
MAKEFLAGS += --silent
PYTHON := python3

all: clear_screen check_style run_tests

run:
	@$(PYTHON) $(entry_point)

run_tests:
	@$(MAKE) announce MESSAGE="Running unit tests - File Storage"
	$(PYTHON) -m unittest discover tests
	@$(MAKE) announce MESSAGE="Running unit tests - Database"
	HBNB_ENV=test HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db HBNB_TYPE_STORAGE=db $(PYTHON) -m unittest discover tests
	@$(MAKE) announce MESSAGE="Checking docstrings"
	@for file in $(PY_FILES); do \
		if ! python check_docstrings.py $$file &> /dev/null; then \
        	python ./helpers/check_docstrings.py "$$file"; \
			exit 1; \
		fi; \
    done
	@$(MAKE) announce MESSAGE="All docstrings are defined"

announce:
	@echo "------------------------------------------"
	@printf "|%*s%s%*s|\n" $$(expr 20 - $${#MESSAGE} / 2) "" "$(MESSAGE)" $$(expr 20 - $$(($${#MESSAGE} + 1)) / 2) ""
	@echo "------------------------------------------"

check_style:
	@$(MAKE) announce MESSAGE="Checking code style"
	pycodestyle --first $(entry_point) models tests && \
	($(MAKE) announce MESSAGE="Code style OK" && exit 0) || \
	($(MAKE) announce MESSAGE="Code style error" && exit 1)

clear_screen:
	clear
