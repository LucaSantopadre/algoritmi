def insertionSort(A):
    for k in range(0,len(A)-1):
        x=A[k+1]
        j=k
        while(j>=0):
            if(j>0 and A[j]<=x): break
            j = j - 1
        if(j<k):
            t=k
            while(t>j):
                A[t+1]=A[t]
                t=t-1
            A[j+1]=x
            j=j-1