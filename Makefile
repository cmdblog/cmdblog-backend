.PHONY: check-all lint test openapi-schema.yaml set-version


check-all: lint test

lint:
	pylint cmdblog_backend

test:
	python manage.py test

openapi-schema.yaml:
	python manage.py generateschema --file openapi-schema.yaml
	sed -i "s/version: ''/version: '$(TAG)'/" openapi-schema.yaml

set-version:
	sed -i 's/__version__ = ".*"/__version__ = "$(TAG)"/' cmdblog_backend/_version.py
