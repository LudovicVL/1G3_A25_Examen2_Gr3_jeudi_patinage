# notation.py
# TODO : Version buggée — à corriger après exécution des tests unitaires
# TODO : Mettre des commentaires pour identifier les bugs trouvés et comment vous les avez corrigés.

def valider_notes(notes: list[float]) -> bool:
    """
    Vérifie que la liste de notes contient exactement 9 entiers entre -3 et +3.
    :param notes: liste de notes
    :returns: vrai si la liste et valide, sinon faux.
    """
    if len(notes) < 9 or len(notes) > 9:
        return False

    for n in notes:
        if -3 > n > 3:
            return False

    else:
        return True


def calculer_points(vbase: float, notes: list[float]) -> float:
    """
        Calcule le total des points pour un mouvement de patinage.
        Paramètres :
            vbase (float) : valeur de base du mouvement
            notes (list[int]) : 9 notes des juges (valeurs entre -3 et 3)
        Retourne :
            float : total des points (vbase + moyenne des notes restantes)
        """
    try:
        valider_notes(notes)

        note_max = max(notes)
        note_min = min(notes)

        for i in range(len(notes)):
            if notes[i] == note_max or note_min:
                notes.remove(notes[i])

        moyenne = sum(notes) / len(notes)
        total = vbase + moyenne
        return total

    except IndexError:
        print("Erreur")
        return 0



