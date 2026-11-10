# %%
"""
exercice : remplacer les clés entourées par "((" et "))"
dans un texte par les valeurs correspondantes dans un dico

1. afficher le contenu entre la première occurence de (( et ))
2. remplacer ((pression)) par 500 dans _template
Hint: regarder la fonction str.replace
3. itérer sur _template pour remplacer toutes les slots (())
par la clé correspondante si celle ci existe ou par N/A
"""

_template = """robinet.pression=((pression))
robinet.section=((section))
robinet.debit=((debit))
robinet.capacite=((capacite))"""

injections = {
    "pression": 500,
    "section": 30,
    "debit": 2
}

# %% ------------------- écraser des fonctions /  classes globales comme un sagouin ------------
_id = 1
_print = 'bonjour'
_str = 3.14

"""
EN PYTHON ON FAIT ATTENTION AUX NOMS DES VARIABLES !!!!!!
"""

# %% ----------------------- trouver les clés à partir des ((  )) ---------------
# 1/
while "((" in _template:
    start_index = _template.index("((") + 2
    end_index = _template.index("))")
    key = _template[start_index:end_index]

    # 2/
    _template = _template.replace("((" + key + "))", str(injections.get(key, "N/A")))

print(_template)
# %% ---------------------- for 

for k, v in injections.items():
    _template = _template.replace("((" + k + "))", str(injections[k]))

# %% --------------------- spliter selon les sauts de lignes -------
lines = []
for line in _template.splitlines():
    start_index = line.index("((") + 2
    end_index = line.index("))")
    key = line[start_index:end_index]
    lines.append(line.replace("((" + key + "))", str(injections.get(key, "N/A"))))

"\n".join(lines)
# %% ----- portage de la cellule précédente en fonction ----------
"""
technique
1/ entourer le code avec l'entête de def et ajouter le nom
2/ transformer le print ou affectation finale en return
3/ réféchir sur les paramètres d'entrée (positionnels / centraux, et optionnels => valeur par défaut) et de sortie
4/ refactorer le code pour utiliser les paramètres d'entrée et construire la sortie
5/ tester dans différents cas
"""


# %%
