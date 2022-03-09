

all:
	poetry install

create:
	poetry run openapi-python-client generate --config config-openapi-python-client.yaml --path swagger.json
	
update:
	#poetry run openapi-python-client update --config config-openapi-python-client.yaml --path swagger.json
	poetry run openapi-python-client update --config config-openapi-python-client.yaml --path mattermost-api-reference/v4/html/static/mattermost-openapi-v4.yaml

