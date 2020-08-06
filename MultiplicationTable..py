string = ""
i = 1
while i < 11:
	j = 1
	while j < 11:
		string += str(j*i)
		string += "\t"
		j += 1

	string += "\n\n"
	i += 1

print(string)
