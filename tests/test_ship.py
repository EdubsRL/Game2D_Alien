import pygame

from src.settings import Settings
from src.ship import Ship


def test_ship_comeca_no_centro_inferior(screen: pygame.Surface, settings: Settings) -> None:
    ship = Ship(screen, settings)
    assert ship.rect.midbottom == screen.get_rect().midbottom


def test_ship_move_esquerda(screen: pygame.Surface, settings: Settings) -> None:
    ship = Ship(screen, settings)
    x_inicial = ship.x

    ship.moving_left = True
    ship.update()

    assert ship.x == x_inicial - settings.ship_speed


def test_ship_parada_nao_se_move(screen: pygame.Surface, settings: Settings) -> None:
    ship = Ship(screen, settings)
    x_inicial = ship.x

    ship.update()

    assert ship.x == x_inicial


def test_ship_nao_passa_da_borda_direita(screen: pygame.Surface, settings: Settings) -> None:
    ship = Ship(screen, settings)
    ship.rect.right = screen.get_rect().right  # encostada na borda
    ship.x = float(ship.rect.x)

    ship.moving_right = True
    ship.update()

    assert ship.rect.right <= screen.get_rect().right
