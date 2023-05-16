import spacy_dbpedia_spotlight
import openai

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

