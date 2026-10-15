"""Dublês de teste (test doubles) reutilizáveis."""

from src.desconto import IDesconto
from src.settings import Settings


class StubSemDesconto(IDesconto):
    """Stub: simula um desconto que sempre retorna 0 (resposta controlada)."""

    def calcular(self, valor: float) -> float:
        return 0


class StubSettingsRapida(Settings):
    """Stub de configurações: nave com velocidade fixa e conhecida."""

    def __init__(self) -> None:
        super().__init__()
        self.ship_speed = 10.0
