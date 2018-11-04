# dato un array di n interi che possono assumere {-1,0,1}
# ordinarlo in tempo O(n)
def ordina1(A):
    x=0
    y=len(A)-1

    i=-1
    j=len(A)

    while(x<y):
        if(A[x]==-1):
            i=i+1
            A[x],A[i]=A[i],A[x]
        elif(A[x]==1):
            while(y>x):
                if(A[y]==1):
                    y=y-1
                    break
                else:
                    A[x],A[y] = A[y],A[x]
                    y=y-1
                    j=j-1
                    break
        x=x+1


X=[0,-1,1,1,1,1,1,0,0,0,0,-1,-1,0,-1,-1,1,1,0,0,-1]
ordina1(X)
print(X)