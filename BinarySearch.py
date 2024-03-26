aSampleSortedList = [1,2,3,4,5,6,7,8,9,10]
aSampleUnSortedList = [14,1,45,11,24,4]

def BinarySearch(value,array):
    sortedArrayList = array.copy()
    sortedArrayList.sort()

    if (sortedArrayList != array):
        array.sort()
        print("binary search cannot be done on an unsorted array, the list will be sorted first")
        print("final sorted list :",array)
    
    start = 0
    end = len(array)-1

    while (start<=end):
        center = (start+end)//2

        if (array[center] == value):
            return center
        elif(array[center]<value):
            start=center+1 #+1 : right section except the center value
        else: #array[center]>value
            end=center-1
    return "404"

#Usage :
val = 4
result = BinarySearch(val,aSampleSortedList)

if (result == "404"):
    print("requested value doesnt exist in array")
else:
    print("index of",val,"in array, is",result)