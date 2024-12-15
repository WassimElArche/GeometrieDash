from tkinter import *
import sqlite3
#----------------------
# INTERFACE DE LA PAGE
#----------------------
fenetre = Tk()
fenetre.title("Geometry Dash")
fenetre.geometry("350x400")
fenetre.config(bg="#606060")
#-------------------
# Les records
#-------------------
connexion = sqlite3.connect(':memory:')
curseur=connexion.cursor()
curseur.execute('''CREATE TABLE IF NOT EXISTS records(
                id INTEGER PRIMARY KEY,
                nom TEXT,
                record INTEGER)''')
#---------------------
# Les fonctions
#---------------------
def affichage():
    name.set("Nom d'utilisateur :" +compte1.get()+"")
    compte1.delete(0,END)
name=StringVar()
name.set("Nom d'utilisateur")
texteLabel2 = Label(fenetre, textvariable = name)
texteLabel2.pack()
compte1 = Entry()
bouton3= Button(fenetre , text= "Confirmer", command = affichage )
compte1.pack()
bouton3.pack()

#---------------------
# LES CLASS
#---------------------
def niva():
    class jeu(Tk):
        def __init__(self):
            Tk.__init__(self)
            self.canevas = Canvas(self,bg= "white", height = 1000, width= 1000)
            self.canevas.pack()
            self.canevas.create_line(4,600,10000,600, fill = "#606060",width=100)
            self.canevas.create_rectangle(19,535,29,535,fill = "Blue", width =30)
    fenniv1=jeu()
    fenniv1.title("Niveau1")
    bouton1= Button(fenniv1, text = "Quittez",bg="red", height = 4 , width = 13 , command = fenniv1.destroy )
    bouton1.pack()
    bouton1.place(x=800 , y= 20)


    nom = Label
    fenetre.mainloop()

def nivb():
    class oo(Tk):
        def __init__(self):
            Tk.__init__(self)
            self.canevas = Canvas(self,bg= "blue", height = 1000, width= 1000)
            self.canevas.pack()
            self.canevas.create_line(4,600,10000,600, fill = "purple",width=100)
            self.canevas.create_rectangle(19,535,29,535,fill = "dark blue", width =30)
    fenniv2=oo()
    fenniv2.title("Niveau 2")
    bouton1= Button(fenniv2, text = "Quittez",bg="red", height = 4 , width = 13 , command = fenniv2.destroy )
    bouton1.pack()
    bouton1.place(x=800 , y= 20)
    nom = Label
    fenetre.mainloop()

def nivc():
    class zz(Tk):
        def __init__(self):
            Tk.__init__(self)
            self.canevas = Canvas(self,bg= "red", height = 1000, width= 1000)
            self.canevas.pack()
            self.canevas.create_line(4,600,10000,600, fill = "blue",width=100)
            self.canevas.create_rectangle(19,535,29,535,fill = "dark blue", width =30)
    fenniv3=zz()
    fenniv3.title("Niveau 3")
    bouton1= Button(fenniv3, text = "Quittez",bg="red", height = 4 , width = 13 , command = fenniv3.destroy )
    bouton1.pack()
    bouton1.place(x=800 , y= 20)
    nom = Label
    fenetre.mainloop()

#---------------------
# Niveau
#---------------------

def page_des_niveau():
    class niv0(Tk):
        def __init__(self):
            Tk.__init__(self)
            self.canevas = Canvas(self, bg="blue", height=100000, width=10000)


    fena = niv0()
    niv1 = Button(fena , text = "Niveau 1", bg = "white" , height=4,width=13, command =niva)
    niv1.pack()
    niv2 = Button(fena , text = "Niveau 2", bg = "white" , height=4,width=13, command =nivb)
    niv2.pack()
    niv3 = Button(fena, text="Niveau 3", bg="white", height=4, width=13, command= nivc)
    niv3.pack()
    fena.title("Les Niveau")
    fena.mainloop()
#---------------------
# LES BOUTONS
#---------------------
bouton2= Button(fenetre,text="Jouer", heigh="4",width="9", command = page_des_niveau )
bouton2.pack()
bouton2.place(x= 140 , y=150)
bouton1= Button(fenetre,text="Quitter", command = fenetre.destroy , bg = "red")
bouton1.pack()
bouton1.place(x=149, y=260)



connexion.close()
fenetre.mainloop()
