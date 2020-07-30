from tkinter import *

creditBase=Tk()

creditFrame=Frame(creditBase)
creditFrame.pack()

Label(creditFrame, text="Credits!", fg="red", font=15).pack()
creditLabel=Label(creditFrame, text="""My Hello! was an App Started In 15 of November of 2018 by Me, Your Author, Andres Quiroz Valdovinos, or Andres_QuiVal.\n
	I Have Been A Software Developer since i get the aficion of making and creating apps, but the entusiasm in me was not really presented\n
	So I lasted with no concept of programing at least 1 year but then i enter to the school and i realized that it was time to make something\n
	in my life so i decided to start programing. I haven't losed the entusiasm even how much time  have spent on programing, i just love doing it\n
	I spent the major time in my life on programing new things and learning and it's my passion and it will never end, for Sure!, so i'm proud to \n
	welcome you to My Hello!, enjoy it beacuse it's made for you, but this is not the only project that i will do, big proyects are coming on...\n
	and i will be proud of showing you what i have on hand!\n
	Gretings\n
	Andres_QuiVal :)""")
creditLabel.pack(fill="x")
creditButton=Button(creditFrame, text="Return!", width=20, font="12")
creditButton.pack()

creditBase-mainloop()