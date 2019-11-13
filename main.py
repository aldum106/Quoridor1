import argparse
from api import débuter_partie, jouer_coup


def jouer_a_lejeu():
    idul = analyser_commande().idul
    etat = débuter_partie(idul)[1]
    identif = débuter_partie(idul)[0]

    while True:
        afficher_damier_ascii(etat)
        type_coup = input('Voulez-vous jouer un mur ou un déplacement ? (entrez D, MH ou MV) ')
        while True:
            if type_coup == 'D':
                break
            if type_coup == 'MH':
                break
            if type_coup == 'MV':
                break
            type_coup = input("L'entrée est invalide, entrez D, MH ou MV : ")
        position_x = int(input('Choisissez une case en x :'))
        position_y = int(input('Choisissez une case en y :'))
        etat = jouer_coup(identif, type_coup, (position_x, position_y))


def analyser_commande():
    parser = argparse.ArgumentParser(description='Jeu Quoridor - Phase 1')
    parser.add_argument(metavar='idul', default='idul du joueur', dest ='idul',
                        help='IDUL du joueur.')
    parser.add_argument('-l', '--lister', dest='accumulate', action='store_const',
                        const=sum, default=False,
                        help='Lister les identifiants de vos 20 dernières parties.')
    args = parser.parse_args()
    return args


def afficher_damier_ascii(dic):
    premiere_ligne = 'Légende: 1=' + dic['joueurs'][0]['nom'] + ', 2=automate \n' + '   ' + '-'*35 + '\n'
    plateau = [['.', ' ', ' ', ' ', '.', ' ', ' ', ' ', '.', ' ', ' ', ' ', '.', ' ', ' ', ' ', '.', ' ', ' ', ' ', '.',
                ' ', ' ', ' ', '.', ' ', ' ', ' ', '.', ' ', ' ', ' ', '.', ' | ', '\n',
                ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', '\n'
                ]for ligne in range(9)]

    plateau[8 - dic["joueurs"][0]['pos'][1] + 1][(dic["joueurs"][0]['pos'][0] - 1)*4] = '1'
    plateau[8 - dic["joueurs"][1]['pos'][1] + 1][(dic["joueurs"][1]['pos'][0] - 1) * 4] = '2'

    for i in range(9):
        plateau[i].insert(0, str(9-i) + ' | ')

    plateau.append(['--|-----------------------------------\n'])
    plateau.append([' ', ' ', '| ', '1', '   2', '   3', '   4', '   5', '   6', '   7', '   8', '   9'])
    plateau[8] = plateau[8][:36]

    for pos in dic['murs']['horizontaux']:
        x, y = pos[0], pos[1]
        for i in range(7):
            plateau[9-y][35 + x*4 + i] = '-'

    for pos in dic['murs']['verticaux']:
        x, y = pos
        plateau[9-y-1][x*4 -5] = '|'
        plateau[9-y-1][34 + x*4] = '|'
        plateau[9-y][x*4 -5] = '|'

    print(premiere_ligne + ''.join(''.join(i for i in ligne) for ligne in plateau) + '\n')

jouer_a_lejeu()

