import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import logging
import os

# Initialize the recognizer
recognizer = sr.Recognizer()
microphone = sr.Microphone()

translator = Translator()

def recognize_speech():
    with microphone as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def translate_text(text):
    translated = translator.translate(text, src='auto', dest='en')
    return translated.text

def speak_text(text):
    tts = gTTS(text=text, lang='en')
    tts.save("translated_text.mp3")
    os.system("mpg321 translated_text.mp3")  # Use 'mpg321' for Raspberry Pi audio playback

logging.basicConfig(filename='translation_errors.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    try:
        speech = recognize_speech()
        if speech:
            translated_text = translate_text(speech)
            print("Translated:", translated_text)
            speak_text(translated_text)
    except Exception as e:
        error_msg = f"Error occurred: {str(e)}"
        print(error_msg)
        logging.error(error_msg)  # Log the error to the file
