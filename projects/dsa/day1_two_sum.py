def two(arr,target):
    seen = {}
    for i ,num in enumerate(arr):
        compare = target - num
        if compare in seen:
            return [seen[compare],i]
        seen[num] = i
print(two([1,2,3,4,5,6,7,8,9],9))
#time - o(n2)
#space - o(n)
def two_sum(arr,target):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i]+arr[j]==target:
                return [i,j]
        return []
print(two_sum([1,2,3,4,5,6,7,8,9],9))

#optimal solution using hashmap
def two_sum(arr,target):
    seen = {}
    for i,num in enumerate(arr):
        need = target - num
        if need in seen:
            return [seen[need],i]
        seen[num] = i
print(two_sum([3,3],6))
print(two_sum([-3, 4, 3, 90],0))
print(two_sum([5, 1, 8, 4],9))
print(two_sum([1, 2, 3],10))