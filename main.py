import pyttsx3  # text to speech
import datetime  # time
import speech_recognition as sr  # listening
import wikipedia
import smtplib # to be able to access servers and send emails
import webbrowser as wb # browser
import os # operating system
import pyautogui # control pc operations
import psutil # monitoring pc
import pyjokes # jokes library


engine = pyttsx3.init()


def speak(audio):  # speak  block
    engine.say(audio)
    engine.runAndWait()


def time(): # time block
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)


def date(): # date block
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)


def wishme(): # greeting block
    speak("welcome back mohamed")
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("good morning")
    elif hour >= 12 and hour < 18:
        speak("good after noon")
    elif hour >= 18 and hour < 24:
        speak("good evening")
    else:
        speak("good night mohamed")
    speak("kirito at your service please tell me how can i help you")


def takeCommand(): # take user voice input
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("say that again please")

        return "none"

    return query


def sendEmail(to, content): # send emails block  not working probably google it
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mohmad1234567625@gmail.com', '@kirito99')
    server.sendmail('mohmad1234567625@gmail.com', to, content)
    server.close()


def screenShot(): # normal screen shot block
    img = pyautogui.screenshot()
    img.save("C:\\Users\kirito\PycharmProjects\jarvis\\ss.png")


def cpu(): # tells you cpu and battery usage
    usage = str(psutil.cpu_percent())
    speak(f"cpu is at{usage}")
    battery = psutil.sensors_battery()
    speak(f"battery is at")
    speak(battery.percent)


def jokes(): # jokes block
    speak(pyjokes.get_joke())


if __name__ == "__main__":   # the main body of the script it controls the other functions by user voice input
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query: # then here compare the input with the  built-in text
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("searching......")
            query = query.replace("wikipedia", "") # here if the user say wikipedia and  dogs AI search wiki for dogs
            result = wikipedia.summary(query, sentences=2) # gives you the results to a certain limit
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = "msaifeldin46@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
                speak(content)
            except Exception as e:
                print(e)
                speak("unable to send the email")
        elif 'search' in query:
            speak("what should i search?")
            chromepath = 'C:\Program Files\Google\Chrome\Application/chrome.exe %s'
            search = takeCommand().lower
            wb.get(chromepath).open_new_tab(f'{search}.com')
        elif 'logout' in query:
            os.system("shutdown -1")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'play music' in query:
            musics_dir = 'C:\\Users\kirito\Desktop\music'
            musics = os.listdir(musics_dir)
            os.startfile(os.path.join(musics_dir, musics[0]))
        elif 'remember that' in query:
            speak("what should i remember?")
            data = takeCommand()
            speak(f"you asked me to remember{data}")
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()
        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak(f"you asked me to remember that{remember.read()}")
        elif 'screenshot' in query:
            screenShot()
            speak("your screen shot has been taken")
        elif 'pc' in query:
            cpu()
        elif 'joke' in query:
            jokes()
        elif 'offline' in query:
            quit()
