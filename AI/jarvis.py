import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import pyaudio
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes


engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty('voice',voices[1].id)
newVoiceRate=200                  #for speech rate
engine.setProperty('rate',newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def time(): 
   Time= datetime.datetime.now().strftime('%I:%M:%S')
   speak("The current time is")
   speak(Time)

def date():
   year=int(datetime.datetime.now().year)
   month=int(datetime.datetime.now().month)
   day=int(datetime.datetime.now().day)
   speak("The current date is")
   speak(day)
   speak(month)
   speak(year)

def wishme():
   hour=datetime.datetime.now().hour
   if hour<12 and hour>=0:
    speak("Good Morning")
   if hour>12 and hour<=18:
    speak("Good Afternoon")  
   if hour>18 and hour<=24:
    speak("Good Evening")
   else:
    speak("Good Night")    
 
   speak("Welcome back sir!")
   time()
   date()
         
   speak("Jarvis at you service. How can i help you?")

def takeCommand():
    r=sr.Recognizer()
    m=sr.Microphone()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        sr.Microphone(device_index=None,sample_rate=16000,  chunk_size=1024)
    try:
        print("Recognizing")
        query=r.recognize_google(audio)      
        print(query)
    except Exception as e:
        print(e)
        speak("Speak again please..")
        return "None"

    return query   

def sendemail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("deveshdutt16")
def screenshot():
    img=pyautogui.screenshot()
    img.save("D:\\AI\\ss.png")    
def cpu():
    usage=str(psutil.cpu_percent())  
    speak("CPU is at" + usage)  
    battery= psutil.sensors_battery
    speak("Battery is at")
    speak(battery.percent)








if __name__=="__main__":

     wishme()

     while True:
               query= takeCommand().lower()
               print(query)

               if "Time" in query:
                   time()
               elif "Date" in query:
                   date()
               elif "offline" in query:
                   quit()  
               elif "wikipedia" in query:
                    speak("Searching..")
                    query =query.replace("wikipedia",'')
                    result= wikipedia.summary(query,sentences = 2)
                    speak(result)
               elif "send email" in query:
                   try:
                       speak("What should i say?")      
                       content=takeCommand()
                       to="deveshdutt1619@gmail.com"
                       sendemail(to,content)
                       speak("Email sent succesfuly")
                       speak(content)
                   except Exception as e:
                       speak(e)
                       speak("Unable to send email")
               elif "search in chrome" in query:
                   speak("What should i search??")
                   chromepath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
                   search = takeCommand().lower()
                   wb.get(chromepath).open_new_tab(search+".com")
               elif "shutdown" in query:
                   os.system("shutdown /s /t 1")
               elif "restart" in query:
                   os.system("shutdown /r /t 1")   
               elif "play songs" in query:
                   songs_dir="D:\\New folder"
                   songs= os.listdir(songs_dir)    
                   os.startfile(os.path.join(songs_dir,songs[0]))
               elif "remember that" in query:
                   speak("what should i remember")
                   data= takeCommand()
                   speak("You said me to remember" + data)
                   remember= open("data.txt","w")
                   remember.write(data)
                   remember.close()    
               elif "do you know anything" in query:
                   remember= open("data.txt","r")
                   speak("You said me to remember that" + remember.read())
               elif "screenshot" in query:
                   screenshot()
                   speak("Done!")
               elif "cpu" in query:
                     cpu() 
               elif "joke" in query:
                      joke=pyjokes.get_joke(language='en', category= 'neutral')
                      speak(joke)        








       
