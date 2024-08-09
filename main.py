import g1111
import g1112

#g1111.presentation()
#print(g1111.hasard(9))
liste=[2,5,2,6,6,7,4]
#print(g1111.filtrer(liste))
#print(g1111.generer(10))
#print(g1111.nbUnique(liste))
Matrice=[ [1,2,2], [2,5,6] ]
#print(g1111.sommeMatrice(Matrice))
oeuvres = [
{ "title": "Le petit cheval de manège", "year": 1998 },
{ "title": "L'aventure c'est l'aventure", "year": 1972 },
{ "title": "Tout l'or du monde", "year": 1961 },
{ "title": "Des racines et des ailes", "year": 1997},
{ "title": "Élever des poules", "year": 2012 },
{ "title": "Hades, un Dieu vivant", "year": 2039 }]
#print(g1111.Apres1980(oeuvres))


tab = ['-','-','-','S','-','-','-']
t = g1112.jouer_un_coup()
print(t)
print(g1112.deplacer_la_souris(tab,t))