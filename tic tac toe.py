from tkinter import *
def evaluateTerminal(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return 1 if board[i][0] == "X" else -1
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != "":
            return 1 if board[0][j] == "X" else -1
    if board[0][0] == board[1][1] == board[2][2] != "":
        return 1 if board[0][0] == "X" else -1
    if board[0][2] == board[1][1] == board[2][0] != "":
        return 1 if board[0][2] == "X" else -1
    return 0
def minimax(board, isMaximizing):
    score = evaluateTerminal(board)
    if score != 0:
        return score
    if not any("" in row for row in board):
        return 0
    bestScore = -float('inf') if isMaximizing else float('inf')
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = "X" if isMaximizing else "O"
                score = minimax(board, not isMaximizing)
                board[i][j] = ""
                bestScore = max(score, bestScore) if isMaximizing else min(score, bestScore)
    return bestScore

def getBoard():
    return [[Buttons[i][j]["text"] for j in range(3)] for i in range(3)]

def bestMove():
    board = getBoard()
    bestScore = float('inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = "O"
                score = minimax(board, True)
                board[i][j] = ""
                if score < bestScore:
                    bestScore = score
                    move = (i, j)
    if move:
        row, col = move
        Buttons[row][col]["text"] = "O"
        updateAfterMove()

def checkWinner():
    for i in range(3):
        if Buttons[i][0]["text"] == Buttons[i][1]["text"] == Buttons[i][2]["text"] != "":
            for j in range(3):
                Buttons[i][j].config(bg="green")
            return 1 if Buttons[i][0]["text"] == "X" else -1
    for j in range(3):
        if Buttons[0][j]["text"] == Buttons[1][j]["text"] == Buttons[2][j]["text"] != "":
            for i in range(3):
                Buttons[i][j].config(bg="green")
            return 1 if Buttons[0][j]["text"] == "X" else -1
    if Buttons[0][0]["text"] == Buttons[1][1]["text"] == Buttons[2][2]["text"] != "":
        for i in range(3):
            Buttons[i][i].config(bg="green")
        return 1 if Buttons[0][0]["text"] == "X" else -1
    if Buttons[0][2]["text"] == Buttons[1][1]["text"] == Buttons[2][0]["text"] != "":
        for i in range(3):
            Buttons[i][2-i].config(bg="green")
        return 1 if Buttons[0][2]["text"] == "X" else -1
    if all(Buttons[i][j]["text"] != "" for i in range(3) for j in range(3)):
        [Buttons[i][j].config(bg="yellow") for i in range(3) for j in range(3)]
        return 2
    return 0
def updateAfterMove():
    result = checkWinner()
    global Turn
    if result == 1:
        disableButtons()
        label.config(text="Player Wins!")
    elif result == -1:
        disableButtons()
        label.config(text="AI Wins!")
    elif result == 2:
        disableButtons()
        label.config(text="Tie!")
    else:
        if Turn == 1:
            Turn = 0
            label.config(text="Player's Turn")
        else:
            Turn = 1
            label.config(text="AI's Turn")
            window.after(200, bestMove)

def nextTurn(row, column):
    global Turn
    if Turn == 0 and Buttons[row][column]["text"] == "":
        Buttons[row][column]["text"] = "X"
        updateAfterMove()

def disableButtons():
    for i in range(3):
        for j in range(3):
            Buttons[i][j].config(state=DISABLED)

def resetGame():
    global Turn
    Turn = None
    label.config(text="Choose who starts!")
    for i in range(3):
        for j in range(3):
            Buttons[i][j].config(text="", state=NORMAL, bg="#f0f0f0")
    startFrame.pack()
    gameFrame.pack_forget()

def startGame(starter):
    global Turn
    Turn = 0 if starter == "Player" else 1
    startFrame.pack_forget()
    gameFrame.pack()
    label.config(text=f"{starter}'s Turn")
    if Turn == 1:
        window.after(500, bestMove)

window = Tk()
window.title("Tic Tac Toe with AI")

# Start Menu Frame
startFrame = Frame(window)
Label(startFrame, text="Who should start?", font=("Arial", 24)).pack(pady=20)
Button(startFrame, text="Player", font=("Arial", 20), command=lambda: startGame("Player")).pack(pady=10)
Button(startFrame, text="AI", font=("Arial", 20), command=lambda: startGame("AI")).pack(pady=10)
startFrame.pack()

# Game Frame (initially hidden)
gameFrame = Frame(window)

label = Label(gameFrame, text="Choose who starts!", font=("Arial", 24))
label.pack(side=TOP, pady=20)

resetBTN = Button(gameFrame, text="Reset", font=("Arial", 20), command=resetGame)
resetBTN.pack(side=TOP, pady=10)

frame = Frame(gameFrame)
frame.pack()

# Increase button size and font for a larger board
Buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        Buttons[i][j] = Button(frame, text="", bg="#f0f0f0", font=("Arial", 28), width=6, height=3,
                                 command=lambda i=i, j=j: nextTurn(i, j))
        Buttons[i][j].grid(row=i, column=j, padx=5, pady=5)

window.mainloop()
