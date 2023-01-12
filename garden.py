# import module
import spacy 

nlp = spacy.load("en_core_web_sm")


# List containing garden path sentences
garden_path_sentences = ["The horse raced past the barn fell.", 
"The old man the boat.", 
"The complex houses married and single soldiers and their families.",
"I told the girl the cat scratched Bill would help her.",
"The cotton clothing is made of grows in Mississippi."
]

# Iterate over the sentences and perform tokenisation
for sentence in garden_path_sentences:
    doc = nlp(sentence)
    for token in doc:
        print(token.orth_)

# Iterate over the sentences and perform entity recognition
for sentence in garden_path_sentences:
    doc = nlp(sentence)
    for ent in doc.ents:
        print(ent.text, ent.label_)

# I did not recognise what GPE meant but discovered ""GPE" stands for "Geo-Political Entity". 
# These are entities that represent countries, cities, states, or other geopolitical entities."

# My code also recognised Bill as a PERSON but I do know what a person is, so instead I looked up
# something I didn't know from the example file which was ORG, and discoverd that the ORG
# entity and found that '"ORG" stands for "organization". These are entities that represent companies, 
# institutions, agencies, or other organizations'. I find this topic quite fascinating.