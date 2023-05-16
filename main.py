from flask import Flask, request
import spacy_dbpedia_spotlight
import openai
import json

file = open("/Users/rubenvandijkhuizen/OneDrive/Studie/Jaar 2/Data Driven Research/data.json")
data = json.load(file)

openai.api_key = data["key"]

app = Flask(__name__)

@app.route('/ocr', methods=["POST", "GET"])
def ocr():

    if request.method == "POST":
    
        text = request.form.get("text")
        language = request.form.get("language")

        nlp = spacy_dbpedia_spotlight.create(language)
        query = nlp(text)
        
        result = {}

        for ent in query.ents:
            result[ent.text] = ent.kb_id_

        return result
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)