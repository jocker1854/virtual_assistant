import datetime
import os
import time
import tkinter as tk
import webbrowser as wb
import winsound
from tkinter import filedialog
import PyPDF2
import cv2
import playsound
import pyautogui as pg
import pyjokes
import pyttsx3
import speech_recognition as sr
from gtts import gTTS
from pynput.keyboard import Controller
from PIL import Image
import pywhatkit
##variables
keyboard = Controller
path = 'C:\\WINDOWS\\system32\\Taskmgr.exe'
listener = sr.Recognizer()
listener = sr.Recognizer()
engine = pyttsx3.init()
num = 1
# functions
def assistant_speaks(output):
    #num = 1
    global num

    # num to rename every audio file
    # with different name to remove ambiguity
    num += 1
    # print("PerSon : ", output)

    toSpeak = gTTS(text=output, lang='en', slow=False)
    # saving the audio file given by google text to speech
    file = str(num) + ".mp3"
    toSpeak.save(file)

    # playsound package is used to play the same file.
    playsound.playsound(file, True)
    os.remove(file)
def youtube():
    print('opening youtube')
    assistant_speaks('opening youtube')
    wb.open('www.youtube.com/')
def open_file(path):
    print('opening' + path)
    os.startfile(path)
def Read_book():
    print("running...")
    import_file_path = filedialog.askopenfilename()
    import_file_path = os.path.realpath(import_file_path)
    book = open(import_file_path, 'rb')
    print("Opening FileExplorer..")
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    print(pages)
    open_file(import_file_path)
    for num in range(8, pages):
        page = pdfReader.getPage(num)
        print(num)
        text = page.extractText()
        print("Extracting text...")
        assistant_speaks(text)
        print("Done")
def read_book():
    import_file_path = filedialog.askopenfilename()
    import_file_path = os.path.realpath(import_file_path)
    print("Opening "+import_file_path)
    book = open(import_file_path, 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    print(pages)
    for num in range(8, pages):
        page = pdfReader.getPage(num)
        print(num)
        text = page.extractText()
        print("Extracting PDF.....")
        assistant_speaks(text)
def command_prompt():
    os.startfile('C:\\WINDOWS\\system32\\cmd.exe')
def split(words):
    return [char for char in words]
def count(fa, tb):
    for x in range(fa, tb):
        print(x)
        assistant_speaks(x)
def type1(content):
    time.sleep(5)
    for t in content:
        # for i in t:
        pg.write(t)
def type_command():
    try:
        with sr.Microphone() as source:
            print('say content...')
            assistant_speaks('say content...')
            listener.pause_threshold = 1
            voice_type = listener.listen(source)
            command_1 = listener.recognize_google(voice_type, language='en-in')
            print(f'you said: {command_1}\n')
            type1(command_1)
            if 'return command' in command_1:
                return
    except Exception as e:
        print("Say the content again")
        return "None"
    while True:
        type_command()
    return command_1
def run_alexa():
    command = take_command()
    print(command)
    if 'time' in command:
        tyme = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is ' + tyme)
        assistant_speaks('Current time is ' + tyme)
    elif 'joke' in command:
        assistant_speaks(pyjokes.get_joke())
    elif 'introduce yourself' in command:
        assistant_speaks("now me introduce myself........."
                         "i am alexaa... the virtual assistant...."
                         "i can automate your tasks....."
                         "twenty four hours a day..."
                         "sevven days... a week")
    elif 'youtube' in command:
        print('opening youtube')
        assistant_speaks('opening youtube')
        wb.open('www.youtube.com/')
    elif 'play' in command:
        song = command.replace('play', '')
        assistant_speaks('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'book' in command:
        print('should i read a book')
        assistant_speaks('should i read a book')
        command = take_command()
        print(command)
        if 'yes' in command:
            print("what book should i read")
            assistant_speaks("what book should i read")
            command = take_command()
            if 'python book' in command:
                read_book("book_name")
            if 'return command' in command:
                return run_alexa()
        if 'no' in command:
            pass
        else:
            return command
    if 'count' in command:
        count(1, 100)
    elif 'type' in command:
        print('typing')
        type_command()
    elif 'task manager' in command:
        print('opening ' + path)
        open_file(path)
    elif 'quit' in command:
        print('ok sir quitting')
        assistant_speaks('ok sir..,quitting')
        quit()

    else:
        assistant_speaks('Please say the command again.')
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            assistant_speaks('listening...')

            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)

    except:
        pass
    while True:
        return command
def extract_book(book_name):
    book = open(book_name, 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    print(pages)
    for num in range(10, pages):
        page = pdfReader.getPage(num)
        text = page.extractText()
        time.sleep(4)
        pg.write(text, interval=0.001)
def speak(text):
    engine = pyttsx3.init
    engine.say(text)
    engine.runAndWait()
def speak_file(a):
    # engine = pyttsx3.init(driverName='sapi5')
    # engine.setProperty()
    # infile = f_read
    for i in a:
        # print('Which file : '+input())
        # x = input()
        # if x in a:
        f = open(i, 'r')
        theText = f.read()
        assistant_speaks(theText)
        # engine.runAndWait()
        # talk(theText)
def type_file(a):
    # engine = pyttsx3.init(driverName='sapi5')
    # engine.setProperty()
    # infile = f_read
    for i in a:
        # print('Which file : '+input())
        # x = input()
        # if x in a:
        f = open(i, 'r')
        theText = f.read()
        type1(theText)
        # engine.runAndWait()
        # talk(theText)
def assistant_speaks(output):
    global num
    # num to rename every audio file
    # with different name to remove ambiguity
    num += 1
    # print("PerSon : ", output)

    toSpeak = gTTS(text=output, lang='en', slow=False)
    # saving the audio file given by google text to speech
    file = str(num) + ".mp3"
    toSpeak.save(file)

    # playsound package is used to play the same file.
    playsound.playsound(file, True)
    os.remove(file)
def repeat():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ..re")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...re")
        query = r.recognize_google(audio, language='en-in')
        assistant_speaks(query)
    except Exception as e:
        print("Say that again please...")
        assistant_speaks("Say that again please...")
        return "None"
        # return audio
    return query
def repeatraw():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ..re")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...re")
        query = r.recognize_google(audio, language='en-in')
        assistant_speaks(query)
    except Exception as e:
        print("Say that again please...")
        assistant_speaks("Say that again please...")
        return "None"
        # return audio
    return query
