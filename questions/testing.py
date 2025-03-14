import spacy

with open('questions/txts/HP_1ru.txt', 'r') as file:
    text_ru = file.read()

doc = spacy(text_ru)
print(doc.ents)
