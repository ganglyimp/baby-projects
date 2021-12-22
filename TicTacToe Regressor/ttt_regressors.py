import numpy
from sklearn.model_selection import KFold, train_test_split
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsRegressor 
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import classification_report

def linearRegression(X, y):
    kf = KFold(10)

    allPredictions = numpy.empty_like(y)
    allTargets = numpy.empty_like(y)

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

        allPredictions = numpy.append(allPredictions, predictions, axis=0)
        allTargets = numpy.append(allTargets, y_test, axis=0)

        #MSE
        for i in range(9):
            loss = numpy.sum((predictions[:, i] - y_test[:, i]) ** 2) / y_test[:, i].size
            if best_loss[i] == -1 or best_loss[i] > loss:
                best_loss[i] = loss
                best_theta[:, i] = theta[:, i]
    
    allPredictions = numpy.interp(allPredictions, (allPredictions.min(), allPredictions.max()), (0, 1))
    allPredictions = numpy.around(allPredictions, 0)
    print(classification_report(allTargets, allPredictions)) 

def runRegressor(reg, X, y):
    kf = KFold(10)

    predictions = numpy.empty_like(y)
    targets = numpy.empty_like(y)
    
    for train, test in kf.split(X):
        X_train = X[train]
        X_test = X[test]
        y_train = y[train]
        y_test = y[test]

        thisFoldReg = reg.fit(X_train, y_train)
        predictions = numpy.append(predictions, thisFoldReg.predict(X_test), axis=0)
        targets = numpy.append(targets, y_test, axis=0)

    predictions = numpy.around(predictions, 0)

    print(classification_report(targets, predictions))


A = numpy.loadtxt('tictac_multi.txt')
numpy.random.shuffle(A)

X = A[:, :9]
y = A[:, 9:]

exitProgram = False 
while exitProgram == False:
    print('Choose a regressor:')
    print('1. Linear Regression')
    print('2. k-Nearest Neighbors')
    print('3. Multilayer Perceptron')
    print('4. Exit Program')
    print()

    command = input('Enter Number: ')
    print()

    if command == '1':
        linearRegression(X, y)
    elif command == '2':
        runRegressor(KNeighborsRegressor(), X, y)
    elif command == '3':
        runRegressor(MLPRegressor(alpha=1e-5, max_iter=1500), X, y)
    elif command == '4':
        exitProgram = True 
        print('Exiting...')
    else:
        print('Invalid command.')