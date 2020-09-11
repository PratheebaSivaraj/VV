import tkinter as tk
from tkinter import messagebox
import face_recognition
import cv2 
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import json
import re
import requests
import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from bs4 import BeautifulSoup
import win32com.client as wincl
import win32api, fnmatch
from tkinter import filedialog
import shutil
import sqlite3
from sqlite3 import Error
cpwd=os.getcwd()
def VirtualAss():
     while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant G-one is shutting down,Good bye')
            return
        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)
        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")
        elif "weather" in statement:
            api_key="d0943fa08be5740614cb752d844a0827"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            print(x)
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))
            else:
                speak(" City Not Found ")
        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am G-one version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')
        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Priya")
            print("I was built by Priya")
        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif "camera" in statement or "take a photo" in statement:
            cam = cv2.VideoCapture(0)
            cv2.namedWindow("test")
            img_counter = 0
            speak("Esc to close and space bar to take a snap")
            while True:
                ret, frame = cam.read()
                if not ret:
                    print("failed to grab frame")
                    break
                cv2.imshow("test", frame)
                k = cv2.waitKey(1)
                if k%256 == 27:
                    # ESC pressed        aq
                    speak("Escape hit, closing...")
                    break
                elif k%256 == 32:
                    # SPACE pressed
                    img_name = "opencv_frame_{}.jpg".format(img_counter)
                    cv2.imwrite(img_name, frame)
                    speak("{} written!".format(img_name))
                    img_counter += 1
            cam.release()
            cv2.destroyAllWindows()

        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)
        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])
        elif 'what\'s up' in statement:
            speak('Just doing my thing')
        elif 'joke' in statement:
            res = requests.get('https://icanhazdadjoke.com/',headers={"Accept":"application/json"})
            if res.status_code == requests.codes.ok:
                speak(str(res.json()['joke']))
            else:
                speak('oops!I ran out of jokes')
        elif 'mail' in  statement:
            sender_email = "pratheebaniit@gmail.com"
            while True:
                speak("receiver mail id")
                receiver_email=takeCommand(10)
                if receiver_email!="None":
                    receiver_email=''.join(receiver_email.split())
                    receiver_email=receiver_email+"@gmail.com"
                    break
            password = "Tamilprathee"
            message = MIMEMultipart("alternative")
            while True:
                speak("Subject of the mail")
                message["Subject"] =takeCommand()
                if message["Subject"] !="None":
                    break
            message["From"] = sender_email
            message["To"] = receiver_email
            while True:
                speak("Message")
                mess = takeCommand(15)
                if mess !="None":
                    break
            part1 = MIMEText(mess, "plain")
            message.attach(part1)
            context = ssl.create_default_context()
            try:
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, message.as_string())
                    server.quit()
                    speak("Message send")
            except:
                speak("Message sending failed check the internet or password")
        elif "where is" in statement:
            while True:
                speak("Tell the place")
                query_split=takeCommand()
                if query_split!="None":
                    query_split=''.join(query_split.split())
                    break
            location_url = "https://www.google.co.in/maps/place/" + str(query_split)
            speak("Hold on User, I will show you where " + query_split+ " is.")
            webbrowser.open(location_url)
        
        elif 'flipkart' in statement or 'amazon' in statement:
            amazon_search = "https://www.amazon.in/s/keywords={}"
            flipkart_search = "https://www.flipkart.com/search?q={}"
            while True:
                speak("Tell the product")
                query_split=takeCommand()
                if query_split!="None":
                    query_split=''.join(query_split.split())
                    break
            if( statement in "amazon"):
                amazon_search = amazon_search.format('+'.join(query_split))
                webbrowser.open(amazon_search)
            if( statement in "flipkart"):
                flipkart_search = flipkart_search.format('+'.join(query_split))
                webbrowser.open(flipkart_search)
        elif "music" in statement or "play" in statement:
            while True:
                speak("Tell the music name")
                query_split=takeCommand()
                if query_split!="None":
                    query_split=''.join(query_split.split())
                    break
            url = 'https://www.youtube.com/results?search_query={}'.format('+'.join(query_split))
            webbrowser.open(url)
        elif "note" in statement:
             while True:
                speak("To read or write")
                details=takeCommand(15).lower()
                if details=="None" and details=="" :
                    continue
                elif details=="write":
                    while True:
                        speak("Tell the details to be stored")
                        detail=takeCommand(15).lower()
                        if detail=="None" and detail=="" :
                            continue
                        break
                    with open("test.txt",'w',encoding = 'utf-8') as f:
                        f.write(detail)
                    break
                elif details=="read":
                    with open("test.txt",'r',encoding = 'utf-8') as f:
                        detail=f.read()
                        print(detail)
                        speak(detail)
                    break
            
        elif "open" in statement:
            while True:
                speak("Tell the file name")
                filename=takeCommand().lower()
                if filename=="None" and filename=="" :
                    continue
                filename=''.join(filename.split())
                break
            while True:
                speak("extension text or python")
                extension=takeCommand().lower()
                if extension=="text":
                    extension="txt"
                    break
                elif extension=="python":
                    extension="py"
                    break
                elif extension=="image":
                    extension="jpg"
                    break
                elif extension=="None":
                    continue
                extension=''.join(filename.split())
            filename=filename+"."+extension
            drives = win32api.GetLogicalDriveStrings()
            drives = drives.split('\000')[:-1]
            for drive in drives[-1]:
                filesList = []
                print("Searching")
                filesList.append("\t\t\t ------------------------------ Files in " +drive+ " Drive ------------------------------------")
                for dirpath, dirnames, filenames in os.walk(drive):
                    for fileName in filenames:
                        if fnmatch.fnmatch(fileName, filename):
                            if  not isList:
                                print("Opening " + filename)
                                os.startfile(os.path.join(dirpath, fileName))
                                return
                            else:
                                filesList.append(os.path.join(dirpath, fileName))
        
