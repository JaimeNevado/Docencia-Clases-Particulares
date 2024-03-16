def removeDuplicates(nums):
	if (len(nums) == 0):
		return 0
	unique = 0
	for elemento in nums:
		if (elemento in nums):
			nums.remove(elemento)
	return nums

lista = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
lista2 = [1, 1, 2]

print(removeDuplicates(lista))
print(removeDuplicates(lista2))

