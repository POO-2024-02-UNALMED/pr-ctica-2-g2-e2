from tkinter import Tk,Button,Event,Frame, Text, Label

class Ventana:
    def __init__(self):
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
        inicio = self.inicio = Button(master = back,text = "Inicio", bg = "white")
        inicio.place(relheight = 0.04, relwidth = 0.1, relx = 0.05, rely = 0.02)
        bienvenida = self.p3 = Label(master = p1, fg = "white", bg = "black",text = "👨‍🍳Bienvenido a la\npágina oficial de\nnuestro restaurante\nGuzman's food👨‍🍳", font = ("Arial", 20))
        bienvenida.place(relheight = 0.35, relwidth = 0.94, relx = 0.03, rely = 0.015)
        vida = self.p5 = Label(master = p2, fg = "black")
        vida.place(relheight = 0.35, relwidth = 0.94, relx = 0.03, rely = 0.015)
        entrar = self.p4 = Button(master = p1, text = "🤯Ingresar al sistema🤯", bg = "blue", fg = "white", font = ("Arial", 18))
        entrar.place(relheight = 0.60, relwidth = 0.94, relx = 0.03, rely = 0.38)       
        fotos = self.p6 = Frame(master = p2, bg = "yellow")
        fotos.place(relheight = 0.60, relwidth = 0.94, relx = 0.03, rely = 0.38) 
x = Ventana()
x.ventana.mainloop()
