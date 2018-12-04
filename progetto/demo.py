
import time
import random
from progetto.quickSampleMedianSelect import quickSortProject as Sort
import sorting.Sorting as Sorting


def sortingTest(*params):               # *params ==

    l = list(params[0])
    numParams = len(params)
    sortingFunction = params[1]

    start = time.time()

    if numParams == 4:
        sortingFunction(l, params[2], params[3])
    elif numParams == 3:
        sortingFunction(l, params[2])
    else:
        sortingFunction(l)


    return (time.time() - start)


if __name__ == "__main__":
    # Inizializzazione
    inputType = 0                    # 1 = lista ordinata crescentemente / -1 = lista ordinata decresentemente / 0 = lista generata casualmente / 2 = lista di tutti elementi uguali

    numElements = 10000
    slowAlgorithms = False


    print(f"\n\nTEST PERFORMED ON A LIST OF {numElements} ELEMENTS\n\nslowAlgorithms = {slowAlgorithms}\n")

    choise = {0: "Random List", 1: "Increasing List", -1: "Decreasing List", 2: "List of only '0'"}
    for i in choise.keys():
        if i == inputType:
            print("inputType: {}".format(choise[i]))
            break


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




    print(inputList)
    print("\n\n -- LIST CREATED --")

    print("\n\n-------------- EXECUTION TIME -------------------")
    runningTime = sortingTest(inputList, Sort)
    print("QuickSort with sampleMedianSelect required {} seconds.".format(runningTime))

    runningTime = sortingTest(inputList, Sort, 1)
    print("QuickSort with quickSelectRand required {} seconds.".format(runningTime))

    runningTime = sortingTest(inputList, Sort, 2)
    print("QuickSort with quickSelectDet required {} seconds.".format(runningTime))

    # runningTime = sortingTest(inputList, Sort.quickSortConSelectDeterministo)
    # print("QuickSort with quickSelectDet required {} seconds.".format(runningTime))
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
    print("quickSortIter-Det required  {} seconds.".format(runningTime))

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



    base = 400
    runningTime = sortingTest(inputList, Sorting.radixSort, numElements, base)
    print("radixSort({},{}) required {} seconds.".format(numElements, base, runningTime))
    base = 100
    runningTime = sortingTest(inputList, Sorting.radixSort, numElements, base)
    print("radixSort({},{}) required {} seconds.".format(numElements, base, runningTime))
    base = 10
    runningTime = sortingTest(inputList, Sorting.radixSort, numElements, base)
    print("radixSort({},{}) required {} seconds.".format(numElements, base, runningTime))
    base = 2
    runningTime = sortingTest(inputList, Sorting.radixSort, numElements, base)
    print("radixSort({},{}) required {} seconds.".format(numElements, base, runningTime))