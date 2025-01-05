from tkinter import *

root = Tk() # Création de la fenêtre
root.title('Encyclopédie du monde') # Titre de la fenêtre
root.iconbitmap('') # Icone de la fenêtre
root.geometry("1920x1080") # Résolution de la fenêtre

def update_pays_box(data):
    Pays_box.delete(0, END)  # Supprimer les éléments actuelles de la listbox
    
    # Mettre à jour la list box avec les pays fournis dans data
    for item in data:
        Pays_box.insert(END, item)

# Affiche le pays sélectionnez dans la listbox dans la barre de recherche
def select_pays(e):
    Barre_recherche.delete(0, END)
    Barre_recherche.insert(0, Pays_box.get(ANCHOR))


def verif_recherche(e):
    taped = Barre_recherche.get() # Récupération du texte saisie dans la barre de recherche

    if taped == '': # Si la barre de recherche est vide
        data = pays # Afficher tous les pays
    else:
        data = [] # Liste vide pour stocker les pays qui corresponde à la recherche
        for item in pays:
            if taped.lower() in item.lower(): # Vérifie si le texte de la barre de recherche correspond à un pays
                data.append(item) # Ajouter les pays filtrées à la liste vide

    update_pays_box(data) # Mettre à jour la list box avec les pays filtrés

def info(e):
    Recherche = Barre_recherche.get()
    if Recherche in pays:                                                     # Si Le pays rentrer et dans le dictionnaire des pays
        info_pays = pays[Recherche]                                           # Récupère les informations du dictionnaire
        print("-----------------------------------------------------")        # Affichage ligne séparation dans la console
        for titre, info_titre in info_pays.items():                           # Boucle pour afficher les informations du pays
            print(f"{titre}: {info_titre}")
            info_widget = (f"{titre}: {info_titre}")
            info_box = Label(root, text=info_widget ,font=("Segoe UI Black", 16))
            info_box.pack(pady=5)
        print("-----------------------------------------------------")
    
    else:
        print("Désolé, les informations sur ce pays ne sont pas disponibles.")     # Affichage message d'erreur si le pays n'est pas valide


Entrer_pays = Label(root, text="Entrer le nom du pays", font=("Segoe UI Black", 16), fg="Black") # Texte au dessus de la barre de recherche
Entrer_pays.pack(pady=20) # Placement de ce texte dans la fenêtre

Barre_recherche = Entry(root, font=("Segoe UI Black", 16)) ## Barre de recherche
Barre_recherche.pack(pady=20) # Placement de la barre de recherche

Pays_box = Listbox(root, width=50) # Zone de la list des pays
Pays_box.pack(pady=40)             # Placement de la zone

