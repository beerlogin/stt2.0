from gtts import gTTS
import os
import pygame
import time

# Инициализация микшера
pygame.mixer.init()

#Прекрасный вариант, быстрый, но не качественный
def text_to_speech_pyttsx3(text, lang='ru'):
    import pyttsx3

    tts = pyttsx3.init()

    voices = tts.getProperty('voices')

    # Задать голос по умолчанию

    tts.setProperty('voice', "ru")

    # Попробовать установить предпочтительный голос

    for voice in voices:
        print(voice.name)
        if 'Irina' in voice.name:

            tts.setProperty('voice', voice.id)

            tts.say(text)

            tts.runAndWait()

def text_to_speech_google(text, directory="./", name='temp.mp3', temp=True, lang='ru'):
    tts = gTTS(text=text, lang=lang)
    if directory[len(directory) - 1] != "/":
        print(directory[len(directory) - 1])
        directory = directory + "/"
    tts.save(directory + name)
    pygame.mixer.music.load(directory + name)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    pygame.mixer.music.unload()
    time.sleep(0.2)
    if temp == True:
        os.system(f"del {directory}{name}")

if __name__ == "__main__":
    while True:
        print("Добро пожаловать, сэр.")
        print("Я готов создать любой голос")
        print("------------------------")
        print("Выберите вариант технологии text-to-speech (текст в голос)")
        print("Enter - google")
        print("1 - pyttsx3")
        select = input("- ")
        if select == "":
            print("Напишите директорию куда сохранять")
            print("Enter - './'")
            directory = input("- ")
            if directory == "":
                directory = "./"
            
            print("Напишите название файла")
            print("Enter - temp.mp3")
            name = input("- ")
            if name == "":
                name = "temp.mp3"
        
            print("Напишите текст для озвучивания")
            text = input("- ")
            if text == "":
                text = "Командный голос вырабатываю, товарищ генерал-полковник!"
            
            print("Стоит ли удалять файл после сохранения?")
            print("Enter - да")
            print("1 - нет")
            temp = input("- ")
            if temp == "1":
                temp = False
        
            print("Язык, на котором будет аудио")
            print("Enter - ru (русский)")
            lang = input("- ")
            if lang == "":
                lang = "ru"
        
            text_to_speech_google(text, directory=directory, name=name, temp=temp, lang=lang)
        elif select == "1":
            print("Директория куда сохранять при этом выборе не поддерживается")
            print("Название файла при этом выборе не поддерживается\n")
        
            print("Проигрывание временное, ни куда не сохраняется")
        
            print("Напишите текст для озвучивания")
            text = input("- ")
            if text == "":
                text = "Командный голос вырабатываю, товарищ генерал-полковник!"
            
            print("Стоит ли удалять файл после сохранения?")
            print("да - иное не поддерживается")
        
            print("Язык, на котором будет аудио")
            print("Enter - ru (русский)")
            lang = input("- ")
            if lang == "":
                lang = "ru"
        
            text_to_speech_pyttsx3(text, lang=lang)