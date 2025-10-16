# test_notation.py
import notation
# Tests unitaires pour le module notation.py

# -----------------------------
# TODO : Tests unitaires pour valider_notes()
# -----------------------------
def test_valider_notes1(): # Cas normal
    # Arrange
    notes = [3, 2, 1, 2, 3, 3, 2, 2, 3]
    resultat_attendu = True
    # Act
    resultat_validation = notation.valider_notes(notes)

    # Assert
    assert resultat_validation == resultat_attendu

#-----------------------------------------------------------------------------------------------------------------------
def test_valider_notes2(): # Cas avec plusieurs max/min identiques
    # Arrange
    notes = [3, 2, 1, 1, 3, 3, 1, 2, 3]
    resultat_attendu = True
    # Act
    resultat_validation = notation.valider_notes(notes)

    # Assert
    assert resultat_validation == resultat_attendu

#-----------------------------------------------------------------------------------------------------------------------
def test_valider_notes3(): # Cas avec des notes négatives
    # Arrange
    notes = [3, -2, 1, 2, -3, 3, -2, 2, -3]
    resultat_attendu = True
    # Act
    resultat_validation = notation.valider_notes(notes)

    # Assert
    assert resultat_validation == resultat_attendu

#-----------------------------------------------------------------------------------------------------------------------
def test_valider_notes4(): # Cas avec une liste invalide (taille)
    # Arrange
    notes = [3, 2, 1, 2, 3, 3, 2]
    resultat_attendu = False
    # Act
    resultat_validation = notation.valider_notes(notes)

    # Assert
    assert resultat_validation == resultat_attendu

#-----------------------------------------------------------------------------------------------------------------------
def test_valider_notes5(): # Cas avec des valeurs hors bornes
    # Arrange
    notes = [3, 2, 10, 2, 3, 3, -20, 2, 50]
    resultat_attendu = False
    # Act
    resultat_validation = notation.valider_notes(notes)

    # Assert
    assert resultat_validation == resultat_attendu


# -----------------------------
# TODO : Tests unitaires pour calculer_points()
# -----------------------------


def test_calculer_points1():  # Cas normal
    # Arrange
    notes = [3, 2, 1, 2, 3, 3, 2, 2, 3]
    vbase = 3.2
    resultat_attendu = 5.63
    # Act
    resultat_calculs = notation.calculer_points(vbase, notes)

    # Assert
    assert resultat_calculs == resultat_attendu


# -----------------------------------------------------------------------------------------------------------------------
def test_calculer_points2():  # Cas avec plusieurs max/min identiques
    # Arrange
    notes = [3, 2, 1, 1, 3, 3, 1, 2, 3]
    vbase = 2.5
    resultat_attendu = 4.64
    # Act
    resultat_calculs = notation.calculer_points(vbase, notes)

    # Assert
    assert resultat_calculs == resultat_attendu


# -----------------------------------------------------------------------------------------------------------------------
def test_calculer_points3():  # Cas avec des notes négatives
    # Arrange
    notes = [3, -2, 1, 2, -3, 3, -2, 2, -3]
    vbase = 1.0
    resultat_attendu = 1.14
    # Act
    resultat_calculs = notation.calculer_points(vbase, notes)

    # Assert
    assert resultat_calculs == resultat_attendu


# -----------------------------------------------------------------------------------------------------------------------
def test_calculer_points4():  # Cas avec une liste invalide (taille)
    # Arrange
    notes = [3, 2, 1, 2, 3, 3, 2]
    vbase = 3.0
    resultat_attendu = 0
    # Act
    resultat_calculs = notation.calculer_points(vbase, notes)

    # Assert
    assert resultat_calculs == resultat_attendu


# -----------------------------------------------------------------------------------------------------------------------
def test_calculer_points5():  # Cas avec des valeurs hors bornes
    # Arrange
    notes = [3, 2, 10, 2, 3, 3, -20, 2, 50]
    vbase = 2.5
    resultat_attendu = 0
    # Act
    resultat_calculs = notation.calculer_points(vbase, notes)

    # Assert
    assert resultat_calculs == resultat_attendu
