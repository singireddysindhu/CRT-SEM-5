'''
res=[]
for ele in arr:
    if  ele % 2 == 0:
        res.append(ele)
print(res)

arr = list(map(int,input().split()))
i=0
for j in range(len(arr)):
    if arr[j]%2==0:
        arr[i]=arr[j]
        i+=1
print(arr[:i])
'''