from tkinter import *
def evaluateTerminal(board):
    for i in range(3):
        
        if board[i][0] == board[i][1] == board[i][2] != "":
            return 1 if board[i][0] == "X" else -1
        if board[0][i] == board[1][i] == board[2][i] != "":
            return 1 if board[0][i] == "X" else -1
        
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
            [Buttons[i][j].config(bg="green") for j in range(3)]
            return 1 if Buttons[i][0]["text"] == "X" else -1
        
        if Buttons[0][i]["text"] == Buttons[1][i]["text"] == Buttons[2][i]["text"] != "":
            [Buttons[j][i].config(bg="green") for j in range(3)]
            return 1 if Buttons[0][i]["text"] == "X" else -1
    
    if Buttons[0][0]["text"] == Buttons[1][1]["text"] == Buttons[2][2]["text"] != "":
        [Buttons[j][j].config(bg="green") for j in range(3)]
        return 1 if Buttons[0][0]["text"] == "X" else -1
    
    if Buttons[0][2]["text"] == Buttons[1][1]["text"] == Buttons[2][0]["text"] != "":
        [Buttons[j][2-j].config(bg="green") for j in range(3)]
        return 1 if Buttons[0][2]["text"] == "X" else -1
    
    if all(Buttons[i][j]["text"] != "" for i in range(3) for j in range(3)):
        [Buttons[i][j].config(bg="yellow") for i in range(3) for j in range(3)]
        return 2
    return 0
def updateAfterMove():
    global Turn
    result = checkWinner()
    if result == 1:
        disableButtons()
        label.config(text="Player Wins!")
    elif result == -1:
        disableButtons()
        label.config(text=" Ai wins and You will never win ")
    elif result == 2:
        disableButtons()
        label.config(text=" it's a Tie and You will never win ")
    else:
        if Turn == 1:
            label.config(text="Player's Turn")
        else:
            label.config(text="AI is Thinking")
            window.after(500, bestMove)
        Turn = 1 - Turn    

def nextTurn(row, column):
    global Turn
    if Turn == 0 and Buttons[row][column]["text"] == "":
        Buttons[row][column]["text"] = "X"
        updateAfterMove()

def disableButtons():
    [Buttons[i][j].config(state=DISABLED) for i in range(3) for j in range(3)]


def resetGame():
    startFrame.pack()
    gameFrame.pack_forget()

def startGame(starter):
    global Turn
    # reset game btns
    [Buttons[i][j].config(text="", state=NORMAL, bg="#f0f0f0") for i in range(3) for j in range(3)]
    startFrame.pack_forget()
    gameFrame.pack()
    if starter == "AI":
        Turn = 1
        label.config(text=f"AI is Thinking")
        window.after(500, bestMove)
    else:
        Turn = 0    
        label.config(text=f"Player's Turn")

window = Tk()
window.title("AI Task")

startFrame = Frame(window)
Label(startFrame, text=" it is a tie or Ai Wins game\n but choose Who should start ", font=("Arial", 24)).pack(pady=20)
Button(startFrame, text="Player", font=("Arial", 20), command=lambda: startGame("Player")).pack(pady=10)
Button(startFrame, text="AI", font=("Arial", 20), command=lambda: startGame("AI")).pack(pady=10)
startFrame.pack()

# hidden
gameFrame = Frame(window)

label = Label(gameFrame, font=("Arial", 24))
label.pack(side=TOP, pady=20)

resetBTN = Button(gameFrame, text="Reset", font=("Arial", 20), command=resetGame)
resetBTN.pack(side=TOP, pady=10)

frame = Frame(gameFrame)
frame.pack()

Buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        Buttons[i][j] = Button(frame, text="", bg="#f0f0f0", font=("Arial", 28), width=6, height=3,
                                 command=lambda i=i, j=j: nextTurn(i, j))
        Buttons[i][j].grid(row=i, column=j, padx=5, pady=5)

window.mainloop()
