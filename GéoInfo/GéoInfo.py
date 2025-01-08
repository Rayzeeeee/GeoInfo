from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

#Gestion globale de l'application
root = Tk() # Création de la fenêtre

#Gestion du placement de la fenêtre dans l'écran
Largeur = 750
Hauteur = 700
Largeur_ecran= root.winfo_screenwidth()
Hauteur_ecran = root.winfo_screenheight()
Horizontal = (Largeur_ecran/2) - (Largeur/2)
Verticale = (Hauteur_ecran/2) - (Hauteur/2)
root.title('GéoInfo') # Titre de la fenêtre
root.iconbitmap('GéoInfo\Ressources\Icons\Earth_design.ico') # Icone de la fenêtre
root.geometry('%dx%d+%d+%d' % (Largeur, Hauteur, Horizontal, Verticale)) # Résolution de la fenêtre
root.configure(bg="#292929")
root.resizable(height=False, width=False)


#Gestion des paramètres et positions de la liste des pays
list_frame = Frame(root)
list_frame.place(x=80, y=150)
list_frame.configure(bg="#292929")

#Gestion des paramètres et positions des infos pays
info_frame = Frame(root)
info_frame.place(x=120, y=370)
info_frame.configure(bg="#292929")

# Mettre à jour la liste des pays
def update_pays_list(data):
    Pays_list.delete(0, END)  # Supprimer les éléments actuelles de la listbox
    
    # Mettre à jour la list box avec les pays fournis dans data
    for item in data:
        Pays_list.insert(END, item)

# Affiche le pays sélectionnez dans la listbox dans la barre de recherche
def select_pays(e):
    Barre_recherche.delete(0, END)
    Barre_recherche.insert(0, Pays_list.get(ANCHOR))

# Vérification de la recherche
def verif_recherche(e):
    taped = Barre_recherche.get() # Récupération du texte saisie dans la barre de recherche

    if taped == '': # Si la barre de recherche est vide
        data = pays # Afficher tous les pays
    else:
        data = [] # Liste vide pour stocker les pays qui corresponde à la recherche
        for item in pays:
            if taped.lower() in item.lower(): # Vérifie si le texte de la barre de recherche correspond à un pays
                data.append(item) # Ajouter les pays filtrées à la liste vide

    update_pays_list(data) # Mettre à jour la list box avec les pays filtrés

#Affichage des infos
def info(e):
    Recherche = Barre_recherche.get()
    if Recherche in pays:                                                     # Si Le pays rentrer et dans le dictionnaire des pays
        info_pays = pays[Recherche]                                           # Récupère les informations du dictionnaire
        print("-----------------------------------------------------")        # Affichage ligne séparation dans la console
        for titre, info_titre in info_pays.items():                           # Boucle pour afficher les informations du pays
            print(f"{titre}: {info_titre}")
            titre_info = (f"{titre}:")                                        # Récupération du texte dans le titre du dictionnaire
            titre_widget = StringVar()
            titre_widget = Label(info_frame, text=titre_info ,font=("Segoe UI Black", 14), fg="White", bg="#292929") # Affichage des titres d'infos (Capitales...)
            titre_widget.pack(side="top")

            pays_info = (f"{info_titre}")
            info_widget = StringVar()
            info_widget = Label(info_frame, text=pays_info ,font=("Segoe UI", 14), fg="White", bg="#292929")
            info_widget.pack(side="top")
        print("-----------------------------------------------------")
    
    else:
        messagebox.showerror("Erreur", "Pays invalide !")                          # Message d'erreur
        print("Désolé, les informations sur ce pays ne sont pas disponibles.")     # Affichage message d'erreur si le pays n'est pas valide


# Logo en haut à gauche de la page
PIL_logo = Image.open("GéoInfo\Ressources\Icons\Earth_design.png")
PIL_logo_resize = PIL_logo.resize((35, 35))
logo = ImageTk.PhotoImage(PIL_logo_resize)
logo_label = Label(root, image=logo, bg="#292929")
logo_label.place(x=5, y=4)

# Titre au-dessus de la page
Title = Label(root, text="GéoInfo", font=("Segoe UI Black", 16), fg="White", bg="#292929") 
Title.place(x=50, y=5) 

limite1 = Canvas(root, width=750, height=1, bg="#6a6a6a", highlightbackground="#6a6a6a", highlightthickness  = 1, bd = 0) # Barre de délimitation List -> Infos
limite1.place(x=0, y=45)
#---------------------------------------------------

# Texte au dessus de la barre de recherche
Texte_barre_recherche = Label(root, text="Entrer le nom du pays", font=("Segoe UI Black", 16), fg="White", bg="#292929")
Texte_barre_recherche.place(x=115, y=50)

## Barre de recherche
Barre_recherche = Entry(root, width=31, font=("Segoe UI", 16), fg="White", bg="#434343", bd="1", relief=FLAT, insertbackground="White") ## Barre de recherche
Barre_recherche.place(x=60, y=90)

# Bouton de recherche
PIL_valider = Image.open("GéoInfo\Ressources\Icons\loupe.png")
PIL_valider_resize = PIL_valider.resize((20, 20))
valider = ImageTk.PhotoImage(PIL_valider_resize)
valider_label = Button(root, image=valider, bg="#434343", bd=0, width=25, height=25, relief=FLAT, activebackground="#434343", command=lambda:info(root))
valider_label.place(x=375, y=93)

# Barre de défilement de la liste
scrollbar = Scrollbar(list_frame)
scrollbar.pack(side=RIGHT, fill=Y)

# Liste des pays
Pays_list = Listbox(list_frame, width=40, font=("Segoe UI", 10), yscrollcommand=scrollbar.set, fg="White", bg="#434343")
Pays_list.pack(side="top")
scrollbar.config(command=Pays_list.yview)    # Liaison Scrollbar -> List

