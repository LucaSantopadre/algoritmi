def heapify(X,i):
    l = 2 * i + 1
    r = 2 * i + 2
    if(l>len(X)-1):
        return
    print("------------",X,"INDICI padre",i,"figli",l,r,"---------------")
    heapify(X,l)
    heapify(X,r)
    fixHeap(X,i)
    return X

def fixHeap(A,i):
    # indice out ,foglia trovata
    if(i>=len(A)-1):
        return
    else:
        # prendo il massimo dei figli di i
        max=getMaxSon(A,i)
        # scambio se un figlio è più grande del padre
        print("confronto padre",A[i],"  con figlio",A[max])
        if(A[max]>A[i]):
            swap(A,i,max)
            # richiamo ricorsivo per fixHeap con indice max
            fixHeap(A,max)
    print(".....fixHeap",A,"\n")


# prendo il figlio più grande oppure ritorno la foglia(se non ha figli)
def getMaxSon(X,i):
    if(i*2+1>len(X)-1):
        return i
    elif(i*2+1==len(X)-1):
        return i*2+1
    else:
        if(A[2*i+1]>A[2*i+2]):
            print("         ",A[i],"\n       ",A[2*i+1]," ",A[2*i+2])
            return 2*i+1
        else:
            print("         ",A[i],"\n       ", A[2 * i + 1], " ", A[2 * i + 2])
            return 2*i+2

# elimina e ritorna la radice dell'Heap
def getMaxHeap(A):
    swap(A,0,len(A)-1)
    print(A)
    max = A.pop(len(A)-1)
    print("eliminato:",max)
    fixHeap(A,0)
    return max

# swap di una lista
def swap(X,i,j):
    X[i],X[j]=X[j],X[i]

# ALGORITMO HeapSort
def heapSort(A):
    # costruisco l'Heap
    A=heapify(A,0)
    X=[]
    print("STRUTTURA HEAP:",A)
    while(len(A)>0):
        # inserisco il massimo nell' array addizionale X
        X.append(getMaxHeap(A))
    print("FINE",X)

# inserisce un nuovo elemento in coda, e chiama scivolaSu
def insert(H,k):
    H.append(k)
    print(H)
    scivolaSu(H,len(H)-1)
    print(H)

# scivola sopra l'elemento
def scivolaSu(H,i):
    print("scivolaSu")
    if(i%2==1):
        padre=i//2
    else:
        padre=i//2-1
    if(i==0):
        return
    print(H[i], H[padre], padre)
    if(H[i]>H[padre]):

        swap(H,i,padre)
        print(H)
        scivolaSu(H,padre)

# scivola giu un elemento
def scivolaGiu(H,i):
    if(len(H)+1 < i ):
        return
    else:
        m = getMaxSon(H,i)
        if(H[i]<H[m]):
            swap(H,i,m)
            scivolaGiu(H,m)


# ese 4.4
def aumentaChiave(H,i,k):
    print("aumentaChiave")
    if(H[i]>=k):
        return
    else:
        H[i]=k
        scivolaSu(H,i)

# ese 4.4
def decrementaChiave(H,i,k):
    print("decrementaChiave")
    if(H[i]<=k):
        return
    else:
        H[i]=k
        scivolaGiu(H,i)


A=[11,19,24,30,8,80,60,2,50]
heapify(A,0)

#aumentaChiave(A,0,8)
#decrementaChiave(A,1,1)
print(A)

#insert(A,100)

#heapSort(A)
