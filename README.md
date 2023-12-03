# Auto Scaling Flask App Using Any Serverless Platform
[![CI](https://github.com/nogibjj/Auto_Scaling_Flask_App_TR/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Auto_Scaling_Flask_App_TR/actions/workflows/cicd.yml)

Tianji Rao

## App
[Bartender](https://aibartender.orangecliff-0f706743.westus2.azurecontainerapps.io/)

## Video
[YouTube link](https://youtu.be/nrHcGgkP7wg)

## Overview
In this project, we've developed a Flask application that incorporates OpenAI's powerful GPT-3.5. Our AI bartender is designed to assist you in crafting a personalized cocktail experience by taking into account your available ingredients, preferences, and any specific requirements you may have. This innovative system leverages the capabilities of GPT-3.5 from OpenAI to provide a tailored and engaging cocktail customization process.

## Introduction
1. Flask App
In the `main.py`, we design routes for the index page, result page, and a predict endpoint. In the index page, users can specify their requirements in the chatbox. When they finish writing and press the button, they will be moved to the result page where the AI bartender can provide a detailed recipe.

2. HTML templates
We design two HTML templates for UI:
- `index.html`: home page
- `result.html`: result page

3. OpenAI ChatGPT 
The application interfaces with the ChatGPT 3.5 via OpenAI API. It can send a special designed prompt to the LLM and  capture results.

4. Docker Containerization
A docker file is included in this repo to containerize the Flask app

5. Azure Container Apps
We deploy the container via Azure Web App to a public endpoint. The Docker image is hosted on Azure Container Registry. The functioning container is hosted on DockerHub.


## Format, Lint, and Test
- format: `make format`
- lint: `make lint`
- test: `make test`

## Preparation
1. Clone this repo
2. Install required packages using `make install`
3. Get openai API and save it to the env file
4. Run main.py locally and test the functionality
5. Build docker image
6. Login to Azure CLI
7. Deploy azure web app
8. Use this app 

## Reference
- https://github.com/nogibjj/python-ruff-template
- https://stackoverflow.com/questions/72705471/how-to-reference-secrets-in-azure-container-apps
- https://learn.microsoft.com/en-us/azure/developer/python/tutorial-containerize-simple-web-app?tabs=web-app-flask
- https://learn.microsoft.com/en-us/azure/container-apps/scale-app?pivots=azure-cli
- https://openai.com/product
- https://openai.com/chatgpt
