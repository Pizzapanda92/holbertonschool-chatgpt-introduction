#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.reveal_count = 0  # Ajout d'un compteur pour le nombre de révélations

    def print_board(self, reveal=False):
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if not self.revealed[y][x]:
            self.revealed[y][x] = True
            self.reveal_count += 1  # Incrémenter le compteur de révélations
            if (y * self.width + x) in self.mines:
                return False
            if self.count_mines_nearby(x, y) == 0:
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < self.width and 0 <= ny < self.height:
                            self.reveal(nx, ny)
        return True

    def play(self):
        total_cells = self.width * self.height
        while True:
            self.print_board()
            try:
                x = int(input("Entrez la coordonnée x : "))
                y = int(input("Entrez la coordonnée y : "))
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Partie terminée ! Vous avez touché une mine.")
                    break
                if self.reveal_count == total_cells - len(self.mines):
                    self.print_board(reveal=True)
                    print("Félicitations ! Vous avez gagné la partie.")
                    break
            except ValueError:
                print("Entrée invalide. Veuillez entrer uniquement des chiffres.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()

