
import time
import random
from quickSampleMedianSelect import quickSortProject as Sort
import quickSampleMedianSelect
from sorting import Sorting
from writeOnCsv import write
import math


def sortingTest(*params):               # *params == lista di parametri

    l = list(params[0])
    numParams = len(params)
    if numParams > 1 :
        sortingFunction = params[1]

    start = time.time()

    if numParams == 5:
        sortingFunction(l, params[2], params[3], params[4])
    elif numParams == 4:
        sortingFunction(l, params[2], params[3])
    elif numParams == 3:
        sortingFunction(l, params[2])
    elif numParams == 1:
        l.sort()
    else:
        sortingFunction(l)


    return (time.time() - start)


if __name__ == "__main__":
    # Inizializzazione
    inputType = 0                    # 1 = lista ordinata crescentemente / -1 = lista ordinata decresentemente / 0 = lista generata casualmente / 2 = lista di tutti elementi uguali

    #numElements = 50000

    MAX = 110000
    START = 100000
    STEP = 10000

    slowAlgorithms = False
    flagWrite = True


    choice = {0: "Random List", 1: "Increasing List", -1: "Decreasing List", 2: "List of only '0'"}
    for i in choice.keys():
        if i == inputType:
            print("inputType: {}".format(choice[i]))
            break

    for numElements in range(START,MAX,STEP):

        print(f"\n\nTEST PERFORMED ON A LIST OF {numElements} ELEMENTS\n\nslowAlgorithms = {slowAlgorithms}\n")
        print("\n-- LIST CREATION --\n\n")


        inputList = [None] * numElements

        for i in range(0, numElements):
            if inputType == 1:
                inputList[i] = i
            elif inputType == -1:
                inputList[i] = numElements - i
            elif inputType == 0:
                inputList[i] = random.randint(0, numElements)
            elif inputType == 2:
                inputList[i] = 0
            else:
                raise Exception("You used an invalid inputType parameter!")



        dimension = len(inputList)


        print(inputList)
        print("\n\n -- LIST CREATED --")

        """

        print("\n\n-------------- SAMPLE MEDIAN SELECT -------------------")
        runningTime = sortingTest(inputList, quickSampleMedianSelect.sampleMedianSelect, math.ceil(dimension / 2), 10, 3)
        print("Only sampleMedianSelect required {} seconds.".format(runningTime))
        print("-------------------------------------------\n\n")


        print("\n\n-------------- EXECUTION TIME -------------------")
        runningTime = sortingTest(inputList, Sort)
        if flagWrite : write("../progetto/results/quickSampleMedianSelect.csv",[[numElements,runningTime]])
        print("QuickSort with sampleMedianSelect required {} seconds.".format(runningTime))

        runningTime = sortingTest(inputList, Sort, 1)
        if flagWrite: write("../progetto/results/quickWithSelectRand.csv", [[numElements, runningTime]])
        print("QuickSort with quickSelectRand required {} seconds.".format(runningTime))

        runningTime = sortingTest(inputList, Sort, 2)
        if flagWrite: write("../progetto/results/quickWithSelectDet.csv", [[numElements, runningTime]])
        print("QuickSort with quickSelectDet required {} seconds.".format(runningTime))
        print("-------------------------------------------\n\n")





        if slowAlgorithms:
            runningTime = sortingTest(inputList, Sorting.selectionSort)
            if flagWrite: write("../progetto/results/selectionSort.csv", [[numElements, runningTime]])
            print("selectionSort required {} seconds.".format(runningTime))

            runningTime = sortingTest(inputList, Sorting.insertionSortUp)
            if flagWrite: write("../progetto/results/insertionSortUp.csv", [[numElements, runningTime]])
            print("insertionSortUp required {} seconds.".format(runningTime))

            runningTime = sortingTest(inputList, Sorting.insertionSortDown)
            if flagWrite: write("../progetto/results/insertionSortDown.csv", [[numElements, runningTime]])
            print("insertionSortDown required {} seconds.".format(runningTime))

            runningTime = sortingTest(inputList, Sorting.bubbleSort)
            if flagWrite: write("../progetto/results/bubbleSort.csv", [[numElements, runningTime]])
            print("bubbleSort required {} seconds.".format(runningTime))

            print('\n')


        
        runningTime = sortingTest(inputList, Sorting.quickSortIter, True)
        if flagWrite: write("../progetto/results/quickSortIterDet.csv", [[numElements, runningTime]])
        print("quickSortIter-Det required  {} seconds.".format(runningTime))

        runningTime = sortingTest(inputList, Sorting.quickSortIter)
        if flagWrite: write("../progetto/results/quickSortIterNonDet.csv", [[numElements, runningTime]])
        print("quickSortIter-NonDet required  {} seconds.".format(runningTime))

        runningTime = sortingTest(inputList, Sorting.quickSort, True)
        if flagWrite: write("../progetto/results/quickSortRecDet.csv", [[numElements, runningTime]])
        print("quickSort(Rec)-Det required    {} seconds.".format(runningTime))

        runningTime = sortingTest(inputList, Sorting.quickSort)
        if flagWrite: write("../progetto/results/quickSortRecNonDet.csv", [[numElements, runningTime]])
        print("quickSort(Rec)-NonDet required {} seconds.".format(runningTime))
        
        """

        print('')

        runningTime = sortingTest(inputList)
        if flagWrite: write("../progetto/results/pythonSort.csv", [[numElements, runningTime]])
        print("pythonSort required {} seconds.".format(runningTime))


        """

        runningTime = sortingTest(inputList, Sorting.mergeSort)
        if flagWrite: write("../progetto/results/mergeSort.csv", [[numElements, runningTime]])
        print("mergeSort required {} seconds.".format(runningTime))
        print('')
        runningTime = sortingTest(inputList, Sorting.heapSort)
        if flagWrite: write("../progetto/results/heapSort.csv", [[numElements, runningTime]])
        print("heapSort required {} seconds.".format(runningTime))


        
        base = 400
        runningTime = sortingTest(inputList, Sorting.radixSort, numElements, base)
        if flagWrite: write("../progetto/results/radixBase400.csv", [[numElements, runningTime]])
        print("radixSort({},{}) required {} seconds.".format(numElements, base, runningTime))
        base = 100
        runningTime = sortingTest(inputList, Sorting.radixSort, numElements, base)
        if flagWrite: write("../progetto/results/radixBase100.csv", [[numElements, runningTime]])
        print("radixSort({},{}) required {} seconds.".format(numElements, base, runningTime))
        base = 10
        runningTime = sortingTest(inputList, Sorting.radixSort, numElements, base)
        if flagWrite: write("../progetto/results/radixBase10.csv", [[numElements, runningTime]])
        print("radixSort({},{}) required {} seconds.".format(numElements, base, runningTime))
        base = 2
        runningTime = sortingTest(inputList, Sorting.radixSort, numElements, base)
        if flagWrite: write("../progetto/results/radixBase2.csv", [[numElements, runningTime]])
        print("radixSort({},{}) required {} seconds.".format(numElements, base, runningTime))
        
        """
