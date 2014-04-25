def fact(n):
	if (n == 1):
		return 1
	return n * fact(n-1)

print fact(12)

def freq(array):
	total = sum(array)
	newarray = [item / float(total) for item in array]
	return newarray


print freq([1,1,1,1])

dict1 = {"hi":1, "what":2}

dict2 = {"hi":3, "what":4}

newdict = (dict1.items() + dict2.items())
print newdict