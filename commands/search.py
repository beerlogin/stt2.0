import webbrowser

def search_in_browser(query):
    print(f"Ищу: {query}")
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.get("brave").open(search_url, new=2)