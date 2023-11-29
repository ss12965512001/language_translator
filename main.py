from translate import Translator

languages = {
	"afrikaans" : "af",
	"albanian" : "sq",
	"amharic" : "am",
	"arabic" : "ar",
	"armenian" : "hy",
	"azerbaijani" : "az",
	"basque" : "eu",
	"belarusian" : "be",
	"bengali" : "bn",
	"bosnian" : "bs",
	"bulgarian" : "bg",
	"catalan" : "ca",
	"cebuano" : "ceb",
	"chichewa" : "ny",
	"chinese (simplified)" : "zh-cn",
	"chinese (traditional)" : "zh-tw",
	"corsican" : "co",
	"croatian" : "hr",
	"czech" : "cs",
	"danish" : "da",
	"dutch" : "nl",
	"english" : "en",
	"esperanto" : "eo",
	"estonian" : "et",
	"filipino" : "tl",
	"finnish" : "fi",
	"french" : "fr",
	"frisian" : "fy",
	"galician" : "gl",
	"georgian" : "ka",
	"german" : "de",
	"greek" : "el",
	"gujarati" : "gu",
	"haitian creole" : "ht",
	"hausa" : "ha",
	"hawaiian" : "haw",
	"hebrew" : "iw",
	"hebrew" : "he",
	"hindi" : "hi",
	"hmong" : "hmn",
	"hungarian" : "hu",
	"icelandic" : "is",
	"igbo" : "ig",
	"indonesian" : "id",
	"irish" : "ga",
	"italian" : "it",
	"japanese" : "ja",
	"javanese" : "jw",
	"kannada" : "kn",
	"kazakh" : "kk",
	"khmer" : "km",
	"korean" : "ko",
	"kurdish (kurmanji)" : "ku",
	"kyrgyz" : "ky",
	"lao" : "lo",
	"latin" : "la",
	"latvian" : "lv",
	"lithuanian" : "lt",
	"luxembourgish" : "lb",
	"macedonian" : "mk",
	"malagasy" : "mg",
	"malay" : "ms",
	"malayalam" : "ml",
	"maltese" : "mt",
	"maori" : "mi",
	"marathi" : "mr",
	"mongolian" : "mn",
	"myanmar (burmese)" : "my",
	"nepali" : "ne",
	"norwegian" : "no",
	"odia" : "or",
	"pashto" : "ps",
	"persian" : "fa",
	"polish" : "pl",
	"portuguese" : "pt",
	"punjabi" : "pa",
	"romanian" : "ro",
	"russian" : "ru",
	"samoan" : "sm",
	"scots gaelic" : "gd",
	"serbian" : "sr",
	"sesotho" : "st",
	"shona" : "sn",
	"sindhi" : "sd",
	"sinhala" : "si",
	"slovak" : "sk",
	"slovenian" : "sl",
	"somali" : "so",
	"spanish" : "es",
	"sundanese" : "su",
	"swahili" : "sw",
	"swedish" : "sv",
	"tajik" : "tg",
	"tamil" : "ta",
	"telugu" : "te",
	"thai" : "th",
	"turkish" : "tr",
	"ukrainian" : "uk",
	"urdu" : "ur",
	"uyghur" : "ug",
	"uzbek" : "uz",
	"vietnamese" : "vi",
	"welsh" : "cy",
	"xhosa" : "xh",
	"yiddish" : "yi",
	"yoruba" : "yo",
	"zulu" : "zu",
}

def print_languages():
    print("Available Languages:")
    for index, lang_name in enumerate(languages, start=1):
        print(f"{index}. {lang_name}")

def get_language_code(lang_name):
    return languages.get(lang_name.lower())

# Input from the user
query = input("Enter the text to translate: ")

print_languages()

# Choose the target language from the list
while True:
    choice = input("Choose the number corresponding to the target language: ")
    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(languages):
            target_lang_name = list(languages.keys())[choice - 1]
            break
    print("Invalid choice. Please enter a valid number.")

source_lang_code = get_language_code("english")  # Set source language as English
target_lang_code = get_language_code(target_lang_name)

if source_lang_code and target_lang_code:
    # invoking Translator 
    translator = Translator(from_lang=source_lang_code, to_lang=target_lang_code)

    # Translating from src to dest 
    text_to_translate = translator.translate(query)

    print(f"Translation from 'English' ({source_lang_code}) to '{target_lang_name}' ({target_lang_code}):")
    print(f"Translate '{query}' here using your preferred translation method.")
    print(text_to_translate)
else:
    print("Invalid language names entered. Please check the language names and try again.")
