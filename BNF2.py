import numpy as np
import random as rand
import tkinter as tk
from tkinter import *

from PIL import ImageTk,Image
#antipattern certified
#class...................................................................................................................................

class Regles(tk.Tk):#classe qui affiche les regles
    def __init__(self):#on initialise la page en lancant les sous programmes necessaire
        tk.Tk.__init__(self)
        self.initJEU()

    def initJEU(self):
        #on créé des zones de textes contenant les regles
        label=Label(self,text="La bataille navale oppose deux joueurs qui s'affrontent. Chacun a une flotte composée de 5 bateaux, qui sont, les ",background="steel blue")
        label.pack()
        label=Label(self,text="suivants : 1 porte-avion (5 cases), 1 cuirasser (4 cases), 1 croiseur (3 cases), 1 sous-marin (3 cases), 1  frégate (2 ",background="steel blue")
        label.pack()
        label=Label(self,text="cases).C'est un jeu tour par tour ou les deux joueurs placent à l'aveugle des 3bombes.Couler un    bateau nécéssite de le",background="steel blue")
        label.pack()
        label=Label(self,text="toucher sur toutes ses cases.Pour gagner il faut couler tout les bateaux de l'adversaire.",background="steel blue")
        label.pack()
        #creation du bouton ok qui permet de quitter et son sous programme
        bouton = Button(self,text="OK",command=lambda:self.bouton())
        bouton.pack()
    def bouton(self):
        self.destroy()

class Erreur_en_dehors_du_plateau(tk.Tk):#fenetre qui s'ouvre quand on place un bateau en dehors du bateau
    def __init__(self):
        tk.Tk.__init__(self)#on initialise la page en lancant les sous programmes necessaire
        self.initButtons()
    def initButtons(self):
        #creation de la zone de texte
        label=Label(self,text="Votre bateau depasse du tableau!",background="steel blue")
        label.pack()
        #creation du bouton ok et son sous programme invouqé dans le lambda
        OK=Button(self,text="ok",relief=GROOVE,bg="light blue",command=lambda:self.bouton())
        OK.pack()
    def bouton (self):
        self.destroy()

class Orientation(tk.Tk):#class permentant de placer les bateaux
    orientation_verticale=True#creation du booleen verfiant si l'orientation et verticale ou pas
    nom_bateau=("","Frégate","Croiseur","Sous-marin","Cuirrasser","Porte-avion")#liste des noms de bateaux dans l'ordre
    def __init__(self,long_bateau,type_bateau,tableau_PLYR):#on initialise la page en lancant les sous programmes necessaire qui a en paramatre la longueur du bateau et le type de bateau
        tk.Tk.__init__(self)
        self.initButtons(long_bateau,type_bateau,tableau_PLYR)
    def initButtons(self,long_bateau,type_bateau,tableau_PLYR):#paramatre la longueur du bateau et le type de bateau
        #creation de la zone de texte
        label=Label(self,text="Comment voulez vous placer votre "+str(self.nom_bateau[type_bateau])+"?",background="steel blue")
        label.pack()
        # creationb des deux boutons un pour la position vertivale et l'autre horizontale
        Verticale=Button(self,text="Verticalement",relief=GROOVE,bg="light blue",command=lambda:self.orientation_v(long_bateau,type_bateau,tableau_PLYR)).pack(side=LEFT, padx=10, pady=10)
        horizontale=Button(self,text="Horizontalement->",relief=GROOVE,bg="light blue",command=lambda:self.orientation_h(long_bateau,type_bateau,tableau_PLYR)).pack(side=RIGHT, padx=10, pady=10)
    def orientation_v(self,long_bateau,type_bateau,tableau_PLYR):#programme du bouton quand le bouton verticale est activé
        self.orientation_verticale=True#la variable orientation_v devient Vrai
        self.destroy()#on ferme la page
        app = Place_les_bateaux(self.orientation_verticale,long_bateau,type_bateau,tableau_PLYR)#on lance la classe qui demande les coordonnées du bateaux et les place et prend comme variable orientation_v la longueur  du bateau et le type de bateau(1,2,3,4,5)
        app.title("Placez votre "+str(self.nom_bateau[type_bateau])+"!")#on donne le titre de la page selon le nom du bateau demandé donc je prend la liste de nom ou sont placé dans l'ordre des types de bateaux donc l'indice donne accés au bon nom
        app.resizable(height = None, width = None)#on donne la taille de la fenetre
        app.mainloop()#on fait tourner la fenetre en boucle
    def orientation_h(self,long_bateau,type_bateau,tableau_PLYR):#programme du bouton quand le bouton horizontale est activé
        self.orientation_verticale=False#la variable orientation_v devient fausse
        self.destroy()#on detruit la page
        app = Place_les_bateaux(self.orientation_verticale,long_bateau,type_bateau,tableau_PLYR)#on lance la classe qui demande les coordonnées du bateaux et les place et prend comme variable orientation_v la longueur  du bateau et le type de bateau(1,2,3,4,5)
        app.title("Placez votre "+str(self.nom_bateau[type_bateau])+"!")
        app.resizable(height = None, width = None)
        app.mainloop()#on fait tourner la fenetre en boucle




