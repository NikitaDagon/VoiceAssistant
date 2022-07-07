from ast import Num
import os
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import webbrowser
from sound import Sound


# def calc(str):
#     str = str.split()
#     str.remove("x")
#     return str[0] * str[1]
        
    


opts = {
    "Sydney": ('сидни','сидней','sydney'),
    "tbr": ('скажи','расскажи','покажи','сколько','произнеси',),
    "cmds": {
        "google":('открой новую вкладку','открой новую вкладку в браузере'),
        "numbers":('*', "x",'умножить'),
        "volume":('громкость','параметры громкости'),
        "taskmgr":('диспетчер задач','дс','taskmgr'),
        "search":('поиск в интернете','найди в интернете'),
        "turnoff":('off','выключись','закончи работу'),
        "control":('панель управления'),
    }
} 

def speak(what):
    print( what )
    speak_engine.say( what )
    speak_engine.runAndWait()
    speak_engine.stop()

def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language = "ru-RU").lower()
        print("[log] Вот что ты сказал: " + voice)
        
    
        if voice.startswith(opts["Sydney"]):
    
            cmd = voice
 
            for x in opts['Sydney']:
                cmd = cmd.replace(x, "").strip()
            
            for x in opts['tbr']:
                cmd = cmd.replace(x, "").strip()
            
            
            cmd = recognize_cmd(cmd)
            execute_cmd(cmd['cmd'])
 
    except sr.UnknownValueError:
        print("[log] Голос не распознан!")
    except sr.RequestError as e:
        print("[log] Неизвестная ошибка, проверьте интернет!")
def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c,v in opts['cmds'].items():
 
        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
    
    return RC
     

def execute_cmd(cmd):
    if cmd == 'google':
        path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
        webbrowser.open(path)

    elif cmd =="numbers":
        print('Что на что?')
        x = ('123')
        r = sr.Recognizer()
        with sr.Microphone(device_index = 2) as source:
          audio = r.listen(source)
        str = r.recognize_google(audio, language="ru-Ru")
        if len(x) > 0:
             str = str.split()
             a = float(str[0])
             b = float(str[2])
             print(a * b)
             speak('Вот и ответ') 
        else:
            a = float(str[0])
            b = float(str[1])
            print(a * b)
            speak('Вот и ответ') 
               



    elif cmd == "taskmgr":
        os.system('taskmgr')
        speak('Уже открыла')


    elif cmd == 'turnoff':
        speak('Закругляюсь')
        exit()
    

    elif cmd == 'control':
        os.system('control')
        speak('Работаем')

    
    elif cmd == 'search':
         r = sr.Recognizer()
         with sr.Microphone(device_index = 2) as source:
            audio = r.listen(source)
         query = r.recognize_google(audio, language="ru-Ru")
         webbrowser.open_new_tab('https://www.google.com/search?q={}'.format(query))
         speak('Вы сказали найти ' +query.lower())

    elif cmd == 'volume':
        print("На сколько?")
        Num = 0 
        r = sr.Recognizer()
        with sr.Microphone(device_index = 2) as source:
            audio = r.listen(source)
        query = r.recognize_google(audio, language="ru-Ru").split()
        for i in query:
            if i.isnumeric():
                Num = int(i)
                print(Num)
        Sound.volume_set(Num)
              

   
             

    else:
        print('Шота ни так друг')
        
        


r = sr.Recognizer()
m = sr.Microphone(device_index=2)

with m as source:
    r.adjust_for_ambient_noise(source)
speak_engine = pyttsx3.init()

speak("Добрый день")
speak("Сидни слушает")

stop_listening = r.listen_in_background(m,callback)
while True:time.sleep(0.1)

    

