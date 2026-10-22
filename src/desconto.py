"""Exemplo didático de descontos aplicando os princípios SOLID (Aula 06).

- S (SRP): cada classe tem uma única responsabilidade (calcular um desconto,
  aplicar cupom, totalizar um pedido...).
- O (OCP): um novo tipo de desconto é uma nova classe; nada existente muda.
- L (LSP): qualquer filha de ``IDesconto`` pode substituir a mãe em
  ``aplicar_desconto`` sem quebrar o programa.
- I (ISP): interfaces pequenas (``IDesconto``, ``ICupom``, ``IVIP``).

  ANTES (fere o princípio 'I'): uma interface única obrigava ``DescontoNormal``
  a implementar métodos que não fazem sentido para ela::

      class IDesconto:
          def calcular(self, valor): raise NotImplementedError
          def aplicar_cupom(self, codigo): raise NotImplementedError
          def validar_usuario_vip(self, usuario): raise NotImplementedError

      class DescontoNormal(IDesconto):
          def calcular(self, valor): return valor * 0.1
          def aplicar_cupom(self, codigo): raise NotImplementedError        # sem sentido
          def validar_usuario_vip(self, usuario): raise NotImplementedError # sem sentido

- D (DIP): ``Pedido`` depende da abstração ``IDesconto`` (recebida no
  construtor), e não de ``DescontoNormal``.

  ANTES (fere o princípio 'D')::

      class Pedido:
          def __init__(self):
              self.desconto = DescontoNormal()   # dependência concreta

          def total(self, valor):
              return valor - self.desconto.calcular(valor)
"""


# ----------------------------------------------------------------- interfaces
# Em Python, uma "interface" pode ser uma classe cujos métodos só levantam
# NotImplementedError: quem herdar é obrigado a sobrescrever.
class IDesconto:
    """Contrato de qualquer desconto."""

    def calcular(self, valor: float) -> float:
        """Retorna o valor do desconto aplicado sobre ``valor``."""
        raise NotImplementedError


class ICupom:
    """Contrato de quem aceita cupom."""

    def aplicar_cupom(self, codigo: str) -> bool:
        """Retorna True se o cupom for aceito."""
        raise NotImplementedError


class IVIP:
    """Contrato de quem valida usuário VIP."""

    def validar_usuario_vip(self, usuario: str) -> bool:
        """Retorna True se o usuário for VIP."""
        raise NotImplementedError


# ------------------------------------------------------------ implementações
class DescontoNormal(IDesconto):
    """Desconto para cliente normal (10%). Só implementa o que precisa (ISP)."""

    def calcular(self, valor: float) -> float:
        """Retorna 10% do valor."""
        return valor * 0.1


class DescontoVIP(IDesconto, ICupom, IVIP):
    """Desconto para cliente VIP (20%), aceita cupom e valida usuário VIP."""

    def calcular(self, valor: float) -> float:
        """Retorna 20% do valor."""
        return valor * 0.2

    def aplicar_cupom(self, codigo: str) -> bool:
        """VIP sempre aceita cupom."""
        return True

    def validar_usuario_vip(self, usuario: str) -> bool:
        """Valida se o usuário é VIP."""
        return usuario == "vip"


class DescontoPremium(IDesconto):
    """Desconto para cliente Premium (30%)."""

    def calcular(self, valor: float) -> float:
        """Retorna 30% do valor."""
        return valor * 0.3


# ---------------------------------------------------------------- uso (LSP)
def aplicar_desconto(desconto: IDesconto, valor: float) -> float:
    """Funciona com QUALQUER filha de IDesconto (Liskov)."""
    return desconto.calcular(valor)


def aplicar_cupom(cupom: ICupom, codigo: str) -> bool:
    """Só recebe objetos que realmente aceitam cupom (ISP)."""
    return cupom.aplicar_cupom(codigo)


# ---------------------------------------------------------------- uso (DIP)
class Pedido:
    """Pedido que depende da abstração IDesconto (injeção de dependência)."""

    def __init__(self, desconto: IDesconto) -> None:
        """Recebe o desconto pronto (não cria a dependência concreta)."""
        self.desconto = desconto

    def total(self, valor: float) -> float:
        """Retorna o valor final do pedido já com desconto."""
        return valor - self.desconto.calcular(valor)


if __name__ == "__main__":  # pragma: no cover
    valor = 100

    # LSP: qualquer filha substitui a mãe
    print("Normal:", aplicar_desconto(DescontoNormal(), valor))
    print("VIP:", aplicar_desconto(DescontoVIP(), valor))
    print("Premium:", aplicar_desconto(DescontoPremium(), valor))

    # ISP
    normal = DescontoNormal()
    vip = DescontoVIP()
    print("Desconto normal:", aplicar_desconto(normal, valor))
    print("Desconto VIP:", aplicar_desconto(vip, valor))
    print("Cupom VIP:", aplicar_cupom(vip, "DESC10"))

    # DIP
    pedido_normal = Pedido(DescontoNormal())
    pedido_vip = Pedido(DescontoVIP())
    print("Normal:", pedido_normal.total(valor))
    print("VIP:", pedido_vip.total(valor))
