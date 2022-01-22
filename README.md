# matterapi-generator

This is a purpose-specific fork of [openapi-python-client](https://github.com/openapi-generators/openapi-python-client) to create a client for the mattermost api.

It includes changes to create a more object oriented client more similar to existing python mattermost clients and utilises pydantic to create data models.


This generator exists to make automatic changes to [MatterApi](https://github.com/gmerz/MatterApi)

## Usage

To make changes to MatterApi endpoint and/or update after updates to the Mattermost Api reference currently you need to perform the following steps

+ Clone this repository and the  MatterApi repository to the same folder 
  - you might to create your own fork of MatterApi and create a branch in the repository
  to be able to create a pull request for the original library
+ get the `swagger.json` file for the current version of the mattermost api and place it in the `matterapi-generator` folder
+ run `make update` inside the `matterapi-generator` folder
+ push the changes for MatterApi and/or create a pull request

