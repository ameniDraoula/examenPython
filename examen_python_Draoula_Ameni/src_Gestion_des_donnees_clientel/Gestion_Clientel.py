# importation des bibliotheque standard
import customtkinter
import tkinter as tk
from tkinter import messagebox
from tkinter import Tk
from collections import namedtuple
from os.path import isfile
import Clients

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

separateur='\t'
ligneRep= namedtuple("ligneRep","nom tel")
#creation du classe principale
class Gestion_Clientel(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Application de gestion des informations clientels")
        self.liste_clients = []
        self.create_Interface_ajout_client()

    def create_Interface_ajout_client(self):
        # Création des étiquettes et champs de saisie
        label_formulaire = tk.Label(self, text=" Remplir le formulaire consernant votre client  attentivement : ")
        label_formulaire.grid(row=0, column=0)
        

        label_nom = tk.Label(self, text=" Nom du client : ")
        label_nom.grid(row=1, column=0)
        self.champ_nom = tk.Entry(self)
        self.champ_nom.grid(row=1, column=1)

        label_prenom = tk.Label(self, text=" Prénom  : ")
        label_prenom.grid(row=2, column=0)
        self.champ_prenom = tk.Entry(self)
        self.champ_prenom.grid(row=2, column=1)

        label_age = tk.Label(self, text=" Âge  : ")
        label_age.grid(row=3, column=0)
        self.champ_age = tk.Entry(self)
        self.champ_age.grid(row=3, column=1)

        label_tel = tk.Label(self, text=" tel : ")
        label_tel.grid(row=4, column=0)
        self.champ_tel = tk.Entry(self)
        self.champ_tel.grid(row=4, column=1)

        label_adresse = tk.Label(self, text=" adresse : ")
        label_adresse.grid(row=5, column=0)
        self.champ_adresse = tk.Entry(self)
        self.champ_adresse.grid(row=5, column=1)

        label_montantA = tk.Label(self, text=" Montant d'achat : ")
        label_montantA.grid(row=6, column=0)
        self.champ_montantA = tk.Entry(self)
        self.champ_montantA.grid(row=6, column=1)

        # Création du bouton d'ajout et du bouton d'affichage
        bouton_ajouter = tk.Button(self, text="Ajouter", command=self.ajouter_client)
        bouton_ajouter.grid(row=7, column=0 , padx=10, pady=10)

        bouton_modifier = tk.Button(self, text="Modifier", command=self.modifier_client)
        bouton_modifier.grid(row=7, column=1 , padx=10, pady=10)

        bouton_supprimer = tk.Button(self, text="Supprimer", command=self.supprimer_client)
        bouton_supprimer.grid(row=7, column=2 , padx=10, pady=10)

        bouton_afficher = tk.Button(self, text="Afficher ", command=self.afficher_client)
        bouton_afficher.grid(row=7, column=3, padx=10, pady=10)

        bouton_gestion_statistique = tk.Button(self, text="Gestion Statistique", command=self.gestion_statistique)
        bouton_gestion_statistique.grid(row=7, column=5 , padx=10, pady=10)




        


    def ajouter_client(self):
        
        nom = self.champ_nom.get()
        prenom = self.champ_prenom.get()
        age = self.champ_age.get()
        tel=self.champ_tel.get()
        adresse=self.champ_adresse.get()
        montantA=self.champ_montantA.get()
        clt = Clients.Clients(nom, prenom, age,tel ,adresse ,montantA)
        if(nom=="" or prenom=="" or age=="" or tel=="" or adresse==""or montantA==""):
           messagebox.showerror("erreur ", "il faux remplir tout les champs")
        else:
            self.liste_clients.append(clt)
            messagebox.showinfo("Succès de l'ajout ", "Le client {} a été ajouté avec succès a la liste de nos clients .".format(clt.nom))
    
    def modifier_client(self ,n ,p,age,a,t,m):
        #modification d'affichage dans le champ de saisi
        self.champ_nom.delete(0,tk.END)
        self.champ_nom.insert(0,n)

        self.champ_prenom.delete(0,tk.END)
        self.champ_prenom.insert(0,p)

        self.champ_age.delete(0,tk.END)
        self.champ_age.insert(0,age)

        self.champ_adresse.delete(0,tk.END)
        self.champ_adresse.insert(0,a)

        self.champ_tel.delete(0,tk.END)
        self.champ_tel.insert(0,t)

        self.champ_montantA.delete(0,tk.END)
        self.champ_montantA.insert(0,m)
        
        
        self.champ_nom.focus()

    def supprimer_client(self):
        
        self.modifier_client('','','','','','')
        #effacer les champs de saisi
    


    def afficher_client(self):
    
        if not self.liste_clients:
            messagebox.showwarning("Avertissement", "la liste des clients est vide.")
        else:
            message = "Liste des client :\n\n"
        for clt in self.liste_clients:
            message += f"Nom: {clt.nom} {clt.prenom}\n"
            message += f"Age: {clt.age} ans\n"
            message += f"n°TEl: {clt.tel}\n"
            message += f"adresse: {clt.adresse}\n"
            message += f"Montant D'achat effectuer: {clt.montant_achat}\n\n"
        messagebox.showinfo("Liste des clients", message)
            
       
    def gestion_statistique():
        pass
#programme principale
if __name__ == "__main__":
        #app = customtkinter.CTk()  # create CTk window like you do with the Tk windowm
    app = Gestion_Clientel()
    app.geometry("800x300")
    app.mainloop()