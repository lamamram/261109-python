# %%
"""
1/ saisir n valeurs entiers relatifs dans le clavier séparés par ","
2/ on veut itérer sur les valeurs saisies pour vérifier
hint: il y a une méthode pour vérifier si tous les car. sont tous numérique
hint: negatif: commence par  - (1/ opérateurs ou 2/ methode)  et le reste est numérique
que ces valeurs sont des entiers relatifs (1er cas entier naturel ensuite 2ème cas négatif)
3/ si c'est convertible on ajoute la valeur convertie dans une liste
# 3b/ si ce n'est pas convertible => "casser la boucle"
4/ calculer la moyenne depuis la liste (fonctions globales)
5/ présenter le résultat avec 2 décimales (arrondi).  
"""
valeurs = input(' n valeurs entiers relatifs dans le clavier séparés par ","')
valeurs = valeurs.split(",")

integers = []
for valeur in valeurs:
    valeur = valeur.strip()
    if (
        valeur.isnumeric() 
        or ( 
            valeur.startswith("-") 
            and valeur[1:].isnumeric() 
        )
    ):
        integers.append(int(valeur))

# if len(integers) != 0:
if integers:
    avg = round(sum(integers) / len(integers), 2)
    print(f"La moyenne de {integers} est {avg:.2f}")



# %%



# condition de convertibilité entre une str et une str convertible
s = "-53"
s = s.strip()
# if s.isnumeric() or ( s[0] == "-" and s[1:].isnumeric() ):
if s.isnumeric() or ( s.startswith("-") and s[1:].isnumeric() ):
    print("entier relatif! ")   
# %%
