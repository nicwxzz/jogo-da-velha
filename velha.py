import os
import time


class Tabuleiro:
    def __init__(self):
        self._grade = [[' ' for _ in range(3)] for _ in range(3)]

    def exibir(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("  JOGO DA VELHA - Python OOP")
        print("  -------------")
        for i, linha in enumerate(self._grade):
            print(f" {linha[0]} | {linha[1]} | {linha[2]} ")
            if i < 2:
                print("---|---|---")
        print("  -------------")

    def fazer_jogada(self, linha, coluna, simbolo):
        if self._jogada_eh_valida(linha, coluna):
            self._grade[linha][coluna] = simbolo
            return True
        return False

    def _jogada_eh_valida(self, linha, coluna):
        if 0 <= linha < 3 and 0 <= coluna < 3:
            return self._grade[linha][coluna] == ' '
        return False

    def verificar_vitoria(self, simbolo):
        for i in range(3):
            if all(self._grade[i][j] == simbolo for j in range(3)) or \
               all(self._grade[j][i] == simbolo for j in range(3)):
                return True

        if all(self._grade[i][i] == simbolo for i in range(3)) or \
           all(self._grade[i][2 - i] == simbolo for i in range(3)):
            return True

        return False

    def esta_cheio(self):
        return all(self._grade[i][j] != ' ' for i in range(3) for j in range(3))


class Jogador:
    def __init__(self, nome, simbolo):
        self.nome = nome
        self.simbolo = simbolo

    def escolher_jogada(self):
        # Contrato da interface: subclasses devem retornar uma tupla (linha, coluna)
        raise NotImplementedError("A subclasse deve implementar este método!")


class JogadorHumano(Jogador):
    def escolher_jogada(self):
        while True:
            try:
                linha = int(input(f"{self.nome} ({self.simbolo}), escolha a linha (1-3): ")) - 1
                coluna = int(input(f"{self.nome} ({self.simbolo}), escolha a coluna (1-3): ")) - 1
                return linha, coluna
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")


class Jogo:
    def __init__(self):
        self._tabuleiro = Tabuleiro()
        self._jogador1 = JogadorHumano("Jogador 1", "X")
        self._jogador2 = JogadorHumano("Jogador 2", "O")
        self._jogador_atual = self._jogador1

    def _trocar_jogador(self):
        self._jogador_atual = (
            self._jogador2 if self._jogador_atual == self._jogador1 else self._jogador1
        )

    def jogar(self):
        print("Iniciando o Jogo da Velha!")
        time.sleep(1)

        while True:
            self._tabuleiro.exibir()

            linha, coluna = self._jogador_atual.escolher_jogada()

            if not self._tabuleiro.fazer_jogada(linha, coluna, self._jogador_atual.simbolo):
                print("Jogada inválida! Tente novamente.")
                time.sleep(1.5)
                continue

            if self._tabuleiro.verificar_vitoria(self._jogador_atual.simbolo):
                self._tabuleiro.exibir()
                print(f"\nPARABÉNS! {self._jogador_atual.nome} venceu!")
                break

            if self._tabuleiro.esta_cheio():
                self._tabuleiro.exibir()
                print("\nDEU VELHA! O jogo empatou.")
                break

            self._trocar_jogador()


if __name__ == "__main__":
    meu_jogo = Jogo()
    meu_jogo.jogar()