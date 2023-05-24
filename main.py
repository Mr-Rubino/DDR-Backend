from flask import Flask, request
import spacy_dbpedia_spotlight
import openai
import json
from program import dbpedia, chatgpt

# Retrieve API key from data file
file = open("/Users/rubenvandijkhuizen/OneDrive/Studie/Jaar 2/Data Driven Research/Final Project/data.json")
data = json.load(file)
file.close()
openai.api_key = data["key"]

# Start API library
app = Flask(__name__)


"""
    /summarize endpoint (POST)

    Generates a summary based on a given text

    Form Arguments:
        String text: text to retrieve dbpedia sources from

    Returns:
        JSON summary: JSON object of the generated summary

"""
@app.route('/summarize', methods=["POST"])
def summarize():

    # Get the data from the POST request
    text = request.form.get("text")

    # Prompt for AI
    gptPrompt = f'Provide a summary on the following text: \n{text}'

    # Access AI
    gptResponse = chatgpt(
        "You are a service that provides short summaries for for studying purposes",
        gptPrompt
        )
    
    # Create a JSON object for returning
    summary = {
        "response": gptResponse
    }

    return summary
    
"""
    /questions endpoint (POST)

    Generates 3 multiple choice questions based on a given text

    Form Arguments:
        String text: text to retrieve dbpedia sources from

    Returns:
        JSON questions: JSON object of the generated questions and answers

"""
@app.route('/questions', methods=["POST"])
def questions():

    # Retrieve text
    text = request.form.get("text")

    # OpenAI
    gptPrompt = f'Provide questions for the following text in JSON format: \n{text}'
    gptBehaviour = "You are a service that provides 3 multiple choice questions based on a given text Provide 3 possible answers to each question of which only one is correct. Also provide the correct answer"
    response = chatgpt(gptBehaviour, gptPrompt)
    

    return response

"""
    /wiki endpoint (POST)

    Finds dbpedia links in a given text using the NLP program

    Form Arguments:
        String text: text to retrieve dbpedia sources from
        String language: language abbreviation according to ISO 639-1

    Returns:
        JSON wikiLinks: JSON object of the found dbpedia articles

"""
@app.route("/wiki", methods=["POST"])
def wiki():
    
    # Get the data from the POST request
    text = request.form.get("text")
    language = request.form.get("language")

    # Parse text through NLP program
    wikiLinks = dbpedia(text, language)

    return wikiLinks



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)