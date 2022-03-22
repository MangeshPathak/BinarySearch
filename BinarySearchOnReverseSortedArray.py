def RevSearch(arr,n,k) :
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
arr = [10,9,8,7,6,5,4,3,2,1]
n = len(arr)
k=11
RevSearch(arr,n,k)
