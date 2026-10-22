"""Stubs e Mocks aplicados no jogo Game2D_Alien."""

import pygame
import pytest
from pytest_mock import MockerFixture

from src.alien_invasion_refactored import AlienInvasion
from src.game_events import GameEventHandler
from src.game_renderer import GameRenderer
from src.settings import Settings
from src.ship import Ship
from tests.doubles import StubSettingsRapida


# ------------------------------------------------------------------- STUB
def test_ship_com_stub_de_settings(screen: pygame.Surface) -> None:
    """O stub devolve uma velocidade conhecida (10), então sabemos o resultado exato."""
    ship = Ship(screen, StubSettingsRapida())
    x_inicial = ship.x

    ship.moving_right = True
    ship.update()

    assert ship.x == x_inicial + 10


# ------------------------------------------------------------------- MOCK
def test_barra_de_espaco_dispara_projetil(
    mocker: MockerFixture, screen: pygame.Surface, settings: Settings
) -> None:
    """Mock: verifica a INTERAÇÃO (_fire_bullet foi chamado uma vez)."""
    mock_bullet_manager = mocker.Mock()
    handler = GameEventHandler(Ship(screen, settings), mock_bullet_manager)
    evento = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE)
    mocker.patch("pygame.event.get", return_value=[evento])

    handler._check_events()

    mock_bullet_manager._fire_bullet.assert_called_once()


def test_seta_direita_liga_movimento(
    mocker: MockerFixture, screen: pygame.Surface, settings: Settings
) -> None:
    ship = Ship(screen, settings)
    handler = GameEventHandler(ship, mocker.Mock())
    mocker.patch(
        "pygame.event.get",
        return_value=[pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT)],
    )

    handler._check_events()

    assert ship.moving_right is True


def test_soltar_seta_esquerda_desliga_movimento(
    mocker: MockerFixture, screen: pygame.Surface, settings: Settings
) -> None:
    ship = Ship(screen, settings)
    ship.moving_left = True
    handler = GameEventHandler(ship, mocker.Mock())
    mocker.patch(
        "pygame.event.get",
        return_value=[pygame.event.Event(pygame.KEYUP, key=pygame.K_LEFT)],
    )

    handler._check_events()

    assert ship.moving_left is False


def test_fechar_janela_encerra_o_jogo(
    mocker: MockerFixture, screen: pygame.Surface, settings: Settings
) -> None:
    handler = GameEventHandler(Ship(screen, settings), mocker.Mock())
    mocker.patch("pygame.event.get", return_value=[pygame.event.Event(pygame.QUIT)])

    with pytest.raises(SystemExit):
        handler._check_events()


def test_renderer_pinta_o_fundo(mocker: MockerFixture, settings: Settings) -> None:
    """Mock da tela: confirma que o fundo foi pintado com a cor configurada."""
    mock_screen = mocker.Mock()
    mock_screen.blits.return_value = []  # o pygame-ce itera sobre o retorno de blits()
    mock_ship = mocker.Mock()
    mock_flip = mocker.patch("pygame.display.flip")  # não precisa de janela de verdade
    renderer = GameRenderer(
        mock_screen, settings.bg_color, mock_ship, pygame.sprite.Group(), pygame.sprite.Group()
    )

    renderer._render_screen()

    mock_screen.fill.assert_called_once_with(settings.bg_color)
    mock_ship.blitme.assert_called_once()
    mock_flip.assert_called_once()


def test_update_game_state_aciona_os_gerenciadores(mocker: MockerFixture) -> None:
    """Mock dos gerenciadores: confirmamos que o laço do jogo delega para cada um."""
    game = AlienInvasion()
    game.bullet_manager = mocker.Mock()
    game.fleet_manager = mocker.Mock()

    game._update_game_state()

    game.bullet_manager._update_bullets.assert_called_once_with(game.fleet_manager.aliens)
    game.fleet_manager._update_aliens.assert_called_once()
