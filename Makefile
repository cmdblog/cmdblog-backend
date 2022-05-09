.PHONY: check-all lint test gen-schema


check-all: lint test

lint:
	pylint cmdblog_backend

test:
	python manage.py test

gen-schema:
	python manage.py generateschema --file openapi-schema.yaml
