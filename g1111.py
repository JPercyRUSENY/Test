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
        
        
    
        