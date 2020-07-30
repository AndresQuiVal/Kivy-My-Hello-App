from tkinter import *

sesionBase=Tk()

sesionFrame=Frame(sesionBase, width="150", height="150")
sesionFrame.pack()

usernamelogin="Andres_QuiVal"
passwordlogin="HolaMundo"
sesionVar=StringVar()
psesionVar=StringVar()

def sesionMethod():
	if sesionVar.get()!=usernamelogin or psesionVar.get()!=passwordlogin:
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
Label(sesionFrame, text="Login!", font=20, fg="red").grid(row=0, column=0, padx=2, pady=2)

sesionLabel=Label(sesionFrame, text="Usuario")
sesionLabel.grid(row=1, column=0, padx=2, pady=2)

secondSesionLabel=Label(sesionFrame, text="Contraseña")
secondSesionLabel.grid(row=2, column=0, padx=2, pady=2)

#------------------------------Sesion Entry------------------------------

sesionEntry=Entry(sesionFrame, textvariable=sesionVar)
sesionEntry.grid(row=1, column=1, padx=2, pady=2)

secondSesionEntry=Entry(sesionFrame, textvariable=psesionVar)
secondSesionEntry.grid(row=2, column=1, padx=2, pady=2)
secondSesionEntry.config(show="*")
#------------------------------Sesion Button-----------------------------

sesionButton=Button(sesionFrame, text="Send!", width=20, command=sesionMethod)
sesionButton.grid(row=3, column=1, padx=2, pady=2)

sesionBase.mainloop() 
