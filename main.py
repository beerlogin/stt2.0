import vosk
import pyaudio
import json
import time
import threading
import json
from playsound import playsound

from commands.browser import open_browser
from commands.search import search_in_browser
from commands.mouse import move_mouse_to_text, click_left, write 

from server.server import update_config

"""
    Конфиги!
"""

LISTENING_DURATION = 5  # Время прослушивания в секундах
is_listening = False

CONFIG = {
    "action": "",
    "is_listening": ""
}

class Sounds():
    main_path = "./tts/sounds/"
    
    greeting = main_path + "greeting.mp3"
    click = main_path + "click.mp3"
    find = main_path + "find.mp3"
    open_browser = main_path + "open_browser.mp3"
    write = main_path + "write.mp3"


"""
    Начало функций для асистента
"""
def reset_timer():
    global is_listening
    is_listening = True
    config(is_listening_value=True)
    time.sleep(LISTENING_DURATION)
    is_listening = False
    config(is_listening_value=False)

def config(action_value=None, is_listening_value=None):
    # Читаем текущие данные из файла
    if action_value != None:
        config['action'] = action_value
    if is_listening_value != None:
        config['is_listening'] = str(is_listening_value)
    update_config(config)

"""
    Начало части с асистентом, начало бэкенда
"""
def main():
    print("Команды Гены:")
    print("'Гена, ищи [ваш запрос]'")
    print("'Гена, открой браузер'")
    print("'Гена, наведи мышь на [текст]'")
    print("'Гена, нажми мышкой'")

    model = vosk.Model("vosk-model-small-ru-0.22")  # Укажите путь к вашей модели
    recognizer = vosk.KaldiRecognizer(model, 16000)

    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True)
    stream.start_stream()

    print("Слушаю...")

    while True:
        data = stream.read(4000)
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            text = result.get('text', '')
            if text:
                print("Вы сказали: " + text)

                if "гена" in text.lower():
                    playsound(Sounds.greeting)  # Проигрываем звук при активации
                    reset_timer_thread = threading.Thread(target=reset_timer)
                    reset_timer_thread.start()

                if is_listening:
                    if "открой браузер" in text.lower():
                        print("Команда открыть")
                        playsound(Sounds.open_browser)
                        open_browser()
                    elif "ищи" in text.lower():
                        print("Команда искать")
                        playsound(Sounds.find)
                        query = text.lower().replace("гена", "").replace("ищи", "").strip()
                        if query:
                            search_in_browser(query)
                    elif "напиши" in text.lower():
                        print("Команда написать")
                        playsound(Sounds.write)
                        query = text.lower().replace("гена", "").replace("напиши", "").strip()
                        if query:
                            print(f"Передаю {query}")
                            write(query)
                    elif "наведи на" in text.lower():
                        print("Команда навести мышку")
                        target_text = text.lower().replace("гена", "").replace("наведи на", "").strip()
                        if target_text:
                            print(f"Передаю {target_text}")
                            move_mouse_to_text(target_text)
                    elif "нажми" in text.lower():
                        playsound(Sounds.click)
                        print("Команда кликнуть")
                        click_left()
"""
    Конец части с асистентом, конец бэкенда
"""




if __name__ == "__main__":
    main()