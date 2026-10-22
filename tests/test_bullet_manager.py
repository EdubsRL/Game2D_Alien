import pygame

from src.bullet_manager import BulletManager
from src.settings import Settings
from src.ship import Ship


def test_fire_bullet_respeita_limite(screen: pygame.Surface, settings: Settings) -> None:
    settings.bullet_allowed = 1
    manager = BulletManager(screen, settings, Ship(screen, settings))

    manager._fire_bullet()
    manager._fire_bullet()  # passou do limite: não deve criar outro

    assert len(manager.bullets) == 1


def test_bullet_sobe_ao_atualizar(screen: pygame.Surface, settings: Settings) -> None:
    manager = BulletManager(screen, settings, Ship(screen, settings))
    manager._fire_bullet()
    bullet = manager.bullets.sprites()[0]
    y_inicial = bullet.y

    manager._update_bullets(pygame.sprite.Group())

    assert bullet.y == y_inicial - settings.bullet_speed


def test_bullet_fora_da_tela_e_removido(screen: pygame.Surface, settings: Settings) -> None:
    manager = BulletManager(screen, settings, Ship(screen, settings))
    manager._fire_bullet()
    bullet = manager.bullets.sprites()[0]
    bullet.y = -100.0  # já saiu pelo topo

    manager._update_bullets(pygame.sprite.Group())

    assert len(manager.bullets) == 0
