import speech_recognition
import pyttsx3

you = "you do not say anything"
robot_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
	print("Robot: I'm Listening")
	audio = robot_ear.listen(mic)
try:
	you = robot_ear.recognize_google(audio)
except:
	you == ""

print("--> "+you)
#say =pyttsx3.init()
#say.say(you)
#say.runAndWait()
