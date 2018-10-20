


def partition(A,i,f):
    # inizializzo variabili
    pivot = A[i]
    x=i
    y=f-1
    print(A,"pivot: ",pivot)
    while(True):
        while (x<=f and pivot >= A[x]):
            x += 1
        while(pivot<A[y]):
            y -= 1
        if(x<y):
            A[x],A[y]=A[y],A[x]
        else:
            break

    A[i],A[y] = A[y],A[i]
    print("A ordinato :",A," INDICE RITORNO m:",y)
    return y

def quickSort(A,i,f):
    if(i>=f):
        return
    else:
        m=partition(A,i,f)
        print(m)
        quickSort(A,i,m)
        quickSort(A,m+1,f)

arr=[5,5,6,7,1,2,3,4]
print(quickSort(arr,0,len(arr)))