class Placement_bombe(tk.Tk):#fenetre qui demande au joueur les coordonéés des 3 bombes
    liste_coo_touche=[]#liste qui enregistre les coordonnées x puis y donc x et en position pair et y en position inpair
    liste_si_touche=[]#liste qui enregistre dans l'ordre des bombes si elles ont touchés
    compteur = 0#compteur d'une nombre de bombe enregistré



    def __init__(self,tableau_touché_PLYR):#on initialise la page en lancant les sous programmes necessaire
        tk.Tk.__init__(self)

        self.initButtons(tableau_touché_PLYR)

    def commande_bouton(self,coord):

        ligne=coord[0]
        colonne=coord[1]
        if tableau_touché_PLYR[ligne][colonne]==0 :
            self.compteur+=1
            if tableau_IA[ligne][colonne]>0:
                 tableau_touché_PLYR[ligne][colonne]=tableau_IA[ligne][colonne]
                 tableau_IA[ligne][colonne]=9
                 self.liste_coo_touche+=[ligne]+[colonne]
                 self.liste_si_touche+=[True]

            else:
                 tableau_touché_PLYR[ligne][colonne]=8
                 self.liste_coo_touche+=[ligne]+[colonne]
                 self.liste_si_touche+=[False]
        else:
            app = Place_deja_prise()
            app.geometry("300x80")
            app.configure(bg="steel blue")
            app.title("OUPS!")
            app.resizable(height = None, width = None)
            app.mainloop()

        if self.compteur==3:
            fenetre.destroy()
            self.destroy()
            self.liste_coo_touche=[]
            self.liste_si_touche=[]

    def initButtons(self,tableau_touché_PLYR):

        for i in range(10):
            Grid.rowconfigure(self, i, weight=1)
            for j in range(10):
                Grid.columnconfigure(self, j, weight=1)

                if tableau_touché_PLYR[i][j]==8:
                    self.label=Label(self, text="A l'eau",bg="light blue").grid(row=i, column=j, sticky=N+S+E+W)


                elif tableau_touché_PLYR[i][j]==0:
                    self.bouton=Button(self, text='L%s-C%s' % (i, j),bg="light green",relief=GROOVE,cursor="target", command=lambda i=i, j=j:self.commande_bouton((i, j))).grid(row=i, column=j, sticky=N+S+E+W)
                else:
                    self.label=Label(self, text="TOUCHEY",bg="red").grid(row=i, column=j, sticky=N+S+E+W)



