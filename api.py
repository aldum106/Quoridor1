import requests


def lister_parties(idul):
    url_base = 'https://python.gel.ulaval.ca/quoridor/api/'
    rep = requests.get(url_base + 'lister/', params={'idul': idul})
    if rep.status_code == 200:
        rep = rep.json()
        if 'message' in rep.keys():
            raise RuntimeError(rep['message'])
        return rep['parties']
    return f"Le GET sur {url} a produit le code d'erreur {rep.status_code}."


def débuter_partie(idul):
    url_base = 'https://python.gel.ulaval.ca/quoridor/api/'
    rep = requests.post(url_base + 'débuter/', data={'idul': idul})
    if rep.status_code == 200:
        rep = rep.json()
        if 'message' in rep.keys():
            raise RuntimeError(rep['message'])
        return (rep['id'], rep['état'])
    else:
        return f"Le POST sur {url} a produit le code d'erreur {rep.status_code}."


def jouer_coup(id_partie, type_coup, position : tuple):
    url_base = 'https://python.gel.ulaval.ca/quoridor/api/'
    rep = requests.post(url_base + 'jouer/', data={'id': id_partie, 'type': type_coup, 'pos': position})
    if rep.status_code == 200:
        rep = rep.json()
        if 'gagnant' in rep.keys():
            raise StopIteration(rep['gagnant'])
        if 'message' in rep.keys():
            raise RuntimeError(rep['message'])
        return rep['état']
    return f"Le POST sur {url} a produit le code d'erreur {rep.status_code}."

