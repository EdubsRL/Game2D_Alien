from pathlib import Path

import pygame

from settings import Settings

# Caminho absoluto da pasta images (funciona rodando de qualquer pasta)
IMAGES_DIR = Path(__file__).resolve().parent.parent / "images"


class Ship:
    """Gerencia a nave espacial."""

    def __init__(
        self, alien_invasion_screen: pygame.Surface, alien_invasion_settings: Settings
    ) -> None:
        """Inicializa a nave e define sua posição inicial."""
        self.screen = alien_invasion_screen
        self.settings = alien_invasion_settings
        self.screen_rect = self.screen.get_rect()  # Rect representa posições/áreas retangulares

        # Carrega a imagem da nave e obtém seu rect
        self.image = pygame.image.load(str(IMAGES_DIR / "ship.bmp"))
        # O pygame trata os elementos como retângulos, tornando seu processamento eficiente
        self.rect = self.image.get_rect()
        # Posiciona a nave no centro inferior da tela
        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False  # Controle do movimento para a direita
        self.moving_left = False  # Controle do movimento para a esquerda

        # Posição horizontal em float para permitir movimentos suaves
        self.x = float(self.rect.x)

    def blitme(self) -> None:
        """Desenha a nave em sua posição atual."""
        self.screen.blit(self.image, self.rect)  # ('o que', 'onde')

    def update(self) -> None:
        """Atualiza a posição da nave com base nas variáveis de controle."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Atualiza o rect da nave
        self.rect.x = int(self.x)
