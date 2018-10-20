def mergeSort(A):
    # Caso base lista<2
    if(len(A)<2):
        return A
    # Divido la lista ricorsivamente
    m=len(A)//2
    left = mergeSort(A[:m])
    right= mergeSort(A[m:])

    # Chiamo merge sulle 2 metà
    merged = merge(left,right)
    return merged

def merge(l,r):
    # Inizializzo variabili indexing sinistra e destra
    # Inizializzo array Temporaneo
    Temp=[]
    x=0
    y=0

    # Ho già singoli elementi , quindi ordinati e allora return
    if(len(l)==0):
        return l
    if(len(r)==0):
        return r

    # Mentre riempio array temporaneo
    while(len(Temp)< len(l)+len(r)):
        # Scambio le posizioni degli elementi
        if(l[x]<r[y]):
            Temp.append(l[x])
            x += 1
        else:
            Temp.append(r[y])
            y += 1

        # Se ho terminato la parte sinistra ,
        # allora è rimasta ancora la Destra(già ordinata)
        # la inserisco alla fine di TEmp
        if x==len(l):
            Temp.extend(r[y:])
        # idem per destra...
        if y==len(r):
            Temp.extend(l[x:])
    return Temp





array=[9, 5, 7, 4, 2, 8, 1, 10, 6, 3]
print(mergeSort(array))