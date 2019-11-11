import argparse


def analyser_commande():
    parser = argparse.ArgumentParser(description='Jeu Quoridor - Phase 1')
    parser.add_argument(default='idul du joueur', metavar='idul', dest ='nom du joueur',
                        help='IDUL du joueur.')
    parser.add_argument('-l', '--lister', dest='accumulate', action='store_const',
                        const=sum, default=False,
                        help='Lister les identifiants de vos 20 dernières parties.')

    args = parser.parse_args()
    return args

dic = {
    "joueurs": [
        {"nom": "idul", "murs": 7, "pos": [5, 5]},
        {"nom": "automate", "murs": 3, "pos": [8, 6]}
    ],

    
    "murs": {
        "horizontaux": [[4, 4], [2, 6], [3, 8], [5, 8], [7, 8]],
        "verticaux": [[6, 2], [4, 4], [2, 6], [7, 5], [7, 7]]
    }
}


def afficher_damier_ascii(dic):
    premiere_ligne = 'Légende: 1=' + dic['joueurs'][0]['nom'] + ', 2=automate \n' + '   ' + '-'*35 + '\n'
    plateau = [['.', ' ', ' ', ' ', '.', ' ', ' ', ' ', '.', ' ', ' ', ' ', '.', ' ', ' ', ' ', '.', ' ', ' ', ' ', '.',
                ' ', ' ', ' ', '.', ' ', ' ', ' ', '.', ' ', ' ', ' ', '.', ' | ', '\n',
                ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', '\n'
                ]for ligne in range(9)]

    pos_x_joueur = dic["joueurs"][0]['pos'][0]
    pos_y_joueur = dic["joueurs"][0]['pos'][1]
    pos_x_automate = dic["joueurs"][1]['pos'][0]
    pos_y_automate = dic["joueurs"][1]['pos'][1]
    plateau[8 - pos_y_joueur + 1][(pos_x_joueur - 1)*4] = '1'
    plateau[8 - pos_y_automate + 1][(pos_x_automate - 1) * 4] = '2'

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


#afficher_damier_ascii(dic)
#print(analyser_commande())
