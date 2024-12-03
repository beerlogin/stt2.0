import pyautogui
import pytesseract
import cv2
import numpy as np
import pyautogui

# Укажите путь к исполняемому файлу Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def generate_search_variants(text):
    variants = [
        text.lower(),
        text.capitalize(),
        text.title(),
        text.upper()
    ]
    return variants

def click_left():
    pyautogui.click()

def write(text):
    pyautogui.write(text)


def move_mouse_to_text(target_text):
    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)
    screenshot_cv = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

    # Применение OCR для распознавания текста на экране с указанием языка
    boxes = pytesseract.image_to_data(screenshot_cv, lang='rus', config='--psm 6')

    found = False  # Флаг для проверки нахождения текста

    # Сначала ищем оригинальный текст
    for i, box in enumerate(boxes.splitlines()):
        if i == 0:
            continue  # пропускаем заголовок
        b = box.split()
        if len(b) == 12:  # проверяем, что все данные присутствуют
            text = b[11]
            print(f"Распознанный текст: '{text}'")  # Отладочный вывод
            if text.lower() in [variant.lower() for variant in generate_search_variants(target_text)]:
                x, y, width, height = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                center_x = x + width // 2
                center_y = y + height // 2
                
                # Телепортируем мышь в центр экрана
                screen_width, screen_height = pyautogui.size()
                center_screen_x = screen_width // 2
                center_screen_y = screen_height // 2
                
                pyautogui.moveTo(center_screen_x, center_screen_y)
                
                # Плавно перемещаем мышь к целевым координатам
                print(f"Навожу мышь на '{text}' в координатах ({center_x}, {center_y})")
                pyautogui.moveTo(center_x, center_y, duration=1)  # Движение к целевой координате за 1 секунду
                
                found = True
                break

    # Если текст не найден, пробуем заменить "е" на "ё"
    if not found and 'е' in target_text:
        modified_target_text = target_text.replace('е', 'ё')
        print(f"Попытка найти '{modified_target_text}' вместо '{target_text}'")

        for i, box in enumerate(boxes.splitlines()):
            if i == 0:
                continue  # пропускаем заголовок
            b = box.split()
            if len(b) == 12:  # проверяем, что все данные присутствуют
                text = b[11]
                print(f"Распознанный текст: '{text}'")  # Отладочный вывод
                if text.lower() in [variant.lower() for variant in generate_search_variants(modified_target_text)]:
                    x, y, width, height = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                    center_x = x + width // 2
                    center_y = y + height // 2
                    
                    # Телепортируем мышь в центр экрана
                    screen_width, screen_height = pyautogui.size()
                    center_screen_x = screen_width // 2
                    center_screen_y = screen_height // 2
                    
                    pyautogui.moveTo(center_screen_x, center_screen_y)
                    
                    # Плавно перемещаем мышь к целевым координатам
                    print(f"Навожу мышь на '{text}' в координатах ({center_x}, {center_y})")
                    pyautogui.moveTo(center_x, center_y, duration=1)  # Движение к целевой координате за 1 секунду
                    
                    found = True
                    break