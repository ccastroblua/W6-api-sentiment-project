import pandas as pd
import json
from langdetect import detect
import spacy
import re
from googletrans import Translator
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from config.configuration import engine


def tokenizer(message):
    try:
        if detect(message) == "en":
            nlp = spacy.load("en_core_web_sm")
        elif detect(message) == "es":
            nlp = spacy.load("es_core_news_sm")
        else:
            return "Couldn't recognize language"
    except:
        return "Didn't analize the message"
    
    tokens = nlp(message)
    important_words = []
    
    for word in tokens:
        if not word.is_stop:
            lemma = word.lemma_.lower().strip()
            if re.search("^[a-zA-Z]+$", lemma):
                important_words.append(lemma)
    
    return " ".join(important_words)


def translate_to_english(phrase):
    trans = Translator()

    try:
        en = trans.translate(phrase, dest="en")
        return en.text
    except:
        return phrase

    
def sentimental_analysis(phrase):
    sia = SentimentIntensityAnalyzer()
    polarity = sia.polarity_scores(phrase)
    return polarity["compound"]


def query_sia_nulls():
        query = """
        SELECT mess_id, content, emotional_value
        FROM messages
        WHERE emotional_value IS NULL;
        """
        
        sia_nulls = pd.read_sql_query(query, engine)
        return sia_nulls.to_json()


def insert_sia(mess_id, emotional_value):
    engine.execute(
        f"""
        UPDATE messages
        SET emotional_value = {emotional_value}
        WHERE mess_id = {mess_id};
        """
    )


def update_sia_nulls():
    data = query_sia_nulls()
    json_data = json.loads(data)
    df_nulls = pd.DataFrame(json_data)

    for row in df_nulls.iterrows():
        tokens = tokenizer(row[1][1])
        translation = translate_to_english(tokens)
        sia_value = sentimental_analysis(translation)

        insert_sia(row[1][0], sia_value)