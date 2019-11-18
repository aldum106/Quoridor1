'''
Ce module pose differente fonction qui nous permette d'entrer un idul
sur la ligne de commande et de jouer au jeu Quoridor directement.
On peut soir y jouer ou bien demander l'historique des 20 dernières parties.
'''

import argparse
from api import débuter_partie, jouer_coup, lister_parties


def jouer():
    '''
    Fonction permettant de jouer au jeu.
    '''
    idul = analyser_commande().idul
    etat = débuter_partie(idul)[1]
    identif = débuter_partie(idul)[0]

    while True:
        afficher_damier_ascii(etat)
        try:
            type_coup = input('Voulez-vous jouer un mur ou un déplacement ? (entrez D, MH ou MV) ')
            position_x = input('Choisissez une case en x :')
            position_y = input('Choisissez une case en y :')
            etat = jouer_coup(identif, type_coup, (position_x, position_y))
        except RuntimeError as err:
            print(err)
            print('Veuillez reprendre votre coup')
        except StopIteration as name:
            print(f'Partie terminée, {name} a gagné !')
            break


def analyser_commande():
    '''
    Fonction permettant de filtrer ce qu'on passedans la ligne de commande.

    :return: arguments
    '''
    parser = argparse.ArgumentParser(description='Jeu Quoridor - Phase 1')
    parser.add_argument(metavar='idul', default='idul du joueur', dest='idul',
                        help='IDUL du joueur.')
    parser.add_argument('-l', '--lister', dest='lister', action='store_const',
                        const=sum, default=False,
                        help='Lister les identifiants de vos 20 dernières parties.')
    args = parser.parse_args()
    return args


def afficher_damier_ascii(dic):
    '''
    Fonction nous permettant de voir le plateau de jeu à chaque coup.

    :param dic: état du jeu sous forme de dictionnaire
    :affiche: état du jeu sous forme de damier, le plateau de jeu.
    '''

    premiere_ligne = 'Légende: 1=' + dic['joueurs'][0]['nom']\
                     + ', 2=automate \n' + '   ' + '-'*35 + '\n'
    plateau = [['.', ' ', ' ', ' ',
                '.', ' ', ' ', ' ',
                '.', ' ', ' ', ' ',
                '.', ' ', ' ', ' ',
                '.', ' ', ' ', ' ',
                '.', ' ', ' ', ' ',
                '.', ' ', ' ', ' ',
                '.', ' ', ' ', ' ',
                '.', ' | ', '\n',
                ' ', ' ', '|',
                ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|',
                ' ', '\n'
                ]for ligne in range(9)]

    y_1 = dic["joueurs"][0]['pos'][1]
    x_1 = dic["joueurs"][0]['pos'][0]
    y_2 = dic["joueurs"][1]['pos'][1]
    x_2 = dic["joueurs"][1]['pos'][0]

    plateau[8 - y_1 + 1][(x_1 - 1)*4] = '1'
    plateau[8 - y_2 + 1][(x_2 - 1)*4] = '2'

    for i in range(9):
        plateau[i].insert(0, str(9-i) + ' | ')

    plateau.append(['--|-----------------------------------\n'])
    plateau.append([' ', ' ', '| ', '1', '   2', '   3', '   4'
                    , '   5', '   6', '   7', '   8', '   9'])
    plateau[8] = plateau[8][:36]

    for pos in dic['murs']['horizontaux']:
        x, y = pos
        for i in range(7):
            plateau[9-y][35 + x*4 + i] = '-'

    for pos in dic['murs']['verticaux']:
        x, y = pos
        plateau[9-y-1][x*4 -5] = '|'
        plateau[9-y-1][34 + x*4] = '|'
        plateau[9-y][x*4 -5] = '|'

    print(premiere_ligne + ''.join(''.join(i for i in ligne) for ligne in plateau) + '\n')


if analyser_commande().lister:
    print(lister_parties(analyser_commande().idul))
else:
    jouer()
