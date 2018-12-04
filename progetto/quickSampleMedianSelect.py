import random
from lezioni_selection import Selection
import math
from lezioni_sorting import Sorting

# SAMPLEMEDIANSELECT ---------------------------------------------------------------------------------------------------
# Sceglie il pivot su cui partizionare
def sampleMedianSelect(A,left,right, m):
    # @param A : int list[] ; lista di elementi
    # @param left: int      ; indice di start sottoinsieme lista
    # @param right: int     ; indice di end sottoinsieme lista
    # @param m: int         ; grandezza del sottoinsieme V
    # @return int           ; elemento mediano del sottoinsieme V

    # prendo sottoinsieme V di  num elementi <=m
    numElements = m
    while(numElements > right-left+1):
        numElements -= 1
    V = random.sample(A[left:right+1],numElements)

    return Selection.trivialSelect(V,numElements//2)

# END SAMPLE_MEDIAN_SELECT ---------------------------------------------------------------------------------------------


# QUICKSORT ------------------------------------------------------------------------------------------------------------

def quickSortProject(l, case = 0):
    recursiveQuickSort(l, 0, len(l) - 1, case)


def recursiveQuickSort(l, left, right, case):
    if left >= right:
        return
    pivot = partitionByValue(l, left, right, case)
    recursiveQuickSort(l, left, pivot - 1, case)
    recursiveQuickSort(l, pivot + 1, right, case)

# END QUICKSORT --------------------------------------------------------------------------------------------------------


#  PARTITION -----------------------------------------------------------------------------------------------------------
#  modificata nella scelta del pivot tramite algoritmi di selezione :
#    - algoritmi di selezione , ritornando l'elemento!!  non ho informazione sulla chiave
#    - utilizzeremo un indice per memorizzare la chiave del pivot quando incontrata nella scansione

def partitionByValue(l, left, right, case):
    inf = left
    sup = right
    dim = right - left + 1
    k   = math.ceil(dim / 2)   # parametro k del select
    #k = random.choice(range(left+1,right+1))
    m   = 5

    if(case == 1):
        pivot = Selection.quickSelectRand(l[left:right+1], k)
    elif(case == 2):
        pivot = Selection.quickSelectDet(l[left:right+1], k, 1)
    else:
        pivot = sampleMedianSelect(l, left, right, m)

    indexPivot = None   # utilizzato per mantenere la chiave del pivot quando incontrato nella scansione
    while True:

        while inf < right and l[inf] <= pivot:
            # se scorrendo da sinistra a destra trovo un valore uguale al pivot, memorizzo l'indice del valore trovato
            if(l[inf]== pivot):
                indexPivot = inf
            inf += 1

        while  l[sup] > pivot:
            sup -= 1

        if inf < sup:
            l[inf], l[sup] = l[sup], l[inf]
        else:
            break

    # se nella scansione di partitionByValue trovo un valore uguale al pivot
    # lo scambio con il sup e ritorno la chiave del pivot trovato
    if(indexPivot != None):
        l[indexPivot],l[sup]= l[sup],l[indexPivot]
    return sup

#  END PARTITION -------------------------------------------------------------------------------------------------------


#l=[1,20,3,4,6,70,8,9,10,110,12,13,14,3,213,541,52,5,3,643324,1234321,6,454,42,13,214231423,5,6,7,8,1]
#l=[1,20,3,44,5,6,70,8,99,10,110,12,14,140,1555]
#a=l
#a.sort()
#print(a)
#l=[1,20,3,44,5,6,70,8,99,10,110,12,14,140,1555]
l=[3,4,5,6,6,6,3]
quickSortProject(l,2)
print(l)



