import sys

import pygame


class AlienInvasion:
    """Gerencia o jogo e seus comportamentos."""

    def __init__(self):
        """Inicializa o jogo e cria os recursos básicos."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Laço principal: mantém a tela visível até o usuário fechar a janela."""
        while True:
            # Observa os eventos de teclado e de mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Torna visível a tela mais recente
            pygame.display.flip()


if __name__ == "__main__":
    # Cria uma instância do jogo e executa o jogo
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()
