import pyttsx3
import speech_recognition as sr
import openai as op


key = "insert Open AI API key here "
op.api_key = key

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
        print("Listerning...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(query)

        except Exception as e:
            print("Please repeat")
            return "None"
        return query

val = takecommand()


response = op.Completion.create(
  engine="text-davinci-001",
  prompt=val,
  temperature=0.9,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0.6,
)

response = str(response)
presponse = response.split("\n")[6]
presponse = presponse.strip( '"text": ')

print(presponse)
tell(presponse)