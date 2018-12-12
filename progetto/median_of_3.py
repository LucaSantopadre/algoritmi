
# trovo il mediano con al più 3 confronti
def median3(a):
    if len(a)<= 2:
        if a[0] > a[1]:
            a[0] , a[1] = a[1], a[0]
            return a[0]

    else:
        if a[0] < a[1]:
            if a[1] > a[2]:
                if a[0] < a[2]:
                    temp = a[1]
                    a[1] = a[2]
                    a[2] = temp
                else:
                    temp = a[0]
                    a[0] = a[2]
                    a[2] = a[1]
                    a[1] = temp
            else:
                pass
        else:
            if a[1] < a[2]:
                if a[0] < a[2]:
                    temp = a[0]
                    a[0] = a[1]
                    a[1] = temp
                else:
                    temp = a[0]
                    a[0] = a[1]
                    a[1] = a[2]
                    a[2] = temp
            else:
                temp = a[0]
                a[0] = a[2]
                a[2] = temp

    return a[1]