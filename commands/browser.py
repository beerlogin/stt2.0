import webbrowser

# Регистрация браузера Brave
webbrowser.register('brave', None, webbrowser.BackgroundBrowser("C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"))

def open_browser():
    print("Открываю браузер...")
    url = "https://ya.ru"
    webbrowser.get("brave").open(url, new=2)