from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv
import json
import requests
import time

load_dotenv()

app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = os.environ["OPENAI_API_KEY"]

# Initialize conversation list
conversation = [
    {
        "role": "system",
        "content": "You are an assistant with knowledge in every domain, and you also have live information about everything",
    }
]

# Function definitions


@app.route("/")
def index():
    return render_template("index.html")


def get_current_weather(location):
    """Get the current weather in a given location"""
    url = "https://ai-weather-by-meteosource.p.rapidapi.com/find_places"

    querystring = {"text": location, "language": "en"}

    headers = {
        "X-RapidAPI-Key": "a03bc80604msh28ba8479f7aa165p1c3d47jsn141e0833430f",
        "X-RapidAPI-Host": "ai-weather-by-meteosource.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()


def get_stock_info(query):
    """Get stock info based on the query"""
    url = "https://bloomberg-market-and-financial-news.p.rapidapi.com/market/auto-complete"

    querystring = {"query": query}

    headers = {
        "X-RapidAPI-Key": "a03bc80604msh28ba8479f7aa165p1c3d47jsn141e0833430f",
        "X-RapidAPI-Host": "bloomberg-market-and-financial-news.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()


def search_on_google(query):
    url = "https://google-search72.p.rapidapi.com/search"

    querystring = {"q": query, "gl": "in", "lr": "lang_en", "num": "2", "start": "0"}

    headers = {
        "X-RapidAPI-Key": "a03bc80604msh28ba8479f7aa165p1c3d47jsn141e0833430f",
        "X-RapidAPI-Host": "google-search72.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=querystring)
    print(response.json())
    return response.json()


@app.route("/get_response", methods=["POST"])
def get_response():
    functions = [
        {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    },
                },
                "required": ["location"],
            },
        },
        {
            "name": "get_stock_info",
            "description": "Get the current price of a stock",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Name of the company, stock, organization",
                    },
                },
                "required": ["query"],
            },
        },
        {
            "name": "search_on_google",
            "description": "Search on google",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Query that needs to be searched on internet",
                    },
                },
                "required": ["query"],
            },
        },
    ]
    # Get user input from the form
    user_input = request.form["user_input"]

    # Append user input to conversation
    conversation.append({"role": "user", "content": f"{user_input}"})

    # Get response from OpenAI API
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        temperature=0.0,
        messages=conversation,
        functions=functions,
        function_call="auto",
    )

    if completion.choices[0].message["content"]:
        return {"response": completion.choices[0].message["content"]}

    else:
        response = completion.choices[0].message

        function_name = response["function_call"]["name"]
        print(function_name)
        if function_name == "get_current_weather":
            location = eval(response["function_call"]["arguments"])["location"]

            conversation.append(response)  # extend conversation with assistant's reply

            conversation.append(
                {"role": "function", "name": function_name, "content": location}
            )

            second_response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0613", messages=conversation, functions=functions
            )
            return {"response": second_response.choices[0].message["content"]}

        if function_name == "get_stock_info":
            query = eval(response["function_call"]["arguments"])["query"]

            conversation.append(response)  # extend conversation with assistant's reply

            conversation.append(
                {"role": "function", "name": function_name, "content": query}
            )

            second_response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0613", messages=conversation, functions=functions
            )
            return {"response": second_response.choices[0].message["content"]}

        if function_name == "search_on_google":
            query = eval(response["function_call"]["arguments"])["query"]

            conversation.append(response)  # extend conversation with assistant's reply

            conversation.append(
                {"role": "function", "name": function_name, "content": query}
            )

            second_response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0613", messages=conversation, functions=functions
            )
            return {"response": second_response.choices[0].message["content"]}

    return {"response": "ERROR OCCURED"}


if __name__ == "__main__":
    app.run(debug=True)
