import math
import tkinter as tk

class TicTacToe_AGENT:
    def __init__(main):
        main.window = tk.Tk()
        main.window.title("Tic-Tac-Toe")
        main.window.title
        main.Panel = [[' ' for _ in range(3)] for _ in range(3)]
        main.buttons = [[None for _ in range(3)] for _ in range(3)]
        main.Window_frogame()
        main.window.mainloop()

    def Window_frogame(main):
        for row in range(3):
            for col in range(3):
                main.buttons[row][col] = tk.Button(main.window, text=' ', font=('Courier', 32), width=4, height=1, command=lambda row=row, col=col: main.Humans_Chance(row, col))
                main.buttons[row][col].grid(row=row, column=col)
        Start_again_button = tk.Button(main.window, text='RESTART THE GAME', height=3,command=main.Start_again )
        Start_again_button.grid(row=3, column=0, columnspan=3)

    def Humans_Chance(main, row, col):
        if main.Panel[row][col] == ' ':
            main.Panel[row][col] = 'X'
            main.buttons[row][col].config(text='X', state='disabled')
            if main.check_win('X'):
                main.RESULT("HUMAN WINS !!")
                return
            if main.DRAW():
                main.RESULT("DRAW !!")
                return
            main.AI_Chance()

    def AI_Chance(main):
        best_score = -math.inf
        best_move = None
        for row in range(3):
            for col in range(3):
                if main.Panel[row][col] == ' ':
                    main.Panel[row][col] = 'O'
                    score = main.Medium_M(0, False, -math.inf, math.inf)
                    main.Panel[row][col] = ' '
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)
        row, col = best_move
        main.Panel[row][col] = 'O'
        main.buttons[row][col].config(text='O', state='disabled')
        if main.check_win('O'):
            main.RESULT("AI WINS !!")
            return
        if main.DRAW():
            main.RESULT("DRAW !!")
            return

    def Medium_M(main, depth, is_maximizing, alpha, beta):
        if main.check_win('O'):
            return 10 - depth
        elif main.check_win('X'):
            return depth - 10
        elif main.DRAW():
            return 0

        if is_maximizing:
            best_score = -math.inf
            for row in range(3):
                for col in range(3):
                    if main.Panel[row][col] == ' ':
                        main.Panel[row][col] = 'O'
                        score = main.Medium_M(depth + 1, False, alpha, beta)
                        main.Panel[row][col] = ' '
                        best_score = max(best_score, score)
                        alpha = max(alpha, best_score)
                        if beta <= alpha:
                            break
            return best_score
        else:
            best_score = math.inf
            for row in range(3):
                for col in range(3):
                    if main.Panel[row][col] == ' ':
                        main.Panel[row][col] = 'X'
                        score = main.Medium_M(depth + 1, True, alpha, beta)
                        main.Panel[row][col] = ' '
                        best_score = min(best_score, score)
                        beta = min(beta, best_score)
                        if beta <= alpha:
                            break
            return best_score

    def check_win(main, player):
        # Checking  ROWS
        for row in range(3):
            if all([main.Panel[row][col] == player for col in range(3)]):
                return True

        # Checking  COLUMNS
        for col in range(3):
            if all([main.Panel[row][col] == player for row in range(3)]):
                return True

        # Checking DIAGONALS
        if all([main.Panel[i][i] == player for i in range(3)]):
            return True
        if all([main.Panel[i][2-i] == player for i in range(3)]):
            return True

        return False

    def DRAW(main):
        return all([main.Panel[row][col] != ' ' for row in range(3) for col in range(3)])

    def RESULT(main, result):
        result_window = tk.Toplevel(main.window)
        result_window.title("Result")
        tk.Label(result_window, text=result).pack()
        tk.Button(result_window, text="OK", command=result_window.destroy).pack()

    def Start_again(main):
        for row in range(3):
            for col in range(3):
                main.Panel[row][col] = ' '
                main.buttons[row][col].config(text=' ', state='normal')

if __name__ == "__main__":
    TicTacToe_AGENT()
