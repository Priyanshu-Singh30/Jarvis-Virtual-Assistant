import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
from openai import OpenAI
from gtts import gTTS
import pygame
import os



#  pip install pocketsphinx

recognizer = sr.Recognizer()
engine= pyttsx3.init()

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    # Initialize mixer
    pygame.mixer.init()

    # Load MP3 file (make sure the file path is correct)
    pygame.mixer.music.load("temp.mp3")

    # Play the song (loops=0 means play once, -1 means loop forever)
    pygame.mixer.music.play()

    # Keep program running until song ends
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("temp.mp3")

def aiProcess(command):
    client= OpenAI(api_key="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",
    base_url="https://openrouter.ai/api/v1"
   )   

    completion = client.chat.completions.create(
    model="mistralai/mistral-7b-instruct:free",  # free daily usage available
    messages=[{"role": "system", "content": "You are virtual assistant named jarvis skilled in general task like alexa and google cloud give short responses "},
        {"role":"user", "content": command}         
    ]
    )

    return completion.choices[0].message.content



def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https:/youtube.com")
    elif "open LinkedIn" in c.lower():
        webbrowser.open("https://LinkedIn.com")
    elif c.lower().startswith("play"):
        song= c.lower().split(" ")[1]
        link= musicLibrary.music[song]
        webbrowser.open(link)

    else:
        # let openAI handle the request
        output=aiProcess(c)
        speak(output)
    


if __name__== "__main__":
    speak("Initialise jarvis...")
    while True:
    #listen for the wake word "jarvis"
    # obtain audio from the microphone
        r = sr.Recognizer()
        
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower()=="jarvis"):
               speak("ya")
               #listen for command
               with sr.Microphone() as source:
                    print("Jarvis active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("error; {0}".format(e))
    

