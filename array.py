def Collect():
	try:
		num = input("Please your set of numbers:")
		num = int(num)
		Run(num)
	except Exception: 
		print("Sorry, but that's not how finding consecutive runs work. Try Again.")
		Collect()

		

def Run(num):
	final = []
	numStr = str(num)
	for i, x in enumerate(numStr):
		if i < len(numStr)-2:
			one = int(numStr[i])
			two = int(numStr[i+1])
			three = int(numStr[i+2])
			if one+1 == two and two+1 == three:
				final.append(i)
				
			if one-1 == two and two-1 == three:
				final.append(i)
	print(final)
	Collect()
		
Collect()