class Place_deja_prise(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.initButtons()
    def initButtons(self):

        label=Label(self,text="Place déjà prise!",background="steel blue")
        label.pack()
        bouton=Button(self,text="Reesayer",relief=GROOVE,bg="light blue",command=lambda:self.bouton())
        bouton.pack()
    def bouton (self):
        self.destroy()

class Place_les_bateaux(tk.Tk,):
    nom_bateau=("","Frégate","Croiseur","Sous-marin","Cuirrasser","Porte-avion")#liste des noms de bateaux dans l'ordre

    def __init__(self,orientation,long_bateau,type_bateau,tableau_PLYR):
        tk.Tk.__init__(self)

        self.initButtons(orientation,long_bateau,type_bateau,tableau_PLYR)

    def commande_bouton(self,coord,orientation,long_bateau,type_bateau):
        ligne=coord[0]
        colonne=coord[1]
        taille=9-long_bateau


        if (orientation==True and ligne>taille) or (orientation==False and colonne>taille):
            app = Erreur_en_dehors_du_plateau()
            app.geometry("300x80")
            app.configure(bg="steel blue")
            app.title("OUPS!")
            app.resizable(height = None, width = None)
            app.mainloop()
        elif (orientation==True and ligne<taille) or (orientation==False and colonne<taille):
            prise=test_place_prise(tableau_PLYR,long_bateau,colonne,ligne,orientation)
            if prise==True:
                app = Place_deja_prise()
                app.geometry("300x80")
                app.configure(bg="steel blue")
                app.title("OUPS!")
                app.resizable(height = None, width = None)
                app.mainloop()
            else:
                placage(long_bateau,type_bateau,orientation,ligne,colonne)
                self.destroy()






    def initButtons(self,orientation,long_bateau,type_bateau,tableau_PLYR):

        for i in range(10):
            Grid.rowconfigure(self, i, weight=1)
            for j in range(10):
                Grid.columnconfigure(self, j, weight=1)
                if tableau_PLYR[i][j]==0:
                    self.bouton=Button(self, text='L%s-C%s' % (i, j),bg="blue",relief=GROOVE,cursor="tcross", command=lambda i=i, j=j:self.commande_bouton((i, j),orientation,long_bateau,type_bateau)).grid(row=i, column=j, sticky=N+S+E+W)
                elif tableau_PLYR[i][j]==1:
                    self.label=Label(self, text=str(self.nom_bateau[1]),bg="red").grid(row=i, column=j, sticky=N+S+E+W)
                elif tableau_PLYR[i][j]==2:
                    self.label=Label(self, text=str(self.nom_bateau[2]),bg="red").grid(row=i, column=j, sticky=N+S+E+W)
                elif tableau_PLYR[i][j]==3:
                    self.label=Label(self, text=str(self.nom_bateau[3]),bg="red").grid(row=i, column=j, sticky=N+S+E+W)
                elif tableau_PLYR[i][j]==4:
                    self.label=Label(self, text=str(self.nom_bateau[4]),bg="red").grid(row=i, column=j, sticky=N+S+E+W)
                elif tableau_PLYR[i][j]==5:
                    self.label=Label(self, text=str(self.nom_bateau[5]),bg="red").grid(row=i, column=j, sticky=N+S+E+W)

class parti_fini (tk.Tk):
    def __init__(self,fin_partie1,fin_partie2):
        tk.Tk.__init__(self)
        self.fenetre(fin_partie1,fin_partie2)
    def fenetre(self,fin_partie1,fin_partie2):
        canvas = Canvas(self, width=600, height=100, background='sky blue')
        canvas.pack()

        if fin_partie2==True:
            txt=canvas.create_text(300, 25, text="Vous avez perdu!:(", font="Arial 16 italic", fill="black")
        if fin_partie1==True:
            txt=canvas.create_text(300, 25, text="Vous avez gagné! :D", font="Arial 16 italic", fill="black")
        B_rejouer=Button(self,text="Rejouer",command=lambda:self.rejouer())
        W_rejouer = canvas.create_window((100, 70), window=B_rejouer)
        B_quitter=Button(self,text="Quitter",command=lambda:quitter2())
        W_quitter = canvas.create_window((500, 70), window=B_quitter)
    def rejouer(self):
        self.destroy()


class Fenetre_de_jeu(tk.Tk):

    def __init__(self,tableau_IA,tableau_PLYR,tableau_touché_PLYR,tableau_touché_IA,copie_tab_IA,copie_tab_PLYR,mode_triche):
        tk.Tk.__init__(self)
        self.initJEU(tableau_IA,tableau_PLYR,tableau_touché_PLYR,tableau_touché_IA,copie_tab_IA,copie_tab_PLYR,mode_triche)

    def initJEU(self,tableau_IA,tableau_PLYR,tableau_touché_PLYR,tableau_touché_IA,copie_tab_IA,copie_tab_PLYR,mode_triche):


        canvas = Canvas(self, width=1920, height=1080, background='sky blue')

        ovale1= canvas.create_oval(-50,515,1970,565,fill="aquamarine")
        ovale2= canvas.create_oval(-50,-50,1970,50,fill="aquamarine")
        txt = canvas.create_text(950, 20, text="CE QUE VOUS AVEZ TOUCHE", font="Arial 16 italic", fill="black")
        canvas.pack()
        txt2 = canvas.create_text(950, 530, text="VOS BATEAUX", font="Arial 16 italic", fill="black")
        canvas.pack()


        cpt_bateau_enemie=self.nb_reste_bateau(tableau_IA)
        cpt_bateau_joueur=self.nb_reste_bateau(tableau_PLYR)

        canvas.pack()
        txt5 = canvas.create_text(1352, 540, text="Il vous reste "+str(cpt_bateau_joueur)+" bateau(x)", font="Arial 16 italic", fill="black")
        canvas.pack()
        txt5 = canvas.create_text(576, 540, text="L'enemie n'a plus que "+str(cpt_bateau_enemie)+" bateau(x)", font="Arial 16 italic", fill="black")
        canvas.pack()

        lignemilhaut = canvas.create_line(960, 50, 960, 515)
        ligne2 = canvas.create_line(192, 34, 192,524)
        ligne3 = canvas.create_line(384, 42, 384,519)
        ligne4 = canvas.create_line(576, 47, 576,517)
        ligne5 = canvas.create_line(768, 50, 768,515)
        ligne6 = canvas.create_line(1152, 50, 1152,515)
        ligne7 = canvas.create_line(1344, 47, 1344,517)
        ligne8 = canvas.create_line(1536, 42, 1536,519)
        ligne9 = canvas.create_line(1728, 34, 1728,524)

        lignemilbas = canvas.create_line(960, 565, 960, 1080)
        ligne2 = canvas.create_line(192, 556, 192,1080)
        ligne3 = canvas.create_line(384, 561, 384,1080)
        ligne4 = canvas.create_line(576, 563, 576,1080)
        ligne5 = canvas.create_line(768, 565, 768,1080)
        ligne6 = canvas.create_line(1152, 565, 1152,1080)
        ligne7 = canvas.create_line(1344, 563, 1344,1080)
        ligne8 = canvas.create_line(1536, 561, 1536,1080)
        ligne9 = canvas.create_line(1728, 556, 1728,1080)
        #
        tire = Button(self, text=" TIRER ", command=lambda:
        self.bouton_j(tableau_IA,tableau_PLYR,tableau_touché_PLYR,tableau_touché_IA,copie_tab_IA,copie_tab_PLYR) and canvas.config(bg="blue"))
        tire_w = canvas.create_window((960, 565), window=tire)

        save = Button(self, text=" Sauvegarder ", command=lambda:
        self.sauvegarde_tout_tableau())
        save_w = canvas.create_window((960, 55), window=save)

        Regle = Button(self, text="REGLES", command=lambda:
        self.bouton_info() and canvas.config(bg="blue"))
        Regle_w = canvas.create_window((1300, 40), window=Regle)

        for i in range(101,515,46):
            ligne= canvas.create_line(0,i,1920,i)
        for j in range(615,1080,46):
            ligne= canvas.create_line(0,j,1920,j)
        x=self.coo_case_en_x()
        y_tab_bas,y_tab_haut=self.coo_case_tab_y()



        nom_bateau=("","Frégate","Croiseur","Sous-marin","Cuirrasser","Porte-avion")
        for i in range (0,10):#tableau du haut
            for j in range (0,10):
                if mode_triche==True:
                    if tableau_touché_PLYR[i][j]==8:
                        txtremplissage = canvas.create_text(x[j],y_tab_haut[i], text="O", font="Arial 16 italic", fill="black")
                        canvas.pack()

                    elif tableau_touché_PLYR[i][j]==5 or tableau_touché_PLYR[i][j]==4 or tableau_touché_PLYR[i][j]==3 or tableau_touché_PLYR[i][j]==2 or tableau_touché_PLYR[i][j]==1:
                        txtremplissage = canvas.create_text(x[j],y_tab_haut[i], text="X"+nom_bateau[tableau_touché_PLYR[i][j]]+"X", font="Arial 16 italic", fill="red")
                        canvas.pack()
                    else:
                        txtremplissage = canvas.create_text(x[j],y_tab_haut[i], text="-", font="Arial 16 italic", fill="blue")
                        canvas.pack()

                else:
                    if tableau_touché_PLYR[i][j]==8:
                        txtremplissage = canvas.create_text(x[j],y_tab_haut[i], text="O", font="Arial 16 italic", fill="black")
                        canvas.pack()

                    elif tableau_touché_PLYR[i][j]==5 or tableau_touché_PLYR[i][j]==4 or tableau_touché_PLYR[i][j]==3 or tableau_touché_PLYR[i][j]==2 or tableau_touché_PLYR[i][j]==1:
                        txtremplissage = canvas.create_text(x[j],y_tab_haut[i], text="X", font="Arial 16 italic", fill="red")
                        canvas.pack()
                    else:
                        txtremplissage = canvas.create_text(x[j],y_tab_haut[i], text="-", font="Arial 16 italic", fill="blue")
                        canvas.pack()






        for i in range (0,10):#tableau du bas
            for j in range (0,10):
                if tableau_PLYR[i][j]==8:
                    txtremplissage = canvas.create_text(x[j],y_tab_bas[i], text="O", font="Arial 16 italic", fill="black")
                    canvas.pack()

                elif tableau_PLYR[i][j]==9:
                    txtremplissage = canvas.create_text(x[j],y_tab_bas[i], text="X", font="Arial 16 italic", fill="red")
                    canvas.pack()

                elif tableau_PLYR[i][j]==1:
                    txtremplissage = canvas.create_text(x[j],y_tab_bas[i], text="Frégate", font="Arial 16 italic", fill="blue")
                    canvas.pack()

                elif tableau_PLYR[i][j]==2:
                    txtremplissage = canvas.create_text(x[j],y_tab_bas[i], text="Croiseur", font="Arial 16 italic", fill="blue")
                    canvas.pack()

                elif tableau_PLYR[i][j]==3:
                    txtremplissage = canvas.create_text(x[j],y_tab_bas[i], text="Sous-marin", font="Arial 16 italic", fill="blue")
                    canvas.pack()

                elif tableau_PLYR[i][j]==4:
                    txtremplissage = canvas.create_text(x[j],y_tab_bas[i], text="Cuirrasser", font="Arial 16 italic", fill="blue")
                    canvas.pack()

                elif tableau_PLYR[i][j]==5:
                    txtremplissage = canvas.create_text(x[j],y_tab_bas[i], text="Porte-avions", font="Arial 16 italic", fill="blue")
                    canvas.pack()

                else:
                    txtremplissage = canvas.create_text(x[j],y_tab_bas[i], text="-", font="Arial 16 italic", fill="blue")
                    canvas.pack()

    def sauvegarde_tout_tableau(self):
        sauvegarde(tableau_PLYR,"tableau_PLYR")
        sauvegarde(tableau_IA,"tableau_IA")
        sauvegarde(tableau_touché_PLYR,"tableau_touché_PLYR")
        sauvegarde(tableau_touché_IA,"tableau_touché_IA")


    def coo_case_en_x (self):
        #x
        x=[]
        x+=[]

        for i in range (96,1920,192):
            x+=[i]
        return x
    def coo_case_tab_y (self):
        y_tab_bas=[]
        y_tab_bas+=[]
        y_tab_haut=[]
        y_tab_haut+=[]
        for i in range (75,515,46):
            y_tab_haut+=[i]
        for j in range (590,1080,46):
            y_tab_bas+=[j]
        return (y_tab_bas,y_tab_haut)

    def bouton_info(self):
        app=Regles()
        app.geometry("900x150")
        app.configure(bg="steel blue")
        app.title("Les Regles")
        app.mainloop()

    def Tirer(self,tableau_touché_PLYR):
        app = Placement_bombe(tableau_touché_PLYR)
        app.title("Posez vos trois bombes !")
        app.resizable(height = None, width = None)
        app.mainloop()


    def bouton_j(self,tableau_IA,tableau_PLYR,tableau_touché_PLYR,tableau_touché_IA,copie_tab_IA,copie_tab_PLYR):
        app = Placement_bombe(tableau_touché_PLYR)
        app.title("Posez vos trois bombes !")
        app.resizable(height = None, width = None)
        app.mainloop()



    def nb_reste_bateau(self,tab):
        bateau1=True
        bateau2=True
        bateau3=True
        bateau4=True
        bateau5=True
        cpt_bateau=0
        for i in range(0,10):
            for j in range(0,10):
                if tab[i][j]==1 and bateau1:
                    bateau1=False
                    cpt_bateau+=1
                elif tab[i][j]==2 and bateau2:
                    bateau2=False
                    cpt_bateau+=1
                elif tab[i][j]==3 and bateau3:
                    bateau3=False
                    cpt_bateau+=1
                elif tab[i][j]==4 and bateau4:
                    bateau4=False
                    cpt_bateau+=1
                elif tab[i][j]==5 and bateau5:
                    bateau5=False
                    cpt_bateau+=1


        return cpt_bateau

#sous prog---------------------------------------------------------------------------------------------------------------
def sauvegarde(tab,nom_tableau):
    fichier = open(str(nom_tableau), "w")        #Créer le fichier s'il n'existe pas
    fichier.write(str(tab)  )      #à chaque ouverture le contenu du fichier est écrasé. Si le fichier n'existe pas python le crée.
    fichier.close()
def lecture_sauvegarde(nom_tableau):
    fichier = open(str(nom_tableau), "r")
    contenu_sauvegarde=fichier.read()
    fichier.close()
    return contenu_sauvegarde
def traduction(tab,fichier):
    cpt_x=0
    cpt_y=0
    for i in range (0,len(fichier)):

        if fichier[i]=="0"  or  fichier[i]=="1" or  fichier[i]=="2" or  fichier[i]=="3" or  fichier[i]=="4" or  fichier[i]=="5" or  fichier[i]=="8" or  fichier[i]=="9":
            tab[cpt_y][cpt_x]=fichier[i]
            if cpt_x==9:
                cpt_x=0
                cpt_y+=1

            else:
                cpt_x+=1
def bouton_continuer_partie_precedente():
    root.destroy()

    tableau_PLYR_str=lecture_sauvegarde("tableau_PLYR")
    traduction(tableau_PLYR,tableau_PLYR_str)

    tableau_IA_str=lecture_sauvegarde("tableau_IA")
    traduction(tableau_IA,tableau_IA_str)

    tableau_touché_PLYR_str=lecture_sauvegarde("tableau_touché_PLYR")
    traduction(tableau_touché_PLYR,tableau_touché_PLYR_str)

    tableau_touché_IA_str=lecture_sauvegarde("tableau_touché_IA")
    traduction(tableau_touché_IA,tableau_touché_IA_str)
    print(1)
    global mode_triche
    mode_triche=False

def bouton_manu():#sous-prog du bouton ou on place manuellement les bateaux
    root.destroy()#on detruit la fenetre
    placage_des_bateaux_joueurs(tableau_PLYR)#on invoque la fenetre qui demande les coordonnées des bateaux
    global mode_triche
    mode_triche=False
def bouton_auto():#sous-prog du bouton qui place les bateaux automatiquement
    root.destroy()#on détruit la fenetre
    BATEAU(2,1,tableau_PLYR)#fregate , on invoque le sous programme qui place les bateaux aléatoirement dans le tableau indiqué dans la 3e variable , sa longueur dans la premiere et son type dans le 2e
    BATEAU(3,2,tableau_PLYR)#croiseur
    BATEAU(3,3,tableau_PLYR)#sousmarin
    BATEAU(4,4,tableau_PLYR)#cuirasser
    BATEAU(5,5,tableau_PLYR)#porte avions
    global mode_triche
    mode_triche=False


def bouton_triche():#sous-prog du bouton qui place les bateaux manuellement et affiche le tableau de l'ia dans l'invite de commande

    root.destroy()#on detruit la page
    print(tableau_IA)
    BATEAU(2,1,tableau_PLYR)#fregate , on invoque le sous programme qui place les bateaux aléatoirement dans le tableau indiqué dans la 3e variable , sa longueur dans la premiere et son type dans le 2e
    BATEAU(3,2,tableau_PLYR)#croiseur
    BATEAU(3,3,tableau_PLYR)#sousmarin
    BATEAU(4,4,tableau_PLYR)#cuirasser
    BATEAU(5,5,tableau_PLYR)#porte avions
    global mode_triche
    mode_triche=True
def CREATION ():
     tableau=np.full((10,10),0)
     return tableau

def test_place_prise(tableau,long_bateau,colonne,ligne,orientation):#test si la place est prise
    taille=10-long_bateau

    prise=False
    if orientation==0:
         for i in range(0,long_bateau):#test pour les bateaux sur une colonne
             if tableau[ligne][colonne+i]>0:
                 prise=True
    else:
         for j in range(0,long_bateau):#test pour les bateaux sur une ligne
             if tableau[ligne+j][colonne]>0:
                 prise=True

    return prise

def BATEAU (long_bateau,type_bateau,tableau):#placement bateau
    taille=10-long_bateau

    orientation=rand.randint(0,1)#horizontale ou verticale
    if orientation==0:
        ligne=rand.randint(0,9)
        colonne=rand.randint(0,taille)
    else:
        ligne=rand.randint(0,taille)
        colonne=rand.randint(0,9)
    prise = test_place_prise(tableau,long_bateau,colonne,ligne,orientation)#test si la place est prise
    testfin=False
    while testfin==False:
         if prise==True:#si la place est prise on ressort des variables aléatoires
             if orientation==0:
                 ligne=rand.randint(0,9)
                 colonne=rand.randint(0,taille)
             else:
                 ligne=rand.randint(0,taille)
                 colonne=rand.randint(0,9)
             prise = test_place_prise(tableau,long_bateau,colonne,ligne,orientation)
         else : #sinon le tests'arrete
             testfin=True
    for c in range (0,long_bateau):
         if orientation==0:
             tableau[ligne][colonne+c]=type_bateau

         else:
             tableau[ligne+c][colonne]=type_bateau

def placage(long_bateau,type_bateau,orientation,ligne,colonne):#place les bateaux type bateau est le numéro du bateau
    for c in range(0,long_bateau):
        if orientation==False:
            tableau_PLYR[ligne][colonne+c]=type_bateau
        else:
            tableau_PLYR[ligne+c][colonne]=type_bateau

def placage_des_bateaux_joueurs(tableau_PLYR):#demande ou vous voulez placer votre bateau
    longueur_des_bateaux=[0,2,3,3,4,5]
    for i in range (1,6):
        app = Orientation((longueur_des_bateaux[i]),i,tableau_PLYR)
        app.geometry("450x100")
        app.configure(bg="steel blue")
        app.title("Orientation")
        app.resizable(height = None, width = None)
        app.mainloop()
def test_fin_partie (tab):#verifie si il y a encore des beateaux sur le tableau
    fin_partie=True
    for i in range(0,10):
        for j in range(0,10):
            if tab[i][j]>0:
                fin_partie=False
    return fin_partie
def test_pour_IA(ligne,colonne):#verifie si la place est deja prise par une bombe
    testIA=False
    if tableau_touché_IA[ligne][colonne]!=0:
        testIA=False
    else:
        testIA=True
    return testIA

def bombe_IA(touché_coo,toucher_avant):
     lignebombe=[]
     colonnebombe=[]
     liste_coo_touche=[]
     liste_si_touche=[]
     if toucher_avant==False:#si le bateau n'a pas deja touché avant
        dejatoucher=True
        cpt=0
        while cpt<=2 or dejatoucher==True:
             a=rand.randint(0,9)
             b=rand.randint(0,9)
             if tableau_touché_IA[a][b]==0:#si la place est libre
                 dejatoucher=False
                 lignebombe+=[a]
                 colonnebombe+=[b]
                 cpt+=1
             else:#sinon ressort des nombres alea
                 a=rand.randint(0,9)
                 b=rand.randint(0,9)
     else:
         toucher_avant=False
         cptbombe=0
         essayé1=False
         essayé2=False
         essayé3=False
         essayé4=False
         lignetouché=touché_coo[0]
         colonnetouché=touché_coo[1]
         touché_coo=[]
         while cptbombe<=2 :

             if  tableau_IA[lignetouché+1][colonnetouché]==0 and lignetouché!=9 and essayé1==False and (lignetouché+1)<10:
                 lignebombe+=[(lignetouché+1)]
                 colonnebombe+=[(colonnetouché)]
                 essayé1=True

                 cptbombe+=1
             elif tableau_IA[lignetouché-1][colonnetouché]==0 and lignetouché!=0 and essayé2==False and (lignetouché-1)>=0:
                 lignebombe+=[(lignetouché-1)]
                 colonnebombe+=[(colonnetouché)]
                 essayé2=True
                 cptbombe+=1

             elif tableau_IA[lignetouché][colonnetouché-1]==0 and colonnetouché !=0 and essayé3==False and (colonnetouché-1)>=0:
                 lignebombe+=[(lignetouché)]
                 colonnebombe+=[(colonnetouché-1)]
                 essayé3=True
                 cptbombe+=1

             elif tableau_IA[lignetouché][colonnetouché+1]==0 and colonnetouché !=9 and essayé4==False and (colonnetouché+1)<10:
                  colonnebombe+=[(colonnetouché+1)]
                  lignebombe+=[(lignetouché)]
                  essayé4=True
                  cptbombe+=1

             else:
                 dejatoucher=True
                 while dejatoucher==True:
                      a=rand.randint(0,9)
                      b=rand.randint(0,9)
                      if tableau_touché_IA[a][b]==0:#si la place est libre
                          dejatoucher=False
                          lignebombe+=[a]
                          colonnebombe+=[b]
                          cptbombe+=1
                      else:#sinon ressort des nombres alea
                          a=rand.randint(0,9)
                          b=rand.randint(0,9)


     for j in range(0,3):

        coo=tableau_PLYR[lignebombe[j]][colonnebombe[j]]

        if coo==1 or coo==2 or coo==3 or coo==4 or coo==5:
            tableau_touché_IA[lignebombe[j]][colonnebombe[j]]=9
            tableau_PLYR[lignebombe[j]][colonnebombe[j]]=9
            touché_coo=[]
            touché_coo+=[lignebombe[j]]+[colonnebombe[j]]
            toucher_avant=True
            liste_coo_touche+=[lignebombe[j]]+[colonnebombe[j]]
            liste_si_touche+=[True]

        else:
            tableau_touché_IA[lignebombe[j]][colonnebombe[j]]=8
            tableau_PLYR[lignebombe[j]][colonnebombe[j]]=8
            liste_coo_touche+=[lignebombe[j]]+[colonnebombe[j]]
            liste_si_touche+=[False]

     return touché_coo,toucher_avant
def quitter():
    self.destroy()
    partie=False
def copie_tab(tab):
    copie=CREATION()
    for i in range (0,10):
        for j in range(0,10):
            copie[i][j]=tab[i][j]
    return copie
def bateau_coulé (tab_copie,tab):

    copie=copie_tab(tab_copie)

    for k in range (1,6):
        for i in range (0,10):
            for j in range(0,10):
                if copie[i][j]==k and (tab[i][j]==8 or tab[i][j]==9):
                    copie[i][j]=0
        coulé=True
        while coulé==True:
            for i in range(0,10):
                for j in range (0,10):
                    if copie[i][j]==k:
                        coulé=False


            if coulé==True:
                for i in range(0,10):
                    for j in range (0,10):
                        if(tab[i][j]==8 or tab[i][j]==9) and copie[i][j]==0:
                            tab[i][j]=0
            coulé=False
def quitter2():
    parti.destroy()
    partie=False


partie=True
while partie==True:
    # creation des tableau des touches et des bateaux des 2 joueurs
    tableau_touché_PLYR=CREATION()
    tableau_touché_IA=CREATION()
    tableau_PLYR=CREATION()
    tableau_IA=CREATION()
    #remplissage tableau de l'IA
    BATEAU(2,1,tableau_IA)#fregate
    BATEAU(3,2,tableau_IA)#croiseur
    BATEAU(3,3,tableau_IA)#sousmarin
    BATEAU(4,4,tableau_IA)#cuirasser
    BATEAU(5,5,tableau_IA)#porte avions
    copie_tab_IA=copie_tab(tableau_IA)
    root = Tk()
    root.configure(bg="steel blue")
    root.title("Bienvenue !")
    canvas = Canvas(root,width =960 , height =540 )
    canvas.pack()
    photo = PhotoImage(file="anime2.gif")
    canvas.create_image(0,0, image = photo, anchor = NW)
    #creation des bouton pour le mode triche auto et manuel et leur sous programmes d'execustion
    Mode_triche=Button(root,text="Jouer en mode triche",relief=GROOVE,bg="light blue",command=lambda:bouton_triche()).pack( padx=10, pady=10)
    Mode_normal_manu=Button(root,text="Jouer en mode normal(placement manuel)",bg="light blue",anchor='w',relief=GROOVE,command=lambda:bouton_manu()).pack(padx=10, pady=10)
    Mode_normal_auto=Button(root,text="Jouer en mode normal(placement Automatique)",bg="light blue",relief=GROOVE,command=lambda:bouton_auto()).pack( padx=10, pady=10)
    Mode_continuer_Partie_precedente=Button(root,text="Continuer la partie precedente",bg="light blue",relief=GROOVE,command=lambda:bouton_continuer_partie_precedente()).pack( padx=10, pady=10)
    root.mainloop()

    copie_tab_PLYR=copie_tab(tableau_PLYR)
    touché_coo=[]
    toucher_avant=False
    fin_partie1=False
    fin_partie2=False
    while fin_partie1==False and fin_partie2==False:
        print(tableau_PLYR)
        fenetre=Fenetre_de_jeu(tableau_IA,tableau_PLYR,tableau_touché_PLYR,tableau_touché_IA,copie_tab_IA,copie_tab_PLYR,mode_triche)
        fenetre.title("Partie en cours")
        fenetre.resizable(height = None, width = None)

        fenetre.mainloop()

        touché_coo,toucher_avant=bombe_IA(touché_coo,toucher_avant)
        bateau_coulé(copie_tab_PLYR,tableau_PLYR)
        bateau_coulé(copie_tab_IA,tableau_IA)
        fin_partie1=test_fin_partie(tableau_IA)
        fin_partie2=test_fin_partie(tableau_PLYR)#le test sort le booleen en vrai si il n'y a plus de bateaux dans le tableau donc arrete la partie
        print(fin_partie1)
        print(fin_partie2)

    parti=parti_fini(fin_partie1,fin_partie2)
    parti.title("Partie terminé")
    parti.mainloop()
