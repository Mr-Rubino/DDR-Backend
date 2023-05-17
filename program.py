import spacy_dbpedia_spotlight
import openai


"""
    Function that takes a text and retrieves relevant dbpedia pages

    Args:
        String text: text to parse
        String language: language of the text (in ISO 639-1 standard)

    Returns:
        dict result: dict of all results

"""
def dbpedia(text, language):
    
    # Query the nlp program
    nlp = spacy_dbpedia_spotlight.create(language)
    query = nlp(text)

    result = {}
    
    for ent in query.ents:
        result[ent.text] = ent.kb_id_

    return result

"""
    Function that takes a text and retrieves relevant dbpedia pages

    Args:
        String behaviour: setup the behaviour of the AI
        String prompt: prompt to give the AI

    Returns:
        String response: AI response

"""
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

