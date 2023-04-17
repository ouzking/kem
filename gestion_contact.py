import sqlite3
print("Application de Gestion de contact avec Python et Sqlite3")
with sqlite3.connect('contactDB.db') as connection:
    cursor = connection.cursor()

cursor.execute("create table if not exists contact(id integer primary key autoincrement, nom text, prenom text, email text, numero_de_telephone text, adresse text, complet BOOLEAN)")

class Gestion_Contact:
    
    def __init__(self):
        print("l'application de gestion de contact")
        
    def ajouter_contact(self):
        print("ajouté le contact s'il vous plait:")
        nom = input("donnez le nom:")
        prenom = input("donnez le prenom:")
        email = input("donnez l'email:")
        numero_de_telephone = input("donnez le numero de telephone:")
        adresse = input("donnez l'adresse s'il vous plait:")
        cursor.execute("insert into contact (nom, prenom, email, numero_de_telephone, adresse, complet) values (?,?,?,?,?, false)", (nom, prenom, email, numero_de_telephone, adresse))
        connection.commit()
        print("le contact est bien enregistré:")
        
    def modifier_contact(self):
        print("modifiez le contact")
        id_contact = input("donnez l'ID que vous voulez modifier:")
        complet = input("choississez 1 si le contact est bon, et 0 dans l'autre cas\n")
        cursor.execute("UPDATE contact SET complet = ? WHERE id = ?", (int(complet), int(id_contact)))
        connection.commit()
        print("le contact a bien été modifié")
        
    def supprimer_contact(self):
        print("supprimez le contact s'il vous plait")
        id_contact = input("donnez ID que vous voulez supprimer:")
        cursor.execute("DELETE FROM contact WHERE id = ?", (id_contact,))
        connection.commit()
        print("le contact a bien été supprimé")
      
    def afficher_les_contacts(self):
        print("affichez les contacts")
        contacts = cursor.execute("SELECT * FROM contact").fetchall()
        for contact in contacts:
            print(f"ID: {contact[0]}, nom: {contact[1]}, prenom: {contact[2]}, Email: {contact[3]}, numero_de_telephone: {contact[4]}, Adresse: {contact[5]}") 
    
    def affiche_contact(self):
        print("vous voulez affichez le contact:")
        numero_de_telephone = input("ID du contact que vous voulez afficher")
        contact = cursor.execute("SELECT * FROM contact WHERE id = ?", (int(numero_de_telephone),)).fetchone()
        print("le contact est:", contact)
        
    def menu_des_contacts(self):
        choix =""
        print("      Bienvenue sur les contacts       ")
        print("                                       ")
        print("   1) ajouter un contact")
        print("   2) modifier un contact")
        print("   3) supprimer un contact")
        print("   4) Afficher les contacts")
        print("   5) Afficher un contact")
        print("   0) quitter l'application")
        choix = input("que voulez vous faire\n")
        if choix == "1":
            self.ajouter_contact()
            self.menu_des_contacts()
        elif choix == "2":
            self.modifier_contact()
            self.menu_des_contacts()
        elif choix == "3":
            self.supprimer_contact()
            self.menu_des_contacts()
        elif choix == "4":
            self.afficher_les_contacts()
            self.menu_des_contacts()
        elif choix == "5":
            self.affiche_contact()
            self.menu_des_contacts()
        elif choix == "0":
            print("Quitter")
            exit()
        else:
            print("votre choix n'est pas reconnu" )
            exit()
        

gestioncaisse = Gestion_Contact()
gestioncaisse.menu_des_contacts()