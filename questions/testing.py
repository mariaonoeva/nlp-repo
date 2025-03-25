import spacy

nlp = spacy.load("ru_core_news_sm")
with open('/Users/maria.onoeva/Desktop/new_folder/GitHub/nlp-repo/questions/txts/HP_1ru.txt', 'r') as file:
    text_ru = file.read()

doc = nlp(text_ru)
print(text_ru)
