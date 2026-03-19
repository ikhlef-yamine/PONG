"""
Module pour la classe de la balle.
"""
import pygame
# On ajoute BALL_SPEED_X, BALL_SPEED_Y et HEIGHT aux imports
from constants import WHITE, BALL_SPEED_X, BALL_SPEED_Y, HEIGHT


__author__ = "ikhlef_y"


class Ball:
    def __init__(self, x, y):
        """Initialiser la balle.
        :param x: la position x de la balle
        :param y: la position y de la balle
        """
        self.rect = pygame.Rect(x, y, 15, 15)
        self.dx = BALL_SPEED_X
        self.dy = BALL_SPEED_Y

    def draw(self, screen):
        """Dessiner la balle.
        :param screen: l'écran sur lequel dessiner
        """
        pygame.draw.ellipse(screen, WHITE, self.rect)

    def move(self):
        """Gérer le mouvement et les rebonds haut/bas."""
        self.rect.x += self.dx
        self.rect.y += self.dy
        
        # Rebond sur le haut et le bas en utilisant HEIGHT
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.dy *= -1
