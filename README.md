# Game2D_Alien

Jogo **Invasão Alienígena 2D** (Pygame) usado na disciplina **Alta Qualidade de Software** — SENAI CIMATEC.
O projeto começou como um código funcional e foi evoluindo, aula a aula, para um código com qualidade:
análise estática, tipagem, princípios SOLID e testes automatizados.

## Como rodar

```powershell
python -m venv .venv
.\.venv\Scripts\activate          # Windows (PowerShell)
pip install -r requirements-dev.txt
python src/alien_invasion_refactored.py   # rode a partir da raiz do projeto
```

Controles: setas ← → movem a nave, barra de espaço atira.

## Estrutura

```
Game2D_Alien/
├── images/                 # sprites (ship.bmp, alien.bmp)
├── src/
│   ├── alien_invasion_refactored.py  # classe principal: monta os objetos e roda o laço
│   ├── settings.py         # configurações do jogo
│   ├── ship.py             # nave
│   ├── bullet.py           # projétil
│   ├── alien.py            # alienígena
│   ├── fast_alien.py       # alienígena rápido (OCP: extensão sem modificar Alien)
│   ├── bullet_manager.py   # SRP: cria/atualiza projéteis
│   ├── fleet_manager.py    # SRP: cria/atualiza a frota (recebe o tipo de alien)
│   ├── game_events.py      # SRP: trata teclado/janela
│   ├── game_renderer.py    # SRP: desenha a tela
│   └── desconto.py         # exemplo didático SOLID (S, O, L, I, D)
├── tests/                  # pytest: assert, fixture, parametrize, stub e mock
├── pytest.ini
├── pyproject.toml          # configuração do ruff, mypy e coverage
├── requirements.txt
└── requirements-dev.txt
```

## Qualidade

| Ferramenta | Comando |
|---|---|
| Lint (PEP 8 / PEP 257) | `ruff check .` |
| Formatação | `ruff format .` |
| Tipagem estática | `mypy --strict src` |
| Testes | `pytest -v` |
| Relatório HTML dos testes | `pytest --html=relatorio.html` |
| Cobertura | `coverage run -m pytest` e `coverage report` (ou `coverage html`) |

> `htmlcov/`, `.coverage` e `relatorio.html` estão no `.gitignore` e **não** devem ir para o repositório.

## Branches (Git Flow)

- `main` — versão estável
- `develop` — integração das features
- `feature/analise-estatica` — Ruff, mypy e type hints (já integrada na develop)
- `feature/applying-solid` — refatoração SRP, OCP e exemplos LSP/ISP/DIP
- `feature/tests_units` — testes unitários, stubs, mocks e cobertura

Commits seguem o padrão [Conventional Commits](https://www.conventionalcommits.org/pt-br/).
