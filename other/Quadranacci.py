def quadranacciRic(n):
    if(n<=2):
        return 0
    elif (n==3):
        return 1
    else:
        return quadranacciRic(n-1)+quadranacciRic(n-2)+quadranacciRic(n-3)+quadranacciRic(n-4)


def quadra(n):
        a=0;b=0;c=1;d=1
        for i in range(4,n):
            e=a+b+c+d
            a=b
            b=c
            c=d
            d=e
        return d

print(quadranacciRic(10))
print(quadra(10))