# coding: utf-8 

from time import time
import random
from sorting.__init__ import printSwitch
import progetto.quickSampleMedianSelect as Sort
import lezioni_sorting.Sorting as Sorting


def sortingTest(*params):
    l = list(params[0])  # copy the list. Equivalent to l=input[:].
    numParams = len(params)
    sortingFunction = params[1]

    start = time()

    if numParams == 4:
        sortingFunction(l, params[2], params[3])
    elif numParams == 3:
        sortingFunction(l, params[2])
    else:
        sortingFunction(l)

    # print(l)     # TO PRINT ORDERED LIST
    return time() - start


if __name__ == "__main__":
    # Inizializzazione
    inputType = 0  # 1 crescente, -1 decrescente, 0 random
    steps = 1000000
    slowAlgorithms = False

    # crea lista
    inputList = [None] * steps
    for i in range(0, steps):
        if inputType == 1:
            inputList[i] = i
        elif inputType == -1:
            inputList[i] = steps - i
        elif inputType == 0:
            inputList[i] = random.randint(0, steps)
        else:
            raise Exception("You used an invalid inputType parameter!")
    printSwitch.dumpOperations = False


    print(inputList)

    print("\n\n-------------- PROGETTO -------------------")
    runningTime = sortingTest(inputList, Sort.quickSort)
    print("PROGETTO: quickSort with sampleMedianSelect required {} seconds.".format(runningTime))
    print("-------------------------------------------\n\n")





    if slowAlgorithms:
        runningTime = sortingTest(inputList, Sorting.selectionSort)
        print("selectionSort required {} seconds.".format(runningTime))
        runningTime = sortingTest(inputList, Sorting.insertionSortUp)
        print("insertionSortUp required {} seconds.".format(runningTime))
        runningTime = sortingTest(inputList, Sorting.insertionSortDown)
        print("insertionSortDown required {} seconds.".format(runningTime))
        runningTime = sortingTest(inputList, Sorting.bubbleSort)
        print("bubbleSort required {} seconds.".format(runningTime))

        print('\n')

    runningTime = sortingTest(inputList, Sorting.quickSortIter, True)
    print("quickSortIter-Det required     {} seconds.".format(runningTime))

    runningTime = sortingTest(inputList, Sorting.quickSortIter)
    print("quickSortIter-NonDet required  {} seconds.".format(runningTime))

    runningTime = sortingTest(inputList, Sorting.quickSort, True)
    print("quickSort(Rec)-Det required    {} seconds.".format(runningTime))

    runningTime = sortingTest(inputList, Sorting.quickSort)
    print("quickSort(Rec)-NonDet required {} seconds.".format(runningTime))
    print('')
    runningTime = sortingTest(inputList, Sorting.mergeSort)
    print("mergeSort required {} seconds.".format(runningTime))
    print('')
    runningTime = sortingTest(inputList, Sorting.heapSort)
    print("heapSort required {} seconds.".format(runningTime))

    print("\n\nradix")

    base = 400
    runningTime = sortingTest(inputList, Sorting.radixSort, steps, base)
    print("radixSort({},{}) required {} seconds.".format(steps, base, runningTime))
    base = 100
    runningTime = sortingTest(inputList, Sorting.radixSort, steps, base)
    print("radixSort({},{}) required {} seconds.".format(steps, base, runningTime))
    base = 10
    runningTime = sortingTest(inputList, Sorting.radixSort, steps, base)
    print("radixSort({},{}) required {} seconds.".format(steps, base, runningTime))
    base = 2
    runningTime = sortingTest(inputList, Sorting.radixSort, steps, base)
    print("radixSort({},{}) required {} seconds.".format(steps, base, runningTime))

