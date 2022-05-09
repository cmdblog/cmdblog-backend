<<<<<<< HEAD
.PHONY: check-all lint test openapi-schema.yaml
=======
.PHONY: check-all lint test gen-schema
>>>>>>> 068519e (make targetを用意)


check-all: lint test

lint:
	pylint cmdblog_backend

test:
	python manage.py test

<<<<<<< HEAD
openapi-schema.yaml:
	python manage.py generateschema --file openapi-schema.yaml
	sed -i "s/version: ''/version: '$(TAG)'/" openapi-schema.yaml
=======
gen-schema:
	python manage.py generateschema --file openapi-schema.yaml
>>>>>>> 068519e (make targetを用意)
