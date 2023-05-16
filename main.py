from flask import Flask, request
import spacy_dbpedia_spotlight
import openai
import json

file = open("/Users/rubenvandijkhuizen/OneDrive/Studie/Jaar 2/Data Driven Research/Final Project/data.json")
data = json.load(file)

openai.api_key = data["key"]

app = Flask(__name__)

@app.route('/summarize', methods=["POST"])
def ocr():

    # Get the data from the POST request
    text = request.form.get("text")
    language = request.form.get("language")

    wikiLinks = dbpedia(text, language)

    gptPrompt = f'Provide a summary on the following text: \n{text}'

    gptResponse = chatgpt(
        "You are a service that provides short summaries for for studying purposes",
        gptPrompt
        )
    
    res = {
        "summary": gptResponse,
        "wikiLinks": wikiLinks
    }

    return res
    
@app.route('/wiki', methods=["POST"])
def wiki():

    text = request.form.get("text")

    gptPrompt = f'Provide questions for the following text: \n{text}'

    gptBehaviour = "You are a service that provides 3 multiple choice questions based on a given text Provide 3 possible answers to each question of which only one is correct. Also provide the correct answer"

    response = chatgpt(gptBehaviour, gptPrompt)

    lines = response.split("\n")

    questions = {
        "question_1": {
            "question": lines[0].split(".")[1],
            "A": lines[1].split(") ")[1],
            "B": lines[2].split(") ")[1],
            "C": lines[3].split(") ")[1],
            "correctAnswer": lines[4].split()[2][:1],
            "correctAnswerExpl": lines[4].split(")")[1]
        },
        "question_2": {
            "question": lines[6].split(".")[1],
            "A": lines[7].split(") ")[1],
            "B": lines[8].split(") ")[1],
            "C": lines[9].split(") ")[1],
            "correctAnswer": lines[10].split()[2][:1],
            "correctAnswerExpl": lines[10].split(")")[1]
        },
        "question_3": {
            "question": lines[12].split(".")[1],
            "A": lines[13].split(") ")[1],
            "B": lines[14].split(") ")[1],
            "C": lines[15].split(") ")[1],
            "correctAnswer": lines[16].split()[2][:1],
            "correctAnswerExpl": lines[16].split(")")[1]
        }
    }

    return questions



    
    

    

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