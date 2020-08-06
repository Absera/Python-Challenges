
def reverse_char(string):
	letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	letter_reverse = letter[::-1] # reverse 
	new_string = ''
	letter_dict = {" ":" "}

	for i, j in zip(letter, letter_reverse):
		letter_dict[i] = j

	for char in string.upper():
		new_string += letter_dict[char]

	return new_string.capitalize()
while True:
	print(" ")
	input_string = input("Enter String: ")
	print(reverse_char(input_string)) 





