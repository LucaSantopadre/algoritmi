import random
from selection import Selection
from sorting import Sorting
from selection.Selection import trivialSelect
import math
from writeOnCsv import write


# SAMPLEMEDIANSELECT ---------------------------------------------------------------------------------------------------
# Sceglie il pivot su cui partizionare
def sampleMedianSelect(l, k, minLen, m):
    if k <= 0 or k > len(l):
        return None
    return recursiveSampleMedianSelect(l, 0, len(l) - 1, k, minLen, m)


def recursiveSampleMedianSelect(l, left, right, k, minLen, m):
    if left == right:
        return l[left]

    # si usa stop per decidere quando smettere di ricorrere ed utilizzare un algoritmo diverso
    if len(l) < minLen:
        med = trivialSelect(l[left: right + 1], k - left)
        return med

    # prendo sottoinsieme V di  num elementi <= m
    numElements = m
    while(numElements > right-left+1):
        numElements -= 1
    V = random.sample(l[left:right+1], numElements)

    vperno = trivialSelect(V,math.ceil(len(V) / 2))   # trova mediano di V            O(m)

    perno = partitionDet(l, left, right, vperno)  #  O(n)   Watch: this is a new function which takes the pivot as the parameter

    posperno = perno + 1
    if posperno == k:
        return l[perno]
    if posperno > k:
        return recursiveSampleMedianSelect(l, left, perno - 1, k, minLen, m)
    else:
        return recursiveSampleMedianSelect(l, perno + 1, right, k, minLen, m)
# END SAMPLE_MEDIAN_SELECT ---------------------------------------------------------------------------------------------


# Non ho informazioni sulla chiave, quindi devo scorrere la lista e cercare quando trovo elemento == pivot
# PARTITION_DET --------------------------------------------------------------------------------------------------------
def partitionDet(l, left, right, pivot):
    #nota: pivot è un valore dell'array l e non un indice!
    inf = left
    sup = right

    while True:
        while inf <= right and l[inf] <= pivot:
            if l[inf] == pivot and l[left] != pivot:
                l[left], l[inf] = l[inf], l[left]
            else:
                inf += 1

        while sup >= 0 and l[sup] > pivot:
            sup -= 1

        if inf < sup:
            l[inf], l[sup] = l[sup], l[inf]
        else:
            break

    l[left], l[sup] = l[sup], l[left]

    return sup
# END PARTITION_DET ----------------------------------------------------------------------------------------------------





# QUICKSORT ------------------------------------------------------------------------------------------------------------
# @param case: int    ; (Default) = sampleMedianSelect    1 = quickSelectRandom     2 = quickSelectDet
def quickSortProject(l, case = 0):
    recursiveQuickSort(l, 0, len(l) - 1, case)


def recursiveQuickSort(l, left, right, case):
    if left >= right:
        return
    dim = right - left + 1
    k = math.ceil(dim / 2)
    m = 3
    minLen = 5

    if (case == 1):
        valPivot = Selection.quickSelectRand(l[left:right + 1], k)
    elif (case == 2):
        valPivot = Selection.quickSelectDet(l[left:right + 1], k, 1)
    else:
        valPivot = sampleMedianSelect(l[left:right + 1], k, minLen, m)

    # utilizzo partitionDet dato che non ho informazioni sulla chiave
    # algoritmi di select ritornano il valore del pivot
    pivot = partitionDet(l, left, right, valPivot)

    recursiveQuickSort(l, left, pivot - 1 , case)
    recursiveQuickSort(l, pivot + 1, right, case)
# END QUICKSORT --------------------------------------------------------------------------------------------------------




l=[1,20,3,4,6,70,8,9,10,110,12,13,14,3,213,541,52,5,3,643324,1234321,6,454,42,13,214231423,5,6,7,8,1]
#l=[1,20,3,44,5,6,70,8,99,10,110,12,14,140,1555]
#a=l
#a.sort()
#print(a)
#l=[1,20,3,44,5,6,70,8,99,10,110,12,14,140,1555]
#l=[3,4,5,6,6,6,3]
#quickSortProject(l,0)
#print(l)



#l= [1,2,3,4,5,6,7,8,9]
#print(l)
#val=sampleMedianSelect(l,math.ceil(len(l) / 2),5 ,5)
#print(val)
#Sorting.insertionSortUp(l)
#print(l)
#print(l[math.ceil(len(l) / 2) - 1])
#print(l[len(l) // 2])



