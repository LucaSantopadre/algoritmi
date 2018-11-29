import random
import math
import progetto.Sorting as Sorting


# Sceglie il pivot su cui partizionare
# !!! DEVE RITORNARE LA POSIZIONE DEL MEDIANO DEL SOTTOINSIEME V
def sampleMedianSelect(A):
    m=5

    # scelta random del sottoinsieme V di m elementi
    numGroups = len(A)//m
    print("numero gruppi:",numGroups)
    randIndex = random.randint(0,numGroups-1)
    print("indice random",randIndex)

    B={}
    index=0
    for i in range(randIndex*m,(randIndex*m)+m):
        B[index]=i,A[i]
        index+=1
    print(B)

    return medianDict(B,m)
    print(B)



# procedura che restituisce la CHIAVE del mediano(calcolato per elemento)
# dato in input un dizionario      chiave:(CHIAVE,elemento)
# ed "ordinando" tramite algoritmo insertionSort
def medianDict(dict,m):
    print("--------------- ORDINAMENTO TRAMITE INSERIONSORT . . .")
    for key in dict:
        #print("chiave:",key,"valore:",dict[key],"DA ORDINARE:",dict[key][1])
        for k in range(1, m):
            valDict = dict[k]

            for pos in range(k):
                if dict[pos][1] > valDict[1]:
                    #print("dict[pos][1]>val",dict[pos][1],val)
                    break
            else:
                pos = k  # This value for pos is just a flag to remember that from 0 to k, the list is already ordered

            if pos < k:  # pos==k if no pos<k exists s.t. dict[pos][1]>val. Do nothing, and continue from k+1.
                for j in range(k, pos, -1):
                    dict[j] = dict[j - 1]
                dict[pos] = valDict
    print("FINE --------------- ORDINATO:",dict)
    print("MEDIANO  posizione:",dict[math.ceil((m-1)//2)][0]," valore:",dict[math.ceil((m-1)//2)][1])
    return dict[math.ceil((m-1)//2)][0]



l=[1,20,3,4,5,6,70,8,9,10,110,12,13,14,15]

a=sampleMedianSelect(l)
print(a)



# QuickSort - RECURSIVE, deterministic and non-deterministic

def quickSort(l, det=False):
    recursiveQuickSort(l, 0, len(l) - 1, det)


def recursiveQuickSort(l, left, right, det=False):
    if printSwitch.dumpOperations:
        print("recursiveQuickSort({},{})".format(left, right))

    if left >= right:
        return

    mid = partition(l, left, right, det)
    recursiveQuickSort(l, left, mid - 1, det)
    recursiveQuickSort(l, mid + 1, right, det)

    if printSwitch.dumpOperations:
        print("- " * left + str(l[left:right + 1]) + " -" * (len(l) - right - 1))


def partition(l, left, right, det=False):
    inf = left
    sup = right + 1

    if not det:
        random.seed(1)
        mid = random.randint(left, right)
        l[left], l[mid] = l[mid], l[left]  # exchange first elem with the randomically chosen one

    mid = left # the median is the first elem of the array

    if printSwitch.dumpOperations:
        print("Selected median:", l[mid])

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