def s_camera():
    # import cv2
    # import pyttsx3
    # import winsound
    # def speak(text):
    #     engine = pyttsx3.init
    #     engine.say(text)
    #     engine.runAndWait()

    assistant_speaks('opening web cam')

    cam = cv2.VideoCapture(0)
    while cam.isOpened():
        ret, frame1 = cam.read()
        ret, frame2 = cam.read()
        diff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)q
        for c in contours:
            if cv2.contourArea(c) < 5000:
                continue
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
            winsound.Beep(500, 200)

        if cv2.waitKey(10) == ord('q'):
            speak("breaking")
            break
        cv2.imshow("webcam", frame1)
def Convert_2_PNG():
    root = tk.Tk()

    canvas1 = tk.Canvas(root, width=300, height=250, bg='lightsteelblue2', relief='raised')
    canvas1.pack()

    label1 = tk.Label(root, text='File Conversion Tool', bg='lightsteelblue2')
    label1.config(font=('helvetica', 20))
    canvas1.create_window(150, 60, window=label1)

    def getJPG():
        global im1

        import_file_path = filedialog.askopenfilename()
        im1 = Image.open(import_file_path)

    browseButton_JPG = tk.Button(text="      Import JPG File     ", command=getJPG, bg='royalblue', fg='white',
                                 font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 130, window=browseButton_JPG)

    def convertToPNG():
        global im1

        export_file_path = filedialog.asksaveasfilename(defaultextension='.png')
        im1.save(export_file_path)

    saveAsButton_PNG = tk.Button(text='Convert JPG to PNG', command=convertToPNG, bg='royalblue', fg='white',
                                 font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 180, window=saveAsButton_PNG)

    root.mainloop()
def Convert_2_PDF():
    root = tk.Tk()

    canvas1 = tk.Canvas(root, width=300, height=300, bg='lightsteelblue2', relief='raised')
    canvas1.pack()

    label1 = tk.Label(root, text='File Conversion Tool', bg='lightsteelblue2')
    label1.config(font=('helvetica', 20))
    canvas1.create_window(150, 60, window=label1)

    def getFile():
        global im1

        import_file_path = filedialog.askopenfilename()
        image1 = Image.open(import_file_path)
        im1 = image1.convert('RGB')

    browseButton = tk.Button(text="     Select File     ", command=getFile, bg='green', fg='white',
                             font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 130, window=browseButton)

    def convertToPdf():
        global im1

        export_file_path = filedialog.asksaveasfilename(defaultextension='.pdf')
        im1.save(export_file_path)

    saveAsButton = tk.Button(text='Convert to PDF', command=convertToPdf, bg='green', fg='white',
                             font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 180, window=saveAsButton)

    def exitApplication():
        MsgBox = tk.messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',
                                           icon='warning')
        if MsgBox == 'yes':
            root.destroy()

    exitButton = tk.Button(root, text='Exit Application', command=exitApplication, bg='brown', fg='white',
                           font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 230, window=exitButton)

    root.mainloop()
def show_img(img):
    img = cv2.imread(img)
    cv2.imshow('Image', img)
    cv2.waitKey(0)