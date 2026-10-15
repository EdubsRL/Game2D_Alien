import pygame
import pytest

from src.alien import Alien
from src.fast_alien import FastAlien
from src.settings import Settings


def test_alien_move_na_direcao_da_frota(screen: pygame.Surface, settings: Settings) -> None:
    alien = Alien(screen, settings)
    x_inicial = alien.x

    alien.update()

    assert alien.x == x_inicial + settings.alien_speed * settings.fleet_direction


def test_alien_check_edges_na_borda_esquerda(screen: pygame.Surface, settings: Settings) -> None:
    alien = Alien(screen, settings)
    alien.rect.left = 0
    assert alien.check_edges() is True


def test_alien_check_edges_no_meio(screen: pygame.Surface, settings: Settings) -> None:
    alien = Alien(screen, settings)
    alien.rect.x = 300
    assert alien.check_edges() is False


def test_fast_alien_e_mais_rapido_que_alien(screen: pygame.Surface, settings: Settings) -> None:
    """LSP/OCP: FastAlien substitui Alien e anda o dobro."""
    alien = Alien(screen, settings)
    rapido = FastAlien(screen, settings)
    x_alien, x_rapido = alien.x, rapido.x

    alien.update()
    rapido.update()

    assert (rapido.x - x_rapido) == pytest.approx(2 * (alien.x - x_alien))
