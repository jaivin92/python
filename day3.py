print("Array list ", end='')

arr = [12,2,12,5,9,20,78]
arr.append(12)
arr.insert(len(arr)+1, 5)
print(arr)

max = arr[0]
min = arr[0]

dub = []
single = []
for i in arr:
    
    #print(i)
    if(max > i):
        max = i
    else :
        min = i    

for i in range(0, len(arr)):
    
    if arr[i] not in single :
        single.append(arr[i])


    for j in range (i+1, len(arr)):
        if(arr[i]== arr[j]) :
            dub.append(arr[j]);
            # print("dublicate is ", arr[i])
        # else :
        #     print("Single", arr[i])    
    

print("dbulicate ", dub)
print("unique ", single)

arr.sort(reverse=False)
print("reverse", arr)

print("min", min)
print("max", max)
k = len(arr)    
print("array length", k)