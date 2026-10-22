from typing import Any

import pygame
from pygame.sprite import Sprite

from settings import Settings
from ship import Ship


# HERANÇA: Bullet herda atributos e métodos de Sprite (objeto visual do Pygame).
class Bullet(Sprite):
    """Gerencia os projéteis disparados pela nave."""

    rect: pygame.Rect

    def __init__(
        self,
        alien_invasion_screen: pygame.Surface,
        alien_invasion_settings: Settings,
        alien_invasion_ship: Ship,
    ) -> None:
        """Cria um projétil na posição atual da nave."""
        super().__init__()
        self.screen = alien_invasion_screen
        self.settings = alien_invasion_settings
        self.ship = alien_invasion_ship
        self.color = self.settings.bullet_color

        # Cria um rect em (0, 0) e depois define a posição correta
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = self.ship.rect.midtop  # Parte superior da nave

        # Posição vertical em float para permitir movimentos suaves
        self.y = float(self.rect.y)

    def update(self, *args: Any, **kwargs: Any) -> None:
        """Move o projétil para cima na tela."""
        self.y -= self.settings.bullet_speed
        self.rect.y = int(self.y)

    def draw_bullet(self) -> None:
        """Desenha o projétil na tela."""
        pygame.draw.rect(self.screen, self.color, self.rect)
