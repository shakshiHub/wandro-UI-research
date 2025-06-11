import speech_recognition as sr

# creating instance of sr's recognizer class
r = sr.Recognizer()

# creating instance of sr's microphone class
mic = sr.Microphone()


with mic as source:
    print("Say something!")
    # call recognizer object's listen method on source (speech) and save as AudioData object
    audio = r.listen(source)
    

try:
    print("You said:", r.recognize_google(audio))
except:
    print("Sorry, I didn’t catch that.")
