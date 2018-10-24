# NO, esegue 2 passate sull'array, in modo separato
def ordinaBandiera1(A):
    fv=-1
    ir=len(A)
    i=0
    while(i<len(A)-1):
        if(A[i]=="v"):
            fv+=1
            A[i],A[fv]=A[fv],A[i]
        i+=1
    i=len(A)-1
    while(i>fv):
        if(A[i]=="r"):
            ir-=1
            A[i],A[ir]=A[ir],A[i]
        i-=1


def ordinaBandiera2(A):
    fv=-1       # fine verde
    ir=len(A)   # inizio rosso
    i=0         # indice scorrimento array
    f=len(A)-1  # fine array
    while(i<len(A)-1):
        print("_______________________________________")
        if(A[i]=="v"):
            fv+=1
            A[i],A[fv]=A[fv],A[i]
        elif (A[i]=="r"):
            while(f>fv):
                print("inner-----------")
                if (A[f] == "r"):
                    ir -= 1
                    A[f], A[ir] = A[ir], A[f]
                f -= 1
                print(A)
        print(A)
        i+=1

"""
    

"""



A=["r","v","b","r","b","v","r","v","v","b","r"]
ordinaBandiera2(A)
print(A)