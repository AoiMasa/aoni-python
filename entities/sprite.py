class Sprite(object):
    """Classe définissant chaque élément grapghique du jeu"""

    def __init__(self,x,y,image):
        """Constructeur de la classe"""
        self.x = x
        self.y = y
        self.image = image

    def load_image(self):
        """Charge l'image du sprite en mémoire"""
        raise NotImplementedError
