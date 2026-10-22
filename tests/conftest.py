"""Configurações compartilhadas pelos testes.

Usamos o driver de vídeo "dummy" do SDL para o pygame funcionar sem abrir
janela (inclusive em servidores de CI, sem monitor).
"""

import os

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")

import pygame  # noqa: E402  (precisa vir depois das variáveis de ambiente)
import pytest  # noqa: E402

from src.settings import Settings  # noqa: E402


@pytest.fixture
def settings() -> Settings:
    return Settings()


@pytest.fixture
def screen(settings: Settings) -> pygame.Surface:
    pygame.init()
    return pygame.display.set_mode((settings.screen_width, settings.screen_height))
