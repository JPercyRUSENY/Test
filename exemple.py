#1. Definition de la fonction Max
def Maximum(Nombre1,Nombre2):
    if Nombre1 > Nombre2:
        return Nombre1
    elif Nombre2 > Nombre1:
        return Nombre2
    else:
        return "Les deux sont egaux"
 
# Appel de la fonction Max   
def AppelMax():    
    N=int(input("Entrez le nombre 1: "))
    L=int(input("Entrez le nombre 2: "))
    print(Maximum(N,L)) # Appel de la fontion
    
#2. Definition de la fonction Salutation
def Salutation(Prenom):
    return "Bonjour " + Prenom

# Appel de la fonction Salutations
def AppelSalution():
    prenom = input("Entrez le prenom: ")
    print (Salutation(prenom))


def ValeurAbsolue(Nombre):
    if Nombre > 0:
        valeur = Nombre
        return  "Valeur Absolue" , Nombre , '=' , valeur
    elif Nombre < 0:
        valeur = Nombre * (-1)
        return "Valeur Absolue" , Nombre , "=" , valeur
    else:
        return "Valeur Nulle"
    
# Appel de la fonction Salutations
def AppelValeurAbsolue():
    Valeur = int(input("Entrez le valeur: "))
    print (ValeurAbsolue(Valeur))

def bissextile(annee):
    if annee % 4 == 0:
        if annee % 100 == 0:
            if annee % 400 == 0:
                return True
        else:
            return True
    else:
        return False
    
def jourMois(mois,annee):
    if mois == 2:
        if bissextile(annee):
            return 29
        else:
            return 28
    elif mois in [4,6,9,11]:
        return 30
    elif mois in [1,3,5,7,8,10,12]:
        return 31
    else:
        return "Le mois n'existe pas"
    
def compris(x,max):
    if 1<=x <=max:
        return "Est compris"
    return "Ne pas compris"
        

def appelbissextile():
    a = int(input("Entrez a: "))
    b = int(input("Entrez b: "))
    print(compris(a,b))

#Boucles Pour et TantQue
def compte():
    i = True
    while i:
        x = int(input("Entrez un nombre: "))
        i = x!=0
def Appelcompte():
    print(compte())
    
def NombreDeCinq():
    Nombre = int(input("Entrez le nombre: "))
    cpt = 0
    while Nombre != 0:
        chiffre = Nombre % 10
        if chiffre == 5 :
            cpt +=1
        Nombre = Nombre // 10
    print ("le nombre de 5 est: ",cpt)

def AppelNombreDeCinq():
    print(NombreDeCinq())
    
def Decroissant():
    for i in range(10,1,-1):
        print(i)
        
def DecroissantWhile():
    i=10
    while i>=1:
        print(i)
        i-=1 

def NombrePremier(n):
    i=1
    cpt = 0
    while cpt < n:
        serie = (i*(i+1))//2
        print(serie)
        i+=1
        cpt+=1
        
def Fibonacci(n):
    a = 0
    b = 1
    cpt = 0
    while cpt < n:
        print(a, end=' ')
        c=a+b
        a=b
        b=c
        cpt+=1

def AffichierEntier():
    for i in range(1,100):
        if i % 10 ==1:
            print(i, end=' ')

def Carre(n):
    for i in range(1,n+1):
        print(i*i, end=' ')
        

def PremierImpairs(n):
    cpt = 0
    i = 1
    while cpt<n:
        print(i, end=' ')
        i+=2
        cpt+=1
        
def Tableau():
    tab = []
    for i in range(0,9+1):
        n=int(input("Entrez le nombre: "))
        tab.append(n)
    print(tab[5])
    
    
def GrandeValeur(tab):
    if not tab:
        return  "Le tableau est vide"
    maxValeur = tab[0]
    for valeur in tab:
        if valeur < maxValeur:
            maxValeur = valeur
    return maxValeur

def IndicePlusGrandeValeur(tab):
    maxValeur = tab[0]
    indice = 0
    for i in range(1,len(tab)):
        if tab[i] > maxValeur:
            maxValeur = tab[i]
            indice = i
    return indice

def PremierTermes(n):
    tab = []
    for i in range(n):
        if i % 2 == 0:
            tab.append(1)
        else:
            tab.append(-1)
    return tab

class Commune:
    def __init__(self, code, nom):
        self.code = code
        self.nom = nom

    def CodePostal(Communes, nom_commune):
        for communeRecherche in Communes:
            if communeRecherche.nom == nom_commune:
                return communeRecherche.code

def AppleCommune():
    Communes=[Commune(5555,'kenya'),
                Commune(4545,'Kamal'),
                Commune(9686,'Golf')]
    nom_commune = 'kenya'
    code_postal = Commune.CodePostal(Communes,nom_commune)
    return (f'le code postal de {nom_commune} est {code_postal}')       


def DecaleElement(tab):
    return [tab[-1]] + tab[:-1]

def Occurrence(nombre):
    Occurrences = [0]* 10
    for chiffre in str(nombre):
        Occurrences[int(chiffre)]+=1
    
    for i in range(10):
        if Occurrences[i] > 0:
            print(f"{i} apparait {Occurrences[i]} fois")
        
    
def Renverser(tab):
    taille = len(tab)
    for i in range(taille//2):
        temp = tab[i]
        tab[i] = tab[taille-i-1]
        tab[taille-i-1]=temp
    return tab

def doubleElement(tab):
    for i in range(len(tab)):
        tab[i]= tab[i] * 2
    return tab

def compterSequence(tab):
    cpt = 0
    i = 0
    while i<len(tab)-2:
        if tab[i]=="O" and tab[i+1]=="X" and tab[i+2]=="O":
            cpt+=1
            i+=3
        else:
            i+=1
    return cpt
            
if __name__ == "__main__":
    tab = ['O', 'X', 'X', 'X', 'X', 'O', 'X', 'O', 'X', 'O', 'O', 'O', 'O', 'X', 'X', 'O', 'X', 'O', 'O', 'X']
    print(compterSequence(tab))
    