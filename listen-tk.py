from tkinter import *
from datetime import date
import speech_recognition

win = Tk()
win.geometry("600x200")
win.config(bg = "yellow")
fr1 = Frame()
fr1.pack()
fr2 = Frame()
fr2.pack()
fr3 = Frame()
fr3.place( x=1,y=165)
#you = "you do not say anything"
robot_ear = speech_recognition.Recognizer()
# function/ham tinh tuoi
def start():
	with speech_recognition.Microphone() as mic:
		print("Robot: I'm Listening")
		audio = robot_ear.listen(mic,3,3)
	try:
		you = robot_ear.recognize_google(audio)
	except:
		lb4.config(text = "nothing")
	lb4.config(text = you)
#hien thi label
lb1 = Label (fr1, text = "diu nâu mi? dét, Ai đu",font=("Arial",12,"bold"), bg = "red")
lb1.pack(side="top")

#label  nhap nam sinh
lb2 = Label (fr2, text = "Nhập năm sinh của mày vào đây: ", font=("Arial",12,"bold"))
lb2.pack(side = "left")

# button
but1 = Button(win,font=("Arial",12),text="Mic on",command=start)
but1.place(x=240,y=90)
# button thoat
but2 = Button(win,font=("Arial",12),text="exit",command=win.destroy)
but2.place(x=300, y = 90)
#but2.pack(pady=20)

#label ket qy=ua
lb3 = Label(fr3,text = "Mày vừa sủa: ", font=("Arial",12,"bold"))
lb3.pack(side="left")

#xuat ket qua ra fr3
lb4 = Label(fr3, font =("Arial",12,"bold"))
lb4.pack()

#run
win.mainloop()



#import pyttsx3



#print("--> "+you)
#say =pyttsx3.init()
#say.say(you)
#say.runAndWait()
