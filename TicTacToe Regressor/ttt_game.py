import numpy
from sklearn.model_selection import KFold
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsRegressor 
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import classification_report

def linearRegression(X, y):
    kf = KFold(10)

    best_loss = numpy.array([-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0])
    best_theta = numpy.full((10, 9), -1.0)
    for train, test in kf.split(X):
        X_train = X[train]
        X_test = X[test]
        y_train = y[train]
        y_test = y[test]

        #add column of 1s to leftmost column of X_train and X_test
        X_train = numpy.append(numpy.ones((len(X_train), 1)), X_train, axis=1)
        X_test = numpy.append(numpy.ones((len(X_test), 1)), X_test, axis=1)
        
        theta = numpy.linalg.inv(X_train.T.dot(X_train)).dot(X_train.T).dot(y_train)
        predictions = X_test.dot(theta)

        #MSE
        for i in range(9):
            loss = numpy.sum((predictions[:, i] - y_test[:, i]) ** 2) / y_test[:, i].size
            if best_loss[i] == -1 or best_loss[i] > loss:
                best_loss[i] = loss
                best_theta[:, i] = theta[:, i]
    
    return best_theta

def printGameBoard(gameGrid):
    gameSpaces = numpy.array(['1', '2', '3', '4', '5', '6', '7', '8', '9'])

    for i in range(9):
        if gameGrid[i] == 1:
            gameSpaces[i] = 'X'
        elif gameGrid[i] == -1:
            gameSpaces[i] = 'O'
    
    gameBoard = numpy.array(['     |     |',
                             f'  {gameSpaces[0]}  |  {gameSpaces[1]}  |  {gameSpaces[2]}  ',
                             '_____|_____|_____',
                             '     |     |',
                             f'  {gameSpaces[3]}  |  {gameSpaces[4]}  |  {gameSpaces[5]}  ',
                             '_____|_____|_____',
                             '     |     |',
                             f'  {gameSpaces[6]}  |  {gameSpaces[7]}  |  {gameSpaces[8]}  ',
                             '     |     |'])
    
    for line in gameBoard:
        print(line)
    print()

def isGameOver(gameGrid):
    # Check for tie
    zeroCount = 0
    for cell in gameGrid:
        if cell == 0:
            zeroCount = zeroCount + 1
    if zeroCount < 1:
        return True
    
    # Top Row
    if gameGrid[0] == gameGrid[1] == gameGrid[2] != 0:
        return True
    # Middle Row
    elif gameGrid[3] == gameGrid[4] == gameGrid[5] != 0:
        return True
    # Bottom Row
    elif gameGrid[6] == gameGrid[7] == gameGrid[8] != 0:
        return True
    # Left Column
    elif gameGrid[0] == gameGrid[3] == gameGrid[6] != 0:
        return True
    # Middle Column
    elif gameGrid[1] == gameGrid[4] == gameGrid[7] != 0:
        return True
    # Right Column
    elif gameGrid[2] == gameGrid[5] == gameGrid[8] != 0:
        return True
    # L2R Diagonal
    elif gameGrid[0] == gameGrid[4] == gameGrid[8] != 0:
        return True
    # R2L Diagonal
    elif gameGrid[2] == gameGrid[4] == gameGrid[6] != 0:
        return True
    else:
        return False

def gameLoop(compAI):
    playerTurn = True
    gameGrid = numpy.array([0, 0, 0, 0, 0, 0, 0, 0, 0])

    print("Starting new game....")
    print()

    turnNum = 0
    gameOver = False
    while gameOver == False:
        printGameBoard(gameGrid)
        if playerTurn:
            selectedSpace = input('Enter Cell #: ')

            try:
                spaceNum = int(selectedSpace)-1

                if gameGrid[spaceNum] == 0:
                    gameGrid[spaceNum] = 1
                    playerTurn = False
                else:
                    print('That space is already taken. Please select another space.')
                    print()
            except:
                print('Invalid input. Please enter a valid cell number in the range of 1-9.')
                print()
        else:
            print('Computer is now making a move...')

            if type(compAI) is numpy.ndarray:
                theGrid = numpy.append([1], gameGrid, axis=0)
                compMoves = theGrid.dot(compAI)
                
                moveMade = False
                while moveMade == False:
                    bestMove = numpy.argmax(compMoves)
                    if gameGrid[bestMove] == 0:
                        gameGrid[bestMove] = -1
                        moveMade = True
                    else:
                        compMoves[bestMove] = -1
            else:     
                compMoves = compAI.predict([gameGrid])

                moveMade = False
                while moveMade == False:
                    bestMove = numpy.argmax(compMoves)
                    if gameGrid[bestMove] == 0:
                        gameGrid[bestMove] = -1
                        moveMade = True
                    else:
                        compMoves[bestMove] = -1

            playerTurn = True
        
        gameOver = isGameOver(gameGrid)
        turnNum = turnNum + 1
    
    printGameBoard(gameGrid)
    if turnNum > 8:
        print('It\'s a tie.')
    elif playerTurn == True:
        print('O wins!')
    else:
        print('X wins!')


print('Loading datasets...')

A = numpy.loadtxt('tictac_multi.txt')
numpy.random.shuffle(A)

X = A[:, :9]
y = A[:, 9:]

print('Fitting regressors...')
print()

linReg = linearRegression(X, y)

kNeighbors = KNeighborsRegressor(weights='distance')
kNeighbors.fit(X, y)

mlp = MLPRegressor(alpha=1e-5, random_state=1, max_iter=1500)
mlp.fit(X, y)

exitProgram = False 
while exitProgram == False:
    print('Choose a regressor for the AI:')
    print('1. Linear Regression')
    print('2. k-Nearest Neighbors')
    print('3. Multilayer Perceptron')
    print('4. Exit Program')
    print()

    command = input('Enter Number: ')
    print()

    if command == '1':
        gameLoop(linReg)
    elif command == '2':
        gameLoop(kNeighbors)
    elif command == '3':
        gameLoop(mlp)
    elif command == '4':
        exitProgram = True 
        print('Exiting...')
    else:
        print('Invalid command.')