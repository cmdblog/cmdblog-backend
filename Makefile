.PHONY: check-all lint test


check-all: lint test

lint:
	pylint cmdblog_backend

test:
	python manage.py test
