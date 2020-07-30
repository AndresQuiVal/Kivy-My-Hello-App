topRoot=Toplevel(mainroot)

def varb():

	if var2.get()!= var.get():
		root2=Tk()
		frame2=Frame(root2, width=40, height=30)
		frame2.pack()
		label=Label(frame2, text="Acceso Denegado \nLo Sentimos", fg="red")
		label.pack()
			
	elif var2.get() == var.get():
		root2=Tk()
		frame2=Frame(root2, width=40, height=30)
		frame2.pack()
		label=Label(frame2, text="Acceso Permitido \nTu Nombre de Usuario es: " +  pvar.get() +  "\nTu Contraseña es: " +  var.get(), fg="green")
		label.pack()

	else:
		print("hola")
		

		

pvar=StringVar()
var=StringVar()
var2=StringVar()

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



#if var2.get() == var.get():
#		label.config(text="Acceso Permitido", fg="green")
#	elif var2.get() is not var.get():
#		label.config(text="Acceso Denegado", fg="red")	
#	else:
#		label.config(text="El Programa se Rompera", fg="gray")
