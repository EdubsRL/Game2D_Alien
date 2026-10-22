"""Exemplo didático de descontos: princípio Aberto/Fechado (OCP).

ANTES (fere o OCP): toda regra nova obriga a modificar o mesmo método.

    class Desconto:
        def calcular(self, tipo, valor):
            if tipo == "normal":
                return valor * 0.1
            elif tipo == "vip":
                return valor * 0.2
            elif tipo == "premium":
                return valor * 0.3

DEPOIS (respeita o OCP): uma classe abstrata define o contrato e cada tipo de
desconto é uma extensão. Um novo desconto = uma nova classe.
"""

from abc import ABC, abstractmethod


class Desconto(ABC):
    """Classe abstrata que define o contrato de um desconto."""

    @abstractmethod
    def calcular(self, valor: float) -> float:
        """Retorna o valor do desconto aplicado sobre ``valor``."""


class DescontoNormal(Desconto):
    """Desconto para cliente normal (10%)."""

    def calcular(self, valor: float) -> float:
        """Retorna 10% do valor."""
        return valor * 0.1


class DescontoVIP(Desconto):
    """Desconto para cliente VIP (20%)."""

    def calcular(self, valor: float) -> float:
        """Retorna 20% do valor."""
        return valor * 0.2


class DescontoPremium(Desconto):
    """Desconto para cliente Premium (30%)."""

    def calcular(self, valor: float) -> float:
        """Retorna 30% do valor."""
        return valor * 0.3


def main() -> None:
    """Demonstra os descontos no terminal."""
    valor = 100

    normal = DescontoNormal()
    vip = DescontoVIP()
    premium = DescontoPremium()

    print(f"Desconto Normal: R$ {normal.calcular(valor):.2f}")
    print(f"Desconto VIP: R$ {vip.calcular(valor):.2f}")
    print(f"Desconto Premium: R$ {premium.calcular(valor):.2f}")


if __name__ == "__main__":  # pragma: no cover
    main()
