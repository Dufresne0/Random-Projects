def calc(x,y,ops):

	if ops not in "+-/*":
		return "Only +-/* "

	if ops == "+":
		return(str(x) + " " + ops + " " + str(y) + " = "+ str(x+y))
	elif ops == "-":
		return(str(x) + " " + ops + " " + str(y) + " = "+ str(x-y))
	elif ops == "/":
		return(str(x) + " " + ops + " " + str(y) + " = "+ str(x/y))
	elif ops == "*":
		return(str(x) + " " + ops + " " + str(y) + " = "+ str(x*y))

while True:

	x = int(input("Please enter first number"))
	y = int(input("Please enter second number"))
	ops = input("Choose between +,-,/,* ")

	print(calc(x,y,ops))