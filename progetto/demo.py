# coding: utf-8 

from time import time
import random
from sorting.__init__ import printSwitch
import progetto.quickSampleMedianSelect as Sort
import lezioni_sorting.Sorting as Sorting


# Esiste un modo migliore per passare un numero arbitrario di argomenti alle funzioni, ed un modo molto semplice per gestirli in fase di chiamata...!
def sortingTest(inputList, sortingFunction):
    l = list(inputList)  # copy the list. Equivalent to l=input[:].
    start = time()
    sortingFunction(l)
    # print(l)     # TO PRINT ORDERED LIST
    return time() - start


if __name__ == "__main__":
    # Inizializzazione
    inputType = 0  # 1 crescente, -1 decrescente, 0 random
    steps = 5000
    slowAlgorithms = True

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
    runningTime = sortingTest(inputList, Sort.quickSort)
    print("quickSort - sampleMedianSelect required {} seconds.".format(runningTime))




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

    #runningTime = sortingTest(inputList, Sorting.quickSortIter, True)
    #print("quickSortIter-Det required {} seconds.".format(runningTime))

    runningTime = sortingTest(inputList, Sorting.quickSortIter)
    print("quickSortIter-NonDet required {} seconds.".format(runningTime))
    #runningTime = sortingTest(inputList, Sorting.quickSort, True)
    #print("quickSort(Rec)-Det required {} seconds.".format(runningTime))

    runningTime = sortingTest(inputList, Sorting.quickSort)
    print("quickSort(Rec)-NonDet required {} seconds.".format(runningTime))
    print('')
    runningTime = sortingTest(inputList, Sorting.mergeSort)
    print("mergeSort required {} seconds.".format(runningTime))
    print('')
    runningTime = sortingTest(inputList, Sorting.heapSort)
    print("heapSort required {} seconds.".format(runningTime))


    """
    @TODO radix
    """


