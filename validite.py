import re

def parse_formula_input(input_string):
    clauses_match = re.findall(r'\{(.*?)\}', input_string)
    if not clauses_match:
        raise ValueError("Format d'entrée invalide. Veuillez utiliser le format {¬P v ¬Q v R, ¬R, P, ¬T v Q, T}")
    clauses = [[-ord(literal[1]) + ord("A") + 1 if literal.startswith("¬") else ord(literal) - ord("A") + 1 
                for literal in clause.split(' v ')]
                for clause in clauses_match[0].split(', ')]
    return clauses

def negation(F):
    return [[-literal for literal in clause] for clause in F]

def mettre_sous_forme_de_clauses(F):
    return [F] if isinstance(F[0], int) else F

def chercher_clauses_resolvantes(clauses):
    result = []
    for i in range(len(clauses)):
        for j in range(i+1, len(clauses)):
            for literal_i in clauses[i]:
                for literal_j in clauses[j]:
                    if literal_i == -literal_j:  
                        resolvant = [literal for literal in clauses[i] if literal != literal_i] + \
                                    [literal for literal in clauses[j] if literal != literal_j]
                        resolvant = list(set(resolvant))  
                        if resolvant not in result:  
                            result.append(resolvant)
    return result

def resolution(F):
    clauses = mettre_sous_forme_de_clauses(negation(F))
    while True:
        new_resolvantes = chercher_clauses_resolvantes(clauses)
        if not new_resolvantes:
            return "F est invalide"
        for resolvant in new_resolvantes:
            if resolvant not in clauses:
                clauses.append(resolvant)
        if [] in clauses:
            return "F est valide"


formula_input = "{¬P v ¬Q v R, ¬R, P, ¬T v Q, T}"
try:
    formula = parse_formula_input(formula_input)
except ValueError as e:
    result = str(e)
    formula = None


if formula:
    resolution_result = resolution(formula)
    print(f"Formule: {formula}")
    print(f"Résultat: {resolution_result}")
