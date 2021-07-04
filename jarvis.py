import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)

engine.setProperty('voice' , voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good morning!")

    elif hour >= 12 and hour <= 18:
        speak("Good afternoom!")
    
    else :
        speak("Good evevning!")

    speak("I am Jarvis Sir. Please tell me how may I help you")

def takecommand():
    # it takes microphone input from thr user and returns string output from the user.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try :
        print("Recognizing....")
        query = r.recognize_google(audio , language='en-in')
        print(f"User said : {query}\n")

    except Exception as e :
        # print(e)

        print("Say that again please...")
        return "None"

    return query

def sendEmail(to , content):
    server = smtplib.SMTP('smtb.gmail.com' , 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com' , 'your-password')
    server.sendmail('youremail@gmail.com' , to , content)
    server.close()
 
if __name__ == "__main__":
    wishMe()
    # while True:
    if 1:
        query = takecommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia" , "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favourite Songs2'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime  = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\adil\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "harryyourEmail@gamail.com"
                sendEmail(to , content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)



                speak("Sorry my friend Aadil bhai . I am not able to send this emial.")
        
        elif 'wish alayna' in query:
            speak("Happy Birthday Alayna")

        elif 'Please quit' in query:
           
            exit()