def facedect(loc):
    ch=0
    face_1_face_encoding=[]
    global cam
    cam = cv2.VideoCapture(0)  
    while True:
        s, img = cam.read()
        if s:
            try:
                for i in loc:
                    face_1_image=face_recognition.load_image_file(i)
                    face_1_face_encoding.append(face_recognition.face_encodings(face_1_image)[0])
                small_frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
                rgb_small_frame = small_frame[:, :, ::-1]
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
                for i in face_1_face_encoding:
                    check=face_recognition.compare_faces(i, face_encodings)
                    print(check)
                    if check[0]:
                        ch=1
                        break
                    else :
                        continue    
                if ch==1:
                    break
                else:
                    continue
            except Exception:
                speak("show your face straight to the cam")
                continue
        
    if ch==1:
        cam.release()
        cv2.destroyAllWindows()
        VirtualAss()
        app.destroy()
def uspw():
    global uname,passw,master
    master = tk.Tk() 
    master.title('Voice Login')
    master.geometry('350x200')   
    label1 = tk.Label(master,text='Username')
    label1.grid(row=1,column=1)
    uname = tk.Entry(master,width=30)
    uname.grid(row=2, column=2)
    label2 = tk.Label(master,text='Password')
    label2.grid(row=3,column=1)
    passw= tk.Entry(master,width=30)
    passw.grid(row=4, column=2)
    submitb=tk.Button(master, text='Submit', command=login)
    submitb.grid(row=5, column=2,  sticky=tk.W,pady=4)
    
def login():
    uname_=uname.get().strip()
    passw_=passw.get().strip()
    conn = sqlite3.connect("new.db")
    cur = conn.cursor()
    res=cur.execute("SELECT * from users")
    un,ps=[],[]
    for i in res:
        un.append(i[0])
        ps.append(i[1])
    cur.close()
    conn.close()
    if len(uname_)==0 or len(passw_)==0:
        messagebox.showinfo("Error","Enter Username or Password")
        return
    elif uname_ in un and passw_ in ps:
        master.destroy()
        VirtualAss()
        app.destroy()
    else:
        messagebox.showinfo("Error","Invalid password")
        return
        