pays = {
    # Asie
    "Afghanistan": {
        "Capitale": "Kaboul",
        "Président": "Hibatullah Akhundzada",
        "Superficie": "652,230 km²",
        "Population": "38 928 341 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Afghanistan"
    },
    "Algérie": {
        "Capitale": "Alger",
        "Président": "Abdelmadjid Tebboune",
        "Superficie": "2,381,741 km²",
        "Population": "45 750 000 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Algérie"
    },
    "Angola": {
        "Capitale": "Luanda",
        "Président": "João Lourenço",
        "Superficie": "1,246,700 km²",
        "Population": "34 646 000 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Angola"
    },
    "Antigua-et-Barbuda": {
        "Capitale": "Saint John's",
        "Président": "Gaston Browne",
        "Superficie": "442 km²",
        "Population": "97 929 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Antigua-et-Barbuda"
    },
    "Arabie saoudite": {
        "Capitale": "Riyad",
        "Président": "Salmane ben Abdelaziz Al Saoud",
        "Superficie": "2,149,690 km²",
        "Population": "35 340 676 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Arabie_saoudite"
    },
    "Argentine": {
        "Capitale": "Buenos Aires",
        "Président": "Javier Milei",
        "Superficie": "2,780,400 km²",
        "Population": "45 605 829 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Argentine"
    },
    "Arménie": {
        "Capitale": "Erevan",
        "Président": "Vahagn Khatchatourian",
        "Superficie": "29,743 km²",
        "Population": "2 963 243 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Arménie"
    },
    "Australie": {
        "Capitale": "Canberra",
        "Président": "Charles III",
        "Superficie": "7,692,024 km²",
        "Population": "25 687 041 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Australie"
    },
    "Azerbaïdjan": {
        "Capitale": "Bakou",
        "Président": "Ilham Aliyev",
        "Superficie": "86,600 km²",
        "Population": "10 139 177 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Azerbaïdjan"
    },
    "Bahamas": {
        "Capitale": "Nassau",
        "Président": "Philip Davis",
        "Superficie": "13,878 km²",
        "Population": "391 232 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Bahamas"
    },
    "Bahreïn": {
        "Capitale": "Manama",
        "Président": "Hamad ben Issa Al Khalifa",
        "Superficie": "765 km²",
        "Population": "1 701 575 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Bahreïn"
    },
    "Bangladesh": {
        "Capitale": "Dacca",
        "Président": "Mohammad Shahabuddin",
        "Superficie": "147,570 km²",
        "Population": "164 689 383 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Bangladesh"
    },
    "Barbade": {
        "Capitale": "Bridgetown",
        "Président": "Sandra Mason",
        "Superficie": "430 km²",
        "Population": "287 730 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Barbade"
    },
    "Belgique": {
        "Capitale": "Bruxelles",
        "Président": "Alexander De Croo",
        "Superficie": "30,528 km²",
        "Population": "11 582 808 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Belgique"
    },
    "Bénin": {
        "Capitale": "Porto-Novo",
        "Président": "Patrice Talon",
        "Superficie": "114,763 km²",
        "Population": "12 864 634 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Bénin"
    },
    "Belize": {
        "Capitale": "Belmopan",
        "Président": "Johnny Briceño",
        "Superficie": "22,966 km²",
        "Population": "419 199 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Belize"
    },
    "Bhoutan": {
        "Capitale": "Thimphou",
        "Président": "Jigme Khesar Namgyel Wangchuck",
        "Superficie": "38,394 km²",
        "Population": "779 631 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Bhoutan"
    },
    "Birmanie": {
        "Capitale": "Naypyidaw",
        "Président": "Myint Swe",
        "Superficie": "676,578 km²",
        "Population": "54 409 800 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Birmanie"
    },
    "Bolivie": {
        "Capitale": "Sucre",
        "Président": "Luis Arce",
        "Superficie": "1,098,581 km²",
        "Population": "11 673 021 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Bolivie"
    },
    "Botswana": {
        "Capitale": "Gaborone",
        "Président": "Mokgweetsi Masisi",
        "Superficie": "581,730 km²",
        "Population": "2 391 750 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Botswana"
    },
    "Brésil": {
        "Capitale": "Brasília",
        "Président": "Luiz Inácio Lula da Silva",
        "Superficie": "8,515,767 km²",
        "Population": "213 993 437 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Brésil"
    },
    "Brunei": {
        "Capitale": "Bandar Seri Begawan",
        "Président": "Hassanal Bolkiah",
        "Superficie": "5,765 km²",
        "Population": "437 479 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Brunei"
    },
    "Burkina Faso": {
        "Capitale": "Ouagadougou",
        "Président": "Ibrahim Traoré",
        "Superficie": "274,200 km²",
        "Population": "21 510 181 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Burkina_Faso"
    },
    "Burundi": {
        "Capitale": "Gitega",
        "Président": "Évariste Ndayishimiye",
        "Superficie": "27,834 km²",
        "Population": "12 213 565 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Burundi"
    },
    "Cambodge": {
        "Capitale": "Phnom Penh",
        "Président": "Norodom Sihamoni",
        "Superficie": "181,035 km²",
        "Population": "16 718 965 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Cambodge"
    },
    "Cameroun": {
        "Capitale": "Yaoundé",
        "Président": "Paul Biya",
        "Superficie": "475,442 km²",
        "Population": "27 743 967 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Cameroun"
    },
    "Canada": {
        "Capitale": "Ottawa",
        "Président": "Charles III",
        "Superficie": "9,984,670 km²",
        "Population": "38 008 005 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Canada"
    },
    "Cap Vert": {
        "Capitale": "Praia",
        "Président": "José Maria Neves",
        "Superficie": "4,033 km²",
        "Population": "560 899 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Cap-Vert"
    },
    "Chili": {
        "Capitale": "Santiago",
        "Président": "Gabriel Boric",
        "Superficie": "756,096 km²",
        "Population": "19 493 300 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Chili"
    },
    "Chine": {
        "Capitale": "Pékin",
        "Président": "Xi Jinping",
        "Superficie": "9,596,961 km²",
        "Population": "1 411 778 724 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Chine"
    },
    "Chypre": {
        "Capitale": "Nicosie",
        "Président": "Níkos Anastasiádis",
        "Superficie": "9,251 km²",
        "Population": "1 207 359 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Chypre"
    },
    "Colombie": {
        "Capitale": "Bogota",
        "Président": "Gustavo Petro",
        "Superficie": "1,141,748 km²",
        "Population": "50 882 884 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Colombie"
    },
    "Comores": {
        "Capitale": "Moroni",
        "Président": "Azali Assoumani",
        "Superficie": "2,034 km²",
        "Population": "873 724 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Comores"
    },
    "Corée du Nord": {
        "Capitale": "Pyongyang",
        "Président": "Kim Jong-un",
        "Superficie": "120,538 km²",
        "Population": "25 778 816 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Corée_du_Nord"
    },
    "Corée du Sud": {
        "Capitale": "Séoul",
        "Président": "Yoon Suk-yeol",
        "Superficie": "100,210 km²",
        "Population": "51 780 579 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Corée_du_Sud"
    },
    "Costa Rica": {
        "Capitale": "San José",
        "Président": "Rodrigo Chaves Robles",
        "Superficie": "51,100 km²",
        "Population": "5 094 118 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Costa_Rica"
    },
    "Côte d'Ivoire": {
        "Capitale": "Yamoussoukro",
        "Président": "Alassane Ouattara",
        "Superficie": "322,463 km²",
        "Population": "27 480 153 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Côte_d%27Ivoire"
    },
    "Cuba": {
        "Capitale": "La Havane",
        "Président": "Miguel Díaz-Canel",
        "Superficie": "109,884 km²",
        "Population": "11 326 616 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Cuba"
    },
    "Djibouti": {
        "Capitale": "Djibouti",
        "Président": "Ismaïl Omar Guelleh",
        "Superficie": "23,200 km²",
        "Population": "994 372 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Djibouti"
    },
    "Dominique": {
        "Capitale": "Roseau",
        "Président": "Roosevelt Skerrit",
        "Superficie": "751 km²",
        "Population": "71 986 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Dominique"
    },
    "Égypte": {
        "Capitale": "Le Caire",
        "Président": "Abdel Fattah al-Sissi",
        "Superficie": "1,010,408 km²",
        "Population": "104 258 326 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Égypte"
    },
    "Émirats arabes unis": {
        "Capitale": "Abou Dabi",
        "Président": "Mohammed ben Zayed Al Nahyane",
        "Superficie": "83,600 km²",
        "Population": "9 890 402 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Émirats_arabes_unis"
    },
    "Équateur": {
        "Capitale": "Quito",
        "Président": "Daniel Noboa",
        "Superficie": "283,561 km²",
        "Population": "17 643 644 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Équateur"
    },
    "Érythrée": {
        "Capitale": "Asmara",
        "Président": "Isaias Afwerki",
        "Superficie": "117,600 km²",
        "Population": "3 546 430 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Érythrée"
    },
    "Espagne": {
        "Capitale": "Madrid",
        "Président": "Pedro Sánchez",
        "Superficie": "505,992 km²",
        "Population": "47 351 567 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Espagne"
    },
    "Eswatini": {
        "Capitale": "Mbabane",
        "Président": "Mswati III (Roi)",
        "Superficie": "17,364 km²",
        "Population": "1 164 935 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Eswatini"
    },
    "États-Unis": {
        "Capitale": "Washington, D.C.",
        "Président": "Joe Biden",
        "Superficie": "9,833,517 km²",
        "Population": "331 893 745 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/États-Unis"
    },
    "Éthiopie": {
        "Capitale": "Addis-Abeba",
        "Président": "Sahle-Work Zewde",
        "Superficie": "1,104,300 km²",
        "Population": "118 247 865 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Éthiopie"
    },
    "Fidji": {
        "Capitale": "Suva",
        "Président": "Wiliame Katonivere",
        "Superficie": "18,274 km²",
        "Population": "896 445 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Fidji"
    },
    "France": {
        "Capitale": "Paris",
        "Président": "Emmanuel Macron",
        "Superficie": "640,679 km²",
        "Population": "67 713 000 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/France"
    },
    "Gabon": {
        "Capitale": "Libreville",
        "Président": "Ali Bongo Ondimba",
        "Superficie": "267,667 km²",
        "Population": "2 256 440 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Gabon"
    },
    "Gambie": {
        "Capitale": "Banjul",
        "Président": "Adama Barrow",
        "Superficie": "11,300 km²",
        "Population": "2 486 941 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Gambie"
    },
    "Géorgie": {
        "Capitale": "Tbilissi",
        "Président": "Salomé Zourabichvili",
        "Superficie": "69,700 km²",
        "Population": "3 714 085 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Géorgie_(pays)"
    },
    "Ghana": {
        "Capitale": "Accra",
        "Président": "Nana Akufo-Addo",
        "Superficie": "238,533 km²",
        "Population": "31 504 467 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Ghana"
    },
    "Grenade": {
        "Capitale": "Saint-Georges",
        "Président": "Dickon Mitchell",
        "Superficie": "344 km²",
        "Population": "112 523 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Grenade"
    },
    "Guatemala": {
        "Capitale": "Ciudad de Guatemala",
        "Président": "Bernardo Arévalo",
        "Superficie": "108,889 km²",
        "Population": "18 244 522 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Guatemala"
    },
    "Guinée": {
        "Capitale": "Conakry",
        "Président": "Mamady Doumbouya",
        "Superficie": "245,857 km²",
        "Population": "13 469 192 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Guinée"
    },
    "Guinée Bissau": {
        "Capitale": "Bissau",
        "Président": "Umaro Sissoco Embaló",
        "Superficie": "36,125 km²",
        "Population": "1 986 107 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Guinée-Bissau"
    },
    "Guinée équatoriale": {
        "Capitale": "Malabo",
        "Président": "Teodoro Obiang Nguema Mbasogo",
        "Superficie": "28,051 km²",
        "Population": "1 454 789 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Guinée_équatoriale"
    },
    "Guyana": {
        "Capitale": "Georgetown",
        "Président": "Irfaan Ali",
        "Superficie": "214,969 km²",
        "Population": "786 552 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Guyana"
    },
    "Haïti": {
        "Capitale": "Port-au-Prince",
        "Président": "Ariel Henry",
        "Superficie": "27,750 km²",
        "Population": "11 402 528 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Haïti"
    },
    "Honduras": {
        "Capitale": "Tegucigalpa",
        "Président": "Xiomara Castro",
        "Superficie": "112,492 km²",
        "Population": "9 904 607 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Honduras"
    },
    "Inde": {
        "Capitale": "New Delhi",
        "Président": "Droupadi Murmu",
        "Superficie": "3,287,263 km²",
        "Population": "1 393 409 038 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Inde"
    },
    "Indonésie": {
        "Capitale": "Jakarta",
        "Président": "Joko Widodo",
        "Superficie": "1,904,569 km²",
        "Population": "273 523 615 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Indonésie"
    },
    "Irak": {
        "Capitale": "Bagdad",
        "Président": "Abdul Latif Rashid",
        "Superficie": "438,317 km²",
        "Population": "40 222 493 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Irak"
    },
    "Iran": {
        "Capitale": "Téhéran",
        "Président": "Ebrahim Raïssi",
        "Superficie": "1,648,195 km²",
        "Population": "83 992 946 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Iran"
    },
    "Îles Marshall": {
        "Capitale": "Majuro",
        "Président": "David Kabua",
        "Superficie": "181 km²",
        "Population": "59 190 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Îles_Marshall"
    },
    "Îles Salomon": {
        "Capitale": "Honiara",
        "Président": "David Vunagi",
        "Superficie": "28,896 km²",
        "Population": "686 878 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Îles_Salomon"
    },
    "Israel": {
        "Capitale": "Jérusalem",
        "Président": "Isaac Herzog",
        "Superficie": "20,770 km²",
        "Population": "9 053 300 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Israël"
    },
    "Italie": {
        "Capitale": "Rome",
        "Président": "Sergio Mattarella",
        "Superficie": "301,338 km²",
        "Population": "58 982 687 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Italie"
    },
    "Jamaïque": {
        "Capitale": "Kingston",
        "Président": "Andrew Holness",
        "Superficie": "10,991 km²",
        "Population": "2 961 167 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Jamaïque"
    },
    "Japon": {
        "Capitale": "Tokyo",
        "Président": "Naruhito",
        "Superficie": "377,975 km²",
        "Population": "125 810 000 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Japon"
    },
    "Jordanie": {
        "Capitale": "Amman",
        "Président": "Abdallah II",
        "Superficie": "89,342 km²",
        "Population": "10 203 134 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Jordanie"
    },
    "Kazakhstan": {
        "Capitale": "Astana",
        "Président": "Kassym-Jomart Tokaïev",
        "Superficie": "2,724,900 km²",
        "Population": "18 776 092 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Kazakhstan"
    },
    "Kenya": {
        "Capitale": "Nairobi",
        "Président": "William Ruto",
        "Superficie": "580,367 km²",
        "Population": "54 985 698 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Kenya"
    },
    "Kirghizistan": {
        "Capitale": "Bichkek",
        "Président": "Sadyr Japarov",
        "Superficie": "199,951 km²",
        "Population": "6 524 195 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Kirghizistan"
    },
    "Kiribati": {
        "Capitale": "Tarawa-Sud",
        "Président": "Taneti Maamau",
        "Superficie": "811 km²",
        "Population": "119 449 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Kiribati"
    },
    "Koweït": {
        "Capitale": "Koweït",
        "Président": "Nawaf Al-Ahmad Al-Jaber Al-Sabah",
        "Superficie": "17,818 km²",
        "Population": "4 270 571 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Koweït"
    },
    "Laos": {
        "Capitale": "Vientiane",
        "Président": "Thongloun Sisoulith",
        "Superficie": "236,800 km²",
        "Population": "7 275 560 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Laos"
    },
    "Lesotho": {
        "Capitale": "Maseru",
        "Président": "Letsie III (Roi)",
        "Superficie": "30,355 km²",
        "Population": "2 153 514 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Lesotho"
    },
    "Liban": {
        "Capitale": "Beyrouth",
        "Président": "Michel Aoun",
        "Superficie": "10,452 km²",
        "Population": "6 825 445 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Liban"
    },
    "Libéria": {
        "Capitale": "Monrovia",
        "Président": "George Weah",
        "Superficie": "111,369 km²",
        "Population": "5 160 335 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Liberia"
    },
    "Libye": {
        "Capitale": "Tripoli",
        "Président": "Mohamed al-Menfi",
        "Superficie": "1,759,540 km²",
        "Population": "6 977 429 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Libye"
    },
    "Madagascar": {
        "Capitale": "Antananarivo",
        "Président": "Andry Rajoelina",
        "Superficie": "587,041 km²",
        "Population": "28 427 310 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Madagascar"
    },
    "Malaisie": {
        "Capitale": "Kuala Lumpur",
        "Président": "Abdullah de Pahang",
        "Superficie": "330,803 km²",
        "Population": "32 365 999 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Malaisie"
    },
    "Malawi": {
        "Capitale": "Lilongwe",
        "Président": "Lazarus Chakwera",
        "Superficie": "118,484 km²",
        "Population": "19 722 622 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Malawi"
    },
    "Mali": {
        "Capitale": "Bamako",
        "Président": "Assimi Goïta",
        "Superficie": "1,240,192 km²",
        "Population": "20 855 555 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Mali"
    },
    "Maldives": {
        "Capitale": "Malé",
        "Président": "Ibrahim Mohamed Solih",
        "Superficie": "298 km²",
        "Population": "540 544 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Maldives"
    },
    "Maroc": {
        "Capitale": "Rabat",
        "Président": "Mohammed VI (Roi)",
        "Superficie": "446,550 km²",
        "Population": "37 108 501 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Maroc"
    },
    "Maurice": {
        "Capitale": "Port-Louis",
        "Président": "Prithvirajsing Roopun",
        "Superficie": "2,040 km²",
        "Population": "1 273 072 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Maurice"
    },
    "Mauritanie": {
        "Capitale": "Nouakchott",
        "Président": "Mohamed Ould Ghazouani",
        "Superficie": "1,030,700 km²",
        "Population": "4 687 606 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Mauritanie"
    },
    "Mexique": {
        "Capitale": "Mexico",
        "Président": "Andrés Manuel López Obrador",
        "Superficie": "1,964,375 km²",
        "Population": "128 932 753 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Mexique"
    },
    "Micronésie": {
        "Capitale": "Palikir",
        "Président": "Wesley Simina",
        "Superficie": "702 km²",
        "Population": "115 023 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Micronésie_(pays)"
    },
    "Mongolie": {
        "Capitale": "Oulan-Bator",
        "Président": "Ukhnaagiin Khürelsükh",
        "Superficie": "1,564,116 km²",
        "Population": "3 278 290 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Mongolie"
    },
    "Mozambique": {
        "Capitale": "Maputo",
        "Président": "Filipe Nyusi",
        "Superficie": "801,590 km²",
        "Population": "32 063 476 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Mozambique"
    },
    "Namibie": {
        "Capitale": "Windhoek",
        "Président": "Hage Geingob",
        "Superficie": "825,615 km²",
        "Population": "2 550 604 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Namibie"
    },
    "Nauru": {
        "Capitale": "Yaren",
        "Président": "Russ Kun",
        "Superficie": "21 km²",
        "Population": "10 824 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Nauru"
    },
    "Népal": {
        "Capitale": "Katmandou",
        "Président": "Ram Chandra Poudel",
        "Superficie": "147,181 km²",
        "Population": "29 164 578 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Népal"
    },
    "Nicaragua": {
        "Capitale": "Managua",
        "Président": "Daniel Ortega",
        "Superficie": "130,373 km²",
        "Population": "6 624 554 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Nicaragua"
    },
    "Niger": {
        "Capitale": "Niamey",
        "Président": "Mohamed Bazoum",
        "Superficie": "1,267,000 km²",
        "Population": "25 223 447 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Niger"
    },
    "Nigeria": {
        "Capitale": "Abuja",
        "Président": "Bola Tinubu",
        "Superficie": "923,768 km²",
        "Population": "211 400 708 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Nigeria"
    },
    "Nouvelle-Zélande": {
        "Capitale": "Wellington",
        "Président": "Charles III",
        "Superficie": "268,021 km²",
        "Population": "5 084 300 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Nouvelle-Zélande"
    },
    "Oman": {
        "Capitale": "Mascate",
        "Président": "Haitham ben Tariq",
        "Superficie": "309,500 km²",
        "Population": "4 667 407 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Oman"
    },
    "Ouganda": {
        "Capitale": "Kampala",
        "Président": "Yoweri Museveni",
        "Superficie": "241,550 km²",
        "Population": "47 785 495 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Ouganda"
    },
    "Ouzbékistan": {
        "Capitale": "Tachkent",
        "Président": "Shavkat Mirziyoyev",
        "Superficie": "447,400 km²",
        "Population": "34 232 200 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Ouzbékistan"
    },
    "Pakistan": {
        "Capitale": "Islamabad",
        "Président": "Arif Alvi",
        "Superficie": "796,095 km²",
        "Population": "220 892 340 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Pakistan"
    },
    "Palaos": {
        "Capitale": "Ngerulmud",
        "Président": "Surangel Whipps Jr.",
        "Superficie": "459 km²",
        "Population": "18 092 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Palaos"
    },
    "Palestine": {
        "Capitale": "Jérusalem",
        "Président": "Mahmoud Abbas",
        "Superficie": "6,025 km²",
        "Population": "5 166 000 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Palestine_(État)"
    },
    "Panama": {
        "Capitale": "Panama",
        "Président": "Laurentino Cortizo",
        "Superficie": "75,417 km²",
        "Population": "4 378 343 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Panama"
    },
    "Papouasie-Nouvelle-Guinée": {
        "Capitale": "Port Moresby",
        "Président": "Charles III",
        "Superficie": "462,840 km²",
        "Population": "8 947 024 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Papouasie-Nouvelle-Guinée"
    },
    "Paraguay": {
        "Capitale": "Asunción",
        "Président": "Santiago Peña",
        "Superficie": "406,752 km²",
        "Population": "7 359 002 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Paraguay"
    },
    "Pays-Bas": {
        "Capitale": "Amsterdam",
        "Président": "Mark Rutte",
        "Superficie": "41,543 km²",
        "Population": "17 595 017 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Pays-Bas"
    },
    "Pérou": {
        "Capitale": "Lima",
        "Président": "Dina Boluarte",
        "Superficie": "1,285,216 km²",
        "Population": "33 296 434 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Pérou"
    },
    "Philippines": {
        "Capitale": "Manille",
        "Président": "Bongbong Marcos",
        "Superficie": "300,000 km²",
        "Population": "110 818 325 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Philippines"
    },
    "Portugal": {
        "Capitale": "Lisbonne",
        "Président": "Marcelo Rebelo de Sousa",
        "Superficie": "92,090 km²",
        "Population": "10 291 027 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Portugal"
    },
    "Qatar": {
        "Capitale": "Doha",
        "Président": "Tamim ben Hamad Al Thani",
        "Superficie": "11,586 km²",
        "Population": "2 881 053 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Qatar"
    },
    "République centrafricaine": {
        "Capitale": "Bangui",
        "Président": "Faustin-Archange Touadéra",
        "Superficie": "622,984 km²",
        "Population": "4 884 405 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/République_centrafricaine"
    },
    "République démocratique du Congo": {
        "Capitale": "Kinshasa",
        "Président": "Félix Tshisekedi",
        "Superficie": "2,344,858 km²",
        "Population": "92 409 378 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/République_démocratique_du_Congo"
    },
    "République dominicaine": {
        "Capitale": "Saint-Domingue",
        "Président": "Luis Abinader",
        "Superficie": "48,670 km²",
        "Population": "10 847 910 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/République_dominicaine"
    },
    "République du Congo": {
        "Capitale": "Brazzaville",
        "Président": "Denis Sassou-Nguesso",
        "Superficie": "342,000 km²",
        "Population": "5 655 403 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/République_du_Congo"
    },
    "Roumanie": {
        "Capitale": "Bucarest",
        "Président": "Klaus Iohannis",
        "Superficie": "238,397 km²",
        "Population": "19 286 123 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Roumanie"
    },
    "Royaume-Uni": {
        "Capitale": "Londres",
        "Président": "Roi Charles III",
        "Superficie": "242,495 km²",
        "Population": "67 215 293 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Royaume-Uni"
    },
    "Russie": {
        "Capitale": "Moscou",
        "Président": "Vladimir Poutine",
        "Superficie": "17,098,242 km²",
        "Population": "145 934 462 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Russie"
    },
    "Rwanda": {
        "Capitale": "Kigali",
        "Président": "Paul Kagame",
        "Superficie": "26,338 km²",
        "Population": "13 246 317 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Rwanda"
    },
    "Saint-Christophe-et-Niévès": {
        "Capitale": "Basseterre",
        "Président": "Terrance Drew",
        "Superficie": "261 km²",
        "Population": "53 199 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Saint-Christophe-et-Niévès"
    },
    "Sainte-Lucie": {
        "Capitale": "Castries",
        "Président": "Philip J. Pierre",
        "Superficie": "616 km²",
        "Population": "183 627 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Sainte-Lucie"
    },
    "Saint-Vincent-et-les-Grenadines": {
        "Capitale": "Kingstown",
        "Président": "Ralph Gonsalves",
        "Superficie": "389 km²",
        "Population": "110 947 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Saint-Vincent-et-les-Grenadines"
    },
    "Salvador": {
        "Capitale": "San Salvador",
        "Président": "Nayib Bukele",
        "Superficie": "21,041 km²",
        "Population": "6 539 573 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Salvador"
    },
    "Samoa": {
        "Capitale": "Apia",
        "Président": "Tuimalealiʻifano Vaʻaletoʻa Sualauvi II",
        "Superficie": "2,831 km²",
        "Population": "200 624 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Samoa"
    },
    "São Tomé et Principe": {
        "Capitale": "São Tomé",
        "Président": "Carlos Vila Nova",
        "Superficie": "964 km²",
        "Population": "222 760 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/São_Tomé_et_Principe"
    },
    "Sénégal": {
        "Capitale": "Dakar",
        "Président": "Macky Sall",
        "Superficie": "196,712 km²",
        "Population": "17 228 625 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Sénégal"
    },
    "Seychelles": {
        "Capitale": "Victoria",
        "Président": "Wavel Ramkalawan",
        "Superficie": "459 km²",
        "Population": "99 291 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Seychelles"
    },
    "Sierra Leone": {
        "Capitale": "Freetown",
        "Président": "Julius Maada Bio",
        "Superficie": "71,740 km²",
        "Population": "8 032 457 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Sierra_Leone"
    },
    "Singapour": {
        "Capitale": "Singapour",
        "Président": "Halimah Yacob",
        "Superficie": "728 km²",
        "Population": "5 685 807 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Singapour"
    },
    "Somalie": {
        "Capitale": "Mogadiscio",
        "Président": "Hassan Sheikh Mohamud",
        "Superficie": "637,657 km²",
        "Population": "16 607 217 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Somalie"
    },
    "Soudan": {
        "Capitale": "Khartoum",
        "Président": "Abdel Fattah al-Burhan",
        "Superficie": "1,886,068 km²",
        "Population": "45 000 000 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Soudan"
    },
    "Soudan du Sud": {
        "Capitale": "Djouba",
        "Président": "Salva Kiir Mayardit",
        "Superficie": "644,329 km²",
        "Population": "11 344 429 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Soudan_du_Sud"
    },
    "Sri Lanka": {
        "Capitale": "Sri Jayawardenapura Kotte",
        "Président": "Ranil Wickremesinghe",
        "Superficie": "65,610 km²",
        "Population": "21 803 000 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Sri_Lanka"
    },
    "Suède": {
        "Capitale": "Stockholm",
        "Président": "Ulf Kristersson",
        "Superficie": "450,295 km²",
        "Population": "10 452 326 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Suède"
    },
    "Suisse": {
        "Capitale": "Berne",
        "Président": "Aline Trede",
        "Superficie": "41,285 km²",
        "Population": "8 703 398 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Suisse"
    },
    "Suriname": {
        "Capitale": "Paramaribo",
        "Président": "Chan Santokhi",
        "Superficie": "163,820 km²",
        "Population": "586 632 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Suriname"
    },
    "Syrie": {
        "Capitale": "Damas",
        "Président": "Bachar el-Assad",
        "Superficie": "185,180 km²",
        "Population": "17 500 658 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Syrie"
    },
    "Tadjikistan": {
        "Capitale": "Douchanbé",
        "Président": "Emomali Rahmon",
        "Superficie": "143,100 km²",
        "Population": "9 537 645 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Tadjikistan"
    },
    "Taïwan": {
        "Capitale": "Taipei",
        "Président": "Tsai Ing-wen",
        "Superficie": "36,193 km²",
        "Population": "23 577 271 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Taïwan"
    },
    "Tanzanie": {
        "Capitale": "Dodoma",
        "Président": "Samia Suluhu",
        "Superficie": "945,087 km²",
        "Population": "60 341 188 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Tanzanie"
    },
    "Tchad": {
        "Capitale": "N'Djaména",
        "Président": "Mahamat Idriss Déby",
        "Superficie": "1,284,000 km²",
        "Population": "16 878 574 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Tchad"
    },
    "Thaïlande": {
        "Capitale": "Bangkok",
        "Président": "Maha Vajiralongkorn",
        "Superficie": "513,120 km²",
        "Population": "69 802 180 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Thaïlande"
    },
    "Timor oriental": {
        "Capitale": "Dili",
        "Président": "José Ramos-Horta",
        "Superficie": "14,874 km²",
        "Population": "1 318 445 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Timor_oriental"
    },
    "Togo": {
        "Capitale": "Lomé",
        "Président": "Faure Gnassingbé",
        "Superficie": "56,785 km²",
        "Population": "8 408 590 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Togo"
    },
    "Tonga": {
        "Capitale": "Nuku'alofa",
        "Président": "Tupou VI",
        "Superficie": "747 km²",
        "Population": "105 697 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Tonga"
    },
    "Trinité-et-Tobago": {
        "Capitale": "Port-d'Espagne",
        "Président": "Paula-Mae Weekes",
        "Superficie": "5,128 km²",
        "Population": "1 399 488 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Trinité-et-Tobago"
    },
    "Tunisie": {
        "Capitale": "Tunis",
        "Président": "Kaïs Saïed",
        "Superficie": "163,610 km²",
        "Population": "11 935 043 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Tunisie"
    },
    "Turkménistan": {
        "Capitale": "Achgabat",
        "Président": "Serdar Berdimuhamedow",
        "Superficie": "488,100 km²",
        "Population": "6 031 187 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Turkménistan"
    },
    "Turquie": {
        "Capitale": "Ankara",
        "Président": "Recep Tayyip Erdoğan",
        "Superficie": "783,356 km²",
        "Population": "84 680 273 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Turquie"
    },
    "Tuvalu": {
        "Capitale": "Funafuti",
        "Président": "Charles III",
        "Superficie": "26 km²",
        "Population": "11 192 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Tuvalu"
    },
    "Uruguay": {
        "Capitale": "Montevideo",
        "Président": "Luis Lacalle Pou",
        "Superficie": "176,215 km²",
        "Population": "3 473 727 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Uruguay"
    },
    "Vanuatu": {
        "Capitale": "Port-Vila",
        "Président": "Nikenike Vurobaravu",
        "Superficie": "12,189 km²",
        "Population": "307 145 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Vanuatu"
    },
    "Venezuela": {
        "Capitale": "Caracas",
        "Président": "Nicolás Maduro",
        "Superficie": "916,445 km²",
        "Population": "28 440 073 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Venezuela"
    },
    "Vietnam": {
        "Capitale": "Hanoï",
        "Président": "Võ Văn Thưởng",
        "Superficie": "331,212 km²",
        "Population": "97 338 579 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Viêt_Nam"
    },
    "Yémen": {
        "Capitale": "Sanaa",
        "Président": "Abdrabbo Mansour Hadi",
        "Superficie": "527,968 km²",
        "Population": "29 825 968 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Yémen"
    },
    "Zambie": {
        "Capitale": "Lusaka",
        "Président": "Hakainde Hichilema",
        "Superficie": "752,618 km²",
        "Population": "19 107 569 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Zambie"
    },
    "Zimbabwe": {
        "Capitale": "Harare",
        "Président": "Emmerson Mnangagwa",
        "Superficie": "390,757 km²",
        "Population": "15 164 298 habitants",
        "Wikipédia": "https://fr.wikipedia.org/wiki/Zimbabwe"
    }
}

update_pays_box(pays) # Mise à jour de la listbox avec tous les pays

Pays_box.bind("<<ListboxSelect>>", select_pays) # Lie l'événement de sélection dans la listbox à la fonction select_pays
Barre_recherche.bind("<KeyRelease>", verif_recherche) #  Lie l'événement de relachement d'une touche à la fonction verif_recherche
Barre_recherche.bind("<Return>", info)

root.mainloop()