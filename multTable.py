def arrMult(arr, m):
    newArr = []
    for i in arr:
        thing = arr[i-1]*m
        newArr.append(thing)
    return newArr

def stringify(arr):
    myStr = ""
    for i in arr:
        myStr += "  "
        myStr += str(arr[i-1])
    return myStr

myArr = [1,2,3,4,5,6,7,8,9,10,11,12]
print "x", stringify(myArr)
for j in range(1,13):
    print j, arrMult(myArr, j)