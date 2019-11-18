'''
Ce fichier gère 3 fonctions permettant de communiquer avec le serveur.
'''

import requests


def lister_parties(idul):
    '''
    :param idul: Idul duquel on souhaite recevoir
                l'historique de ces 20 dernieres parties.
    :return: L'historique des 20 dernière parties d'un idul particulié.
    '''
    u = 'https://python.gel.ulaval.ca/quoridor/api/'
    rep = requests.get(u + 'lister/', params={'idul': idul})
    if rep.status_code == 200:
        rep = rep.json()
        if 'message' in rep.keys():
            raise RuntimeError(rep['message'])
        return rep['parties']
    return f"Le GET sur {u} a produit le code d'erreur {rep.status_code}."


def débuter_partie(idul):
    '''
    Fait une requête au serveur pour débuter une partie

    :param idul: idul avec lequel on souhaite commencer une partie
    :return: l'état de départ que doit avoir toute partie
    '''
    u = 'https://python.gel.ulaval.ca/quoridor/api/'
    rep = requests.post(u + 'débuter/', data={'idul': idul})
    if rep.status_code == 200:
        rep = rep.json()
        if 'message' in rep.keys():
            raise RuntimeError(rep['message'])
        return (rep['id'], rep['état'])
    return f"Le POST sur {u} a produit le code d'erreur {rep.status_code}."


def jouer_coup(id_partie, type_coup, position: tuple):
    '''
    Fonction permettant de jouer tous les coup

    :param id_partie: Identifiant de la partie
    :param type_coup: La sorte de coup que le joueur souhaite jouer.
    :param position: La position à laquelle on souhaite jouer le coup.
    :return: L'état actuel du jeu
    '''
    u = 'https://python.gel.ulaval.ca/quoridor/api/'
    rep = requests.post(u + 'jouer/',
                        data={'id': id_partie,
                              'type': type_coup, 'pos': position})
    if rep.status_code == 200:
        rep = rep.json()
        if 'gagnant' in rep.keys():
            raise StopIteration(rep['gagnant'])
        if 'message' in rep.keys():
            raise RuntimeError(rep['message'])
        return rep['état']
    return f"Le POST sur {u} a produit le code d'erreur {rep.status_code}."