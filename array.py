def Collect():
	try:
		num = input("Please your set of numbers:") # User adds array of number. example:123654789.
		num = int(num) # Converts input to integers to assure there isnt any letters involed.
		Run(num) # Sends input data to Run function.
	except Exception: 
		print("Sorry, but that's not how finding consecutive runs work. Try Again.") # Error message.
		Collect() # Reset current function. 
		
def Run(num):
	final = [] # Collection of where such runs begins.
	numStr = str(num) # Convert int to string
	for i, x in enumerate(numStr): 
		if i < len(numStr)-2: # Adds an offset 
			one = int(numStr[i]) # Current number
			two = int(numStr[i+1]) # Current number + 1
			three = int(numStr[i+2]) # Current number + 2
			if one+1 == two and two+1 == three:
				final.append(i) # Adds run start to final array
				
			if one-1 == two and two-1 == three:
				final.append(i) # Adds run start to final array
	print(final) # Prints collection of where such runs begins.
	Collect() # Start Again
		
Collect()
