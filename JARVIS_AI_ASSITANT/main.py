import speech_recognition as sr  # Taking voice command from the user.
import webbrowser  # For opening any URL.
import pyttsx3  # For text-to-speech.
import requests  # To fetch news.
import musicLibrary  # Music Library.
from openai import OpenAI 




recognizer = sr.Recognizer()
engine = pyttsx3.init()

newsapi = "d80d229d53f94c618919bc8bd0bd94f6"

# Text-to-Speech function
def speak(text):
    engine.say(text)
    engine.runAndWait()


def aiProcess(command):
    client = OpenAI(api_key="api-key",
    )

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content

# Processing command and perform tasks
def processCommand(c):
    c = c.lower()

    if c == "open google":
        webbrowser.open("https://google.com")

    elif c == "open youtube":
        webbrowser.open("https://youtube.com")

    elif c == "open facebook":
        webbrowser.open("https://facebook.com")

    elif c == "open linkedin":
        webbrowser.open("https://linkedin.com")

    elif c.startswith("play"):
        try:
            song = c.split(" ")[1]
            link = musicLibrary.music[song]
            if link:
                webbrowser.open(link)
                speak(f"Playing {song}")
            else:
                speak("Song not found in the library.")
        except IndexError:
            speak("Please say the song name after 'play'.")

    elif "news" in c:
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            speak("Here are the latest headlines:")
            for article in articles[:5]:  # Only speak top 5 headlines
                speak(article['title'])
        else:
            speak("Failed to fetch news.")

    else:
        #let openAI handle this.
        output = aiProcess(c)
        speak(output) 


if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        print("\nListening for wake word...")

        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)

            word = recognizer.recognize_google(audio)
            print(f"You said: {word}")

            if word.lower() == "jarvis":
                speak("Yes?")
                print("Jarvis Activated...")

                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source, duration=1)
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                    command = recognizer.recognize_google(audio)
                    print(f"Command: {command}")

                    if command.strip() != "":
                        processCommand(command)
                    else:
                        speak("I didn't catch that.")
        except sr.UnknownValueError as v:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google; {e}")
        except Exception as e:
            print(f"Error: {e}")
