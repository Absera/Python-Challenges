list = [ 2, 7, 11, 15, 2, 5, 4 ]
target = 9
indices = []


for i in list:
	for j in list:
		if i + j == target:
			index_i = list.index(i)
			index_j = list.index(j)
			if [index_i, index_j] and [index_j, index_i] not in indices:
				indices.append([index_i, index_j])

print(indices)


