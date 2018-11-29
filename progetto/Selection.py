import random
import progetto.Sorting as Sorting


# Sceglie il pivot su cui partizionare
# !!! DEVE RITORNARE LA POSIZIONE DEL MEDIANO DEL SOTTOINSIEME V
def sampleMedianSelect(A):
    m=5

    # scelta random del sottoinsieme V di m elementi
    numGroups = len(A)//m
    randIndex = random.randint(0,numGroups-1)
    print("indice sottoinsieme",randIndex)

    B={}
    index=0
    for i in range(randIndex*m,(randIndex*m)+m):
        print(A[i])
        B[index]=i,A[i]
        index+=1
    print(B)

    #medianDict(B,m)
    print(B)
    print(sorted(B.values()))



# procedura che restituisce la chiave del mediano
# dato in input un dizionario chiave:elemento
def medianDict(dict,m):
    for key in dict:
        print("chiave:",key,"valore:",dict[key],"DA ORDINARE:",dict[key][1])

    print("posizione MEDIANOOOOO",dict[m//2][0])



l=[1,20,3,4,5,6,70,8,9,10,110,12,13,14,15]

a=sampleMedianSelect(l)





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
