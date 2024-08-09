import random
from collections import defaultdict

matricule = "1111"
prenom = "Loic"

def presentation():
    print(prenom, matricule)

def hasard(n):
    return random.randint(1,n)

def filtrer(liste):
    listeNvelle = []
    for i in liste:
        if i % 2 == 0:
            listeNvelle.append(i)
    return listeNvelle

def generer(n):
    liste = []
    for i in range (n):
        liste.append(random.randint(1,1001))
    return liste

def nbUnique(liste):
    listeUnique = set()
    for i in liste:
        listeUnique.add(i)
    return listeUnique
#Matrice[ [1,2,2], [2,5,6] ]
def sommeMatrice(matrice):
    SommeTotal = 0
    for liste in matrice:
        for element in liste:
            SommeTotal += element
    return SommeTotal

def Ancien(oeuvres):
    annee_min = oeuvres[0]['year']
    for oeuvre in oeuvres:
        if oeuvre['year']< annee_min:
            annee_min = oeuvre['year']
    return annee_min

def AncienDeux(oeuvres):
    return min(oeuvres,key=lambda x: x['year'])['year']
        
def Apres1980(oeuvres):
    liste = []
    for oeuvre in oeuvres:
        if oeuvre['year'] > 1980:
            liste.append(oeuvre)
    return liste
    
def MarcheAleatoire():
    position = 0
    lancer = 0
    visite =defaultdict(int)
    
    while abs(position) < 20:
        lancer+=1
        de = random.randint(1,6)
        piece = random.choice(["Pile","Face"])
        
        if piece=="Pile":
            position+=de
        else:
            position-=de
    visite[position]+=1
    print(f"Lancer: {lancer} :({piece}, {de}) (Positions : {position})")
    
    positionVisiter = [p for p, v in visite.items() if v==max(visite.values())]
    print(f"Vous y êtes !")
    print(f"Nombre de lancers : {lancer}")
    print(f"Position la plus visitée :{positionVisiter}")
    
def afficher_titre():
    print("**********************************************")
    print("*** Bienvenue dans le programme de statistique")
    print("**********************************************")
    
    
def demander_mot():
    while True:
        mot = input("Entrez le mot ou une ligne vide : ")
        if mot =="":
            return mot
        if mot.isalpha():
            return mot
        else:
            print("Erreur, Entrez un mot ou une ligne vide ")



def dico_lettres():
    lettres = 'abcdefghijklmnopqrstuvwxyz'
    dico = {}
    for lettre in lettres:
        dico[lettre] = 0
    return dico


def maj_dico(dictionnaire,mot):
    for lettre in mot:
        if lettre in dictionnaire:
            dictionnaire[lettre] += 1
    return dictionnaire



def diagramme(dictionnaire):
    lettres = sorted(dictionnaire.keys())
    for lettre in lettres:
        alphabet = dictionnaire[lettre]
        if alphabet > 0:
            print(f"{lettre} : {'*' * alphabet}")
        

def statistique():
    afficher_titre()
    dictionnaire = dico_lettres()
    mots = []
    while True:
        mot = demander_mot()
        if mot == "":
            break 
        mots.append(mot)
        maj_dico(dictionnaire,mot)
    if mots:
        print(f"Vous avez entré {len(mots)} mots")
        print(f"Le mot le plus long comporte {max(len(m)for m in mots)} caractères")
        print(f"Le mot le plus court comporte {min(len(m)for m in mots)} caractères")
        print("Voici le diagramme des fréquences des lettres")
        diagramme(dictionnaire)
    else:
        print("le mot est vide")


def hazard(n):
    return random.randint(1,n)


def init_plateau_jeu(n):
    return ['-'] * (2 * n + 1)

def print_plateau_jeu(plateau_jeu):
    for i in plateau_jeu:
        print(f'|-', end='')
    print('|')

def demarrer_le_jeu(plateau_jeu):
    milieu = len(plateau_jeu) // 2
    plateau_jeu[milieu] = 'S'
    return plateau_jeu

def jouer_un_coup():
    return [hasard(4),hasard(4)]

def donne_position_souris(plateau_jeu):
    for position, element in enumerate(plateau_jeu):
        if element == 'S':
            return position 
    return -1

def deplacer_la_souris(plateau_jeu, mises_joueurs):
    position = donne_position_souris(plateau_jeu)
    if position == -1:
        return
    deplace = mises_joueurs[0] - mises_joueurs[1]
    if deplace > 0:
        ChangePosition = position - deplace
    elif deplace < 0:
        ChangePosition = position - deplace
    else:
        ChangePosition = position
    
    ChangePosition = max(0,min(len(plateau_jeu)-1,ChangePosition))
    
    plateau_jeu[position]='-'
    plateau_jeu[ChangePosition] = 'S'
    
    return plateau_jeu


    
    
    
    
        
        
    
        