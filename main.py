import pyttsx3
import speech_recognition as sr
from translate import Translator
from langdetect import detect

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said + "\n")
        except Exception as e:
            print("Exception: " + str(e))
            speak(str(e));

    return said

# # Takes audio input from user.
# query = get_audio()
query = "नमस्ते, आप कैसे हैं"

# Detect the language of the query
detected_language = detect(query)

# invoking Translator 
translator = Translator(from_lang=detected_language, to_lang='en')

# Translating from src to dest 
text_to_translate = translator.translate(query)

# Speaks the give text.
speak(text_to_translate);

