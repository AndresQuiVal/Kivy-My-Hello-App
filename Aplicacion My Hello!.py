from tkinter import *
from tkinter import messagebox

mainroot=Tk()
#----------------------------------------Base De Variables----------------------------------------

mainvariable=IntVar()
pvar=StringVar()
var=StringVar()
var2=StringVar()

#----------------------------------------Funciones Base-------------------------------------------
		
def bymainFunction():

		global pvar
		global var
		global var2

		topRoot=Toplevel(mainroot, highlightcolor="brown")
		def varb():

			if var2.get()!= var.get():
				root2=Tk()
				frame2=Frame(root2, width=40, height=30)
				frame2.pack()
				label=Label(frame2, text="Your Password Are Not Similar or Your User Name is Invalid \nTry Again", fg="red")
				label.pack()

			elif pvar.get()=="" or var2.get()=="" or var.get()=="":
				root2=Tk()
				frame2=Frame(root2, width=40, height=30)
				frame2.pack()
				label=Label(frame2, text="You Are Missing Data! ", fg="red")
				label.pack()

			
			elif var2.get() == var.get():
				root2=Tk()
				frame2=Frame(root2, width=40, height=30)
				frame2.pack()
				label=Label(frame2, text="User Registered! \nYour User Name is: " +  pvar.get() +  "\nYour Password Is: " +  var.get(), fg="green")
				label.pack()

			else:
				print("hola")
		

		plabel=Label(topRoot, text="Nombre", font=(12))
		plabel.grid(row=0, column=0, sticky="e")

		slabel=Label(topRoot, text="Contraseña", font=(12))
		slabel.grid(row=1, column=0, sticky="e")

		tlabel=Label(topRoot, text="Registro_Contraseña", font=(12))
		tlabel.grid(row=2, column=0, sticky="e")

		pentry=Entry(topRoot, width=20, textvariable=pvar)
		pentry.grid(row=0, column=1, sticky="e")

		sentry=Entry(topRoot, width=20, textvariable=var)
		sentry.grid(row=1, column=1, sticky="e")
		sentry.config(show="*")

		rentry=Entry(topRoot, width=20, textvariable=var2)
		rentry.grid(row=2, column=1, sticky="e")
		rentry.config(show="*")

		passb=Button(topRoot, text="Enter", font=(12), command=varb, width="13")
		passb.grid(row=3, column=0, sticky="e", columnspan="1")

		label=Label(topRoot)
		label.grid(row=3, column=1, sticky="e", columnspan="2")

def mainFunction():
		global pvar
		global var
		global var2

		mainTopRoot=Toplevel()

		#usernamelogin=pvar
		#passwordlogin=var2
		sesionVar=StringVar()
		psesionVar=StringVar()

		def sesionMethod():
			if sesionVar.get()!=pvar.get() or psesionVar.get()!=var2.get():
				anotherSesionRoot=Tk()
				anotherSesionLabel=Label(anotherSesionRoot, text="Your User Name Or Password Are Incorrect!\nTry Again Please!\nIf You Hadn't Register Go And Register Please", fg="red")
				anotherSesionLabel.pack()
				anotherSesionRoot.mainloop()
			elif sesionVar.get()=="" or psesionVar.get()=="":
				anotherSesionRoot=Tk()
				anotherSesionLabel=Label(anotherSesionRoot, text="You Are Missing Data!", fg="red")
				anotherSesionLabel.pack()
				anotherSesionRoot.mainloop()
			else:
				anotherSesionRoot=Tk()
				anotherSesionLabel=Label(anotherSesionRoot, text="You Are In!", fg="green")
				anotherSesionLabel.pack()
				anotherSesionRoot.mainloop()


		#------------------------------Sesion Labels-----------------------------
		Label(mainTopRoot, text="Login!", font=20, fg="red").grid(row=0, column=0, padx=2, pady=2)

		sesionLabel=Label(mainTopRoot, text="Usuario")
		sesionLabel.grid(row=1, column=0, padx=2, pady=2)

		secondSesionLabel=Label(mainTopRoot, text="Contraseña")
		secondSesionLabel.grid(row=2, column=0, padx=2, pady=2)

		#------------------------------Sesion Entry------------------------------

		sesionEntry=Entry(mainTopRoot, textvariable=sesionVar)
		sesionEntry.grid(row=1, column=1, padx=2, pady=2)

		secondSesionEntry=Entry(mainTopRoot, textvariable=psesionVar)
		secondSesionEntry.grid(row=2, column=1, padx=2, pady=2)
		secondSesionEntry.config(show="*")
		#------------------------------Sesion Button-----------------------------

		sesionButton=Button(mainTopRoot, text="Send!", width=20, command=sesionMethod)
		sesionButton.grid(row=3, column=1, padx=2, pady=2)

	

def trimainFunction():
	messagebox.showinfo("About!","My Hello is a base program created iin november of 2018 with the purpose of creating a social media for the people and ask whatever question they have on hand!")

		


#----------------------------------------Base Del Programa----------------------------------------
mainframe=Frame(mainroot)
mainframe.pack()

Label(mainframe, text="Welcome To My Hello!", font=20).pack()

loginButton=Button(mainframe, text="Login!", width="10", command=mainFunction)
loginButton.pack(padx=3, pady=2)

registerButton=Button(mainframe, text="Register!", width="10", command=bymainFunction)
registerButton.pack(padx=3, pady=2)

aboutButton=Button(mainframe, text="About!", width="10", command=trimainFunction)
aboutButton.pack(padx=3, pady=2)


mainroot.mainloop()

