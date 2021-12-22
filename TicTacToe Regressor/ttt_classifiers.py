import numpy
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, ConfusionMatrixDisplay

def runClassifier(clf, X, y):
    kf = KFold(10)

    predictions = numpy.array([])
    targets = numpy.array([])
    
    for train, test in kf.split(X):
        X_train = X[train]
        X_test = X[test]
        y_train = y[train]
        y_test = y[test]

        thisFoldClf = clf.fit(X_train, y_train)
        predictions = numpy.append(predictions, thisFoldClf.predict(X_test))
        targets = numpy.append(targets, y_test)

    print(classification_report(targets, predictions))

    ConfusionMatrixDisplay.from_predictions(targets, predictions, normalize='true')
    plt.show()

def loadDataset(filename):
    A = numpy.loadtxt(filename)
    numpy.random.shuffle(A)
    
    X = A[:, :9]
    y = numpy.ravel(A[:, 9:])

    exitClassifierLoop = False
    while exitClassifierLoop == False:
        print(f'[CURRENT DATASET: {filename}]')
        print('Choose a classifier to run:')
        print('1. Linear SVM')
        print('2. k-Nearest Neighbors')
        print('3. Multilayer Perceptron')
        print('4. Load another dataset')
        print()

        command = input('Enter Number: ')
        print()

        if command == '1':
            runClassifier(LinearSVC(loss='hinge', random_state=0, tol=1e-5), X, y)
        elif command == '2':
            runClassifier(KNeighborsClassifier(n_neighbors=3), X, y)
        elif command == '3':
            runClassifier(MLPClassifier(random_state=1, max_iter=1000), X, y)
        elif command == '4':
            exitClassifierLoop = True
            print()
        else:
            print('Invalid command.')

exitProgram = False 
while exitProgram == False:
    print('Choose a dataset to load:')
    print('1. Final Boards Classification Dataset')
    print('2. Intermediate Boards Optimal Play (single label)')
    print('3. Exit Program')
    print()

    command = input('Enter Number: ')
    print()

    if command == '1':
        loadDataset('tictac_final.txt')
    elif command == '2':
        loadDataset('tictac_single.txt')
    elif command == '3':
        exitProgram = True 
        print('Exiting...')
    else:
        print('Invalid command.')