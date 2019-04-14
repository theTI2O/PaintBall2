
class Player:
    '''
    Class Player : Cette classe comprend le modèle du joueur, sa position, son pseudo etc.
    '''
    def __init__(self, coords=(0,0,0), pseudo='unknown'):
        '''
        :param coords: triplet (x, y, alpha)
        :param pseudo: chaîne de caractère
        '''

        self.vitesse = 100
        self.coords = coords
        self.pseudo = pseudo
        self.compteur_tir = '1'
        self.etat = 0  # 0  tir, 1 en tir, 2 demande déplacement, 3 en dep


