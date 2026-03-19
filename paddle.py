"""
ce module contiens la classe pour les raquettes
"""


import pygame
from constants import PADDLE_SPEED, WHITE


__author__ = "ikhlef_y"


class Paddle:
    def __init__(self, x, y):
        """initialiser les raquettes
        :param x: la position x de la raquette
        :param y: la position y de la raquette
        """
        self.speed = PADDLE_SPEED
        self.color = WHITE
        self.rect = pygame.Rect(x, y, 15, 90)

    def draw(self, screen):
        """dessiner les raquettes
        :param screen: l'écran sur lequel dessiner
        """
        pygame.draw.rect(screen, WHITE, self.rect)

    def move(self, up_key, down_key):
        """déplacer les raquettes
        :param up_key: la touche pour déplacer vers le haut
        :param down_key: la touche pour déplacer vers le bas
        """
        keys = pygame.key.get_pressed()
        if keys[up_key] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[down_key] and self.rect.bottom < 600:
            self.rect.y += self.speed
