from flask import Flask, request
import spacy_dbpedia_spotlight
import openai
import json

file = open("/Users/rubenvandijkhuizen/OneDrive/Studie/Jaar 2/Data Driven Research/Final Project/data.json")
data = json.load(file)

openai.api_key = data["key"]

app = Flask(__name__)

@app.route('/ocr', methods=["POST"])
def ocr():

    # Get the data from the POST request
    text = request.form.get("text")
    language = request.form.get("language")

    wikiLinks = dbpedia(text, language)

    gptPrompt = f'Provide a summary on the following text: \n "{text}"'

    gptResponse = chatgpt(
        "You are a service that provides short summaries for for studying purposes",
        gptPrompt
        )
    
    res = {
        "summary": gptResponse,
        "wikiLinks": wikiLinks
    }

    return res
    


def dbpedia(text, language):
    
    # Query the nlp program
    nlp = spacy_dbpedia_spotlight.create(language)
    query = nlp(text)

    result = {}
    
    for ent in query.ents:
        result[ent.text] = ent.kb_id_

    return result



def chatgpt(behaviour ,prompt):
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", 
                                                messages = [
                                                    {
                                                        "role": "system",
                                                        "content": behaviour
                                                    },
                                                    {
                                                        "role": "user", 
                                                        "content": prompt
                                                    }

                                                ], 
                                                temperature=0)
    
    return response["choices"][0]["message"]["content"]


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)