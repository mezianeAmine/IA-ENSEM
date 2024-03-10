Ce script Python fournit une implémentation simple pour résoudre des formules logiques en utilisant la méthode de résolution. Le code prend une formule logique en entrée, l'analyse syntaxiquement, puis tente de déterminer sa validité en utilisant la résolution.

Utilisation:
Pour utiliser le script, fournissez une formule logique dans le format spécifié et exécutez le code "python validite.py"

Exemple:
formula_input = "{¬P v ¬Q v R, ¬R, P, ¬T v Q, T}"
try:
    formula = parse_formula_input(formula_input)
except ValueError as e:
    result = str(e)
    formula = None
if formula:
    resolution_result = resolution(formula)
    print(f"Formule : {formula}")
    print(f"Résultat : {resolution_result}")

    
Format d'Entrée:
La formule d'entrée doit être entre accolades et être constituée de clauses séparées par des virgules. Chaque clause contient des littéraux joints par 'v' (OU logique). La négation est représentée par ¬ avant un littéral.

Exemple d'Entrée:
{¬P v ¬Q v R, ¬R, P, ¬T v Q, T}

Sortie:
Le script affiche la formule originale et le résultat du processus de résolution, indiquant si la formule est valide ou invalide.
