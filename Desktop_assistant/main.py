import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 7 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 18:
        speak("Good Afternoon")
    elif 18 <= hour < 21:
        speak("Good Evening")
    else:
        speak("Good Night")
    speak("Hello, I am your desktop assistant. How may I help you?")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Go ahead, I am listening...")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='hi-IN')
        print(f"You said: {query}")
    except Exception:
        speak("Sorry, I didn't catch that. Please say again.")
        return "None"
    return query.lower()


def main():
    wish_me()
    while True:
        query = take_command()

        if query == "none":
            continue

        elif "wikipedia" in query:
            speak("What topic should I search for on Wikipedia?")
            topic = take_command()
            if topic != "none":
                speak(f"Searching Wikipedia for {topic}")
                try:
                    summary = wikipedia.summary(topic, sentences=2)
                    speak("According to Wikipedia:")
                    print(summary)
                    speak(summary)
                except:
                    speak("Sorry, no results found on Wikipedia.")

        elif "open youtube" in query:
            speak("What would you like to watch on YouTube?")
            video = take_command()
            if video != "none":
                speak(f"Playing {video}")
                pywhatkit.playonyt(video)

        elif "open google" in query or "search on google" in query:
            webbrowser.open("https://google.com")

        elif "open stackoverflow" in query:
            webbrowser.open("https://stackoverflow.com")

        elif "open leetcode" in query:
            webbrowser.open("https://leetcode.com")

        elif "the time" in query:
            time_str = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time_str}")

        elif "open code" in query:
            code_path = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)

        elif "stop" in query or "exit" in query:
            speak("Goodbye! Have a great day.")
            break


if __name__ == "__main__":
    main()
