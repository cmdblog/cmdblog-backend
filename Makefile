.PHONY: check-all lint test openapi-schema.yaml


check-all: lint test

lint:
	pylint cmdblog_backend

test:
	python manage.py test

openapi-schema.yaml:
	python manage.py generateschema --file openapi-schema.yaml
