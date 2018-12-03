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



def select(A,k):
    if(len(A)<=10):
        insertionSort(A)
        print("Array ordinato: ",A)
        return(A[k])
    i=0
    x=0
    m=[]
    while(i<len(A)//5):
        m.append(trovaMediano5(A[x:x+5]))
        x=x+5
        i=i+1
    print("array dei mediani:      ",m)
    M = select(m,len(A)//10)
    print("Mediano dei mediani:  M=",M)
    IndexPart=partition(A,M)

    if(k<=IndexPart[0]):
        print("chiamata ricorsiva su :",A[0:IndexPart[0]],k)
        return select(A[0:IndexPart[0]],k)
    elif(k>len(A)-IndexPart[1]):
        print("chiamata ricorsiva su :", A[IndexPart[0]:],k-IndexPart[1])
        return select(A[IndexPart[0]:],k-IndexPart[1])
    else:
        return M



def partition(A,M):
    x=0        # scorre ---->
    y=len(A)-1   # scorre        <----
    dist=0
    IndexPart=[]
    print("______________partition_____________")
    while(True):
        print(A,"    M:",M," A[x]",A[x],"x",x)
        while (M >= A[x] and x < len(A)-1):
            if(M==A[x]):
                dist=dist+1
            x += 1
        while (M < A[y]):
            y -= 1
        if(x<y):
            A[x],A[y]=A[y],A[x]

        else:
            break
    y=y+1
    IndexPart.append(x)
    IndexPart.append(y)
    IndexPart.append(dist)
    print("partizioni create ...")
    print("elementi minori uguali di M = ",A[:x] )
    print("elementi maggiori di      M = ",A[y:],"\n")
    print("num uguali al mediano:",dist)
    return IndexPart



def trovaMediano5(A):
    if(A[0]>A[1]):
        A[0],A[1]=A[1],A[0]
    if(A[2]>A[3]):
        A[2],A[3]=A[3],A[2]
    if(A[0]>A[2]):
        A[0],A[2]=A[2],A[0]
        A[1],A[3]=A[3],A[1]
    if(A[1]>A[4]):
        A[1],A[4]=A[4],A[1]

    if(A[1]<A[2]):
        if(A[2]<A[4]):
            return A[2]
        else:
            return A[4]
    else:
        if(A[1]<A[3]):
            return A[1]
        else:
            return A[3]




X=[4,5,6,7,8,1,2,3,4,5,80,40,70,10,20,1,2,3,4,5,5,5,5,5,5]
#X=[1,2,3,4,5,10,20,30,40,50,12,13,14,15,16,100,110,120,130,140]
#X=[1,2,5,8,88,6,4,7,3,5]
#partitionByValue(X,5)
mediano=len(X)//2
print("\n****************MEDIANO: ",select(X,mediano))