# ----------------------------------------------------
limite2 = Canvas(root, width=750, height=1, bg="#6a6a6a", highlightbackground="#6a6a6a", highlightthickness  = 1, bd = 0)
limite2.place(x=0, y=350)

version = Label(root, text="Version 1.0")



pays = {
    # Asie
    "Afghanistan": {
        "Capitale": "Kaboul",
        "Président": "Hibatullah Akhundzada",
        "Superficie": "652,230 km²",
        "Population": "38 928 341 habitants",
        "Langues": ["Pachto", "Dari"] 
    },

    "Algérie": {
        "Capitale": "Alger",
        "Président": "Abdelmadjid Tebboune",
        "Superficie": "2,381,741 km²",
        "Population": "45 750 000 habitants",
        "Langues": ["Arabe", "Berbère"]
    },

    "Angola": {
        "Capitale": "Luanda",
        "Président": "João Lourenço",
        "Superficie": "1,246,700 km²",
        "Population": "34 646 000 habitants",
        "Langues": ["Portugais"]
    },

    "Antigua-et-Barbuda": {
        "Capitale": "Saint John's",
        "Président": "Gaston Browne",
        "Superficie": "442 km²",
        "Population": "97 929 habitants",
        "Langues": ["Anglais"]
    },

    "Arabie saoudite": {
        "Capitale": "Riyad",
        "Président": "Salmane ben Abdelaziz Al Saoud",
        "Superficie": "2,149,690 km²",
        "Population": "35 340 676 habitants",
        "Langues": ["Arabe"]
    },

    "Argentine": {
        "Capitale": "Buenos Aires",
        "Président": "Javier Milei",
        "Superficie": "2,780,400 km²",
        "Population": "45 605 829 habitants",
        "Langues": ["Espagnol"]
    },

    "Arménie": {
        "Capitale": "Erevan",
        "Président": "Vahagn Khatchatourian",
        "Superficie": "29,743 km²",
        "Population": "2 963 243 habitants",
        "Langues": ["Arménien"]
    },

    "Australie": {
        "Capitale": "Canberra",
        "Président": "Charles III",
        "Superficie": "7,692,024 km²",
        "Population": "25 687 041 habitants",
        "Langues": ["Anglais"]
    },

    "Azerbaïdjan": {
        "Capitale": "Bakou",
        "Président": "Ilham Aliyev",
        "Superficie": "86,600 km²",
        "Population": "10 139 177 habitants",
        "Langues": ["Azéri"]
    },

    "Bahamas": {
        "Capitale": "Nassau",
        "Président": "Philip Davis",
        "Superficie": "13,878 km²",
        "Population": "391 232 habitants",
        "Langues": ["Anglais"]
    },

    "Bahreïn": {
        "Capitale": "Manama",
        "Président": "Hamad ben Issa Al Khalifa",
        "Superficie": "765 km²",
        "Population": "1 701 575 habitants",
        "Langues": ["Arabe"]
    },

    "Bangladesh": {
        "Capitale": "Dacca",
        "Président": "Mohammad Shahabuddin",
        "Superficie": "147,570 km²",
        "Population": "164 689 383 habitants",
        "Langues": ["Bengali"]
    },

    "Barbade": {
        "Capitale": "Bridgetown",
        "Président": "Sandra Mason",
        "Superficie": "430 km²",
        "Population": "287 730 habitants",
        "Langues": ["Anglais"]
    },

    "Belgique": {
        "Capitale": "Bruxelles",
        "Président": "Alexander De Croo",
        "Superficie": "30,528 km²",
        "Population": "11 582 808 habitants",
        "Langues": ["Néerlandais", "Français", "Allemand"]
    },

    "Bénin": {
        "Capitale": "Porto-Novo",
        "Président": "Patrice Talon",
        "Superficie": "114,763 km²",
        "Population": "12 864 634 habitants",
        "Langues": ["Français"]
    },

    "Belize": {
        "Capitale": "Belmopan",
        "Président": "Johnny Briceño",
        "Superficie": "22,966 km²",
        "Population": "419 199 habitants",
        "Langues": ["Anglais"]
    },

    "Bhoutan": {
        "Capitale": "Thimphou",
        "Président": "Jigme Khesar Namgyel Wangchuck",
        "Superficie": "38,394 km²",
        "Population": "779 631 habitants",
        "Langues": ["Dzongkha"]
    },

    "Birmanie": {
        "Capitale": "Naypyidaw",
        "Président": "Myint Swe",
        "Superficie": "676,578 km²",
        "Population": "54 409 800 habitants",
        "Langues": ["Birman"]
    },

    "Bolivie": {
        "Capitale": "Sucre",
        "Président": "Luis Arce",
        "Superficie": "1,098,581 km²",
        "Population": "11 673 021 habitants",
        "Langues": ["Espagnol", "Quechua", "Aymara"]
    },

    "Botswana": {
        "Capitale": "Gaborone",
        "Président": "Mokgweetsi Masisi",
        "Superficie": "581,730 km²",
        "Population": "2 391 750 habitants",
        "Langues": ["Anglais", "Tswana"]
    },

    "Brésil": {
        "Capitale": "Brasília",
        "Président": "Luiz Inácio Lula da Silva",
        "Superficie": "8,515,767 km²",
        "Population": "213 993 437 habitants",
        "Langues": ["Portugais"]
    },

    "Brunei": {
        "Capitale": "Bandar Seri Begawan",
        "Président": "Hassanal Bolkiah",
        "Superficie": "5,765 km²",
        "Population": "437 479 habitants",
        "Langues": ["Malais"]
    },

    "Burkina Faso": {
        "Capitale": "Ouagadougou",
        "Président": "Ibrahim Traoré",
        "Superficie": "274,200 km²",
        "Population": "21 510 181 habitants",
        "Langues": ["Français"]
    },

    "Burundi": {
        "Capitale": "Gitega",
        "Président": "Évariste Ndayishimiye",
        "Superficie": "27,834 km²",
        "Population": "12 213 565 habitants",
        "Langues": ["Kirundi", "Français"]
    },

    "Cambodge": {
        "Capitale": "Phnom Penh",
        "Président": "Norodom Sihamoni",
        "Superficie": "181,035 km²",
        "Population": "16 718 965 habitants",
        "Langues": ["Khmer"]
    },

    "Cameroun": {
        "Capitale": "Yaoundé",
        "Président": "Paul Biya",
        "Superficie": "475,442 km²",
        "Population": "27 743 967 habitants",
        "Langues": ["Français", "Anglais"]
    },

    "Canada": {
        "Capitale": "Ottawa",
        "Président": "Charles III",
        "Superficie": "9,984,670 km²",
        "Population": "38 008 005 habitants",
        "Langues": ["Anglais", "Français"]
    },

    "Cap Vert": {
        "Capitale": "Praia",
        "Président": "José Maria Neves",
        "Superficie": "4,033 km²",
        "Population": "560 899 habitants",
        "Langues": ["Portugais"]
    },

    "Chili": {
        "Capitale": "Santiago",
        "Président": "Gabriel Boric",
        "Superficie": "756,096 km²",
        "Population": "19 493 300 habitants",
        "Langues": ["Espagnol"]
    },

    "Chine": {
        "Capitale": "Pékin",
        "Président": "Xi Jinping",
        "Superficie": "9,596,961 km²",
        "Population": "1 411 778 724 habitants",
        "Langues": ["Chinois"]
    },

    "Chypre": {
        "Capitale": "Nicosie",
        "Président": "Níkos Anastasiádis",
        "Superficie": "9,251 km²",
        "Population": "1 207 359 habitants",
        "Langues": ["Grec", "Turc"]
    },

    "Colombie": {
        "Capitale": "Bogota",
        "Président": "Gustavo Petro",
        "Superficie": "1,141,748 km²",
        "Population": "50 882 884 habitants",
        "Langues": ["Espagnol"]
    },

    "Comores": {
        "Capitale": "Moroni",
        "Président": "Azali Assoumani",
        "Superficie": "2,034 km²",
        "Population": "873 724 habitants",
        "Langues": ["Comorien", "Arabe", "Français"]
    },

    "Corée du Nord": {
        "Capitale": "Pyongyang",
        "Président": "Kim Jong-un",
        "Superficie": "120,538 km²",
        "Population": "25 778 816 habitants",
        "Langues": ["Coréen"]
    },

    "Corée du Sud": {
        "Capitale": "Séoul",
        "Président": "Yoon Suk-yeol",
        "Superficie": "100,210 km²",
        "Population": "51 780 579 habitants",
        "Langues": ["Coréen"]
    },

    "Costa Rica": {
        "Capitale": "San José",
        "Président": "Rodrigo Chaves Robles",
        "Superficie": "51,100 km²",
        "Population": "5 094 118 habitants",
        "Langues": ["Espagnol"]
    },

    "Côte d'Ivoire": {
        "Capitale": "Yamoussoukro",
        "Président": "Alassane Ouattara",
        "Superficie": "322,463 km²",
        "Population": "27 480 153 habitants",
        "Langues": ["Français"]
    },

    "Cuba": {
        "Capitale": "La Havane",
        "Président": "Miguel Díaz-Canel",
        "Superficie": "109,884 km²",
        "Population": "11 326 616 habitants",
        "Langues": ["Espagnol"]
    },

    "Djibouti": {
        "Capitale": "Djibouti",
        "Président": "Ismaïl Omar Guelleh",
        "Superficie": "23,200 km²",
        "Population": "994 372 habitants",
        "Langues": ["Français", "Arabe"]
    },

    "Dominique": {
        "Capitale": "Roseau",
        "Président": "Roosevelt Skerrit",
        "Superficie": "751 km²",
        "Population": "71 986 habitants",
        "Langues": ["Anglais"]
    },

    "Égypte": {
        "Capitale": "Le Caire",
        "Président": "Abdel Fattah al-Sissi",
        "Superficie": "1,010,408 km²",
        "Population": "104 258 326 habitants",
        "Langues": ["Arabe"]
    },

    "Émirats arabes unis": {
        "Capitale": "Abou Dabi",
        "Président": "Mohammed ben Zayed Al Nahyane",
        "Superficie": "83,600 km²",
        "Population": "9 890 402 habitants",
        "Langues": ["Arabe"]
    },

    "Équateur": {
        "Capitale": "Quito",
        "Président": "Daniel Noboa",
        "Superficie": "283,561 km²",
        "Population": "17 643 644 habitants",
        "Langues": ["Espagnol"]
    },

    "Érythrée": {
        "Capitale": "Asmara",
        "Président": "Isaias Afwerki",
        "Superficie": "117,600 km²",
        "Population": "3 546 430 habitants",
        "Langues": ["Tigrigna", "Arabe"]
    },

    "Espagne": {
        "Capitale": "Madrid",
        "Président": "Pedro Sánchez",
        "Superficie": "505,992 km²",
        "Population": "47 351 567 habitants",
        "Langues": ["Espagnol"]
    },

    "Eswatini": {
        "Capitale": "Mbabane",
        "Président": "Mswati III (Roi)",
        "Superficie": "17,364 km²",
        "Population": "1 164 935 habitants",
        "Langues": ["Swazi", "Anglais"]
    },

    "États-Unis": {
        "Capitale": "Washington, D.C.",
        "Président": "Joe Biden",
        "Superficie": "9,833,517 km²",
        "Population": "331 893 745 habitants",
        "Langues": ["Anglais"]
    },

    "Éthiopie": {
        "Capitale": "Addis-Abeba",
        "Président": "Sahle-Work Zewde",
        "Superficie": "1,104,300 km²",
        "Population": "118 247 865 habitants",
        "Langues": ["Amharique"]
    },

    "Fidji": {
        "Capitale": "Suva",
        "Président": "Wiliame Katonivere",
        "Superficie": "18,274 km²",
        "Population": "896 445 habitants",
        "Langues": ["Anglais", "Fidjien", "Hindi"]
    },

    "France": {
        "Capitale": "Paris",
        "Président": "Emmanuel Macron",
        "Superficie": "640,679 km²",
        "Population": "67 713 000 habitants",
        "Langues": ["Français"]
    },

    "Gabon": {
        "Capitale": "Libreville",
        "Président": "Ali Bongo Ondimba",
        "Superficie": "267,667 km²",
        "Population": "2 256 440 habitants",
        "Langues": ["Français"]
    },

    "Gambie": {
        "Capitale": "Banjul",
        "Président": "Adama Barrow",
        "Superficie": "11,300 km²",
        "Population": "2 486 941 habitants",
        "Langues": ["Anglais"]
    },

    "Géorgie": {
        "Capitale": "Tbilissi",
        "Président": "Salomé Zourabichvili",
        "Superficie": "69,700 km²",
        "Population": "3 714 085 habitants",
        "Langues": ["Géorgien"]
    },

    "Ghana": {
        "Capitale": "Accra",
        "Président": "Nana Akufo-Addo",
        "Superficie": "238,533 km²",
        "Population": "31 504 467 habitants",
        "Langues": ["Anglais"]
    },

    "Grenade": {
        "Capitale": "Saint-Georges",
        "Président": "Dickon Mitchell",
        "Superficie": "344 km²",
        "Population": "112 523 habitants",
        "Langues": ["Anglais"]
    },

    "Guatemala": {
        "Capitale": "Ciudad de Guatemala",
        "Président": "Bernardo Arévalo",
        "Superficie": "108,889 km²",
        "Population": "18 244 522 habitants",
        "Langues": ["Espagnol"]
    },

    "Guinée": {
        "Capitale": "Conakry",
        "Président": "Mamady Doumbouya",
        "Superficie": "245,857 km²",
        "Population": "13 469 192 habitants",
        "Langues": ["Français"]
    },

    "Guinée Bissau": {
        "Capitale": "Bissau",
        "Président": "Umaro Sissoco Embaló",
        "Superficie": "36,125 km²",
        "Population": "1 986 107 habitants",
        "Langues": ["Portugais"]
    },

    "Guinée équatoriale": {
        "Capitale": "Malabo",
        "Président": "Teodoro Obiang Nguema Mbasogo",
        "Superficie": "28,051 km²",
        "Population": "1 454 789 habitants",
        "Langues": ["Espagnol", "Français"]
    },

    "Guyana": {
        "Capitale": "Georgetown",
        "Président": "Irfaan Ali",
        "Superficie": "214,969 km²",
        "Population": "786 552 habitants",
        "Langues": ["Anglais"]
    },

    "Haïti": {
        "Capitale": "Port-au-Prince",
        "Président": "Ariel Henry",
        "Superficie": "27,750 km²",
        "Population": "11 402 528 habitants",
        "Langues": ["Français", "Créole haïtien"]
    },

    "Honduras": {
        "Capitale": "Tegucigalpa",
        "Président": "Xiomara Castro",
        "Superficie": "112,492 km²",
        "Population": "9 904 607 habitants",
        "Langues": ["Espagnol"]
    },

    "Inde": {
        "Capitale": "New Delhi",
        "Président": "Droupadi Murmu",
        "Superficie": "3,287,263 km²",
        "Population": "1 393 409 038 habitants",
        "Langues": ["Hindi", "Anglais"]
    },

    "Indonésie": {
        "Capitale": "Jakarta",
        "Président": "Joko Widodo",
        "Superficie": "1,904,569 km²",
        "Population": "273 523 615 habitants",
        "Langues": ["Indonésien"]
    },

    "Irak": {
        "Capitale": "Bagdad",
        "Président": "Abdul Latif Rashid",
        "Superficie": "438,317 km²",
        "Population": "40 222 493 habitants",
        "Langues": ["Arabe", "Kurde"]
    },

    "Iran": {
        "Capitale": "Téhéran",
        "Président": "Ebrahim Raïssi",
        "Superficie": "1,648,195 km²",
        "Population": "83 992 946 habitants",
        "Langues": ["Persan"]
    },

    "Îles Marshall": {
        "Capitale": "Majuro",
        "Président": "David Kabua",
        "Superficie": "181 km²",
        "Population": "59 190 habitants",
        "Langues": ["Anglais", "Marshallais"]
    },

    "Îles Salomon": {
        "Capitale": "Honiara",
        "Président": "David Vunagi",
        "Superficie": "28,896 km²",
        "Population": "686 878 habitants",
        "Langues": ["Anglais"]
    },

    "Israel": {
        "Capitale": "Jérusalem",
        "Président": "Isaac Herzog",
        "Superficie": "20,770 km²",
        "Population": "9 053 300 habitants",
        "Langues": ["Hébreu", "Arabe"]
    },

    "Italie": {
        "Capitale": "Rome",
        "Président": "Sergio Mattarella",
        "Superficie": "301,338 km²",
        "Population": "58 982 687 habitants",
        "Langues": ["Italien"]
    },

    "Jamaïque": {
        "Capitale": "Kingston",
        "Président": "Andrew Holness",
        "Superficie": "10,991 km²",
        "Population": "2 961 167 habitants",
        "Langues": ["Anglais"]
    },

    "Japon": {
        "Capitale": "Tokyo",
        "Président": "Naruhito",
        "Superficie": "377,975 km²",
        "Population": "125 810 000 habitants",
        "Langues": ["Japonais"]
    },

    "Jordanie": {
        "Capitale": "Amman",
        "Président": "Abdallah II",
        "Superficie": "89,342 km²",
        "Population": "10 203 134 habitants",
        "Langues": ["Arabe"]
    },

    "Kazakhstan": {
        "Capitale": "Astana",
        "Président": "Kassym-Jomart Tokaïev",
        "Superficie": "2,724,900 km²",
        "Population": "18 776 092 habitants",
        "Langues": ["Kazakh", "Russe"]
    },

    "Kenya": {
        "Capitale": "Nairobi",
        "Président": "William Ruto",
        "Superficie": "580,367 km²",
        "Population": "54 985 698 habitants",
        "Langues": ["Swahili", "Anglais"]
    },

    "Kirghizistan": {
        "Capitale": "Bichkek",
        "Président": "Sadyr Japarov",
        "Superficie": "199,951 km²",
        "Population": "6 524 195 habitants",
        "Langues": ["Kirghiz", "Russe"]
    },

    "Kiribati": {
        "Capitale": "Tarawa-Sud",
        "Président": "Taneti Maamau",
        "Superficie": "811 km²",
        "Population": "119 449 habitants",
        "Langues": ["Anglais"]
    },

    "Koweït": {
        "Capitale": "Koweït",
        "Président": "Nawaf Al-Ahmad Al-Jaber Al-Sabah",
        "Superficie": "17,818 km²",
        "Population": "4 270 571 habitants",
        "Langues": ["Arabe"]
    },

    "Laos": {
        "Capitale": "Vientiane",
        "Président": "Thongloun Sisoulith",
        "Superficie": "236,800 km²",
        "Population": "7 275 560 habitants",
        "Langues": ["Lao"]
    },

    "Lesotho": {
        "Capitale": "Maseru",
        "Président": "Letsie III (Roi)",
        "Superficie": "30,355 km²",
        "Population": "2 153 514 habitants",
        "Langues": ["Sotho du Sud", "Anglais"]
    },

    "Liban": {
        "Capitale": "Beyrouth",
        "Président": "Michel Aoun",
        "Superficie": "10,452 km²",
        "Population": "6 825 445 habitants",
        "Langues": ["Arabe"]
    },

    "Libéria": {
        "Capitale": "Monrovia",
        "Président": "George Weah",
        "Superficie": "111,369 km²",
        "Population": "5 160 335 habitants",
        "Langues": ["Anglais"]
    },

    "Libye": {
        "Capitale": "Tripoli",
        "Président": "Mohamed al-Menfi",
        "Superficie": "1,759,540 km²",
        "Population": "6 977 429 habitants",
        "Langues": ["Arabe"]
    },

    "Madagascar": {
        "Capitale": "Antananarivo",
        "Président": "Andry Rajoelina",
        "Superficie": "587,041 km²",
        "Population": "28 427 310 habitants",
        "Langues": ["Malgache", "Français"]
    },

    "Malaisie": {
        "Capitale": "Kuala Lumpur",
        "Président": "Abdullah de Pahang",
        "Superficie": "330,803 km²",
        "Population": "32 365 999 habitants",
        "Langues": ["Malais"]
    },

    "Malawi": {
        "Capitale": "Lilongwe",
        "Président": "Lazarus Chakwera",
        "Superficie": "118,484 km²",
        "Population": "19 722 622 habitants",
        "Langues": ["Anglais", "Chewa"]
    },

    "Mali": {
        "Capitale": "Bamako",
        "Président": "Assimi Goïta",
        "Superficie": "1,240,192 km²",
        "Population": "20 855 555 habitants",
        "Langues": ["Français"]
    },

    "Maldives": {
        "Capitale": "Malé",
        "Président": "Ibrahim Mohamed Solih",
        "Superficie": "298 km²",
        "Population": "540 544 habitants",
        "Langues": ["Divehi"]
    },

    "Maroc": {
        "Capitale": "Rabat",
        "Président": "Mohammed VI (Roi)",
        "Superficie": "446,550 km²",
        "Population": "37 108 501 habitants",
        "Langues": ["Arabe", "Berbère"]
    },

    "Maurice": {
        "Capitale": "Port-Louis",
        "Président": "Prithvirajsing Roopun",
        "Superficie": "2,040 km²",
        "Population": "1 273 072 habitants",
        "Langues": ["Anglais", "Français"]
    },

    "Mauritanie": {
        "Capitale": "Nouakchott",
        "Président": "Mohamed Ould Ghazouani",
        "Superficie": "1,030,700 km²",
        "Population": "4 687 606 habitants",
        "Langues": ["Arabe"]
    },

    "Mexique": {
        "Capitale": "Mexico",
        "Président": "Andrés Manuel López Obrador",
        "Superficie": "1,964,375 km²",
        "Population": "128 932 753 habitants",
        "Langues": ["Espagnol"]
    },

    "Micronésie": {
        "Capitale": "Palikir",
        "Président": "Wesley Simina",
        "Superficie": "702 km²",
        "Population": "115 023 habitants",
        "Langues": ["Anglais"]
    },

    "Mongolie": {
        "Capitale": "Oulan-Bator",
        "Président": "Ukhnaagiin Khürelsükh",
        "Superficie": "1,564,116 km²",
        "Population": "3 278 290 habitants",
        "Langues": ["Mongol"]
    },

    "Mozambique": {
        "Capitale": "Maputo",
        "Président": "Filipe Nyusi",
        "Superficie": "801,590 km²",
        "Population": "32 063 476 habitants",
        "Langues": ["Portugais"]
    },

    "Namibie": {
        "Capitale": "Windhoek",
        "Président": "Hage Geingob",
        "Superficie": "825,615 km²",
        "Population": "2 550 604 habitants",
        "Langues": ["Anglais"]
    },

    "Nauru": {
        "Capitale": "Yaren",
        "Président": "Russ Kun",
        "Superficie": "21 km²",
        "Population": "10 824 habitants",
        "Langues": ["Anglais", "Nauruan"]
    },

    "Népal": {
        "Capitale": "Katmandou",
        "Président": "Ram Chandra Poudel",
        "Superficie": "147,181 km²",
        "Population": "29 164 578 habitants",
        "Langues": ["Népalais"]
    },

    "Nicaragua": {
        "Capitale": "Managua",
        "Président": "Daniel Ortega",
        "Superficie": "130,373 km²",
        "Population": "6 624 554 habitants",
        "Langues": ["Espagnol"]
    },

    "Niger": {
        "Capitale": "Niamey",
        "Président": "Mohamed Bazoum",
        "Superficie": "1,267,000 km²",
        "Population": "25 223 447 habitants",
        "Langues": ["Français"]
    },

    "Nigeria": {
        "Capitale": "Abuja",
        "Président": "Bola Tinubu",
        "Superficie": "923,768 km²",
        "Population": "211 400 708 habitants",
        "Langues": ["Anglais"]
    },

    "Nouvelle-Zélande": {
        "Capitale": "Wellington",
        "Président": "Charles III",
        "Superficie": "268,021 km²",
        "Population": "5 084 300 habitants",
        "Langues": ["Anglais", "Maori"]
    },

    "Oman": {
        "Capitale": "Mascate",
        "Président": "Haitham ben Tariq",
        "Superficie": "309,500 km²",
        "Population": "4 667 407 habitants",
        "Langues": ["Arabe"]
    },

    "Ouganda": {
        "Capitale": "Kampala",
        "Président": "Yoweri Museveni",
        "Superficie": "241,550 km²",
        "Population": "47 785 495 habitants",
        "Langues": ["Anglais", "Swahili"]
    },

    "Ouzbékistan": {
        "Capitale": "Tachkent",
        "Président": "Shavkat Mirziyoyev",
        "Superficie": "447,400 km²",
        "Population": "34 232 200 habitants",
        "Langues": ["Ouzbek"]
    },

    "Pakistan": {
        "Capitale": "Islamabad",
        "Président": "Arif Alvi",
        "Superficie": "796,095 km²",
        "Population": "220 892 340 habitants",
        "Langues": ["Ourdou", "Anglais"]
    },

    "Palaos": {
        "Capitale": "Ngerulmud",
        "Président": "Surangel Whipps Jr.",
        "Superficie": "459 km²",
        "Population": "18 092 habitants",
        "Langues": ["Anglais", "Paluan"]
    },

    "Palestine": {
        "Capitale": "Jérusalem",
        "Président": "Mahmoud Abbas",
        "Superficie": "6,025 km²",
        "Population": "5 166 000 habitants",
        "Langues": ["Arabe"]
    },

    "Panama": {
        "Capitale": "Panama",
        "Président": "Laurentino Cortizo",
        "Superficie": "75,417 km²",
        "Population": "4 378 343 habitants",
        "Langues": ["Espagnol"]
    },

    "Papouasie-Nouvelle-Guinée": {
        "Capitale": "Port Moresby",
        "Président": "Charles III",
        "Superficie": "462,840 km²",
        "Population": "8 947 024 habitants",
        "Langues": ["Anglais", "Tok Pisin", "Hiri Motu"]
    },

    "Paraguay": {
        "Capitale": "Asunción",
        "Président": "Santiago Peña",
        "Superficie": "406,752 km²",
        "Population": "7 359 002 habitants",
        "Langues": ["Espagnol", "Guarani"]
    },

    "Pays-Bas": {
        "Capitale": "Amsterdam",
        "Président": "Mark Rutte",
        "Superficie": "41,543 km²",
        "Population": "17 595 017 habitants",
        "Langues": ["Néerlandais"]
    },

    "Pérou": {
        "Capitale": "Lima",
        "Président": "Dina Boluarte",
        "Superficie": "1,285,216 km²",
        "Population": "33 296 434 habitants",
        "Langues": ["Espagnol", "Quechua", "Aymara"]
    },

    "Philippines": {
        "Capitale": "Manille",
        "Président": "Bongbong Marcos",
        "Superficie": "300,000 km²",
        "Population": "110 818 325 habitants",
        "Langues": ["Filipino", "Anglais"]
    },

    "Portugal": {
        "Capitale": "Lisbonne",
        "Président": "Marcelo Rebelo de Sousa",
        "Superficie": "92,090 km²",
        "Population": "10 291 027 habitants",
        "Langues": ["Portugais"]
    },

    "Qatar": {
        "Capitale": "Doha",
        "Président": "Tamim ben Hamad Al Thani",
        "Superficie": "11,586 km²",
        "Population": "2 881 053 habitants",
        "Langues": ["Arabe"]
    },

    "République centrafricaine": {
        "Capitale": "Bangui",
        "Président": "Faustin-Archange Touadéra",
        "Superficie": "622,984 km²",
        "Population": "4 884 405 habitants",
        "Langues": ["Français", "Sango"]
    },

    "République démocratique du Congo": {
        "Capitale": "Kinshasa",
        "Président": "Félix Tshisekedi",
        "Superficie": "2,344,858 km²",
        "Population": "92 409 378 habitants",
        "Langues": ["Français"]
    },

    "République dominicaine": {
        "Capitale": "Saint-Domingue",
        "Président": "Luis Abinader",
        "Superficie": "48,670 km²",
        "Population": "10 847 910 habitants",
        "Langues": ["Espagnol"]
    },

    "République du Congo": {
        "Capitale": "Brazzaville",
        "Président": "Denis Sassou-Nguesso",
        "Superficie": "342,000 km²",
        "Population": "5 655 403 habitants",
        "Langues": ["Français"]
    },

    "Roumanie": {
        "Capitale": "Bucarest",
        "Président": "Klaus Iohannis",
        "Superficie": "238,397 km²",
        "Population": "19 286 123 habitants",
        "Langues": ["Roumain"]
    },

    "Royaume-Uni": {
        "Capitale": "Londres",
        "Président": "Roi Charles III",
        "Superficie": "242,495 km²",
        "Population": "67 215 293 habitants",
        "Langues": ["Anglais"]
    },

    "Russie": {
        "Capitale": "Moscou",
        "Président": "Vladimir Poutine",
        "Superficie": "17,098,242 km²",
        "Population": "145 934 462 habitants",
        "Langues": ["Russe"]
    },

    "Rwanda": {
        "Capitale": "Kigali",
        "Président": "Paul Kagame",
        "Superficie": "26,338 km²",
        "Population": "13 246 317 habitants",
        "Langues": ["Kinyarwanda", "Anglais", "Français"]
    },

    "Saint-Christophe-et-Niévès": {
        "Capitale": "Basseterre",
        "Président": "Terrance Drew",
        "Superficie": "261 km²",
        "Population": "53 199 habitants",
        "Langues": ["Anglais"]
    },

    "Sainte-Lucie": {
        "Capitale": "Castries",
        "Président": "Philip J. Pierre",
        "Superficie": "616 km²",
        "Population": "183 627 habitants",
        "Langues": ["Anglais"]
    },

    "Saint-Vincent-et-les-Grenadines": {
        "Capitale": "Kingstown",
        "Président": "Ralph Gonsalves",
        "Superficie": "389 km²",
        "Population": "110 947 habitants",
        "Langues": ["Anglais"]
    },

    "Salvador": {
        "Capitale": "San Salvador",
        "Président": "Nayib Bukele",
        "Superficie": "21,041 km²",
        "Population": "6 539 573 habitants",
        "Langues": ["Espagnol"]
    },

    "Samoa": {
        "Capitale": "Apia",
        "Président": "Tuimalealiʻifano Vaʻaletoʻa Sualauvi II",
        "Superficie": "2,831 km²",
        "Population": "200 624 habitants",
        "Langues": ["Samoan", "Anglais"]
    },

    "São Tomé et Principe": {
        "Capitale": "São Tomé",
        "Président": "Carlos Vila Nova",
        "Superficie": "964 km²",
        "Population": "222 760 habitants",
        "Langues": ["Portugais"]
    },

    "Sénégal": {
        "Capitale": "Dakar",
        "Président": "Macky Sall",
        "Superficie": "196,712 km²",
        "Population": "17 228 625 habitants",
        "Langues": ["Français"]
    },

    "Seychelles": {
        "Capitale": "Victoria",
        "Président": "Wavel Ramkalawan",
        "Superficie": "459 km²",
        "Population": "99 291 habitants",
        "Langues": ["Anglais", "Français", "Créole seychellois"]
    },

    "Sierra Leone": {
        "Capitale": "Freetown",
        "Président": "Julius Maada Bio",
        "Superficie": "71,740 km²",
        "Population": "8 032 457 habitants",
        "Langues": ["Anglais"]
    },

    "Singapour": {
        "Capitale": "Singapour",
        "Président": "Halimah Yacob",
        "Superficie": "728 km²",
        "Population": "5 685 807 habitants",
        "Langues": ["Anglais", "Mandarin", "Malais", "Tamoul"]
    },

    "Somalie": {
        "Capitale": "Mogadiscio",
        "Président": "Hassan Sheikh Mohamud",
        "Superficie": "637,657 km²",
        "Population": "16 607 217 habitants",
        "Langues": ["Somali", "Arabe"]
    },

    "Soudan": {
        "Capitale": "Khartoum",
        "Président": "Abdel Fattah al-Burhan",
        "Superficie": "1,886,068 km²",
        "Population": "45 000 000 habitants",
        "Langues": ["Arabe", "Anglais"]
    },

    "Soudan du Sud": {
        "Capitale": "Djouba",
        "Président": "Salva Kiir Mayardit",
        "Superficie": "644,329 km²",
        "Population": "11 344 429 habitants",
        "Langues": ["Anglais"]
    },

    "Sri Lanka": {
        "Capitale": "Sri Jayawardenapura Kotte",
        "Président": "Ranil Wickremesinghe",
        "Superficie": "65,610 km²",
        "Population": "21 803 000 habitants",
        "Langues": ["Cingalais", "Tamoul"]
    },

    "Suède": {
        "Capitale": "Stockholm",
        "Président": "Ulf Kristersson",
        "Superficie": "450,295 km²",
        "Population": "10 452 326 habitants",
        "Langues": ["Suédois"]
    },

    "Suisse": {
        "Capitale": "Berne",
        "Président": "Aline Trede",
        "Superficie": "41,285 km²",
        "Population": "8 703 398 habitants",
        "Langues": ["Allemand", "Français", "Italien", "Romanche"]
    },

    "Suriname": {
        "Capitale": "Paramaribo",
        "Président": "Chan Santokhi",
        "Superficie": "163,820 km²",
        "Population": "586 632 habitants",
        "Langues": ["Néerlandais"]
    },

    "Syrie": {
        "Capitale": "Damas",
        "Président": "Bachar el-Assad",
        "Superficie": "185,180 km²",
        "Population": "17 500 658 habitants",
        "Langues": ["Arabe"]
    },

    "Tadjikistan": {
        "Capitale": "Douchanbé",
        "Président": "Emomali Rahmon",
        "Superficie": "143,100 km²",
        "Population": "9 537 645 habitants",
        "Langues": ["Tadjik"]
    },

    "Taïwan": {
        "Capitale": "Taipei",
        "Président": "Tsai Ing-wen",
        "Superficie": "36,193 km²",
        "Population": "23 577 271 habitants",
        "Langues": ["Mandarin"]
    },

    "Tanzanie": {
        "Capitale": "Dodoma",
        "Président": "Samia Suluhu",
        "Superficie": "945,087 km²",
        "Population": "60 341 188 habitants",
        "Langues": ["Swahili", "Anglais"]
    },

    "Tchad": {
        "Capitale": "N'Djaména",
        "Président": "Mahamat Idriss Déby",
        "Superficie": "1,284,000 km²",
        "Population": "16 878 574 habitants",
        "Langues": ["Français", "Arabe"]
    },

    "Thaïlande": {
        "Capitale": "Bangkok",
        "Président": "Maha Vajiralongkorn",
        "Superficie": "513,120 km²",
        "Population": "69 802 180 habitants",
        "Langues": ["Thaï"]
    },

    "Timor oriental": {
        "Capitale": "Dili",
        "Président": "José Ramos-Horta",
        "Superficie": "14,874 km²",
        "Population": "1 318 445 habitants",
        "Langues": ["Portugais", "Tétoum"]
    },

    "Togo": {
        "Capitale": "Lomé",
        "Président": "Faure Gnassingbé",
        "Superficie": "56,785 km²",
        "Population": "8 408 590 habitants",
        "Langues": ["Français"]
    },

    "Tonga": {
        "Capitale": "Nuku'alofa",
        "Président": "Tupou VI",
        "Superficie": "747 km²",
        "Population": "105 697 habitants",
        "Langues": ["Tongien", "Anglais"]
    },

    "Trinité-et-Tobago": {
        "Capitale": "Port-d'Espagne",
        "Président": "Paula-Mae Weekes",
        "Superficie": "5,128 km²",
        "Population": "1 399 488 habitants",
        "Langues": ["Anglais"]
    },

    "Tunisie": {
        "Capitale": "Tunis",
        "Président": "Kaïs Saïed",
        "Superficie": "163,610 km²",
        "Population": "11 935 043 habitants",
        "Langues": ["Arabe"]
    },

    "Turkménistan": {
        "Capitale": "Achgabat",
        "Président": "Serdar Berdimuhamedow",
        "Superficie": "488,100 km²",
        "Population": "6 031 187 habitants",
        "Langues": ["Turkmène"]
    },

    "Turquie": {
        "Capitale": "Ankara",
        "Président": "Recep Tayyip Erdoğan",
        "Superficie": "783,356 km²",
        "Population": "84 680 273 habitants",
        "Langues": ["Turc"]
    },

    "Tuvalu": {
        "Capitale": "Funafuti",
        "Président": "Charles III",
        "Superficie": "26 km²",
        "Population": "11 192 habitants",
        "Langues": ["Anglais", "Tuvaluan"]
    },

    "Uruguay": {
        "Capitale": "Montevideo",
        "Président": "Luis Lacalle Pou",
        "Superficie": "176,215 km²",
        "Population": "3 473 727 habitants",
        "Langues": ["Espagnol"]
    },

    "Vanuatu": {
        "Capitale": "Port-Vila",
        "Président": "Nikenike Vurobaravu",
        "Superficie": "12,189 km²",
        "Population": "307 145 habitants",
        "Langues": ["Bichlamar", "Anglais", "Français"]
    },

    "Venezuela": {
        "Capitale": "Caracas",
        "Président": "Nicolás Maduro",
        "Superficie": "916,445 km²",
        "Population": "28 440 073 habitants",
        "Langues": ["Espagnol"]
    },

    "Vietnam": {
        "Capitale": "Hanoï",
        "Président": "Võ Văn Thưởng",
        "Superficie": "331,212 km²",
        "Population": "97 338 579 habitants",
        "Langues": ["Vietnamien"]
    },

    "Yémen": {
        "Capitale": "Sanaa",
        "Président": "Abdrabbo Mansour Hadi",
        "Superficie": "527,968 km²",
        "Population": "29 825 968 habitants",
        "Langues": ["Arabe"]
    },

    "Zambie": {
        "Capitale": "Lusaka",
        "Président": "Hakainde Hichilema",
        "Superficie": "752,618 km²",
        "Population": "19 107 569 habitants",
        "Langues": ["Anglais"]
    },

    "Zimbabwe": {
        "Capitale": "Harare",
        "Président": "Emmerson Mnangagwa",
        "Superficie": "390,757 km²",
        "Population": "15 164 298 habitants",
        "Langues": ["Anglais", "Shona", "Ndebele"]
    }
}


update_pays_list(pays) # Mise à jour de la listbox avec tous les pays

Pays_list.bind("<<ListboxSelect>>", select_pays) # Lie l'événement de sélection dans la listbox à la fonction select_pays
Barre_recherche.bind("<KeyRelease>", verif_recherche) #  Lie l'événement de relachement d'une touche à la fonction verif_recherche
Barre_recherche.bind("<Return>", info) # Lie l'événement d'appuie de la touche entrée à info

root.mainloop()