def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")  
    else:
        speak("Hello,Good Evening")
def takeCommand(secwait=5):
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source, phrase_time_limit = secwait)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")
        except Exception as e:
            print(e)
            speak("Pardon me, please say that again")
            return "None"
        return statement
def choice():
    while True:
        speak("Face unlock or Enter the details")
        statement = takeCommand().lower()
        if statement==0:
            continue
        if "face" in statement:
            speak('Opening cam')
            ch=2
            break
            
        elif "details" in statement:
            speak('Opening login page')
            ch=1
            break
    if ch==1:
        uspw()
    elif ch==2:
        l=os.listdir(cpwd)
        r=[i for i in l if (i.endswith(".jpg") or i.endswith(".jpeg"))]
        print(r)
        facedect(r)
def start():
    global engine
    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice','voices[0].id')
    speak("Loading your AI personal assistant G-One")
    wishMe()
    choice()
class SampleApp(tk.Tk):
    type_selected=""
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)
    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid()
class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title('Virtual assistance')
        master.geometry('200x200')
        tk.Button(self, text='Register', command=lambda: master.switch_frame(Register)).grid(row=0,column=0)
        tk.Button(self, text='Login',command=lambda: master.switch_frame(Login)).grid(row=0,column=1)
class Register(tk.Frame):
    def __init__(self, master):
        global uname,passw
        tk.Frame.__init__(self, master)
        master.title('Virtual assistance Registration')
        master.geometry('200x200')
        label1=tk.Label(self,text='Emailid')
        label1.grid(row=1,column=1)
        uname=tk.Entry(self,width=30)
        uname.grid(row=2, column=2)
        label2 = tk.Label(self,text='Password')
        label2.grid(row=3,column=1)
        passw= tk.Entry(self,width=30)
        passw.grid(row=4, column=2)
        tk.Label(self,text="Upload your picture").grid(row=5,column=1)
        tk.Button(self, text="upload",command=self.browse_button).grid(row=5,column=2)
        self.folder_path = tk.StringVar()
        lbl1 = tk.Label(self,textvariable=self.folder_path)
        lbl1.grid(row=5, column=3)
        tk.Button(self, text='Submit', command=lambda: master.switch_frame(WriteLogic)).grid(row=6,column=1)
    def browse_button(self):
        filename = filedialog.askopenfilename(title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        try:
            face_1_image = face_recognition.load_image_file(filename)
            face_1_face_encoding = face_recognition.face_encodings(face_1_image)[0]
            shutil.copy(filename,cpwd)
            self.folder_path.set("Picture Uploaded")
        except Exception as e:
            self.folder_path.set("Upload different picture")
class Login(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title('Virtual assistance Registration')
        master.geometry('200x200')
        label1=tk.Label(self,text='AI')
        label1.grid(row=1,column=1)
        tk.Button(self, text='Submit', command=start).grid(row=2,column=1)
        tk.Button(self, text='Close', command=self.destroy).grid(row=2,column=2)
class WriteLogic(tk.Frame):
    def __init__(self,master):
        us=uname.get()
        ps=passw.get()
        conn = sqlite3.connect("new.db")
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS users (uname VARCHAR NOT NULL,pswd VARCHAR NOT NULL)""")
        conn.commit()
        cur.execute('INSERT INTO users (uname, pswd) VALUES (?, ?)',(us,ps))
        conn.commit()
        cur.close()
        conn.close()
        tk.Frame.__init__(self, master)
        master.title('Virtual assistance Registration')
        master.geometry('200x200')
        label1=tk.Label(self,text='Details Uploaded')
        label1.grid(row=0,column=1)
        tk.Button(self, text='OK', command=lambda: master.switch_frame(StartPage)).grid(row=1,column=1)
        
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
