class AI:

    def __init__(self,board, myMove, myLetter):
        self.board = board
        self.myMove = myMove
        self.myLetter = myLetter
        self.opponentLetter = "X" if myLetter == "O" else "O"

    def score(self):
        a = self.myLetter * 3
        o = self.opponentLetter * 3
        b = self.board

        if b[0] + b[1] + b[2] == a or b[3] + b[4] + b[5] == a or b[6] + b[7] + b[8] == a:
            return 1
        if b[0] + b[3] + b[6] == a or b[1] + b[4] + b[7] == a or b[2] + b[5] + b[8] == a:
            return 1
        if b[0] + b[4] + b[8] == a or b[2] + b[4] + b[6] == a:
            return 1

        if b[0] + b[1] + b[2] == o or b[3] + b[4] + b[5] == o or b[6] + b[7] + b[8] == o:
            return -1
        if b[0] + b[3] + b[6] == o or b[1] + b[4] + b[7] == o or b[2] + b[5] + b[8] == o:
            return -1
        if b[0] + b[4] + b[8] == o or b[2] + b[4] + b[6] == o:
            return -1

        return 0

    def isTerminalState(self):
        return self.score() != 0 or not "-" in self.board

    def possibleStates(self):
        states = []

        for i in range(0,9):
            if self.board[i] == "-":
                tempState = self.board.copy()
                tempState[i] = self.myLetter if self.myMove else self.opponentLetter
                states.append(AI(tempState,not self.myMove, self.myLetter))

        return states

    def minimax(self):
        if self.isTerminalState():
            return (self.score(), self)

        possibleStates = self.possibleStates()
        bestState = possibleStates[0]
        bestResult = -999 if self.myMove else 999

        for state in self.possibleStates():
            stateScore = state.minimax()[0]

            if self.myMove and stateScore > bestResult:
                bestResult = stateScore
                bestState = state
            elif not self.myMove and stateScore < bestResult:
                bestResult = stateScore
                bestState = state

        return (bestResult, bestState)

    def printBoard(self):
        for i in range(0,9):
            if (i+1) % 3 == 0:
                print(self.board[i])
            else:
                print(self.board[i], end=" ")

    def boardStateMessage(self):
        if self.minimax()[0] == 1:
            print("You are in a lost position")
        elif self.minimax()[0] == -1:
            print("You are in a winning position")
        else:
            print("The current position is a draw")

aiLetter = "X" if input("What letter do you want to play as?: ").upper() == "O" else "O"
board = ["-","-","-","-","-","-","-","-","-"]
aiTurn = aiLetter == "X"
ai = AI(board,aiTurn,aiLetter)
ai.printBoard()
print()

while not ai.isTerminalState():
    if ai.myMove:
        bestScore, bestState = ai.minimax()
        bestState.printBoard()
        bestState.boardStateMessage()
        ai.board = bestState.board
        ai.myMove = False
        print()
    else:
        index = int(input("At which index [0-8] do you want to place your letter?: "))
        ai.board[index] = ai.opponentLetter
        ai.printBoard()
        ai.myMove = True
        print()