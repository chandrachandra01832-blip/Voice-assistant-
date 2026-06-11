import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
engine = pyttsx3.init()
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()
recognizer = sr.Recognizer()
def listen():
    with sr.Microphone() as source:
        print("Listening...")

        # Reduce noise
        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        command = command.lower()

        print("You said:", command)
        return command

    except sr.UnknownValueError:
        speak("Sorry, I did not understand.")
        return ""

    except sr.RequestError:
        speak("Internet connection error.")
        return ""

def run_assistant():
    speak("Hello! I am your voice assistant.")

    while True:
        command = listen()

        if "hello" in command:
            speak("Hello, how can I help you?")

        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {current_time}")
        elif "open youtube" in command or "youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")
        elif "open google" in command or "google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
        elif "open facebook" in command or "facebook" in command:
            speak("Opening Facebook")
            webbrowser.open("https://www.facebook.com")
        elif "open snapchat" in command or "Snapchat" in command:
            speak("Opening Snapchat")
            webbrowser.open("https://www.snapchat.com")
        elif "open instagram" in command or "Instagram" in command:
            speak("Opening Instagram")
            webbrowser.open("https://www.instagram.com")
        elif "open photoshop" in command or "photoshop" in command:
            speak("Opening photoshop app")
            webbrowser.open("https://www.inshot.com")
        elif "whatsapp" in command or "whatsapp" in command:
            speak("Opening Whatsapp")
            webbrowser.open("https://www.whatsapp.com")

        elif "exit" in command or "stop" in command:
            speak("Goodbye!")
            break

        elif command != "":
            speak("I can help with simple commands.")

# Start assistant
run_assistant()
