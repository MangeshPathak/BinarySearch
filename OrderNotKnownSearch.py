def ascendingSearch(arr,n,key) :
    start=0
    end=n-1
    while start<=end:
        mid=start+(end-start)//2
        if arr[mid]==key:
            print("Element is found at ",mid," index")
            break
        if arr[mid]>key:
            end=mid-1
        if arr[mid]<key:
            start=mid+1
    else:
        print("Element not found")
def descendingSearch(arr,n,key) :
    s = 0
    e = n - 1
    while s<=e :
        mid = (s+e)//2
        if arr[mid]==k:
            print("element is found at ",mid," index")
            break
        if arr[mid]<k:
            e=mid-1
        if arr[mid]>k:
            s=mid+1
    else:
        print("element is not found")
def checkSearch(arr,n,key) :
    if arr[0] <= arr[n-1] :
        ascendingSearch(arr,n,key)
    else :
        descendingSearch(arr,n,key)
# arr = [10,9,8,7,6,5,4,3,2,1]
arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
n = len(arr)
k = 15
checkSearch(arr,n,k)
    
