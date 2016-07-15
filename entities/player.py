from entities import sprite

class Player(Sprite):
    """Classe définissant le joueur"""

    def __init__(self, x, y, image):
        """Constructeur de la classe"""
        Sprite.__init__(self, x, y, image)

    def move(self):
        """Fait bouger le joueur"""
        raise NotImplementedError
