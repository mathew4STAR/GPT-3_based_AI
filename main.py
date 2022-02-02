import pyttsx3
import speech_recognition as sr
import openai as op
import os


op.api_key = os.getenv("OPENAI_API_KEY")

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def tell(text):
    engine.say(text)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(query)

        except Exception as e:
            print("Please repeat")
            return "Nothing"
        return query


while True:
    query = takecommand()
    response = op.Completion.create(
    engine="text-davinci-001",
    prompt="The following is a conversation with an AI friend. The friend is helpful, creative, clever, and very friendly.\n\nHuman: " + query + "\nAI: ",
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    )

    presponse= response["choices"][0]["text"]
    print(presponse)
    tell(presponse)