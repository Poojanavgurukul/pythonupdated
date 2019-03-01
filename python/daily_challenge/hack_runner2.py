arr=[1 ,-1 ,-2 ,-1]
max,sec_max=None,None
counter=0
while counter<len(arr):
    if arr[counter]>max:
        max,sec_max=arr[counter],max
    elif max>arr[counter]>sec_max:
        sec_max=arr[counter]
    counter+=1
print sec_max