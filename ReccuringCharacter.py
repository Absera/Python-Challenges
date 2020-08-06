def first_occurance(string):
	pair = []

	for char in string:
		if [char, string.count(char)] not in pair:
			pair.append([char, string.count(char)])

	count_list = [i[1] for i in pair]

	count_list_pos = count_list.index(max(count_list))
	return pair[count_list_pos][0]

test = first_occurance('AACCCDDDEDGK')
print(test)














