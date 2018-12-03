import random
import math
from lezioni_selection import Selection


# Sceglie il pivot su cui partizionare
def sampleMedianSelect(A,left,right):
    m=5
    # prendo sottoinsieme V di  num elementi <=m
    numElements = m
    while(numElements > right-left+1):
        numElements -= 1
    C = random.sample(A[left:right+1],numElements)

    return Selection.sortSelect(C,numElements//2)

    """
    # prendo sottoinsieme V di  num elementi <=m
    numElements = m
    while(numElements > right-left+1):
        numElements -= 1

    #randIndex = random.sample(range(left,right+1),numElements)
    # memorizzo V in questo modo:
    # B = [(CHIAVE,valore),(CHIAVE,valore), ... ]
    B=[None]*numElements
    for i in range(numElements):
        B[i]=randIndex[i],A[randIndex[i]]

    # chiamo medianDict che restituisce:
    # calcolo il mediano sull'insieme dei valori e ne restituisco la CHIAVE
    return medianDictInsertionSort(B, numElements)
    """


# NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
# procedura che restituisce la CHIAVE del mediano
# dato in input una lista DISordinata  l=[(CHIAVE,valore), (CHIAVE, valore), ... ]
# ed "ORDINANDOLA" tramite algoritmo insertionSort visto a lezione e modificato per lavorare su questo tipo di struttura
def medianDictInsertionSort(l, dim):
    # INSERTIONSORT -------------------
    for val in l:
        for k in range(1, dim):
            valDict = l[k]

            for pos in range(k):
                if l[pos][1] > valDict[1]:
                    break
            else:
                pos = k  # This value for pos is just a flag to remember that from 0 to k, the list is already ordered

            if pos < k:  # pos==k if no pos<k exists s.t. dict[pos][1]>val. Do nothing, and continue from k+1.
                for j in range(k, pos, -1):
                    l[j] = l[j - 1]
                l[pos] = valDict
    # FINE INSERTIONSORT ---------------

    # return CHIAVE
    return l[math.ceil((dim - 1) // 2)][1]







# QuickSort - RICORSIVO
def quickSortProject(l):
    print("LISTA:",l)
    recursiveQuickSort(l, 0, len(l) - 1)
    print(l)


def recursiveQuickSort(l, left, right):
    if left >= right:
        return
    pivot = partition(l, left, right)
    recursiveQuickSort(l, left, pivot - 1)
    recursiveQuickSort(l, pivot + 1, right)


# PARTITION modificata nella scelta del mediano tramite algoritmo sampleMedianSelect
def partition(l, left, right):
    inf = left
    sup = right

    dim = right - left + 1


    mid = sampleMedianSelect(l,left,right)
    #mid = Selection.quickSelectRand(l[left:right+1],math.ceil(dim / 2))
    # TROVARE LA CHIAVE DI MID!!!!
    #print("mediano",mid)

    """soluzione for
    for i in range(left,right+1):
        if(l[i]==x):
            mid=i
            break
    """


    #l[left], l[mid] = l[mid], l[left]  # exchange first elem with the selected from Algorithm sampleMedianSelect


    #mid = left # the median is the first elem of the array
    indexMid=None
    while True:
        #print(l[inf])
        # boooooo
        if(l[inf]==mid):
            #print("TROVATO PIVOT, posizione",inf)
            indexMid=inf
            #print("trovato pos",inf,l[indexMid])


        while inf < right and l[inf] <= mid:
            if(l[inf]== mid):
                indexMid = inf
                #print("trovato pos", inf, l[indexMid])
            inf += 1


        while  l[sup] > mid:
            sup -= 1

        if inf < sup:
            l[inf], l[sup] = l[sup], l[inf]
        else:
            break

    if(indexMid != None):
        l[indexMid],l[sup]= l[sup],l[indexMid]

    return sup



#l=[1,20,3,4,6,70,8,9,10,110,12,13,14,3,213,541,52,5,3,643324,1234321,6,454,42,13,214231423,5,6,7,8,1]
#l=[1,20,3,44,5,6,70,8,99,10,110,12,14,140,1555]
#a=l
#a.sort()
#print(a)
#l=[1,20,3,44,5,6,70,8,99,10,110,12,14,140,1555]
l=[1,2,3,4,5,6,6,6,3]
quickSortProject(l)


