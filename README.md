# Jogo da Velha feito em Python

## Sobre o Projeto

Este projeto é uma implementação do **Jogo da Velha** no terminal, desenvolvido com foco em conceitos fundamentais de **Programação Orientada a Objetos**. Cada decisão de código foi pensada para demonstrar na prática como aplicar POO de forma clara e organizada.

---

## 🧠 Conceitos de POO Aplicados

| Conceito | Onde foi Aplicado |
|---|---|
| **Classe & Objeto** | `Tabuleiro`, `Jogador`, `Jogo` |
| **Encapsulamento** | Atributo `_grade` e métodos privados com `_` |
| **Herança** | `JogadorHumano` herda de `Jogador` |
| **Abstração** | Método `escolher_jogada()` na classe base |
| **Polimorfismo** | O jogo chama `escolher_jogada()` sem saber o tipo do jogador |
| **Composição** | A classe `Jogo` contém um `Tabuleiro` e `Jogadores` |

---

## 🗂️ Estrutura do Código

```
velha.py
│
├── class Tabuleiro        → Gerencia o estado do tabuleiro
│   ├── exibir()           → Renderiza o grid no terminal
│   ├── fazer_jogada()     → Registra uma jogada (com validação)
│   ├── verificar_vitoria()→ Checa linhas, colunas e diagonais
│   └── esta_cheio()       → Detecta empate
│
├── class Jogador          → Classe base (abstrata)
│   └── escolher_jogada()  → Interface para todos os jogadores
│
├── class JogadorHumano(Jogador)
│   └── escolher_jogada()  → Lê entrada do teclado
│
└── class Jogo             → Orquestra o loop principal
    ├── jogar()            → Loop do jogo
    └── _trocar_jogador()  → Alterna os turnos
```

---

## Como Executar

**Pré-requisito:** Python 3.6+

```bash
# Clone o repositório
git clone https://github.com/nicwxzz/jogo-da-velha.git

# Entre na pasta
cd jogo-da-velha

# Execute o jogo
python velha.py
```

---

## Como Jogar

1. O **Jogador 1** usa o símbolo `X` e o **Jogador 2** usa `O`
2. Cada turno, o jogador informa a **linha** (1–3) e a **coluna** (1–3) desejadas
3. Vence quem completar uma linha, coluna ou diagonal
4. Se o tabuleiro encher sem vencedor: **empate!**

---

## Possíveis Melhorias Futuras

- [ ] Adicionar modo de **IA** (JogadorIA como nova subclasse)
- [ ] Implementar o algoritmo **Minimax** para a IA
- [ ] Criar interface gráfica com `tkinter` ou `pygame`
- [ ] Adicionar placar com **histórico de partidas**

---

## 📚 Tecnologias

![Python](https://img.shields.io/badge/Python-3.6+-3776AB?style=for-the-badge&logo=python&logoColor=white)

---

## 👤 Autor

Nicolas Oliveira.
