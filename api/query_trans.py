from fapi import InputData
import spellchecker
input_data = InputData.lower()


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

