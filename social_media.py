import webbrowser

ining = int(input('Enter 1 to check facebook:\nEnter 2 to check Messenger:\nEnter 3 to check Twitter:\nEnter 4 to check Instagram:\nEnter 5 to check VK:(sorry, this service is temporary disabled\nEnter 6 to check LinkedIn:'))

if ining == 1:
    webbrowser.open('www.facebook.com')
elif ining == 2:
    webbrowser.open('www.messenger.com')
elif ining == 3:
    webbrowser.open('www.twitter.com')
elif ining == 4:
    webbrowser.open('www.instagram.com')
elif ining == 5:
    webbrowser.open()
elif ining == 6:
    webbrowser.open('www.linkedin.com')
