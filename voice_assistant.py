import pywhatkit
import pyjokes
import wikipedia
from utlis import *
from gtts import gTTS
import playsound
import os
import speech_recognition as sr
import webbrowser as wb
from tkinter import filedialog

num = 1
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

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        assistant_speaks("Good Morning")
    elif hour >= 12 and hour <= 18:
        assistant_speaks("Good Afternoon")
    else:
        assistant_speaks("Good Evening")
    assistant_speaks("I am alexa, how can i help you")
#wishMe()
# take the command from user
def takeCommand():
    # it takes microphone input and returns
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        assistant_speaks("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='')
        # assistant_speaks(query)
        query
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        assistant_speaks("Say that again please...")
        return "None"
        # return audio
    return query


if __name__ == "__main__":
    # wishMe()
    while True:
        query = takeCommand().lower()
        # if 'alexa' in query:
       # Logic for execution
        if 'wikipedia' in query:
            assistant_speaks('searching wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print("According to Wikipedia")
            assistant_speaks("According to Wikipedia")
            print(results)
            assistant_speaks(results)
        elif 'open youtube' in query:
            print('opening youtube')
            assistant_speaks('opening youtube')
            wb.open("youtube.com")
        elif 'open google' in query:
            print('opening google')
            assistant_speaks('opening google')
            wb.open("google.com")
        elif 'quit' in query:
            print('ok sir... quitting')
            assistant_speaks('ok sir... quitting')
            quit()
        elif 'play music' in query:
            import_file_path = filedialog.askopenfilename()
            import_file_path = os.path.realpath(import_file_path)
            music_dir = import_file_path
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'play ' in query:
            song = query.replace('play', '')
            assistant_speaks('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'search' in query:
            search = query.replace('search', '')
            assistant_speaks('searching...' + search)
            pywhatkit.search(search)
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%I:%H:%M:%S")
            print(f"The time is {strTime}")
            assistant_speaks(f"The time is {strTime}")
        elif 'joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            assistant_speaks(joke)
        elif 'task manager' in query:
            t_M_path = "C:\\WINDOWS\\system32\\Taskmgr.exe"
            assistant_speaks('opening task manager')
            os.startfile(t_M_path)
        elif 'open notepad' in query:
            note_path = "C:\\WINDOWS\\system32\\notepad.exe"
            assistant_speaks('opening notepad')
            os.startfile(note_path)
        elif 'read book' in query:
            print('what book i need to read')
            print("Action: file or speech"+input())
            if input()=='f':
                Read_book()
            # else:
            #     book = takeCommand()
            #     if 'bookname' in book:
            #         read_book(book_name)
            #     if 'return command' in book:
            #         takeCommand()
        elif 'type' in query:
            type_command()
        elif 'working fine' in query:
            assistant_speaks('Great')
        if 'who are you' or 'introduce yourself' or 'tell me about you' in query:
            intro = ['introduction']
            speak_file(intro)
        elif 'command prompt' in query:
            command_prompt()
        elif 'repeat me' in query:
            while True:
                repeat()
        elif "chrome" in query:
            assistant_speaks("Google Chrome")
            os.startfile('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')
        elif "word" in query:
            assistant_speaks("Opening Microsoft Word")
            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Word 2013.lnk')
        elif "excel" in query:
            assistant_speaks("Opening Microsoft Excel")
            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Excel 2013.lnk')
        elif 'security camera' in query:
            s_camera()
        elif 'convert to png' in query:
            Convert_2_PNG()
        elif 'convert to pdf' in query:
            Convert_2_PDF()
        elif 'list your function' or 'what you can do' in query:
            list = ['list_functions']
            speak_file(list)
