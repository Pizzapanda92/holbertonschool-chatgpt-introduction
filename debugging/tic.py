#!/usr/bin/python3
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")  # Amélioration visuelle pour séparer les lignes

def check_winner(board):
    # Vérifie les lignes
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    # Vérifie les colonnes
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Vérifie les diagonales
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    moves = 0  # Compteur pour suivre le nombre de coups joués

    while True:
        print_board(board)
        try:
            row = int(input(f"Entrez la ligne (0, 1, ou 2) pour le joueur {player}: "))
            col = int(input(f"Entrez la colonne (0, 1, ou 2) pour le joueur {player}: "))
            if 0 <= row <= 2 and 0 <= col <= 2:
                if board[row][col] == " ":
                    board[row][col] = player
                    moves += 1
                    if check_winner(board):
                        print_board(board)
                        print(f"Le joueur {player} gagne !")
                        break
                    if moves == 9:
                        print_board(board)
                        print("Match nul !")
                        break
                    player = "O" if player == "X" else "X"
                else:
                    print("Cette case est déjà prise ! Réessayez.")
            else:
                print("Veuillez entrer des indices valides entre 0 et 2.")
        except ValueError:
            print("Veuillez entrer des valeurs numériques.")

if __name__ == "__main__":
    tic_tac_toe()
  
