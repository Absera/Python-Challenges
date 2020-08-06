# This function returns elements of alist and their pair
# [1, 1, 3, 4, 3, 1, 5, 5, 5, 5, 6, 4]
# 1 --> 2 pairs 3
# 3 --> 1 pair 2
# 4 --> 1 pair 2
# 5 --> 2 pairs 4

def array_pair(array):
	uniqueArray = []
	pairs = {}
	for item in array:
		if item not in uniqueArray:
			uniqueArray.append(item)

	for item in uniqueArray:
		itemCount = array.count(item)
		if itemCount % 2 == 0:
			itemCount = itemCount // 2
		else:
			itemCount = (itemCount -1) // 2
		pairs[item] = itemCount
	return pairs




print(array_pair([1, 1, 3, 4, 3, 1, 5, 5, 5, 5, 6, 4]))





