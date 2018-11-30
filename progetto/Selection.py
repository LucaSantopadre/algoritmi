import random
import math
import progetto.Sorting as Sorting


# Sceglie il pivot su cui partizionare
# !!! DEVE RITORNARE LA POSIZIONE DEL MEDIANO DEL SOTTOINSIEME V
def sampleMedianSelect(A,left,right):
    m=5

    # utilizzo lenA per generare il random
    lenA = right-left+1
    print(lenA)

    # scelta random del sottoinsieme V di m elementi
    if(lenA % m == 0):
        numGroups = lenA//m
    else:
        numGroups = lenA//m + 1
    print("........numero gruppi:",numGroups)
    randIndex = random.randint(0,numGroups-1)
    print("........indice random",randIndex)
    """
    # select last index of dimension <=m
    lastIndex = (randIndex*m)+m - 1
    while(lastIndex >= lenA):
        lastIndex -= 1
    """
    B = {}
    index=0
    for i in range(left,right + 1):
        B[index]=i,A[i]
        index+=1
    #print(B)

    print("mediano da calcolare sU: ",l[randIndex*m:right + 1])
    dimension = right - randIndex*m + 1
    return medianDict(B,m,lenA)
    #print(B)



# procedura che restituisce la CHIAVE del mediano(calcolato per elemento)
# dato in input un dizionario      chiave:(CHIAVE,elemento)
# ed "ordinando" tramite algoritmo insertionSort
def medianDict(dict,m,dimension):

    #print("--------------- ORDINAMENTO TRAMITE INSERIONSORT . . .")
    for key in dict:
        #print("chiave:",key,"valore:",dict[key],"DA ORDINARE:",dict[key][1])
        for k in range(1, dimension):
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
    #print("FINE --------------- ORDINATO:",dict)
    #print("MEDIANO  posizione:",dict[math.ceil((m-1)//2)][0]," valore:",dict[math.ceil((m-1)//2)][1])
    return dict[math.ceil((dimension-1)//2)][0]







# QuickSort - RECURSIVE, deterministic and non-deterministic

def quickSort(l):
    recursiveQuickSort(l, 0, len(l) - 1)


def recursiveQuickSort(l, left, right):
    if left >= right:
        return
    print("LISTA QUICKSORT",l[left:right+1])
    mid = partition(l, left, right)
    print("mediano",l[mid],"pos",mid)
    print("DOPO PARTITION ",l)
    print("----------------------------------------------------------------")
    recursiveQuickSort(l, left, mid - 1)
    print("DESTRAAAA\n")
    recursiveQuickSort(l, mid + 1, right)


def partition(l, left, right):
    inf = left
    sup = right + 1




    mid = sampleMedianSelect(l,left,right)
    l[left], l[mid] = l[mid], l[left]  # exchange first elem with the randomically chosen one


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



l=[1,20,3,4,5,6,70,8,9,10,110,12,13,14,3,213,541,52,5,3,643324,1234321,6,454,42,13,214231423,5,6,7,8,1]

quickSort(l)
print(l)