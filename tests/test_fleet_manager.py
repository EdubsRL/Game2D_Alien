import pygame
import pytest

from src.fast_alien import FastAlien
from src.fleet_manager import FleetManager
from src.settings import Settings
from src.ship import Ship


def test_create_fleet_cria_alienigenas(screen: pygame.Surface, settings: Settings) -> None:
    fleet = FleetManager(screen, settings, Ship(screen, settings))

    fleet.create_fleet()

    assert len(fleet.aliens) > 0


def test_create_fleet_usa_a_classe_de_alien_recebida(
    screen: pygame.Surface, settings: Settings
) -> None:
    """OCP: trocamos o tipo de alien sem alterar o FleetManager."""
    fleet = FleetManager(screen, settings, Ship(screen, settings), FastAlien)

    fleet.create_fleet()

    assert all(isinstance(alien, FastAlien) for alien in fleet.aliens)


def test_frota_na_borda_desce_e_inverte_direcao(screen: pygame.Surface, settings: Settings) -> None:
    fleet = FleetManager(screen, settings, Ship(screen, settings))
    fleet.create_fleet()
    primeiro = fleet.aliens.sprites()[0]
    primeiro.rect.left = 0  # força a borda
    y_inicial = primeiro.rect.y
    direcao_inicial = settings.fleet_direction

    fleet._update_aliens()

    assert primeiro.rect.y == y_inicial + settings.fleet_drop_speed
    assert settings.fleet_direction == -direcao_inicial


def test_sem_colisao_o_jogo_continua(screen: pygame.Surface, settings: Settings) -> None:
    fleet = FleetManager(screen, settings, Ship(screen, settings))
    fleet.create_fleet()
    fleet._check_ship_collision()  # não levanta SystemExit: a frota está longe da nave


def test_alien_encostando_na_nave_encerra_o_jogo(
    screen: pygame.Surface, settings: Settings
) -> None:
    ship = Ship(screen, settings)
    fleet = FleetManager(screen, settings, ship)
    fleet.create_fleet()
    alien = fleet.aliens.sprites()[0]
    alien.rect.center = ship.rect.center  # força a colisão

    with pytest.raises(SystemExit):
        fleet._check_ship_collision()
