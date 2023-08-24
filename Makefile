entry_point = console.py
PY_FILES := $(shell find . -type d -name 'tests' -prune -o -type f -name '*.py' -print)
MAKEFLAGS += --silent
PYTHON := python3

all: clear_screen check_style run_tests

run:
	@$(PYTHON) $(entry_point)

run_db:
	HBNB_MYSQL_USER=root HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=127.0.0.1 HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db $(PYTHON) $(entry_point)

run_tests:
	@$(MAKE) announce MESSAGE="Running unit tests - File Storage"
	$(PYTHON) -m unittest discover tests
	@$(MAKE) announce MESSAGE="Running unit tests - Database"
	HBNB_MYSQL_USER=root HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=127.0.0.1 HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db $(PYTHON) -m unittest discover tests
	@$(MAKE) announce MESSAGE="Checking docstrings"
	echo "checking [$(PY_FILES)]"
	@for file in $(PY_FILES); do \
		if ! python ./helpers/check_docstrings.py $$file >/dev/null; then \
			echo "asdasd"; \
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

setup_db:
	@$(MAKE) announce MESSAGE="Setting up MySql database"
	docker-compose up -d
	sleep 60
	@$(MAKE) announce MESSAGE="Creating databases and users for development"
	cat setup_mysql_dev.sql | mysql -h 127.0.0.1 -P 3306 -u root -phbnb_dev_pwd
	sleep 5
	mysql -h 127.0.0.1 -P 3306 -u root -phbnb_dev_pwd -e "SELECT user FROM mysql.user;"
	@$(MAKE) announce MESSAGE="Creating databases and users for testing"
	cat setup_mysql_test.sql | mysql -h 127.0.0.1 -P 3306 -u root -phbnb_dev_pwd
	sleep 5
	mysql -h 127.0.0.1 -P 3306 -u root -phbnb_dev_pwd -e "SELECT user FROM mysql.user;"

reset_db:
	@$(MAKE) announce MESSAGE="Resetting database"
	docker-compose down -v
	@$(MAKE) setup_db

destroy_db:
	@$(MAKE) announce MESSAGE="Destroying database"
	docker-compose down -v
