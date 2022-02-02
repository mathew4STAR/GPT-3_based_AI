# GPT-3_based_AI
A simple program that gives a voice to open-ai's gpt-3 model. 

The program uses speech recognition module (with google speech recognition) to recognize your voice, and passes reading to Open-AI's API, the reply the API gives is fed into the
another module called pyttsx3 which says the reply out loud.

It uses Open-AI's davinci model, though this can be modified in the code.

You will also have to sign up to Open-AI, to generate an API key, and then create an Environment variable called `OPENAI_API_KEY` with your API key.
