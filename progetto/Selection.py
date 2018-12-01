import random
import math
import progetto.Sorting as Sorting


# Sceglie il pivot su cui partizionare
# !!! DEVE RITORNARE LA POSIZIONE DEL MEDIANO DEL SOTTOINSIEME V
def sampleMedianSelect(A,left,right):
    m=5

    # prendo sottoinsieme V di  num elementi <=m
    numElements = m
    while(numElements > right-left+1):
        numElements -= 1
    randIndex = random.sample(range(left,right+1),numElements)

    # memorizzo in un dizionario V in questo modo:
    # applico una relezionde d'ordine sulla chiave del dizionario
    # B = {chiave:(CHIAVE,valore)
    B={}
    for i in range(numElements):
        B[i]=randIndex[i],A[randIndex[i]]

    # chiamo medianDict che restituisce:
    # return CHIAVE    ,    calcola mediano su insieme dei "valore"
    return medianDictInsertionSort(B, numElements)




# procedura che restituisce la CHIAVE del mediano(calcolato per elemento)
# dato in input un dizionario      chiave:(CHIAVE,elemento)
# ed "ordinando" tramite algoritmo insertionSort
def medianDictInsertionSort(dict, dim):
    # INSERTIONSORT
    # scorro le chiavi del dizionario che mi danno la relazione d'ordine
    for key in dict:
        for k in range(1, dim):
            valDict = dict[k]

            for pos in range(k):
                if dict[pos][1] > valDict[1]:
                    break
            else:
                pos = k  # This value for pos is just a flag to remember that from 0 to k, the list is already ordered

            if pos < k:  # pos==k if no pos<k exists s.t. dict[pos][1]>val. Do nothing, and continue from k+1.
                for j in range(k, pos, -1):
                    dict[j] = dict[j - 1]
                dict[pos] = valDict
    # return CHIAVE
    return dict[math.ceil((dim - 1) // 2)][0]







# QuickSort - RECURSIVE, deterministic and non-deterministic
def quickSort(l):
    recursiveQuickSort(l, 0, len(l) - 1)


def recursiveQuickSort(l, left, right):
    if left >= right:
        return
    mid = partition(l, left, right)
    recursiveQuickSort(l, left, mid - 1)
    recursiveQuickSort(l, mid + 1, right)


def partition(l, left, right):
    inf = left
    sup = right + 1


    mid = sampleMedianSelect(l,left,right)
    l[left], l[mid] = l[mid], l[left]  # exchange first elem with the selected from Algorithm sampleMedianSelect


    mid = left # the median is the first elem of the array

    while True:
        inf += 1
        while inf <= right and l[inf] <= l[mid]:
            inf += 1

        sup -= 1
        while l[sup] > l[mid]:
            sup -= 1

        if inf < sup:
            l[inf], l[sup] = l[sup], l[inf]
        else:
            break

    l[mid], l[sup] = l[sup], l[mid]

    return sup



#l=[1,20,3,4,5,6,70,8,9,10,110,12,13,14,3,213,541,52,5,3,643324,1234321,6,454,42,13,214231423,5,6,7,8,1]
l=[1,20,3,44,5,6,70,8,99,10,110,12,13,140,1555]
l=[1,2444,3,-6]
quickSort(l)
print(l)