from tkinter import Tk,Button,Event,Frame, Text, Label, PhotoImage, Menu

    
class Ventana:
    
    def __init__(self):
        self.actual = 1
        self.ventana = Tk()
        root = self.ventana
        self.ventana.title("Práctica 2, grupo 2-2")
        root.geometry(f"700x600")
        self.back = Frame(master = root,bg = "black")
        back = self.back
        back.pack(expand = True, fill = "both")
        p1 = self.p1 = Frame(master = back, bg = "yellow")
        self.p1.place(relwidth = 0.43, relheight = 0.9, relx = 0.05, rely = 0.08)
        p2 = self.p2 = Frame(master = back, bg = "blue")
        self.p2.place(relwidth = 0.43, relheight = 0.9, relx = 0.52, rely = 0.08)
        bienvenida = self.p3 = Label(master = p1, fg = "white", bg = "black",text = "👨‍🍳Bienvenido a la\npágina oficial de\nnuestro restaurante\nGuzman's food👨‍🍳", font = ("Arial", 20))
        bienvenida.place(relheight = 0.35, relwidth = 0.94, relx = 0.03, rely = 0.015)
        txt = open("imagenes/camiVida.txt", 'r')
        string = ""
        for i in txt:
            string = string + i
        txt.close()
        vida = self.p5 = Button(master = p2, fg = "black", text = string,font = ("Arial", 7), command = self.cambioIng)
        vida.place(relheight = 0.60, relwidth = 0.94, relx = 0.03, rely = 0.015)
        vida.bind()
        entrar = self.p4 = Button(master = p1, text = "🤯Ingresar al sistema🤯", bg = "blue", fg = "white", font = ("Arial", 18))
        entrar.place(relheight = 0.60, relwidth = 0.94, relx = 0.03, rely = 0.38)       
        fotos = self.p6 = Frame(master = p2, bg = "yellow")
        fotos.place(relheight = 0.35, relwidth = 0.94, relx = 0.03, rely = 0.63)
        self.img1 = PhotoImage(file = "imagenes/cami1.png")
        self.img2 = PhotoImage(file = "imagenes/cami2.png")
        self.img3 = PhotoImage(file = "imagenes/cami3.png")
        self.img4 = PhotoImage(file = "imagenes/cami4.png")
        self.foto1 = Label(master = fotos, image = self.img1, bg = "yellow")
        self.foto2 = Label(master = fotos, image = self.img2, bg = "yellow")
        self.foto3 = Label(master = fotos, image = self.img3, bg = "yellow")
        self.foto4 = Label(master = fotos, image = self.img4, bg = "yellow")
        self.foto1.place(relheight = 0.44, relwidth = 0.44, relx = 0.04, rely = 0.04)
        self.foto2.place(relheight = 0.44, relwidth = 0.44, relx = 0.04, rely = 0.52)
        self.foto3.place(relheight = 0.44, relwidth = 0.44, relx = 0.52, rely = 0.04)
        self.foto4.place(relheight = 0.44, relwidth = 0.44, relx = 0.52, rely = 0.52)
        menuBar = Menu(root)
        root.config(menu = menuBar)
        menu1 = Menu(menuBar)
        menuBar.add_cascade(label = "Inicio", menu = menu1)
        menu1.add_command(label = "Saalir de la aplicación", command = self.salir)
        menu1.add_separator()
        menu1.add_command(label = "Descripción del sistema", command = self.descripcion)
    
    def destroy(self):
        self.ventana.destroy()
    
    def salir(self):
        self.destroy()
        
    
    def descripcion(self):
        frame = Frame(master = self.p1, bg = "black")
        frame.place(relheight = 0.35, relwidth = 0.94, relx = 0.03, rely = 0.015)
        mensaje = Label(master = frame, fg = "white", bg = "black",text = ("Nuestro proyecto trata de la un programa\ndestinado a la gestión de una cadena de restaurantes\nde comida rápida," + 
                                                                             "buscando\nun eficaz manejo de recursos humanos,\npresupuestos, sucursales, finanzas, entre otras\ncosas, para permitir el" + 
                                                                             " correcto\ndesarrollo de las actividades del restaurante"))
        mensaje.pack()
        boton = Button(master = frame, text = "ok", command = frame.destroy)
        boton.pack()
    
    def cambioIng(self):
        if self.actual == 5:
            self.actual = 1
        else:
            self.actual += 1
        
 
    
x = Ventana()
x.ventana.mainloop()