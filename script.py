from tkinter import *
root=Tk()
def nextaction():
	frame1.pack_forget()
	frame2.pack()
	frame1=Frame(root)
	canvas=Canvas(frame1)
	img = PhotoImage(file='Web.png')
	canvas.create_image(-18,0, image=img, anchor=NW)
	canvas.grid(row=0)
	b1=Button(frame1,text="GetStarted",command=nextaction).grid(row=1)
	b3=Button(frame2,text="Female",command=male,font=("Helvetica", 22),fg="red",bg="#98fb98").grid(row=4, padx=10, pady=10)
	l4=Label(frame3,text="Select age-group").grid(row=0,column=0)
	frame1.pack()
	root.mainloop()





