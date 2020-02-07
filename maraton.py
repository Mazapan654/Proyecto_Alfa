##Estas son las utileriaspara el odfmgmgom

pérkophk,rpt,hmk, 7kl
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from time import sleep
from random import randint
import subprocess
import pymysql

##Crean la ventana
menu=Tk()
menu.resizable(1,1)
menu.title("Maratón")
menu.geometry("1200x600")
menu.config(bg="slate blue")
menu.iconbitmap("iconos/icono.ico")

##Posiciones de los jugadores
x_juga1=20
y_juga1=340
x_juga2=20
y_juga2=470
x_burro=20
y_burro=600
idmateria=""

str_ale=StringVar()
str_ale.set("")
str_nom=StringVar()
str_id=StringVar()
str_aux=StringVar()
str_op1=StringVar()
str_op2=StringVar()
str_op3=StringVar()
str_opc=StringVar()
str_nom.set("")
str_id.set("")
str_op1.set("")
str_op2.set("")
str_op3.set("")
str_opc.set("")
maximo=0
seleccion=IntVar()
turno=1

def lista_materias():
	## Combo de Usuarios
	conn = pymysql.connect(host='localhost', user='root', passwd='', db='maraton')
	cursor = conn.cursor()
	cursor.execute('select descripcion from materia')
	mts = []
	for row in cursor:
		mts.append(row[0])
	cursor.close()
	conn.close()
	return mts

def as_lista(event):
	global idmateria
	global maximo
	men=mat.get()
	##messagebox.showinfo(message=men)
	sql = "select id_materia from materia where descripcion='"+men+"'"
	db = pymysql.connect(host="localhost", user="root", passwd="", db="maraton")
	cursor = db.cursor()
	cursor.execute(sql)
	idmateria = cursor.fetchone()[0]
	sql = "select max(id_pregunta) from pregunta"
	cursor.execute(sql)
	maximo = cursor.fetchone()[0]
	##messagebox.showinfo(message=idmateria)

def selec_pregunta():
	global idmateria
	global maximo
	db = pymysql.connect(host="localhost", user="root", passwd="", db="maraton")
	cursor = db.cursor()
	registros=0
	while registros==0:
		str_ale.set(str(randint(0,maximo)))
		sql = "select count(*) from pregunta where id_materia="+str(idmateria) + " and id_pregunta=" + str_ale.get()
		cursor.execute(sql)
		registros=cursor.fetchone()[0]
	sql="select id_pregunta, Pregunta, opcion1, opcion2, opcion3, correcto, nivel from pregunta where id_materia="
	sql=sql+str(idmateria)+" and id_pregunta="+str_ale.get()
	cursor.execute(sql)
	for row in cursor:
		##(row)
		str_nom.set(row[1])
		str_op1.set(row[2])
		str_op2.set(row[3])
		str_op3.set(row[4])
		str_opc.set(row[5])

	e_pregunta.config(width=20)
	e_pregunta.place(x=690, y=60)

	pregunta_u.config(width=50)
	pregunta_u.place(x=690, y=90)

	r_opc1.config(width=2)
	r_opc1.place(x=665, y=120)

	opc1_u.config(width=50)
	opc1_u.place(x=690, y=120)
	
	r_opc2.config(width=2)
	r_opc2.place(x=665, y=150)
	
	opc2_u.config(width=50)
	opc2_u.place(x=690, y=150)
	
	r_opc3.config(width=2)
	r_opc3.place(x=665, y=180)
	
	opc3_u.config(width=50)
	opc3_u.place(x=690, y=180)

	##opcc_u = Entry(raiz, textvariable=str_opc, font='Helvetica 8', width=1)
	##opcc_u.place(x=690, y=210)
	##print(sql)
	cursor.close()
	db.close()

##Estos son los apartados para ventanas auxiliares "cat_usu" , "cat_mat" y "cat_preg"
def registra():
	subprocess.Popen(['python' , 'cat_usu.py'])

def catalogo_mat():
	subprocess.Popen(['python' , 'cat_mat.py'])

def catalogo_preg():
	subprocess.Popen(['python' , 'cat_preg.py'])

def sel_prgunta():
	b_pregunta.config(height=3)
	b_pregunta.config(width=3)
	pregunta.config(height=400)
	pregunta.config(width=550)
	selec_pregunta()
	##raiz.update()

##Función del jugador 1
def avanza1():
	global turno
	global x_juga1
	global y_juga1
	x_juga1 = x_juga1 + 50
	juga1.place(x=x_juga1, y=y_juga1)
	if x_juga1>=1200:
		messagebox.showinfo(message="Gano jugador 1")
	turno = 2

##Función del jugador 2
def avanza2():
	global turno
	global x_juga2
	global y_juga2
	x_juga2 = x_juga2 + 50
	juga2.place(x=x_juga2, y=y_juga2)
	if x_juga2>=1200:
		messagebox.showinfo(message="Gano jugador 2")
	turno = 1

##Función de la ignorancia
def avanza_burro():
	global turno
	global x_burro
	global y_burro
	x_burro = x_burro + 50
	burro.place(x=x_burro, y=y_burro)
	if turno==1:
		turno = 2
	else:
		turno = 1
	if x_burro>=1200:
		messagebox.showinfo(message="Gano la ignorancia")

