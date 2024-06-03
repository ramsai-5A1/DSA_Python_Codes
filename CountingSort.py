
def doCountingSort(nums):
	n = len(nums)
	mx = max(nums)
	store = [0] * (mx + 1)
	for ele in nums:
		store[ele] += 1 
		
	for index in range(1, mx + 1):
		store[index] += store[index - 1]
			
	result = [-1] * n
	for index in range(n - 1, -1, -1):
		store[nums[index]] -= 1 
		result[store[nums[index]]] = nums[index]
	
	for index in range(n):
		nums[index] = result[index]
		

nums = [9, 8, 8, 7, 7, 7, 6, 5, 4, 4, 4, 3, 2, 1, 1, 1]
print("Before sorting:", nums)

doCountingSort(nums)

print("After sorting:", nums)
