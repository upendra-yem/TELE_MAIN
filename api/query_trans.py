from openai import api_key
from llm_rewriter import query_rewriter_prompt
from fapi import InputData
import spellchecker
input_data = InputData.lower()
from openai import OpenAI

Domain_words = {
    "Vehicle": ["lorry", "truck"],
    "Telematics": ["gps", "tracking", "location"],
    "Maintenance": ["repair", "service", "inspection"],
    "Driver": ["operator", "chauffeur"],
    "Fuel": ["gasoline", "diesel", "petrol"],
    "Engine": ["motor", "powertrain"],
    "Speed": ["velocity", "pace"],
    "Braking": ["stopping", "deceleration"],
    "Acceleration": ["speeding up", "throttle"],
    "Idling": ["stationary", "inactive"],
    "Mileage": ["distance traveled", "odometer"],
    "Geofence": ["virtual boundary", "location-based alert"],
    "Alerts": ["notifications", "warnings"],
    "Reports": ["summaries", "analytics"],
    "Data": ["information", "statistics"]
}

def spell_correct(sentence):
    spell = spellchecker.SpellChecker()
    corrected_words = []
    for word in sentence.split():
        corrected_word = spell.correction(word)
        corrected_words.append(corrected_word)
    return ' '.join(corrected_words)

input_data = spell_correct(input_data)
def map_domain(input_data):
    l=[]
    words = input_data.split()
    for word in words:
        found = False
        for key, synonyms in Domain_words.items():
            if word == key.lower() or word in synonyms:
                l.append(key)
                found = True
                break

        if not found:
            l.append(word)
    return 
def rewrite_query(input_data):
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages = [
            {"role": "system", "content": "You are an intelligent Query Rewriter for an AI-powered Fleet Intelligence Platform."},
            {"role": "user", "content": query_rewriter_prompt.format(input_data=input_data)}
        ]
    )

    return response.choices[0].message
