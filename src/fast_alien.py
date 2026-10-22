from typing import Any

from alien import Alien


class FastAlien(Alien):
    """Alienígena mais rápido (estende Alien sem modificá-la - princípio O)."""

    def update(self, *args: Any, **kwargs: Any) -> None:
        """Move o alienígena com o dobro da velocidade."""
        self.x += (self.settings.alien_speed * 2) * self.settings.fleet_direction
        self.rect.x = int(self.x)
