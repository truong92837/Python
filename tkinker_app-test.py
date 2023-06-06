from tkinter import *
from datetime import date

win = Tk()
win.geometry("600x200")
win.config(bg = "yellow")

fr1 = Frame()
fr1.pack()
fr2 = Frame()
fr2.pack()
fr3 = Frame()
fr3.place( x=1,y=165)

# function/ham tinh tuoi
def tuoi():
	namsinh = int(te1.get())
	year = date.today().year
	tuoi = year - namsinh
	if(tuoi > 100):
		lb4.config(text = "Thế lone nào mày vẫn còn sống tới giờ này? hả????")
	elif(tuoi==0 or tuoi ==1):
		lb4.config(text = "Miệng còn hôi sữa mà đòi test code của trẫm à")
	elif(tuoi<0):
		lb4.config(text= "Mày đùa tao đấy à con tinh trùng khuyết tật này")
	else:
		lb4.config(text = tuoi)
#hien thi label
lb1 = Label (fr1, text = "diu nâu mi? dét, Ai đu",font=("Arial",12,"bold"), bg = "red")
lb1.pack(side="top")

#label  nhap nam sinh
lb2 = Label (fr2, text = "Nhập năm sinh của mày vào đây: ", font=("Arial",12,"bold"))
lb2.pack(side = "left")

#textbox nhap nam sinh
te1 = Entry(fr2,font = ("Arial",12), width = 15)
te1.pack()

# button
but1 = Button(win,font=("Arial",12),text="Tính",command=tuoi)
but1.place(x=240,y=90)
# button thoat
but2 = Button(win,font=("Arial",12),text="Thoát",command=win.destroy)
but2.place(x=300, y = 90)
#but2.pack(pady=20)

#label ket qy=ua
lb3 = Label(fr3,text = "Tuổi của mày: ", font=("Arial",12,"bold"))
lb3.pack(side="left")

#xuat ket qua ra fr3
lb4 = Label(fr3, font =("Arial",12,"bold"))
lb4.pack()

#run
win.mainloop()
