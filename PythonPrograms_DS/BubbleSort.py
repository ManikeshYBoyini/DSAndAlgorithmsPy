def bubbleSort(arr):
    temp=0;
    length = len(arr)
    for outerIndex in range(length-1):
        for innerIndex in range(0,length-outerIndex-1):
            if(arr[innerIndex]>arr[innerIndex+1]):
                temp=arr[innerIndex]
                arr[innerIndex]=arr[innerIndex+1]
                arr[innerIndex+1]=temp


arr =[6,26,24,27,30]
bubbleSort(arr)

for a in arr:
    print(a)

