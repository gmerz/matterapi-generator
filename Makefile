

all:
	poetry install

create:
	poetry run openapi-python-client --config config-openapi-python-client.yaml generate --path swagger.json
	
update:
	poetry run openapi-python-client --config config-openapi-python-client.yaml update --path swagger.json

