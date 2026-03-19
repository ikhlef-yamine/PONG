"""
module main
    description:    
        Ce module contient la fonction principale du jeu PONG.
        Il initialise le jeu, gère la boucle principale, les 
        événements, les mouvements, les
"""
import pygame
import sys
from constants import WIDTH, HEIGHT, BLACK, FPS
from paddle import Paddle
from ball import Ball

def main():
    # 1. Initialisation de Pygame et de la fenêtre
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PONG - Projet Bonus")
    clock = pygame.time.Clock()

    # 2. Création des objets (Instances)
    # Joueur 1 à gauche, Joueur 2 à droite, Balle au centre
    player1 = Paddle(20, HEIGHT // 2 - 45)
    player2 = Paddle(WIDTH - 40, HEIGHT // 2 - 45)
    ball = Ball(WIDTH // 2, HEIGHT // 2)

    # 3. Boucle principale du jeu
    running = True
    while running:
        # --- Gestion des événements (Clavier/Souris) ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # --- Logique de mouvement ---
        # Joueur 1 : Z (haut) / S (bas) | Joueur 2 : Flèches
        player1.move(pygame.K_z, pygame.K_s)
        player2.move(pygame.K_UP, pygame.K_DOWN)
        ball.move()

        # --- Détection des collisions (Raquettes) ---
        if ball.rect.colliderect(player1.rect) or ball.rect.colliderect(player2.rect):
            ball.dx *= -1
        # --- Gestion des points (Sortie de l'écran) ---
        # Si la balle sort à gauche (Point pour Joueur 2)
        if ball.rect.left < 0:
            ball.rect.center = (WIDTH // 2, HEIGHT // 2)
            ball.dx *= -1  # La balle repart vers celui qui vient de marquer

        # Si la balle sort à droite (Point pour Joueur 1)
        if ball.rect.right > WIDTH:
            ball.rect.center = (WIDTH // 2, HEIGHT // 2)
            ball.dx *= -1

        # --- Dessin (Rendu) ---
        screen.fill(BLACK) # On efface l'écran précédent
        
        player1.draw(screen)
        player2.draw(screen)
        ball.draw(screen)
        
        # Ligne centrale (esthétique)
        pygame.draw.aaline(screen, (100, 100, 100), (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

        pygame.display.flip() # On met à jour l'affichage
        clock.tick(FPS)       # On limite à 60 images par seconde

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
