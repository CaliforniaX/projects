import webbrowser

# Get the trailer URL
trailer_url = "https://www.youtube.com/watch?v=-CtAs-4SBEw&t=11s"  # Replace with your trailer URL

# Register Browser Locations
opera_path = "C:\\Users\\SkyeDD\\AppData\\Local\\Programs\\Opera GX\\opera.exe"
webbrowser.register("opera", None, webbrowser.BackgroundBrowser(opera_path))

chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(chrome_path))

# Ask the user which browser they want to use
browser_choice = input("Which browser would you like to use to watch the trailer? (chrome, firefox, safari, opera): ")

# Open the trailer URL using the selected browser
if browser_choice.lower() == "chrome":
    webbrowser.get("chrome").open(trailer_url)
elif browser_choice.lower() == "firefox":
    webbrowser.get("firefox").open(trailer_url)
elif browser_choice.lower() == "safari":
    webbrowser.get("safari").open(trailer_url)
elif browser_choice.lower() == "opera":
    webbrowser.get("opera").open(trailer_url)
else:
    print("Invalid browser choice.")
