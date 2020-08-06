
def divide(divident, divider):


	divident_range = [i for i in range(divident)]
	if divider != 0:
		result = len(divident_range[::divider])
	else:
		result = None
		print("zero cant be divident!")

	if divider < 0:
		result = -result

	return result



while True:
	num1 = int(input("Divident: "))
	num2 = int(input("Divider: "))


	print(divide(num1, num2))

