def count(self,arr, n, x):
	s = 0
        e = n-1
        res1 = -1
        while s<=e :
            m = s + (e-s)//2
            if arr[m] == x :
                res1 = m
                e = m - 1
            if arr[m] < x :
                s = m + 1
            if arr[m] > x :
                e = m - 1
        s = 0
        e = n-1
        res2 = -1
        while s<=e :
            m = s + (e-s)//2
            if arr[m] == x :
                res2 = m
                s = m + 1
            if arr[m] < x :
                s = m + 1
            if arr[m] > x :
                e = m - 1
        if res1 < 0 and res2 < 0 :
            return 0
        else :
            return res2 - res1 + 1