##Muestra si acertó la pregunrta o no
def seleccionado():
	global turno
	global x_burro
	global y_burro
	global x_juga2
	global y_juga2
	if str(seleccion.get())==str_opc.get():
		messagebox.showinfo(message="Respuesta Correcta :D")
		if turno==1:
			avanza1()
		else:
			avanza2()
	else:
		messagebox.showinfo(message="Respuesta incorrecta D':")
		avanza_burro()

	b_pregunta.config(height=180)
	b_pregunta.config(width=180)

	pregunta.config(height=3)
	pregunta.config(width=3)

	e_pregunta.config(width=0)
	e_pregunta.place(x=620, y=60)

	pregunta_u.config(width=0)
	pregunta_u.place(x=650, y=90)

	r_opc1.config(width=0)
	r_opc1.place(x=655, y=120)

	opc1_u.config(width=0)
	opc1_u.place(x=650, y=120)

	r_opc2.config(width=0)
	r_opc2.place(x=655, y=150)

	opc2_u.config(width=0)
	opc2_u.place(x=650, y=150)

	r_opc3.config(width=0)
	r_opc3.place(x=655, y=180)

	opc3_u.config(width=0)
	opc3_u.place(x=650, y=180)

	str_nom.set("")
	str_id.set("")
	str_op1.set("")
	str_op2.set("")
	str_op3.set("")
	str_opc.set("")

##Reinicia la posición de los jugadores
def reinicia():
	global x_juga1
	global y_juga1
	x_juga1 = x_juga1 
	juga1.place(x=20 , y=340)

	global x_juga2
	global y_juga2
	x_juga2 = x_juga2 
	juga2.place(x=20 , y=470)

	global x_burro
	global y_burro
	x_burro = x_burro
	burro.place(x=20 , y=600)

##Boton para reinciar el programa
reinciarxd=Button(menu, command=reinicia, bg='lavender', text='Reiniciar Juego', font='Helectiva 14 bold').place(x=1205 , y=0)

##Botones para mostrar las ventanas auxiliares
bot_usu=Button(menu, command=registra , bg="lavender" , text="Usuario" , font='Helectiva 14 bold' , width=7).place(x=0 , y=0)
bot_mat=Button(menu, command=catalogo_mat , bg="lavender" , text="Materias" , font='Helectiva 14 bold' , width=7).place(x=94 , y=0)
bot_preg=Button(menu, command=catalogo_preg , bg="lavender" , text="Preguntas" , font='Helectiva 14 bold' , width=8).place(x=188 , y=0)

mate=Label(menu, bg="white", fg="black", font='Helvetica 12 bold', text="Materia").place(x=300, y=1)

mat=ttk.Combobox(menu, font='Helvetica 10', width=20)
mat.place(x=360, y = 1)
mat.bind('<<ComboboxSelected>>', as_lista)
lista=lista_materias()
mat['values']=lista

##Imagenes utilizadas en el programa
meta = PhotoImage(file="meta.png")
i_dado = PhotoImage(file="dados.png")
i_pista = PhotoImage(file="fondo.png")
i_juga1 = PhotoImage(file="jugadores/mario.png")
i_juga2 = PhotoImage(file="jugadores/luigi.png")
i_burro = PhotoImage(file="jugadores/yoshi.png")
i_pregunta = PhotoImage(file="preg_fondo.png")

pista=Label(menu, bg='slate blue' ,image=i_pista)
pista.place(x=0, y=37)

pregunta= Label(menu, bg='slate blue', image=i_pregunta, width=1 , height=1)
pregunta.place(x=600, y=1)

aleatorio = Entry(menu, textvariable=str_ale, font='Helvetica 8', width=2)
aleatorio.place(x=0, y=37)

e_pregunta= Label(menu, bg='SkyBlue3', fg="white", text="Pregunta", font='Helvetica 8 bold', width=0)
e_pregunta.place(x=600, y=60)

pregunta_u = Entry(menu, textvariable=str_nom, font='Helvetica 8', width=0)
pregunta_u.place(x=630, y=90)

r_opc1=Radiobutton(menu, value=1, variable=seleccion, command=seleccionado,width=0)
r_opc1.place(x=635, y=120)

opc1_u = Entry(menu, textvariable=str_op1, font='Helvetica 8', width=0)
opc1_u.place(x=630, y=120)

r_opc2=Radiobutton(menu, value=2, variable=seleccion, command=seleccionado,width=0)
r_opc2.place(x=635, y=150)

opc2_u = Entry(menu, textvariable=str_op2, font='Helvetica 8', width=0)
opc2_u.place(x=630, y=150)

r_opc3=Radiobutton(menu, value=3, variable=seleccion, command=seleccionado, width=0)
r_opc3.place(x=635, y=180)

opc3_u = Entry(menu, textvariable=str_op3, font='Helvetica 8', width=0)
opc3_u.place(x=630, y=180)

##Tamaño e imagen de los jugadores
juga1= Label(menu, bg='slate blue', image=i_juga1, height=100,width=100)
juga1.place(x=x_juga1, y=y_juga1)

juga2= Label(menu, bg='slate blue', image=i_juga2, height=100,width=100)
juga2.place(x=x_juga2, y=y_juga2)

burro= Label(menu, bg='slate blue', image=i_burro, height=100,width=100)
burro.place(x=x_burro, y=y_burro)

b_pregunta = Button(menu, cursor="mouse", bg="white", relief="ridge", image=i_dado, command=sel_prgunta, width=180, height=180)
b_pregunta.place(x=500, y=50)
##Lineas para los carriles de los jugadores
linea=Canvas(menu, bg="lavender", width=1200, height=10).place(x=0, y=320)
linea2=Canvas(menu, bg="lavender", width=1200, height=10).place(x=0, y=450)
linea3=Canvas(menu, bg="lavender", width=1200, height=10).place(x=0, y=580)
##Meta de cada jugador
fin_juda1=Label(menu, image=meta, width=50, height=100).place(x=1200 , y=340)
fin_juga2=Label(menu, image=meta, width=50, height=100).place(x=1200 , y=470)
fin_burro=Label(menu, image=meta, width=50, height=100).place(x=1200 , y=600)



menu.mainloop()
