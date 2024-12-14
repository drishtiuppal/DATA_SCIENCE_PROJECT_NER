import spacy

nlp = spacy.load('en_core_web_sm')

# Extract entities from the given text
def extract_entities(text):
    doc = nlp(text)
    entities = {"ORG": [], "PERSON": []}
    for ent in doc.ents:
        if ent.label_ == "ORG" and len(ent.text.split()) > 1:  
            entities["ORG"].append(ent.text)
        elif ent.label_ == "PERSON" and len(ent.text.split()) > 1: 
            entities["PERSON"].append(ent.text)
    return entities