""" EXO CSV RECUPERATION DE DONNEES
Imports et définition des variables globales """

### import random

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            # Convertir lignes en liste d'entiers
            return [list(map(int, line.strip().split(';'))) for line in file.readlines()]

    except FileNotFoundError:
        print(f"Erreur : Le fichier {filename} est introuvable.")
        return []

def get_list_k(data, k):
    """ Renvoie la k-ieme liste """
    if 0 <= k < len(data):
        return data[k]
    print(f"Erreur : Indice {k} out limites.")
    return None

def get_first(l):
    """ Renvoie le premier element """
    if l :
        return l[0]
    return None

def get_last(l):
    """ Renvoie le dernier element """
    if l :
        return l[-1]
    return None

def get_max(l):
    """ Renvoie l'element maximum """
    if l :
        return max(l)
    return None

def get_min(l):
    """ Renvoie l'element minimum """
    if l :
        return min(l)
    return None

def get_sum(l):
    """ Renvoie la somme de la liste """
    if l :
        return sum(l)
    return 0


#### Fonction principale

def main():
    """ Fonction principale main() """
    # data = read_data(FILENAME)
    # for i, l in enumerate(data):
    #     print(i, l)
    # k = 37
    # print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
