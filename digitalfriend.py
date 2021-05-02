import pyttsx3

friend = pyttsx3.init()
speech=input("write your speech")
friend.say(speech)
friend.runAndWait()